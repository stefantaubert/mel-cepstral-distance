import hashlib
import itertools
import logging
import pickle
from collections import OrderedDict
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List, Tuple
from typing import OrderedDict as ODType

import numpy as np
import pandas as pd
from datasets import (
  load_dataset,
)
from scipy.stats import kendalltau, spearmanr
from tqdm import tqdm

from mel_cepstral_distance import compare_audio_files
from mel_cepstral_distance.helper import samples_to_ms

EXPERIMENTS_BASE_DIR = Path("experiments")

PATH_CACHE = EXPERIMENTS_BASE_DIR / "cache.pkl"
PATH_CACHE_MOS = EXPERIMENTS_BASE_DIR / "cache_mos.pkl"

PARAM_S = "s"
PARAM_D = "D"
PARAM_SAMPLE_RATE = "sample_rate"
PARAM_ALIGN_TARGET = "align_target"
PARAM_ALIGN_METHOD = "align_method"
PARAM_REMOVE_SILENCE = "remove_silence"
PARAM_SILENCE_THRESHOLD_A = "silence_threshold_A"
PARAM_SILENCE_THRESHOLD_B = "silence_threshold_B"
PARAM_DTW_RADIUS = "dtw_radius"
PARAM_FMAX = "fmax"
PARAM_FMIN = "fmin"
PARAM_N_FFT = "n_fft"
PARAM_M = "M"
PARAM_HOP_LEN = "hop_len"
PARAM_WIN_LEN = "win_len"
PARAM_WINDOW = "window"
PARAM_NORM_AUDIO = "norm_audio"
PARAM_EXPERIMENT_NAME = "experiment_name"
PARAM_EXPERIMENT_PARAMS = "experiment_params"
PARAM_EXPERIMENT_CHANGED_PARAMS = "experiment_changed_params"

PARAMS_PROTOTYPE = {
  PARAM_EXPERIMENT_NAME: "default",  # does not count to cache
  PARAM_EXPERIMENT_PARAMS: [],  # does not count to cache
  PARAM_EXPERIMENT_CHANGED_PARAMS: [],  # does not count to cache
  PARAM_SAMPLE_RATE: 96000,
  PARAM_N_FFT: 128,
  PARAM_WIN_LEN: 128,
  PARAM_HOP_LEN: 32,
  PARAM_WINDOW: "hanning",
  PARAM_FMIN: 0,
  PARAM_FMAX: 48000,
  PARAM_S: 1,
  PARAM_M: 20,
  PARAM_D: 16,
  PARAM_ALIGN_METHOD: "dtw",
  PARAM_ALIGN_TARGET: "mfcc",
  PARAM_REMOVE_SILENCE: "no",
  PARAM_SILENCE_THRESHOLD_A: None,
  PARAM_SILENCE_THRESHOLD_B: None,
  PARAM_NORM_AUDIO: True,
  PARAM_DTW_RADIUS: 10,
}


def compare_mel_spectrograms_main(
  alg_name: str,
  wav_a: Path,
  wav_b: Path,
  params: Dict,
) -> ODType[str, Any]:
  mcd, pen = compare_audio_files(
    wav_a,
    wav_b,
    s=params[PARAM_S],
    D=params[PARAM_D],
    align_target=params[PARAM_ALIGN_TARGET],
    aligning=params[PARAM_ALIGN_METHOD],
    remove_silence=params[PARAM_REMOVE_SILENCE],
    silence_threshold_A=params[PARAM_SILENCE_THRESHOLD_A],
    silence_threshold_B=params[PARAM_SILENCE_THRESHOLD_B],
    dtw_radius=params[PARAM_DTW_RADIUS],
    fmax=params[PARAM_FMAX],
    fmin=params[PARAM_FMIN],
    n_fft=params[PARAM_N_FFT],
    M=params[PARAM_M],
    hop_len=params[PARAM_HOP_LEN],
    win_len=params[PARAM_WIN_LEN],
    window=params[PARAM_WINDOW],
    sample_rate=params[PARAM_SAMPLE_RATE],
    norm_audio=params[PARAM_NORM_AUDIO],
  )

  result = OrderedDict()
  result["algo_a"] = "gt"
  result["algo_b"] = alg_name
  assert wav_a.name == wav_b.name
  result["file"] = wav_a.name.replace(".wav", "", 1)

  result["win_len_ms"] = samples_to_ms(params[PARAM_WIN_LEN], params[PARAM_SAMPLE_RATE])
  result["hop_len_ms"] = samples_to_ms(params[PARAM_HOP_LEN], params[PARAM_SAMPLE_RATE])
  result["nfft_ms"] = samples_to_ms(params[PARAM_N_FFT], params[PARAM_SAMPLE_RATE])
  result["wav_a"] = str(wav_a.absolute())
  result["wav_b"] = str(wav_b.absolute())

  result["mcd"] = mcd
  result["pen"] = pen
  return result


def _make_cache_key(*args) -> str:
  key = "_".join(map(str, args))
  return hashlib.md5(key.encode()).hexdigest()


def make_cache_key(settings: Dict) -> str:
  vals = [
    settings[key]
    for key in sorted(settings.keys())
    if key
    not in [
      PARAM_EXPERIMENT_NAME,
      PARAM_EXPERIMENT_PARAMS,
      PARAM_EXPERIMENT_CHANGED_PARAMS,
    ]
  ]
  return _make_cache_key(*vals)


def load_mos_dataset(reset_cache: bool) -> pd.DataFrame:
  if PATH_CACHE_MOS.exists() and not reset_cache:
    with open(PATH_CACHE_MOS, "rb") as f:
      df_mos = pickle.load(f)
  else:
    dataset = load_dataset("stefantaubert/ljs-mos-120")
    df_mos = dataset["train"].to_pandas()
    df_mos["audio"] = df_mos["audio"].apply(lambda x: x["path"])
    with open(PATH_CACHE_MOS, "wb") as f:
      pickle.dump(df_mos, f)
  return df_mos


def get_obj_val(
  params: Dict,
  multicore: bool,
) -> List[Dict]:
  df_mos = load_mos_dataset(reset_cache=False)
  gt_files = sorted(df_mos[df_mos["condition"] == "gt"]["audio"].unique())
  impl_files = sorted(df_mos[df_mos["condition"] == "impl"]["audio"].unique())
  expl_files = sorted(df_mos[df_mos["condition"] == "expl"]["audio"].unique())

  jobs: List[Tuple] = []
  for gt_file, impl_file in zip(gt_files, impl_files):
    jobs.append(
      (
        "impl",
        Path(gt_file),
        Path(impl_file),
        params,
      )
    )
  for gt_file, expl_file in zip(gt_files, expl_files):
    jobs.append(("expl", Path(gt_file), Path(expl_file), params))

  results = []
  if multicore:
    with ProcessPoolExecutor() as executor:
      futures = [executor.submit(run_job, args) for args in jobs]
      for future in tqdm(as_completed(futures), total=len(futures)):
        results.append(future.result())
  else:
    for job in tqdm(jobs, desc="Processing jobs"):
      result = run_job(job)
      results.append(result)
  return results


def run_job(args):
  return compare_mel_spectrograms_main(*args)


def get_mos_df(dimension: str, reset_cache: bool = False) -> pd.DataFrame:
  df_mos = load_mos_dataset(reset_cache)

  df_individual_avg = (
    df_mos[
      df_mos["used_headphone"]
      & (df_mos["state"] == "Approved")
      # & (df_mos["age_group"] == "50+")
      # & (df_mos["gender"] == "female")
      & (df_mos["score_dimension"] == dimension)
      # & (df_mos["score_dimension"] == "intelligibility")
      & (df_mos["condition"].isin(["impl", "expl"]))
    ]
    .groupby(["worker_id", "file", "condition"])
    .agg(score_avg=("score", "mean"))
    .reset_index()
  )

  df_mos_nat = (
    df_individual_avg.groupby(["file", "condition"])
    .agg(mos_mean=("score_avg", "mean"))
    .reset_index()
  )
  return df_mos_nat


def get_experiments_alignment():
  setting_proto = PARAMS_PROTOTYPE.copy()
  setting_proto[PARAM_EXPERIMENT_NAME] = "Alignment method"
  setting_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_ALIGN_METHOD, PARAM_ALIGN_TARGET]

  setting = setting_proto.copy()
  setting[PARAM_ALIGN_METHOD] = "dtw"
  setting[PARAM_ALIGN_TARGET] = "spec"
  yield setting

  setting = setting_proto.copy()
  setting[PARAM_ALIGN_METHOD] = "dtw"
  setting[PARAM_ALIGN_TARGET] = "mel"
  yield setting

  setting = setting_proto.copy()
  setting[PARAM_ALIGN_METHOD] = "dtw"
  setting[PARAM_ALIGN_TARGET] = "mfcc"
  yield setting

  setting = setting_proto.copy()
  setting[PARAM_ALIGN_METHOD] = "pad"
  setting[PARAM_ALIGN_TARGET] = "spec"
  yield setting

  setting = setting_proto.copy()
  setting[PARAM_ALIGN_METHOD] = "pad"
  setting[PARAM_ALIGN_TARGET] = "mel"
  yield setting

  setting = setting_proto.copy()
  setting[PARAM_ALIGN_METHOD] = "pad"
  setting[PARAM_ALIGN_TARGET] = "mfcc"
  yield setting


def get_experiments_SIL():
  setting_proto = PARAMS_PROTOTYPE.copy()
  setting_proto[PARAM_EXPERIMENT_NAME] = "Silence removal"
  setting_proto[PARAM_EXPERIMENT_PARAMS] = [
    PARAM_REMOVE_SILENCE,
    PARAM_SILENCE_THRESHOLD_A,
    PARAM_SILENCE_THRESHOLD_B,
  ]

  setting = setting_proto.copy()
  setting[PARAM_REMOVE_SILENCE] = "no"
  setting[PARAM_SILENCE_THRESHOLD_A] = None
  setting[PARAM_SILENCE_THRESHOLD_B] = None
  yield setting

  setting = setting_proto.copy()
  setting[PARAM_REMOVE_SILENCE] = "mel"
  setting[PARAM_SILENCE_THRESHOLD_A] = -4
  setting[PARAM_SILENCE_THRESHOLD_B] = -4.5
  yield setting

  setting = setting_proto.copy()
  setting[PARAM_REMOVE_SILENCE] = "mel"
  setting[PARAM_SILENCE_THRESHOLD_A] = -3.5
  setting[PARAM_SILENCE_THRESHOLD_B] = -4
  yield setting

  setting = setting_proto.copy()
  setting[PARAM_REMOVE_SILENCE] = "mel"
  setting[PARAM_SILENCE_THRESHOLD_A] = -3
  setting[PARAM_SILENCE_THRESHOLD_B] = -3.5
  yield setting


def get_experiments_WINDOW():
  setting = PARAMS_PROTOTYPE.copy()
  setting_proto = setting.copy()
  setting_proto[PARAM_EXPERIMENT_NAME] = "Window function"
  setting_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_WINDOW]

  setting = setting_proto.copy()
  setting[PARAM_WINDOW] = "hamming"
  yield setting

  setting = setting_proto.copy()
  setting[PARAM_WINDOW] = "hanning"
  yield setting


def get_experiments_D():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = "Number of MFCC coefficients"
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_D]

  current_proto = params_proto.copy()
  current_proto[PARAM_M] = 80
  current_proto[PARAM_EXPERIMENT_NAME] += f" (M={current_proto[PARAM_M]})"
  current_proto[PARAM_EXPERIMENT_CHANGED_PARAMS] = [PARAM_M]

  for D in list(range(2, 20)) + [30, 40, 50, 60, 70, 80]:
    setting = current_proto.copy()
    setting[PARAM_D] = D
    yield setting

  current_proto = params_proto.copy()
  current_proto[PARAM_M] = 40
  current_proto[PARAM_EXPERIMENT_NAME] += f" (M={current_proto[PARAM_M]})"
  current_proto[PARAM_EXPERIMENT_CHANGED_PARAMS] = [PARAM_M]

  for D in list(range(2, 20)) + [25, 30, 35, 40]:
    setting = current_proto.copy()
    setting[PARAM_D] = D
    yield setting

  current_proto = params_proto.copy()
  current_proto[PARAM_M] = 20
  current_proto[PARAM_EXPERIMENT_NAME] += f" (M={current_proto[PARAM_M]})"
  current_proto[PARAM_EXPERIMENT_CHANGED_PARAMS] = [PARAM_M]

  for D in list(range(2, 21)):
    setting = current_proto.copy()
    setting[PARAM_D] = D
    yield setting

  current_proto = params_proto.copy()
  current_proto[PARAM_M] = 10
  current_proto[PARAM_EXPERIMENT_NAME] += f" (M={current_proto[PARAM_M]})"
  current_proto[PARAM_EXPERIMENT_CHANGED_PARAMS] = [PARAM_M]

  for D in list(range(2, 11)):
    setting = current_proto.copy()
    setting[PARAM_D] = D
    yield setting

  current_proto = params_proto.copy()
  current_proto[PARAM_M] = 5
  current_proto[PARAM_EXPERIMENT_NAME] += f" (M={current_proto[PARAM_M]})"
  current_proto[PARAM_EXPERIMENT_CHANGED_PARAMS] = [PARAM_M]

  for D in list(range(2, 6)):
    setting = current_proto.copy()
    setting[PARAM_D] = D
    yield setting


def get_experiments_M():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = "Number of mel filterbanks"
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_M]
  params_proto[PARAM_EXPERIMENT_CHANGED_PARAMS] = [PARAM_D]

  params_proto[PARAM_D] = 10

  for M in [10, 11, 12, 13, 20, 30, 40, 50, 60, 70, 80]:
    setting = params_proto.copy()
    setting[PARAM_M] = M
    yield setting


def get_experiments_SR():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = "Sample rate"
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_SAMPLE_RATE]

  for sampling_rate in [
    4000,
    8000,
    16000,
    22050,
    24000,
    32000,
    44100,
    48000,
    88200,
    96000,
    192000,
  ]:
    setting = params_proto.copy()
    setting[PARAM_SAMPLE_RATE] = sampling_rate
    setting[PARAM_FMAX] = sampling_rate // 2

    yield setting


def get_experiments_S():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = "Starting index"
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_S]

  params_proto[PARAM_REMOVE_SILENCE] = "no"
  params_proto[PARAM_D] = 10
  params_proto[PARAM_M] = 16

  for s in range(0, 9):
    setting = params_proto.copy()
    setting[PARAM_S] = s

    yield setting


def get_experiments_FMAX():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = "Maximum frequency"
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_FMAX]
  params_proto[PARAM_EXPERIMENT_CHANGED_PARAMS] = [PARAM_SAMPLE_RATE]

  params_proto[PARAM_SAMPLE_RATE] = 192000

  for fmax in [
    4000,
    8000,
    11025,
    16000,
    22050,
    24000,
    32000,
    44100,
    48000,
    88200,
    96000,
  ]:
    setting = params_proto.copy()
    setting[PARAM_FMAX] = fmax

    yield setting


def get_experiments_FMIN():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = "Minimum frequency"
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_FMIN]

  for fmin in [0, 100, 500, 1000, 2000, 4000, 8000, 16000, 22050, 44100]:
    setting = params_proto.copy()
    setting[PARAM_FMIN] = fmin

    yield setting


def get_experiments_dtw_radius():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = "Sakoe-Chiba radius"
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_DTW_RADIUS]

  variations = [
    1,
    2,
    3,
    10,
    20,
    40,
    None,
  ]

  for val in variations:
    setting = params_proto.copy()
    setting[PARAM_DTW_RADIUS] = val

    yield setting


def get_experiments_hop_len():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = "Hop length"
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_HOP_LEN]

  variations = [
    8,
    16,
    32,
    64,
    128,
  ]

  for val in variations:
    setting = params_proto.copy()
    setting[PARAM_HOP_LEN] = val

    yield setting


def get_experiments_n_fft():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = "FFT window length"
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_N_FFT]

  variations = [
    8,
    16,
    32,
    64,
    128,
    256,
    512,
    1024,
  ]

  for val in variations:
    setting = params_proto.copy()
    setting[PARAM_N_FFT] = val

    yield setting


def get_experiments_win_len():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = "Window length"
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_WIN_LEN]

  variations = [
    8,
    16,
    32,
    64,
    128,
    256,
    512,
    1024,
  ]

  for val in variations:
    setting = params_proto.copy()
    setting[PARAM_WIN_LEN] = val

    yield setting


def get_experiments_win_len_nfft_hop_one_quarter():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = (
    "FFT window length, window length and hop length with ratio 4:4:1"
  )
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_WIN_LEN, PARAM_N_FFT, PARAM_HOP_LEN]

  variations = [
    8,
    16,
    32,
    64,
    128,
    256,
    512,
    1024,
  ]

  for val in variations:
    setting = params_proto.copy()
    setting[PARAM_WIN_LEN] = val
    setting[PARAM_N_FFT] = val
    setting[PARAM_HOP_LEN] = val // 4

    yield setting


def get_experiments_win_len_nfft_same_hop():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = "Equal FFT window length and window length"
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_WIN_LEN, PARAM_N_FFT]

  variations = [
    8,
    16,
    32,
    64,
    128,
    256,
    512,
    1024,
  ]

  for val in variations:
    setting = params_proto.copy()
    setting[PARAM_WIN_LEN] = val
    setting[PARAM_N_FFT] = val

    yield setting


def get_experiments_n_fft_win_len_hop_len_halfes():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = (
    "FFT window length, window length and hop length with ratio 4:2:1"
  )
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_N_FFT, PARAM_WIN_LEN, PARAM_HOP_LEN]

  variations = [
    8,
    16,
    32,
    64,
    128,
    256,
    512,
    1024,
  ]

  for val in variations:
    setting = params_proto.copy()
    setting[PARAM_N_FFT] = val
    setting[PARAM_WIN_LEN] = val // 2
    setting[PARAM_HOP_LEN] = val // 4

    yield setting


def get_experiments_norm_audio():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = "Normalize audio"
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_NORM_AUDIO]

  variations = [
    True,
    False,
  ]

  for val in variations:
    setting = params_proto.copy()
    setting[PARAM_NORM_AUDIO] = val

    yield setting


def get_experiments_n_fft_win_len_hop_len_thirds():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = (
    "FFT window length, window length and hop length with ratio 9:3:1"
  )
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_N_FFT, PARAM_WIN_LEN, PARAM_HOP_LEN]

  variations = [
    16,
    32,
    64,
    128,
    256,
    512,
    1024,
  ]

  for val in variations:
    setting = params_proto.copy()
    setting[PARAM_N_FFT] = val
    setting[PARAM_WIN_LEN] = val // 3
    setting[PARAM_HOP_LEN] = val // 9

    yield setting


def get_experiments_optimization_spearman():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = "Finding optimal Spearman parameters"

  setting = params_proto.copy()
  setting[PARAM_EXPERIMENT_NAME] += " (baseline)"
  setting[PARAM_EXPERIMENT_PARAMS] = [
    PARAM_N_FFT,
    PARAM_WIN_LEN,
    PARAM_HOP_LEN,
    PARAM_D,
    PARAM_M,
    PARAM_ALIGN_TARGET,
  ]
  setting[PARAM_N_FFT] = 64
  setting[PARAM_WIN_LEN] = 32
  setting[PARAM_HOP_LEN] = 16
  setting[PARAM_D] = 10
  setting[PARAM_M] = 11
  setting[PARAM_ALIGN_TARGET] = "mel"
  yield setting

  setting = setting.copy()
  setting[PARAM_EXPERIMENT_NAME] = params_proto[PARAM_EXPERIMENT_NAME] + " (D, M)"
  setting[PARAM_D] = 13
  setting[PARAM_M] = 20
  yield setting

  setting = setting.copy()
  setting[PARAM_D] = 12
  setting[PARAM_M] = 20
  yield setting

  setting = params_proto.copy()
  setting[PARAM_EXPERIMENT_NAME] += " (norm)"
  setting[PARAM_EXPERIMENT_PARAMS] = [
    PARAM_N_FFT,
    PARAM_WIN_LEN,
    PARAM_HOP_LEN,
    PARAM_D,
    PARAM_M,
    PARAM_ALIGN_TARGET,
    PARAM_NORM_AUDIO,
  ]
  setting[PARAM_N_FFT] = 64
  setting[PARAM_WIN_LEN] = 32
  setting[PARAM_HOP_LEN] = 16
  setting[PARAM_D] = 13
  setting[PARAM_M] = 20
  setting[PARAM_ALIGN_TARGET] = "mel"
  setting[PARAM_NORM_AUDIO] = False
  yield setting

  setting = params_proto.copy()
  setting[PARAM_EXPERIMENT_NAME] += " (radius)"
  setting[PARAM_EXPERIMENT_PARAMS] = [
    PARAM_N_FFT,
    PARAM_WIN_LEN,
    PARAM_HOP_LEN,
    PARAM_D,
    PARAM_M,
    PARAM_ALIGN_TARGET,
    PARAM_DTW_RADIUS,
  ]
  setting[PARAM_N_FFT] = 64
  setting[PARAM_WIN_LEN] = 32
  setting[PARAM_HOP_LEN] = 16
  setting[PARAM_D] = 13
  setting[PARAM_M] = 20
  setting[PARAM_ALIGN_TARGET] = "mel"
  setting[PARAM_DTW_RADIUS] = 4
  yield setting

  setting = setting.copy()
  setting[PARAM_DTW_RADIUS] = 3
  yield setting

  setting = setting.copy()
  setting[PARAM_DTW_RADIUS] = 2
  yield setting

  setting = setting.copy()
  setting[PARAM_DTW_RADIUS] = 1
  yield setting

  setting = setting.copy()
  setting[PARAM_DTW_RADIUS] = 10
  yield setting


def get_experiments_optimization_pearson():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = "Finding optimal Pearson parameters"

  setting = params_proto.copy()
  setting[PARAM_EXPERIMENT_NAME] += " (baseline)"
  setting[PARAM_EXPERIMENT_PARAMS] = [
    PARAM_N_FFT,
    PARAM_WIN_LEN,
    PARAM_HOP_LEN,
    PARAM_D,
    PARAM_ALIGN_TARGET,
    PARAM_NORM_AUDIO,
  ]
  setting[PARAM_N_FFT] = 128
  setting[PARAM_WIN_LEN] = 64
  setting[PARAM_HOP_LEN] = 16
  setting[PARAM_D] = 12
  setting[PARAM_ALIGN_TARGET] = "mel"
  yield setting

  setting = params_proto.copy()
  setting[PARAM_EXPERIMENT_NAME] += " (norm=False)"
  setting[PARAM_EXPERIMENT_PARAMS] = [
    PARAM_N_FFT,
    PARAM_WIN_LEN,
    PARAM_HOP_LEN,
    PARAM_D,
    PARAM_ALIGN_TARGET,
    PARAM_NORM_AUDIO,
  ]
  setting[PARAM_N_FFT] = 128
  setting[PARAM_WIN_LEN] = 64
  setting[PARAM_HOP_LEN] = 16
  setting[PARAM_D] = 12
  setting[PARAM_ALIGN_TARGET] = "mel"
  setting[PARAM_NORM_AUDIO] = False
  yield setting

  setting = params_proto.copy()
  setting[PARAM_EXPERIMENT_NAME] += " (radius)"
  setting[PARAM_EXPERIMENT_PARAMS] = [
    PARAM_N_FFT,
    PARAM_WIN_LEN,
    PARAM_HOP_LEN,
    PARAM_D,
    PARAM_ALIGN_TARGET,
    PARAM_NORM_AUDIO,
    PARAM_DTW_RADIUS,
  ]
  setting[PARAM_N_FFT] = 128
  setting[PARAM_WIN_LEN] = 64
  setting[PARAM_HOP_LEN] = 16
  setting[PARAM_D] = 12
  setting[PARAM_ALIGN_TARGET] = "mel"
  setting[PARAM_DTW_RADIUS] = 1
  yield setting

  setting = setting.copy()
  setting[PARAM_DTW_RADIUS] = 2
  yield setting

  setting = setting.copy()
  setting[PARAM_DTW_RADIUS] = 3
  yield setting

  setting = setting.copy()
  setting[PARAM_DTW_RADIUS] = 4
  yield setting

  setting = setting.copy()
  setting[PARAM_DTW_RADIUS] = 10
  yield setting


def get_experiments_hop_len_win_len_nfft():
  params_proto = PARAMS_PROTOTYPE.copy()
  params_proto[PARAM_EXPERIMENT_NAME] = (
    "FFT window length, window length and hop length with different ratios"
  )
  params_proto[PARAM_EXPERIMENT_PARAMS] = [PARAM_N_FFT, PARAM_WIN_LEN, PARAM_HOP_LEN]

  variations = [
    (8, 8, 2),
    (8, 8, 4),
    (16, 16, 4),
    (16, 16, 8),
    (32, 32, 8),
    (64, 64, 8),
    (64, 64, 32),
    (64, 64, 48),
    (8, 4, 2),
    (32, 16, 8),
    (64, 32, 8),
    (64, 32, 16),
    (100, 50, 25),
    (120, 60, 30),
    (128, 64, 8),
    (128, 64, 16),  # top 1
    (128, 64, 32),
    (128, 128, 32),  # top 2
    (128, 128, 16),
    (128, 128, 64),
    (128, 256, 32),
    (128, 256, 64),
    (128, 32, 8),
    (256, 64, 8),
    (256, 128, 8),
    (256, 128, 16),
    (256, 128, 32),
    (256, 256, 32),
    (512, 256, 32),
    (512, 512, 128),
    (1024, 512, 256),
  ]

  variations.extend(
    [
      (
        samples_to_ms(2**13, 96000),  # 85.333 ms
        samples_to_ms(2**13, 96000),
        samples_to_ms(2**11, 96000),  # 1/4
      ),
      (
        samples_to_ms(2**13, 96000),  # 85.333 ms
        samples_to_ms(2**13, 96000),
        samples_to_ms(2**12, 96000),  # 1/2
      ),
      (
        samples_to_ms(2**14, 96000),  # 170.667 ms
        samples_to_ms(2**14, 96000),
        samples_to_ms(2**12, 96000),  # 1/4
      ),
      (
        samples_to_ms(2**14, 96000),  # 170.667 ms
        samples_to_ms(2**14, 96000),
        samples_to_ms(2**13, 96000),  # 1/2
      ),
      (
        samples_to_ms(1024, 22050),
        samples_to_ms(1024, 22050),
        samples_to_ms(256, 22050),
      ),
    ]
  )

  variations.extend(
    [
      (100, 100, 50),
      (100, 100, 25),
      (120, 120, 60),
      (120, 120, 30),
    ]
  )

  for n_fft, win_len, hop_len in variations:
    setting = params_proto.copy()
    setting[PARAM_N_FFT] = n_fft
    setting[PARAM_WIN_LEN] = win_len
    setting[PARAM_HOP_LEN] = hop_len

    yield setting


def compute_obj_metric_vec(mcd: np.ndarray, pen: np.ndarray, mode: str) -> np.ndarray:
  if mode == "mcd":
    return mcd
  elif mode == "pen":
    return pen
  elif mode == "mcd+pen":
    return mcd + pen
  elif mode == "mcd-pen":
    return mcd - pen
  elif mode == "mcd*pen":
    return mcd * pen
  elif mode == "mcd*(pen+0.1)":
    return mcd * (pen + 0.1)
  elif mode == "mcd*(pen+0.25)":
    return mcd * (pen + 0.25)
  elif mode == "mcd*(pen+0.5)":
    return mcd * (pen + 0.5)
  elif mode == "mcd*(pen+1)":
    return mcd * (pen + 1)
  elif mode == "mcd*(pen+2)":
    return mcd * (pen + 2)
  elif mode == "mcd*(pen-1)":
    return mcd * (pen - 1)
  elif mode == "pen*(mcd+1)":
    return pen * (mcd + 1)
  elif mode == "sqrt(mcd²+pen²)":
    return np.sqrt(mcd**2 + pen**2)
  else:
    raise ValueError(f"Unknown metric: {mode}")


def get_all_experiments():
  yield from get_experiments_SR()
  yield from get_experiments_FMIN()
  yield from get_experiments_FMAX()

  yield from get_experiments_M()
  yield from get_experiments_S()
  yield from get_experiments_D()

  yield from get_experiments_SIL()

  yield from get_experiments_norm_audio()

  yield from get_experiments_alignment()
  yield from get_experiments_dtw_radius()

  yield from get_experiments_WINDOW()
  yield from get_experiments_n_fft()
  yield from get_experiments_win_len()
  yield from get_experiments_hop_len()
  yield from get_experiments_win_len_nfft_same_hop()
  yield from get_experiments_win_len_nfft_hop_one_quarter()
  yield from get_experiments_n_fft_win_len_hop_len_thirds()
  yield from get_experiments_n_fft_win_len_hop_len_halfes()
  yield from get_experiments_hop_len_win_len_nfft()

  yield from get_experiments_optimization_pearson()
  yield from get_experiments_optimization_spearman()


def create_analysis():
  logger = logging.getLogger("mel_cepstral_distance")
  logger.setLevel(logging.ERROR)

  metrics = [
    "mcd",
    "pen",
    "mcd+pen",
    "mcd-pen",
    "mcd*pen",
    "sqrt(mcd²+pen²)",
    "mcd*(pen-1)",
    "mcd*(pen+0.1)",
    "mcd*(pen+0.25)",
    "mcd*(pen+0.5)",
    "mcd*(pen+1)",
    "mcd*(pen+2)",
    "pen*(mcd+1)",
  ]
  dims = ["naturalness", "intelligibility"]

  ignore_new = False

  reset_cache = False
  if PATH_CACHE.exists() and not reset_cache:
    with open(PATH_CACHE, "rb") as f:
      cache = pickle.load(f)
  else:
    cache = {}

  records = []
  df_objs = []

  new_settings = []
  unique_settings = set()
  for setting in get_all_experiments():
    cache_key = make_cache_key(setting)
    if cache_key in cache:
      # print("Cache hit")
      comp_res = cache[cache_key]
      df_objs.append((setting, pd.DataFrame.from_records(comp_res)))
    elif not ignore_new:
      new_settings.append(setting)
    unique_settings.add(cache_key)

  for setting in tqdm(new_settings):
    cache_key = make_cache_key(setting)
    comp_res = get_obj_val(
      setting,
      multicore=True,
    )
    assert cache_key not in cache
    cache[cache_key] = comp_res
    with open(PATH_CACHE, "wb") as f:
      pickle.dump(cache, f)
    df_objs.append((setting, pd.DataFrame.from_records(comp_res)))

  print(f"#Unique experiments: {len(unique_settings)}")

  tqdm_n = len(dims) * len(df_objs) * 3 * len(metrics)
  with tqdm(total=tqdm_n, disable=False) as pbar:
    for dimension in dims:
      df_mos = get_mos_df(dimension, reset_cache=False)
      for setting, df_obj in df_objs:
        # print(df_mos.head())
        # print(df_obj.head())

        df_merged = pd.merge(
          df_obj[["file", "algo_b", "mcd", "pen"]],
          df_mos,
          left_on=["file", "algo_b"],
          right_on=["file", "condition"],
          how="inner",
        ).rename(columns={"algo_b": "comparison"})
        df_merged.drop(columns=["condition"], inplace=True)

        # df_merged.to_csv("/tmp/compare_mcd_mos.csv", index=False)
        # print(df_merged.head())

        for algo in ["ALL", "impl", "expl"]:
          subset = (
            df_merged if algo == "ALL" else df_merged[df_merged["comparison"] == algo]
          )

          for metric in metrics:
            obj_metric_vals = compute_obj_metric_vec(
              subset["mcd"].to_numpy(), subset["pen"].to_numpy(), metric
            )

            mos = subset["mos_mean"]
            pearson = mos.corr(pd.Series(obj_metric_vals, index=mos.index))
            spearman, spearman_p = spearmanr(mos, obj_metric_vals)
            tau, tau_p = kendalltau(mos, obj_metric_vals)

            cache_key = make_cache_key(setting)

            correlation_result = {
              PARAM_EXPERIMENT_NAME: setting[PARAM_EXPERIMENT_NAME],
              "setting_id": cache_key,
              "dimension": dimension,
              "obj_metric": metric,
            }

            correlation_result.update(
              {
                "group": algo,
                "pearson": pearson,
                "spearman": spearman,
                "spearman_p": spearman_p,
                "kendall_tau": tau,
                "kendall_p": tau_p,
                "mcd_min": subset["mcd"].min(),
                "mcd_median": subset["mcd"].median(),
                "mcd_max": subset["mcd"].max(),
                "mcd_mean": subset["mcd"].mean(),
                "mcd_std": subset["mcd"].std(),
                "pen_min": subset["pen"].min(),
                "pen_median": subset["pen"].median(),
                "pen_max": subset["pen"].max(),
                "pen_mean": subset["pen"].mean(),
                "pen_std": subset["pen"].std(),
                "mos_median": subset["mos_mean"].median(),
                "mos_mean": subset["mos_mean"].mean(),
                "mos_std": subset["mos_mean"].std(),
              }
            )

            correlation_result.update(setting)
            correlation_result.pop(PARAM_EXPERIMENT_PARAMS)
            correlation_result.pop(PARAM_EXPERIMENT_CHANGED_PARAMS)

            records.append(correlation_result)
            pbar.update(1)

  res = pd.DataFrame.from_records(records)

  res.to_csv("experiments/compare.csv", index=False)

  df_ALL = res[(res["group"] == "ALL")].sort_values("pearson", ascending=True)
  df_ALL.drop(columns=["group"], inplace=True)

  df_ALL.to_csv("experiments/compare.ALL.csv", index=False)

  meta_analysis = {
    "min_pearson": df_ALL["pearson"].min(),
    "max_pearson": df_ALL["pearson"].max(),
    "mean_pearson": df_ALL["pearson"].mean(),
    "min_spearman": df_ALL["spearman"].min(),
    "max_spearman": df_ALL["spearman"].max(),
    "mean_spearman": df_ALL["spearman"].mean(),
    "min_kendall_tau": df_ALL["kendall_tau"].min(),
    "max_kendall_tau": df_ALL["kendall_tau"].max(),
    "mean_kendall_tau": df_ALL["kendall_tau"].mean(),
  }
  df_meta = pd.DataFrame.from_records([meta_analysis])
  print(df_meta)


def normalize_str(value: Any) -> str:
  if value is None:
    return "None"
  if type(value) is bool or isinstance(value, np.bool):
    return "True" if value else "False"
  if isinstance(value, float) and np.isnan(value):
    return "None"
  if isinstance(value, str):
    return value
  if isinstance(value, (int, float)):
    if isinstance(value, float) and value.is_integer():
      return str(int(value))
    return str(round(value, 2))
  if isinstance(value, np.int64):
    return str(int(value))
  raise TypeError(f"Unsupported type: {type(value).__name__}")


def create_correlation_reports():
  df_ALL = pd.read_csv(
    "experiments/compare.ALL.csv",
    # na_filter=False,
  )

  decimal_accuracy = 3
  metrics = ["Pearson", "Spearman", "Kendall_tau"]
  dims = ["naturalness", "intelligibility"]

  for metric, dim in itertools.product(metrics, dims):
    output_lines = []
    output_lines.append(f"# Analysis of MCD and {dim} MOS {metric} correlation")
    output_lines.append("")

    output_lines.append("## Metrics")
    output_lines.append("")
    best_metric_df = (
      df_ALL[df_ALL["dimension"] == dim]
      .groupby("obj_metric")[[metric.lower()]]
      .agg(
        mean=(metric.lower(), "mean"),
        median=(metric.lower(), "median"),
      )
      .sort_values("mean")
    )
    output_lines.append(
      best_metric_df.round(3).to_markdown(index=True, tablefmt="github")
    )

    best_metric = best_metric_df.index[0]
    best_metric = best_metric

    df_ALL_metric = df_ALL[(df_ALL["obj_metric"] == best_metric)].copy()
    df_ALL_metric.drop(columns=["obj_metric"], inplace=True)

    df_ALL_metric = df_ALL_metric[df_ALL_metric["dimension"] == dim]
    df_ALL_metric.drop(columns=["dimension"], inplace=True)

    df_ALL_metric.sort_values([metric.lower()], ascending=True, inplace=True)
    rounded_metric_name = "metric_rounded"
    df_ALL_metric[rounded_metric_name] = df_ALL_metric[metric.lower()].round(
      decimal_accuracy
    )

    join_vals = ":"
    sep_vals = ", "

    processed_experiments = []

    output_lines.append("")
    output_lines.append("## Default parameters for experiments")
    output_lines.append("")
    output_lines.append(f"- obj_metric = {best_metric}")
    for key, val in PARAMS_PROTOTYPE.items():
      if key in [
        PARAM_EXPERIMENT_NAME,
        PARAM_EXPERIMENT_PARAMS,
        PARAM_EXPERIMENT_CHANGED_PARAMS,
      ]:
        continue
      output_lines.append(f"- {key} = {normalize_str(val)}")
    output_lines.append("")

    for experiment in get_all_experiments():
      experiment_name = experiment[PARAM_EXPERIMENT_NAME]
      if experiment_name in processed_experiments:
        continue
      relevant_cols = experiment[PARAM_EXPERIMENT_PARAMS]
      changed_cols = experiment[PARAM_EXPERIMENT_CHANGED_PARAMS]
      grouped = df_ALL_metric[
        df_ALL_metric["experiment_name"] == experiment_name
      ].groupby(rounded_metric_name)
      output_lines.append(f"## Experiment - {experiment_name}")
      output_lines.append("")
      default_params = {}
      for changed_col in changed_cols:
        changed_vals = set()
        for _, group_df in grouped:
          changed_vals |= set(group_df[changed_col].unique())
        assert len(changed_vals) == 1
        default_params[changed_col] = changed_vals.pop()

      if len(default_params) > 0:
        output_lines.append(
          f"- Changed parameter(s): {''.join(f'{k}={normalize_str(v)}' for k, v in default_params.items())}"
        )

      experiment_params = {}
      for experiment_col in relevant_cols:
        changed_vals = set()
        for _, group_df in grouped:
          changed_vals |= set(group_df[experiment_col].unique())

        experiment_params[experiment_col] = sorted(changed_vals)
      output_lines.append("- Experimented parameter(s):")
      for experiment_col, v in experiment_params.items():
        output_lines.append(
          f"  - {experiment_col} = {', '.join(map(normalize_str, v))}"
        )

      output_lines.append(f"- Results (format = {{{join_vals.join(relevant_cols)}}}):")
      for group_val, group_df in grouped:
        line = f"  - {metric} {group_val:.{decimal_accuracy}f}: "
        vals = []
        for _, row in group_df.iterrows():
          val = join_vals.join(normalize_str(row[col]) for col in relevant_cols)
          vals.append(val)

        line += sep_vals.join(sorted(vals))
        output_lines.append(line)
      output_lines.append("")
      processed_experiments.append(experiment_name)
    best_vals = df_ALL_metric[metric.lower()].sort_values(ascending=True)

    output_lines.append("## Best experiments")
    output_lines.append("")
    for i in range(3):
      val = best_vals.iloc[i]
      output_lines.append(f"### {i + 1}. Place")
      output_lines.append("")
      output_lines.append(f"- {metric}: {val}")
      best_experiments = df_ALL_metric[df_ALL_metric[metric.lower()] == val]
      output_lines.append(f"- Experiments with that score (#{len(best_experiments)}):")
      for j in range(len(best_experiments)):
        best_experiment = best_experiments.iloc[j]
        output_lines.append(
          f"  - '{best_experiment[PARAM_EXPERIMENT_NAME]}' with parameters:"
        )
        for param in PARAMS_PROTOTYPE:
          if param in [
            PARAM_EXPERIMENT_NAME,
            PARAM_EXPERIMENT_PARAMS,
            PARAM_EXPERIMENT_CHANGED_PARAMS,
          ]:
            continue
          val = best_experiment[param]
          output_lines.append(f"    - {param} = {normalize_str(val)}")
      output_lines.append("")

    result = "\n".join(output_lines)
    (EXPERIMENTS_BASE_DIR / f"report.{dim}.{metric}.md").write_text(
      result, encoding="utf-8"
    )


def create_obj_reports():
  df_ALL = pd.read_csv(EXPERIMENTS_BASE_DIR / "compare.ALL.csv")

  decimal_accuracy = 3
  metrics = ["MCD", "PEN"]
  join_vals = ":"
  sep_vals = ", "

  for metric in metrics:
    output_lines = []
    output_lines.append(f"# Analysis of {metric} values depending on the parameters")
    output_lines.append("")

    output_lines.append("## Default parameters for experiments")
    output_lines.append("")
    for key, val in PARAMS_PROTOTYPE.items():
      if key in [
        PARAM_EXPERIMENT_NAME,
        PARAM_EXPERIMENT_PARAMS,
        PARAM_EXPERIMENT_CHANGED_PARAMS,
      ]:
        continue
      output_lines.append(f"- {key} = {normalize_str(val)}")
    output_lines.append("")

    df_ALL_metric = df_ALL[(df_ALL["obj_metric"] == metric.lower())].copy()
    df_ALL_metric.drop(columns=["obj_metric"], inplace=True)

    df_ALL_metric = df_ALL_metric[
      df_ALL_metric["dimension"] == "naturalness"
    ]  # dim is irrelevant
    df_ALL_metric.drop(columns=["dimension"], inplace=True)

    rounded_metric_name = "metric_rounded"
    df_ALL_metric[rounded_metric_name] = df_ALL_metric[f"{metric.lower()}_mean"].round(
      decimal_accuracy
    )

    processed_experiments = []
    for experiment in get_all_experiments():
      experiment_name = experiment[PARAM_EXPERIMENT_NAME]
      if experiment_name in processed_experiments:
        continue
      relevant_cols = experiment[PARAM_EXPERIMENT_PARAMS]
      changed_cols = experiment[PARAM_EXPERIMENT_CHANGED_PARAMS]
      grouped = df_ALL_metric[
        df_ALL_metric["experiment_name"] == experiment_name
      ].groupby(rounded_metric_name)
      output_lines.append(f"## Experiment - {experiment_name}")
      output_lines.append("")
      default_params = {}
      for changed_col in changed_cols:
        changed_vals = set()
        for _, group_df in grouped:
          changed_vals |= set(group_df[changed_col].unique())
        assert len(changed_vals) == 1
        default_params[changed_col] = changed_vals.pop()

      if len(default_params) > 0:
        output_lines.append(
          f"- Changed parameter(s): {''.join(f'{k}={normalize_str(v)}' for k, v in default_params.items())}"
        )

      experiment_params = {}
      for experiment_col in relevant_cols:
        changed_vals = set()
        for _, group_df in grouped:
          changed_vals |= set(group_df[experiment_col].unique())

        experiment_params[experiment_col] = sorted(changed_vals)
      output_lines.append("- Experimented parameter(s):")
      for experiment_col, v in experiment_params.items():
        output_lines.append(
          f"  - {experiment_col} = {', '.join(map(normalize_str, v))}"
        )

      output_lines.append(f"- Results (format = {{{join_vals.join(relevant_cols)}}}):")
      for group_val, group_df in grouped:
        line = f"  - {metric} {group_val:.{decimal_accuracy}f}: "
        vals = []
        for _, row in group_df.iterrows():
          val = join_vals.join(normalize_str(row[col]) for col in relevant_cols)
          vals.append(val)

        line += sep_vals.join(sorted(vals))
        output_lines.append(line)
      output_lines.append("")
      processed_experiments.append(experiment_name)

    result = "\n".join(output_lines)
    (EXPERIMENTS_BASE_DIR / f"report.{metric}.md").write_text(result, encoding="utf-8")


if __name__ == "__main__":
  create_analysis()
  create_correlation_reports()
  create_obj_reports()
