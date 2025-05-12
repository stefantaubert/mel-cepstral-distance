from logging import getLogger
from pathlib import Path
from typing import Literal, Optional, Tuple, Union

import numpy as np
import numpy.typing as npt
from scipy.io import wavfile

from mel_cepstral_distance.alignment import align_MC_s_D, align_X_km, align_X_kn
from mel_cepstral_distance.computation import (
  get_average_MCD,
  get_MC_X_ik,
  get_MCD_k,
  get_w_n_m,
  get_X_km,
  get_X_kn,
)
from mel_cepstral_distance.helper import (
  get_n_fft_bins,
  ms_to_samples,
  norm_audio_signal,
  resample_if_necessary,
)
from mel_cepstral_distance.silence import (
  remove_silence_MC_X_ik,
  remove_silence_rms,
  remove_silence_X_km,
  remove_silence_X_kn,
)


def get_amplitude_spectrogram(
  audio: Union[Path, str],
  *,
  sample_rate: Optional[int] = None,
  n_fft: float = 32,
  win_len: float = 32,
  hop_len: float = 8,
  window: Literal["hamming", "hanning"] = "hanning",
  norm_audio: bool = True,
  remove_silence: bool = False,
  silence_threshold: Optional[float] = None,
) -> npt.NDArray[np.complex128]:
  """
  Computes the complex-valued amplitude spectrogram (STFT) of an audio signal.
  Optionally applies normalization and silence removal. While not invoked
  elsewhere in the module, this function can be used independently to
  experiment with silence removal and STFT configuration. This is useful for
  analyzing the effect of preprocessing on subsequent alignment and distance
  computation.

  Parameters
  ----------
  audio : Path | str
    Path to a mono WAV file. The file must exist and be readable.
  sample_rate : int, optional
    Target sample rate for resampling the audio. If not specified, the
    original sample rate of the audio file is used. Must be > 0.
  n_fft : float, default=32
    Length of the FFT window in milliseconds. Must be > 0. The corresponding
    number of samples should ideally be a power of 2 for efficient FFT
    computation.
  win_len : float, default=32
    Window length in milliseconds. Can differ from `n_fft`. Must be > 0.
  hop_len : float, default=8
    Hop length in milliseconds between consecutive windows. Must be > 0.
  window : {"hamming", "hanning"}, default="hanning"
    Type of window function to apply during the STFT.
  norm_audio : bool, default=True
    If True, normalizes the audio signal to the range [-1, 1] before
    processing.
  remove_silence : bool, default=False
    If True, removes silence from the audio signal based on the
    `silence_threshold` parameter.
  silence_threshold : float, optional
    RMS threshold used to detect silence when `remove_silence` is True.
    Must be >= 0 if specified.

  Returns
  -------
  numpy.ndarray
    A 2D complex-valued amplitude spectrogram of shape (frames, frequency bins).
    Returns an empty array if the input audio is empty or consists only of
    silence.

  Raises
  ------
  ValueError
    If `sample_rate` is not > 0.
  ValueError
    If `n_fft`, `win_len`, or `hop_len` is not > 0.
  ValueError
    If `window` is not "hamming" or "hanning".
  ValueError
    If silence removal is enabled but `silence_threshold` is not set or is < 0.
  FileNotFoundError
    If the specified `audio` file does not exist.
  TypeError
    If the `audio` parameter is not a valid path or string.

  Notes
  -----
  - The function assumes the input audio is mono. If the audio file contains
    multiple channels, additional preprocessing is required.
  - For optimal performance, the FFT window length (`n_fft`) should be a power
    of 2 in samples.
  - If `n_fft` and `win_len` differ, the window will be truncated or padded
    accordingly, which may affect the resulting spectrogram.
  """
  if sample_rate is not None and not sample_rate > 0:
    raise ValueError("sample_rate must be > 0")

  if not n_fft > 0:
    raise ValueError("n_fft must be > 0")

  if not win_len > 0:
    raise ValueError("win_len must be > 0")

  if not hop_len > 0:
    raise ValueError("hop_len must be > 0")

  if window not in ["hamming", "hanning"]:
    raise ValueError("window must be 'hamming' or 'hanning")

  sr, signal = wavfile.read(audio)

  if sample_rate is None:
    sample_rate = sr

  n_fft_samples = ms_to_samples(n_fft, sample_rate)

  if len(signal) == 0:
    logger = getLogger(__name__)
    logger.warning("audio is empty")
    empty_spec = np.empty((0, get_n_fft_bins(n_fft_samples)), dtype=np.complex128)
    return empty_spec

  signal = resample_if_necessary(signal, sr, sample_rate)

  n_fft_is_two_power = n_fft_samples & (n_fft_samples - 1) == 0

  if not n_fft_is_two_power:
    logger = getLogger(__name__)
    logger.warning(
      f"n_fft ({n_fft}ms / {n_fft_samples} samples) should be a power of 2 "
      f"in samples for faster computation"
    )

  if n_fft != win_len:
    logger = getLogger(__name__)
    logger.warning(f"n_fft ({n_fft}ms) should be equal to win_len ({win_len}ms)")
    if n_fft < win_len:
      logger.warning(f"truncating windows to n_fft ({n_fft}ms)")
    else:
      assert n_fft > win_len
      logger.warning(f"padding windows to n_fft ({n_fft}ms)")

  if norm_audio:
    signal = norm_audio_signal(signal)

  win_len_samples = ms_to_samples(win_len, sample_rate)

  if remove_silence:
    if silence_threshold is None:
      raise ValueError("silence_threshold must be set")

    if not silence_threshold >= 0:
      raise ValueError("silence_threshold must be greater than or equal to 0 RMS")

    signal = remove_silence_rms(
      signal, silence_threshold, min_silence_samples=win_len_samples
    )

    if len(signal) == 0:
      logger = getLogger(__name__)
      logger.warning("after removing silence, audio is empty")
      empty_spec = np.empty((0, get_n_fft_bins(n_fft_samples)), dtype=np.complex128)
      return empty_spec

  # STFT - Shape: (#Frames, Bins)
  hop_len_samples = ms_to_samples(hop_len, sample_rate)
  X_km_A = get_X_km(signal, n_fft_samples, win_len_samples, hop_len_samples, window)
  return X_km_A


def get_mel_spectrogram(
  amp_spec: npt.NDArray[np.complex128],
  sample_rate: int,
  n_fft: float,
  /,
  *,
  M: int = 20,
  fmin: int = 0,
  fmax: Optional[int] = None,
  remove_silence: bool = False,
  silence_threshold: Optional[float] = None,
) -> npt.NDArray:
  """
  Converts an amplitude spectrogram to a mel-spectrogram using mel filterbanks.
  Optionally removes silence based on a threshold.

  Parameters
  ----------
  amp_spec : numpy.ndarray
    A 2D complex-valued amplitude spectrogram of shape (frames, frequency bins).
  sample_rate : int
    Sampling rate of the audio signal in Hz. Must be > 0.
  n_fft : float
    FFT window length in milliseconds. Must be > 0.
  M : int, optional, default=20
    Number of mel filterbanks. Must be > 0.
  fmin : int, optional, default=0
    Minimum frequency (in Hz) for mel-band calculation. Must satisfy 0 <= fmin < fmax.
  fmax : int, optional
    Maximum frequency (in Hz) for mel-band calculation. If not set, defaults to
    sample_rate / 2. Must satisfy 0 < fmax <= sample_rate / 2.
  remove_silence : bool, optional, default=False
    If True, removes silence from the amplitude spectrogram
    based on `silence_threshold`.
  silence_threshold : float, optional
    Threshold used to detect silence when `remove_silence` is True.

  Returns
  -------
  numpy.ndarray
    A 2D mel-spectrogram of shape (frames, mel bands). Returns an empty array if
    the input spectrogram is empty or becomes empty after silence removal.

  Raises
  ------
  ValueError
    If `amp_spec` does not have 2 dimensions.
  ValueError
    If `M` is not > 0.
  ValueError
    If `amp_spec` has no frequency bins.
  ValueError
    If `n_fft` is not > 0.
  ValueError
    If `sample_rate` is not > 0.
  ValueError
    If `fmax` is not in (0, sample_rate / 2].
  ValueError
    If `fmin` is not in [0, fmax).
  ValueError
    If the number of frequency bins in `amp_spec` does not match `n_fft` in samples.
  ValueError
    If silence removal is enabled but `silence_threshold` is not set.
  """
  # amp_spec is X_km

  if len(amp_spec.shape) != 2:
    raise ValueError(
      f"amplitude spectrogram must have 2 dimensions but got {len(amp_spec.shape)}"
    )

  if not M > 0:
    raise ValueError("M must be > 0")

  if amp_spec.shape[0] == 0:
    logger = getLogger(__name__)
    logger.warning("spectrogram is empty")
    empty_mel_spec = np.empty((0, M), dtype=np.float64)
    return empty_mel_spec

  if amp_spec.shape[1] == 0:
    raise ValueError("spectrogram must have at least 1 frequency bin")

  if not n_fft > 0:
    raise ValueError("n_fft must be > 0")

  if not sample_rate > 0:
    raise ValueError("sample_rate must be > 0")

  if fmax is not None:
    if not 0 < fmax <= sample_rate // 2:
      raise ValueError(
        f"fmax must be in (0, sample_rate // 2], i.e., (0, {sample_rate // 2}]"
      )
  else:
    fmax = sample_rate // 2

  if not 0 <= fmin < fmax:
    raise ValueError(f"fmin must be in [0, fmax), i.e., [0, {fmax})")

  n_fft_samples = ms_to_samples(n_fft, sample_rate)
  if get_n_fft_bins(n_fft_samples) != amp_spec.shape[1]:
    raise ValueError(
      f"n_fft (in samples) // 2 + 1 must match the number of frequency bins "
      f"in the spectrogram but got {n_fft_samples // 2 + 1} != {amp_spec.shape[1]}"
    )

  if remove_silence:
    if silence_threshold is None:
      raise ValueError("silence_threshold must be set")

    amp_spec = remove_silence_X_km(amp_spec, silence_threshold)

    if amp_spec.shape[0] == 0:
      logger = getLogger(__name__)
      logger.warning("after removing silence, spectrogram is empty")
      empty_mel_spec = np.empty((0, M), dtype=np.float64)
      return empty_mel_spec

  w_n_m = get_w_n_m(sample_rate, n_fft_samples, M, fmin, fmax)
  X_kn = get_X_kn(amp_spec, w_n_m)
  return X_kn


def get_mfccs(
  mel_spec: npt.NDArray,
  /,
  *,
  remove_silence: bool = False,
  silence_threshold: Optional[float] = None,
) -> npt.NDArray:
  """
  Computes the Mel-Frequency Cepstral Coefficients (MFCCs) from a given
  mel-spectrogram. Optionally removes silence based on a threshold.

  Parameters
  ----------
  mel_spec : numpy.ndarray
    A 2D mel-spectrogram of shape (frames, mel bands). Must have at least
    one frame and one mel band.
  remove_silence : bool, optional, default=False
    If True, removes silence from the mel-spectrogram based on the
    `silence_threshold` parameter.
  silence_threshold : float, optional
    Threshold used to detect silence when `remove_silence` is True.

  Returns
  -------
  numpy.ndarray
    A 2D array of MFCCs with shape (mel bands, frames). Returns an empty
    array if the input mel-spectrogram is empty or becomes empty after
    silence removal.

  Raises
  ------
  ValueError
    If `mel_spec` does not have 2 dimensions.
  ValueError
    If `mel_spec` has no mel bands or frames.
  ValueError
    If silence removal is enabled but `silence_threshold` is not set.

  Notes
  -----
  - The function assumes the input mel-spectrogram is precomputed and valid.
  - Silence removal is applied by thresholding the mel-spectrogram frames
    based on their energy.
  - The resulting MFCCs are computed using the Discrete Cosine Transform (DCT)
    on the log-mel-spectrogram.
  """
  if len(mel_spec.shape) != 2:
    raise ValueError(
      f"mel-spectrogram must have 2 dimensions but got {len(mel_spec.shape)}"
    )

  if mel_spec.shape[1] == 0:
    raise ValueError("mel-spectrogram must have at least 1 mel-band")

  if mel_spec.shape[0] == 0:
    logger = getLogger(__name__)
    logger.warning("mel-spectrogram is empty")
    empty_mfccs = np.empty((mel_spec.shape[1], 0), dtype=np.float64)
    return empty_mfccs

  if remove_silence:
    if silence_threshold is None:
      raise ValueError("silence_threshold must be set")

    mel_spec = remove_silence_X_kn(mel_spec, silence_threshold)

    if mel_spec.shape[0] == 0:
      logger = getLogger(__name__)
      logger.warning("after removing silence, mel-spectrogram is empty")
      empty_mfccs = np.empty((mel_spec.shape[1], 0), dtype=np.float64)
      return empty_mfccs

  MC_X_ik = get_MC_X_ik(mel_spec, mel_spec.shape[1])
  return MC_X_ik


def compare_audio_files(
  audio_A: Union[Path, str],
  audio_B: Union[Path, str],
  /,
  *,
  sample_rate: Optional[int] = None,
  n_fft: float = 32,
  win_len: float = 32,
  hop_len: float = 8,
  window: Literal["hamming", "hanning"] = "hanning",
  fmin: int = 0,
  fmax: Optional[int] = None,
  M: int = 20,
  s: int = 1,
  D: int = 16,
  aligning: Literal["pad", "dtw"] = "dtw",
  align_target: Literal["spec", "mel", "mfcc"] = "mfcc",
  remove_silence: Literal["no", "sig", "spec", "mel", "mfcc"] = "no",
  silence_threshold_A: Optional[float] = None,
  silence_threshold_B: Optional[float] = None,
  norm_audio: bool = True,
  dtw_radius: Optional[int] = 10,
) -> Tuple[float, float]:
  """
  Compares two audio signals by computing the mean Mel-Cepstral Distance (MCD) between
  them. Internally computes amplitude and mel spectrograms, extracts MFCCs, and aligns
  them for comparison. Silence can optionally be removed before alignment.

  This is the main entry point for evaluating similarity between two audio files in the
  module.

  Parameters
  ----------
  audio_A : Path | str
      Path to the first mono WAV file.
  audio_B : Path | str
      Path to the second mono WAV file.
  sample_rate : int, optional
      If specified, both signals are resampled to this rate before processing.
      Otherwise, the lower of the two input sample rates is used. Must be > 0.
  n_fft : float, default=32
      FFT window length in milliseconds. Must be > 0. The corresponding number of
      samples should be a power of 2 for efficient FFT computation.
  win_len : float, default=32
      Window length in milliseconds. Should be equal to `n_fft`. Must be > 0.
  hop_len : float, default=8
      Hop length in milliseconds. Must be > 0.
  window : Literal["hamming", "hanning"], default="hanning"
      Type of window function used in the STFT.
  fmin : int, default=0
      Minimum frequency (in Hz) for mel-band calculation. Must satisfy 0 <= fmin < fmax.
  fmax : int, optional
      Maximum frequency (in Hz) for mel-band calculation. If not set, defaults to
      sample_rate / 2. Must satisfy 0 < fmax <= sample_rate / 2.
  M : int, default=20
      Number of mel filterbanks. Must be > 0.
  s : int, default=1
      Starting index (inclusive) for MFCCs used in MCD calculation. Must be in [0, D).
  D : int, default=16
      Number of MFCC coefficients considered for distance computation.
      Must satisfy D <= M.
  aligning : Literal["pad", "dtw"], default="dtw"
      Alignment strategy. "pad" uses zero-padding; "dtw" uses Dynamic Time Warping. DTW
      is more accurate but computationally more expensive.
  align_target : Literal["spec", "mel", "mfcc"], default="mel"
      Spectral level at which alignment is applied. Determines at which stage
      silence can be removed.
  remove_silence : Literal["no", "sig", "spec", "mel", "mfcc"], default="no"
      Stage at which silence is removed. "sig" applies RMS-based silence removal in the
      time domain. Other options apply thresholding to spectral frames.
      Silence is always removed before alignment.
  silence_threshold_A : float, optional
      Threshold used to detect silence in `audio_A`, depending on the selected
      `remove_silence` strategy. For `"sig"`, this is an RMS threshold; for spectral
      stages, it applies to frame energy or amplitude.
  silence_threshold_B : float, optional
      Same as `silence_threshold_A`, but applied to `audio_B`.
  norm_audio : bool, default=True
      If True, normalizes both signals to the range [-1, 1] before processing.
  dtw_radius : int, optional, default=10
      Sakoe-Chiba radius for DTW alignment. A value of 1 is fastest but less accurate.
      None allows unrestricted warping but is slowest. A value of 10 is a good
      compromise between speed and accuracy.

  Returns
  -------
  Tuple[float, float]
      - Mean MCD over all selected coefficients.
      - Alignment penalty. Returns (nan, nan) if either input is empty or becomes empty
        due to silence removal.

  Raises
  ------
  ValueError
      If `audio_A` or `audio_B` is not a valid file path or cannot be read.
  ValueError
      If `sample_rate` is not > 0.
  ValueError
      If `n_fft` is not > 0 or is not a power of 2 in samples.
  ValueError
      If `win_len` is not > 0 or does not match `n_fft`.
  ValueError
      If `hop_len` is not > 0.
  ValueError
      If `window` is not "hamming" or "hanning".
  ValueError
      If `fmin` is not in [0, fmax).
  ValueError
      If `fmax` is not in (0, sample_rate / 2].
  ValueError
      If `M` is not > 0.
  ValueError
      If `D` is not <= `M`.
  ValueError
      If `s` is not in [0, D).
  ValueError
      If `aligning` is not "pad" or "dtw".
  ValueError
      If `align_target` is not "spec", "mel", or "mfcc".
  ValueError
      If `remove_silence` is not "no", "sig", "spec", "mel", or "mfcc".
  ValueError
      If silence removal is enabled but `silence_threshold_A` or `silence_threshold_B`
      is not set.
  ValueError
      If `dtw_radius` is specified but not >= 1.
  """
  if remove_silence not in ["no", "sig", "spec", "mel", "mfcc"]:
    raise ValueError("remove_silence must be 'no', 'sig', 'spec', 'mel' or 'mfcc'")

  if sample_rate is not None and not sample_rate > 0:
    raise ValueError("sample_rate must be > 0")

  if not n_fft > 0:
    raise ValueError("n_fft must be > 0")

  if not win_len > 0:
    raise ValueError("win_len must be > 0")

  if not hop_len > 0:
    raise ValueError("hop_len must be > 0")

  if window not in ["hamming", "hanning"]:
    raise ValueError("window must be 'hamming' or 'hanning'")

  sr1, signalA = wavfile.read(audio_A)
  sr2, signalB = wavfile.read(audio_B)

  if signalA.dtype != signalB.dtype:
    logger = getLogger(__name__)
    logger.warning(
      f"audio A and B have different data types ({signalA.dtype} != {signalB.dtype})"
    )

  if len(signalA) == 0:
    logger = getLogger(__name__)
    logger.warning("audio A is empty")
    return np.nan, np.nan

  if len(signalB) == 0:
    logger = getLogger(__name__)
    logger.warning("audio B is empty")
    return np.nan, np.nan

  if sample_rate is None:
    sample_rate = min(sr1, sr2)

  signalA = resample_if_necessary(signalA, sr1, sample_rate)
  signalB = resample_if_necessary(signalB, sr2, sample_rate)

  n_fft_samples = ms_to_samples(n_fft, sample_rate)
  n_fft_is_two_power = n_fft_samples & (n_fft_samples - 1) == 0

  if not n_fft_is_two_power:
    logger = getLogger(__name__)
    logger.warning(
      f"n_fft ({n_fft}ms / {n_fft_samples} samples) should "
      f"be a power of 2 in samples for faster computation"
    )

  if n_fft != win_len:
    logger = getLogger(__name__)
    logger.warning(f"n_fft ({n_fft}ms) should be equal to win_len ({win_len}ms)")
    if n_fft < win_len:
      logger.warning(f"truncating windows to n_fft ({n_fft}ms)")
    else:
      assert n_fft > win_len
      logger.warning(f"padding windows to n_fft ({n_fft}ms)")

  if norm_audio:
    signalA = norm_audio_signal(signalA)
    signalB = norm_audio_signal(signalB)

  win_len_samples = ms_to_samples(win_len, sample_rate)

  if remove_silence == "sig":
    if silence_threshold_A is None:
      raise ValueError("silence_threshold_A must be set")

    if silence_threshold_B is None:
      raise ValueError("silence_threshold_B must be set")

    if not silence_threshold_A >= 0:
      raise ValueError("silence_threshold_A must be greater than or equal to 0 RMS")

    if not silence_threshold_B >= 0:
      raise ValueError("silence_threshold_B must be greater than or equal to 0 RMS")

    signalA = remove_silence_rms(
      signalA, silence_threshold_A, min_silence_samples=win_len_samples
    )

    signalB = remove_silence_rms(
      signalB, silence_threshold_B, min_silence_samples=win_len_samples
    )

    if len(signalA) == 0:
      logger = getLogger(__name__)
      logger.warning("after removing silence, audio A is empty")
      return np.nan, np.nan

    if len(signalB) == 0:
      logger = getLogger(__name__)
      logger.warning("after removing silence, audio B is empty")
      return np.nan, np.nan

    remove_silence = "no"

  # STFT - Shape: (#Frames, Bins)
  hop_len_samples = ms_to_samples(hop_len, sample_rate)
  X_km_A = get_X_km(signalA, n_fft_samples, win_len_samples, hop_len_samples, window)
  X_km_B = get_X_km(signalB, n_fft_samples, win_len_samples, hop_len_samples, window)

  mean_mcd_over_all_k, res_penalty = compare_amplitude_spectrograms(
    X_km_A,
    X_km_B,
    sample_rate,
    n_fft,
    fmin=fmin,
    fmax=fmax,
    M=M,
    s=s,
    D=D,
    aligning=aligning,
    align_target=align_target,
    remove_silence=remove_silence,
    silence_threshold_A=silence_threshold_A,
    silence_threshold_B=silence_threshold_B,
    dtw_radius=dtw_radius,
  )

  return mean_mcd_over_all_k, res_penalty


def compare_amplitude_spectrograms(
  amp_spec_A: npt.NDArray[np.complex128],
  amp_spec_B: npt.NDArray[np.complex128],
  sample_rate: int,
  n_fft: float,
  /,
  *,
  fmin: int = 0,
  fmax: Optional[int] = None,
  M: int = 20,
  s: int = 1,
  D: int = 16,
  aligning: Literal["pad", "dtw"] = "dtw",
  align_target: Literal["spec", "mel", "mfcc"] = "mfcc",
  remove_silence: Literal["no", "spec", "mel", "mfcc"] = "no",
  silence_threshold_A: Optional[float] = None,
  silence_threshold_B: Optional[float] = None,
  dtw_radius: Optional[int] = 10,
) -> Tuple[float, float]:
  """
  Compares two amplitude spectrograms by computing the mean Mel-Cepstral Distance (MCD)
  and an alignment penalty. The function supports silence removal and alignment at
  different stages of the processing pipeline.

  Parameters
  ----------
  amp_spec_A : numpy.ndarray
      A 2D complex-valued amplitude spectrogram of shape (frames, frequency bins).
  amp_spec_B : numpy.ndarray
      A 2D complex-valued amplitude spectrogram of shape (frames, frequency bins).
  sample_rate : int
      Sampling rate of the audio signals in Hz. Must be > 0.
  n_fft : float
      FFT window length in milliseconds. Must be > 0.
  fmin : int, optional, default=0
      Minimum frequency (in Hz) for mel-band calculation. Must satisfy 0 <= fmin < fmax.
  fmax : int, optional, default=None
      Maximum frequency (in Hz) for mel-band calculation. If not set, defaults to
      sample_rate / 2. Must satisfy 0 < fmax <= sample_rate / 2.
  M : int, optional, default=20
      Number of mel filterbanks. Must be > 0.
  s : int, optional, default=1
      Starting index (inclusive) for MFCCs used in MCD calculation. Must be in [0, D).
  D : int, optional, default=16
      Number of MFCC coefficients considered for distance computation. Must satisfy
      D <= M.
  aligning : {'pad', 'dtw'}, optional, default='dtw'
      Alignment strategy. "pad" uses zero-padding; "dtw" uses Dynamic Time Warping.
      DTW is more accurate but computationally more expensive.
  align_target : {'spec', 'mel', 'mfcc'}, optional, default='spec'
      Spectral level at which alignment is applied. Determines at which stage silence
      can be removed.
  remove_silence : {'no', 'spec', 'mel', 'mfcc'}, optional, default='no'
      Stage at which silence is removed. "spec" applies thresholding to spectral frames,
      while "mel" and "mfcc" apply thresholding to mel-spectrograms or MFCCs,
      respectively. Silence is always removed before alignment.
  silence_threshold_A : float, optional
      Threshold used to detect silence in `amp_spec_A`, depending on the selected
      `remove_silence` strategy. For "spec", this applies to frame energy or amplitude.
  silence_threshold_B : float, optional
      Same as `silence_threshold_A`, but applied to `amp_spec_B`.
  dtw_radius : int, optional, default=10
      Sakoe-Chiba radius for DTW alignment. A value of 1 is fastest but less accurate.
      None allows unrestricted warping but is slowest. Must be >= 1 if specified.

  Returns
  -------
  Tuple[float, float]
      - Mean MCD over all selected coefficients.
      - Alignment penalty. Returns (nan, nan) if either input is empty or becomes empty
        due to silence removal.

  Raises
  ------
  ValueError
      If `amp_spec_A` or `amp_spec_B` does not have 2 dimensions.
  ValueError
      If the number of frequency bins in `amp_spec_A` and `amp_spec_B` do not match.
  ValueError
      If `n_fft` is not > 0 or does not match the number of frequency bins.
  ValueError
      If `sample_rate` is not > 0.
  ValueError
      If `fmin` is not in [0, fmax).
  ValueError
      If `fmax` is not in (0, sample_rate / 2].
  ValueError
      If `M` is not > 0.
  ValueError
      If `D` is not <= `M`.
  ValueError
      If `aligning` is not 'pad' or 'dtw'.
  ValueError
      If `remove_silence` is not 'no', 'spec', 'mel', or 'mfcc'.
  ValueError
      If `dtw_radius` is specified but not >= 1.
  ValueError
      If silence removal is enabled but `silence_threshold_A` or `silence_threshold_B`
      is not set.
  """
  if len(amp_spec_A.shape) != 2:
    raise ValueError(
      f"amplitude spectrogram A must have 2 dimensions but got {len(amp_spec_A.shape)}"
    )

  if len(amp_spec_B.shape) != 2:
    raise ValueError(
      f"amplitude spectrogram B must have 2 dimensions but got {len(amp_spec_B.shape)}"
    )

  if amp_spec_A.shape[0] == 0:
    logger = getLogger(__name__)
    logger.warning("spectrogram A is empty")
    return np.nan, np.nan

  if amp_spec_B.shape[0] == 0:
    logger = getLogger(__name__)
    logger.warning("spectrogram B is empty")
    return np.nan, np.nan

  if not amp_spec_A.shape[1] == amp_spec_B.shape[1]:
    raise ValueError(
      f"both spectrograms must have the same number of frequency bins "
      f"but got {amp_spec_A.shape[1]} != {amp_spec_B.shape[1]}"
    )

  assert amp_spec_A.shape[1] == amp_spec_B.shape[1]
  n_fft_bins = amp_spec_A.shape[1]

  if n_fft_bins == 0:
    raise ValueError("spectrograms must have at least 1 frequency bin")

  n_fft_samples = ms_to_samples(n_fft, sample_rate)
  if get_n_fft_bins(n_fft_samples) != n_fft_bins:
    raise ValueError(
      f"n_fft (in samples) // 2 + 1 must match the number of frequency bins "
      f"in the spectrogram but got {n_fft_samples // 2 + 1} != {n_fft_bins}"
    )
  assert n_fft_samples > 0
  assert sample_rate > 0

  if aligning not in ["pad", "dtw"]:
    raise ValueError("aligning must be 'pad' or 'dtw'")

  if remove_silence not in ["no", "spec", "mel", "mfcc"]:
    raise ValueError("remove_silence must be 'no', 'spec', 'mel' or 'mfcc'")

  if align_target == "spec":
    if remove_silence == "mel":
      raise ValueError(
        "cannot remove silence from mel-spectrogram "
        "after both spectrograms were aligned"
      )
    if remove_silence == "mfcc":
      raise ValueError(
        "cannot remove silence from MFCCs after both spectrograms were aligned"
      )

  if fmax is not None:
    if not 0 < fmax <= sample_rate // 2:
      raise ValueError(
        f"fmax must be in (0, sample_rate // 2], i.e., (0, {sample_rate // 2}]"
      )
  else:
    fmax = sample_rate // 2

  if not 0 <= fmin < fmax:
    raise ValueError(f"fmin must be in [0, fmax), i.e., [0, {fmax})")

  if not M > 0:
    raise ValueError("M must be > 0")

  if remove_silence == "spec":
    if silence_threshold_A is None:
      raise ValueError("silence_threshold_A must be set")
    if silence_threshold_B is None:
      raise ValueError("silence_threshold_B must be set")

    amp_spec_A = remove_silence_X_km(amp_spec_A, silence_threshold_A)
    amp_spec_B = remove_silence_X_km(amp_spec_B, silence_threshold_B)

    if amp_spec_A.shape[0] == 0:
      logger = getLogger(__name__)
      logger.warning("after removing silence, spectrogram A is empty")
      return np.nan, np.nan

    if amp_spec_B.shape[0] == 0:
      logger = getLogger(__name__)
      logger.warning("after removing silence, spectrogram B is empty")
      return np.nan, np.nan

    remove_silence = "no"

  penalty: float
  aligned_here: bool = False
  if align_target == "spec":
    if aligning == "dtw" and dtw_radius is not None and not dtw_radius >= 1:
      raise ValueError("dtw_radius must be None or greater than or equal to 1")
    amp_spec_A, amp_spec_B, penalty = align_X_km(
      amp_spec_A, amp_spec_B, aligning, dtw_radius
    )
    aligned_here = True
    align_target = "mel"
    aligning = "pad"

  # Mel-Bank - Shape: (N, #Frames)
  w_n_m = get_w_n_m(sample_rate, n_fft_samples, M, fmin, fmax)

  # Mel-Spectrogram - Shape: (#Frames, #N)
  X_kn_A = get_X_kn(amp_spec_A, w_n_m)
  X_kn_B = get_X_kn(amp_spec_B, w_n_m)

  mean_mcd_over_all_k, res_penalty = compare_mel_spectrograms(
    X_kn_A,
    X_kn_B,
    s=s,
    D=D,
    aligning=aligning,
    align_target=align_target,
    remove_silence=remove_silence,
    silence_threshold_A=silence_threshold_A,
    silence_threshold_B=silence_threshold_B,
    dtw_radius=dtw_radius,
  )

  if aligned_here:
    assert res_penalty == 0
  else:
    assert "penalty" not in locals()
    assert res_penalty is not None
    penalty = res_penalty

  return mean_mcd_over_all_k, penalty


def compare_mel_spectrograms(
  mel_spec_A: npt.NDArray,
  mel_spec_B: npt.NDArray,
  /,
  *,
  s: int = 1,
  D: int = 16,
  aligning: Literal["pad", "dtw"] = "dtw",
  align_target: Literal["mel", "mfcc"] = "mfcc",
  remove_silence: Literal["no", "mel", "mfcc"] = "no",
  silence_threshold_A: Optional[float] = None,
  silence_threshold_B: Optional[float] = None,
  dtw_radius: Optional[int] = 10,
) -> Tuple[float, float]:
  """
  Compares two mel-spectrograms by computing the mean Mel-Cepstral Distance (MCD)
  and an alignment penalty. Supports silence removal and alignment at different
  stages of the processing pipeline.

  Parameters
  ----------
  mel_spec_A : numpy.ndarray
      A 2D mel-spectrogram of shape (frames, mel bands).
  mel_spec_B : numpy.ndarray
      A 2D mel-spectrogram of shape (frames, mel bands).
  s : int, optional, default=1
      Starting index (inclusive) for MFCCs used in MCD calculation. Must be in [0, D).
  D : int, optional, default=16
      Number of MFCC coefficients considered for distance computation. Must satisfy
      D <= number of mel bands.
  aligning : {'pad', 'dtw'}, optional, default='dtw'
      Alignment strategy. "pad" uses zero-padding; "dtw" uses Dynamic Time Warping.
      DTW is more accurate but computationally more expensive.
  align_target : {'mel', 'mfcc'}, optional, default='mel'
      Spectral level at which alignment is applied. Determines at which stage silence
      should be removed.
  remove_silence : {'no', 'mel', 'mfcc'}, optional, default='no'
      Stage at which silence is removed. "mel" applies thresholding to mel-spectrogram
      frames, while "mfcc" applies thresholding to MFCCs. Silence is always removed
      before alignment.
  silence_threshold_A : float, optional
      Threshold used to detect silence in `mel_spec_A`, depending on the selected
      `remove_silence` strategy.
  silence_threshold_B : float, optional
      Same as `silence_threshold_A`, but applied to `mel_spec_B`.
  dtw_radius : int, optional, default=10
      Sakoe-Chiba radius for DTW alignment. A value of 1 is fastest but less accurate.
      None allows unrestricted warping but is slowest. Must be >= 1 if specified.

  Returns
  -------
  Tuple[float, float]
      - Mean MCD over all selected coefficients.
      - Alignment penalty.
      Returns (nan, nan) if either input is empty or becomes empty
        due to silence removal.

  Raises
  ------
  ValueError
      If `mel_spec_A` or `mel_spec_B` does not have 2 dimensions.
  ValueError
      If the number of mel bands in `mel_spec_A` and `mel_spec_B` do not match.
  ValueError
      If `D` is not <= number of mel bands.
  ValueError
      If `s` is not in [0, D).
  ValueError
      If `aligning` is not 'pad' or 'dtw'.
  ValueError
      If `remove_silence` is not 'no', 'mel', or 'mfcc'.
  ValueError
      If `align_target` is not 'mel' or 'mfcc'.
  ValueError
      If silence removal is enabled but `silence_threshold_A` or `silence_threshold_B`
      is not set.
  ValueError
      If `dtw_radius` is specified but not >= 1.

  Notes
  -----
  - The function assumes the input mel-spectrograms are precomputed and valid.
  - Silence removal is applied by thresholding the mel-spectrogram frames or MFCCs
    based on their energy.
  - Alignment is performed using either zero-padding or Dynamic Time Warping (DTW).
  - The resulting MCD is computed over the selected MFCC coefficients.
  """
  if not len(mel_spec_A.shape) == 2:
    raise ValueError(
      f"mel-spectrogram A must have 2 dimensions but got {len(mel_spec_A.shape)}"
    )

  if not len(mel_spec_B.shape) == 2:
    raise ValueError(
      f"mel-spectrogram B must have 2 dimensions but got {len(mel_spec_B.shape)}"
    )

  if len(mel_spec_A) == 0:
    logger = getLogger(__name__)
    logger.warning("mel-spectrogram A is empty")
    return np.nan, np.nan

  if len(mel_spec_B) == 0:
    logger = getLogger(__name__)
    logger.warning("mel-spectrogram B is empty")
    return np.nan, np.nan

  if not mel_spec_A.shape[1] == mel_spec_B.shape[1]:
    raise ValueError("both mel-spectrograms must have the same number of mel-bands")
  M = mel_spec_A.shape[1]

  if not M > 0:
    raise ValueError("mel-spectrograms must have at least 1 mel-band")

  if aligning not in ["pad", "dtw"]:
    raise ValueError("aligning must be 'pad' or 'dtw'")

  if remove_silence not in ["no", "mel", "mfcc"]:
    raise ValueError("remove_silence must be 'no', 'mel' or 'mfcc'")

  if align_target not in ["mel", "mfcc"]:
    raise ValueError("align_target must be 'mel' or 'mfcc'")

  if align_target == "mel" and remove_silence == "mfcc":
    raise ValueError(
      "cannot remove silence from MFCCs after both mel-spectrograms were aligned"
    )

  if D > M:
    raise ValueError(f"D must be <= number of mel-bands ({M})")

  if remove_silence == "mel":
    if silence_threshold_A is None:
      raise ValueError("silence_threshold_A must be set")
    if silence_threshold_B is None:
      raise ValueError("silence_threshold_B must be set")

    mel_spec_A = remove_silence_X_kn(mel_spec_A, silence_threshold_A)
    mel_spec_B = remove_silence_X_kn(mel_spec_B, silence_threshold_B)

    if mel_spec_A.shape[0] == 0:
      logger = getLogger(__name__)
      logger.warning("after removing silence, mel-spectrogram A is empty")
      return np.nan, np.nan

    if mel_spec_B.shape[0] == 0:
      logger = getLogger(__name__)
      logger.warning("after removing silence, mel-spectrogram B is empty")
      return np.nan, np.nan

    remove_silence = "no"

  penalty: float
  aligned_here: bool = False
  if align_target == "mel":
    if aligning == "dtw" and dtw_radius is not None and not dtw_radius >= 1:
      raise ValueError("dtw_radius must be None or greater than or equal to 1")
    mel_spec_A, mel_spec_B, penalty = align_X_kn(
      mel_spec_A, mel_spec_B, aligning, dtw_radius
    )
    aligned_here = True
    align_target = "mfcc"
    aligning = "pad"

  # Shape: (N, #Frames)
  MC_X_ik = get_MC_X_ik(mel_spec_A, M)
  MC_Y_ik = get_MC_X_ik(mel_spec_B, M)

  remove_silence_mfcc = remove_silence == "mfcc"

  mean_mcd_over_all_k, res_penalty = compare_mfccs(
    MC_X_ik,
    MC_Y_ik,
    s=s,
    D=D,
    aligning=aligning,
    remove_silence=remove_silence_mfcc,
    silence_threshold_A=silence_threshold_A,
    silence_threshold_B=silence_threshold_B,
    dtw_radius=dtw_radius,
  )

  if aligned_here:
    assert res_penalty == 0
  else:
    assert "penalty" not in locals()
    assert res_penalty is not None
    penalty = res_penalty

  return mean_mcd_over_all_k, penalty


def compare_mfccs(
  mfccs_A: npt.NDArray,
  mfccs_B: npt.NDArray,
  /,
  *,
  s: int = 1,
  D: int = 16,
  aligning: Literal["pad", "dtw"] = "dtw",
  remove_silence: bool = False,
  silence_threshold_A: Optional[float] = None,
  silence_threshold_B: Optional[float] = None,
  dtw_radius: Optional[int] = 10,
) -> Tuple[float, float]:
  """
  Compares two sets of MFCCs by computing the mean Mel-Cepstral Distance (MCD)
  and an alignment penalty. Supports silence removal and alignment using
  zero-padding or Dynamic Time Warping (DTW).

  Parameters
  ----------
  mfccs_A : numpy.ndarray
      A 2D array of MFCCs with shape (coefficients, frames).
  mfccs_B : numpy.ndarray
      A 2D array of MFCCs with shape (coefficients, frames).
  s : int, optional, default=1
      Starting index (inclusive) for MFCCs used in MCD calculation. Must be in [0, D).
  D : int, optional, default=16
      Number of MFCC coefficients considered for distance computation. Must satisfy
      D <= number of coefficients in `mfccs_A` and `mfccs_B`.
  aligning : {'pad', 'dtw'}, optional, default='dtw'
      Alignment strategy. "pad" uses zero-padding; "dtw" uses Dynamic Time Warping.
      DTW is more accurate but computationally more expensive.
  remove_silence : bool, optional, default=False
      If True, removes silence from the MFCCs based on the `silence_threshold_A`
      and `silence_threshold_B` parameters.
  silence_threshold_A : float, optional
      Threshold used to detect silence in `mfccs_A`.
  silence_threshold_B : float, optional
      Threshold used to detect silence in `mfccs_B`.
  dtw_radius : int, optional, default=10
      Sakoe-Chiba radius for DTW alignment. A value of 1 is fastest but less accurate.
      None allows unrestricted warping but is slowest. Must be >= 1 if specified.

  Returns
  -------
  Tuple[float, float]
      - Mean MCD over all selected coefficients.
      - Alignment penalty. Returns (nan, nan) if either input is empty or becomes empty
        due to silence removal.

  Raises
  ------
  ValueError
      If `mfccs_A` or `mfccs_B` does not have 2 dimensions.
  ValueError
      If the number of coefficients in `mfccs_A` and `mfccs_B` do not match.
  ValueError
      If `D` is not <= number of coefficients in `mfccs_A` and `mfccs_B`.
  ValueError
      If `s` is not in [0, D).
  ValueError
      If `aligning` is not 'pad' or 'dtw'.
  ValueError
      If silence removal is enabled but `silence_threshold_A` or `silence_threshold_B`
      is not set.
  ValueError
      If `dtw_radius` is specified but not >= 1.

  Notes
  -----
  - The function assumes the input MFCCs are precomputed and valid.
  - Silence removal is applied by thresholding the MFCC frames based on their energy.
  - Alignment is performed using either zero-padding or Dynamic Time Warping (DTW).
  - The resulting MCD is computed over the selected MFCC coefficients.
  """
  if not len(mfccs_A.shape) == 2:
    raise ValueError(f"MFCCs A must have 2 dimensions but got {len(mfccs_A.shape)}")

  if not len(mfccs_B.shape) == 2:
    raise ValueError(f"MFCCs B must have 2 dimensions but got {len(mfccs_B.shape)}")

  if mfccs_A.shape[1] == 0:
    logger = getLogger(__name__)
    logger.warning("MFCCs A are empty")
    return np.nan, np.nan

  if mfccs_B.shape[1] == 0:
    logger = getLogger(__name__)
    logger.warning("MFCCs B are empty")
    return np.nan, np.nan

  if not mfccs_A.shape[0] == mfccs_B.shape[0]:
    raise ValueError("both MFCCs must have the same number of coefficients")

  M = mfccs_A.shape[0]

  if not M > 0:
    raise ValueError("MFCCs must have at least 1 coefficient")

  if not D <= M:
    raise ValueError(f"D must be <= number of MFCC coefficients ({M})")

  if not 0 <= s < D:
    raise ValueError("s must be in [0, D)")

  assert D >= 1

  if aligning not in ["pad", "dtw"]:
    raise ValueError("aligning must be 'pad' or 'dtw'")

  if remove_silence:
    if silence_threshold_A is None:
      raise ValueError("silence_threshold_A must be set")
    if silence_threshold_B is None:
      raise ValueError("silence_threshold_B must be set")

    mfccs_A = remove_silence_MC_X_ik(mfccs_A, silence_threshold_A)
    mfccs_B = remove_silence_MC_X_ik(mfccs_B, silence_threshold_B)

    if mfccs_A.shape[1] == 0:
      logger = getLogger(__name__)
      logger.warning("after removing silence, MFCCs A are empty")
      return np.nan, np.nan

    if mfccs_B.shape[1] == 0:
      logger = getLogger(__name__)
      logger.warning("after removing silence, MFCCs B are empty")
      return np.nan, np.nan

  if aligning == "dtw" and dtw_radius is not None and not dtw_radius >= 1:
    raise ValueError("dtw_radius must be None or greater than or equal to 1")

  mfccs_A, mfccs_B, penalty = align_MC_s_D(mfccs_A, mfccs_B, s, D, aligning, dtw_radius)

  MCD_k = get_MCD_k(mfccs_A, mfccs_B, s, D)
  mean_mcd_over_all_k = get_average_MCD(MCD_k)

  return mean_mcd_over_all_k, penalty
