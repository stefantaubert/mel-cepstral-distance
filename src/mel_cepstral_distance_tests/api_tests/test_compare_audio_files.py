import os
import pickle
from logging import getLogger
from pathlib import Path
from tempfile import NamedTemporaryFile

import numpy as np
import pytest
from scipy.io import wavfile

from mel_cepstral_distance.api import compare_audio_files
from mel_cepstral_distance.helper import resample_if_necessary, samples_to_ms

TEST_DIR = Path("src/mel_cepstral_distance_tests/api_tests")

AUDIO_A = TEST_DIR / "A.wav"
AUDIO_B = TEST_DIR / "B.wav"


def test_uint8_8bitPCM() -> None:
  with NamedTemporaryFile(
    suffix=".wav", delete=False, prefix="test_compare_audio_files"
  ) as file_a_tmp:
    audio_a_tmp_path = Path(file_a_tmp.name)

  with NamedTemporaryFile(
    suffix=".wav", delete=False, prefix="test_compare_audio_files"
  ) as file_b_tmp:
    audio_b_tmp_path = Path(file_b_tmp.name)

  try:
    sr_a, audio_a = wavfile.read(AUDIO_A)
    assert sr_a == 22050
    assert audio_a.dtype == np.int16

    norm_audio = audio_a / 32768.0
    new_audio = ((norm_audio + 1) * 127.5).astype(np.uint8)
    wavfile.write(audio_a_tmp_path, 22050, new_audio)

    sr_b, audio_b = wavfile.read(AUDIO_B)
    assert sr_b == 22050
    assert audio_b.dtype == np.int16

    norm_audio = audio_b / 32768.0
    new_audio = ((norm_audio + 1) * 127.5).astype(np.uint8)
    wavfile.write(audio_b_tmp_path, 22050, new_audio)

    test_cases = [
      (AUDIO_A, AUDIO_B),  # 16 bit vs 8 bit
      (AUDIO_A, audio_b_tmp_path),  # 16 bit vs 8 bit
      (audio_a_tmp_path, AUDIO_B),  # 16 bit vs 8 bit
      (audio_a_tmp_path, audio_b_tmp_path),  # 16 bit vs 8 bit
    ]

    test_results = []

    for a, b in test_cases:
      mcd, pen = compare_audio_files(
        a,
        b,
        sample_rate=22050,
        align_target="mel",
        aligning="dtw",
        remove_silence="no",
        norm_audio=False,
        M=20,
        s=1,
        D=16,
        fmin=0,
        fmax=8000,
        n_fft=32,
        win_len=32,
        hop_len=16,
        window="hanning",
        dtw_radius=1,
      )
      test_results.append([mcd, pen])

    assert_results = [
      [7.64104558175767, 0.14414414414414423],
      [15.955726033561426, 0.16617210682492578],
      [19.39442751788282, 0.06269592476489039],
      [3.8681248602509037, 0.33870967741935476],
    ]

    np.testing.assert_almost_equal(test_results, assert_results)

  finally:
    if audio_a_tmp_path.exists():
      os.remove(audio_a_tmp_path)
    if audio_b_tmp_path.exists():
      os.remove(audio_b_tmp_path)


def test_float32_32bitFloat() -> None:
  with NamedTemporaryFile(
    suffix=".wav", delete=False, prefix="test_compare_audio_files"
  ) as file_a_tmp:
    audio_a_tmp_path = Path(file_a_tmp.name)

  with NamedTemporaryFile(
    suffix=".wav", delete=False, prefix="test_compare_audio_files"
  ) as file_b_tmp:
    audio_b_tmp_path = Path(file_b_tmp.name)

  try:
    sr_a, audio_a = wavfile.read(AUDIO_A)
    assert sr_a == 22050
    assert audio_a.dtype == np.int16

    norm_audio = audio_a / 32768.0
    new_audio = norm_audio.astype(np.float32)
    wavfile.write(audio_a_tmp_path, 22050, new_audio)

    sr_b, audio_b = wavfile.read(AUDIO_B)
    assert sr_b == 22050
    assert audio_b.dtype == np.int16

    norm_audio = audio_b / 32768.0
    new_audio = norm_audio.astype(np.float32)
    wavfile.write(audio_b_tmp_path, 22050, new_audio)

    test_cases = [
      (AUDIO_A, AUDIO_B),  # 16 bit vs 32 bit
      (AUDIO_A, audio_b_tmp_path),  # 16 bit vs 32 bit
      (audio_a_tmp_path, AUDIO_B),  # 16 bit vs 32 bit
      (audio_a_tmp_path, audio_b_tmp_path),  # 16 bit vs 32 bit
    ]

    test_results = []

    for a, b in test_cases:
      mcd, pen = compare_audio_files(
        a,
        b,
        sample_rate=22050,
        align_target="mel",
        aligning="dtw",
        remove_silence="no",
        norm_audio=False,
        M=20,
        s=1,
        D=16,
        fmin=0,
        fmax=8000,
        n_fft=32,
        win_len=32,
        hop_len=16,
        window="hanning",
        dtw_radius=1,
      )
      test_results.append([mcd, pen])

    assert_results = [
      [7.64104558175767, 0.14414414414414423],
      [8.386707066033125, 0.044303797468354444],
      [8.402813719266112, 0.044303797468354444],
      [7.641045506653429, 0.14414414414414423],
    ]

    np.testing.assert_almost_equal(test_results, assert_results)

  finally:
    if audio_a_tmp_path.exists():
      os.remove(audio_a_tmp_path)
    if audio_b_tmp_path.exists():
      os.remove(audio_b_tmp_path)


def test_int32_32bitPCM() -> None:
  with NamedTemporaryFile(
    suffix=".wav", delete=False, prefix="test_compare_audio_files"
  ) as file_a_tmp:
    audio_a_tmp_path = Path(file_a_tmp.name)

  with NamedTemporaryFile(
    suffix=".wav", delete=False, prefix="test_compare_audio_files"
  ) as file_b_tmp:
    audio_b_tmp_path = Path(file_b_tmp.name)

  try:
    sr_a, audio_a = wavfile.read(AUDIO_A)
    assert sr_a == 22050
    assert audio_a.dtype == np.int16

    norm_audio = audio_a / 32768.0
    new_audio = (norm_audio * 2147483647).astype(np.int32)
    wavfile.write(audio_a_tmp_path, 22050, new_audio)

    sr_b, audio_b = wavfile.read(AUDIO_B)
    assert sr_b == 22050
    assert audio_b.dtype == np.int16

    norm_audio = audio_b / 32768.0
    new_audio = norm_audio.astype(np.float32)
    wavfile.write(audio_b_tmp_path, 22050, new_audio)

    test_cases = [
      (AUDIO_A, AUDIO_B),  # 16 bit vs 32 bit
      (AUDIO_A, audio_b_tmp_path),  # 16 bit vs 32 bit
      (audio_a_tmp_path, AUDIO_B),  # 16 bit vs 32 bit
      (audio_a_tmp_path, audio_b_tmp_path),  # 16 bit vs 32 bit
    ]

    test_results = []

    for a, b in test_cases:
      mcd, pen = compare_audio_files(
        a,
        b,
        sample_rate=22050,
        align_target="mel",
        aligning="dtw",
        remove_silence="no",
        norm_audio=False,
        M=20,
        s=1,
        D=16,
        fmin=0,
        fmax=8000,
        n_fft=32,
        win_len=32,
        hop_len=16,
        window="hanning",
        dtw_radius=1,
      )
      test_results.append([mcd, pen])

    assert_results = [
      [7.64104558175767, 0.14414414414414423],
      [8.386707066033125, 0.044303797468354444],
      [8.386707040162092, 0.044303797468354444],
      [8.386707040119276, 0.044303797468354444],
    ]

    np.testing.assert_almost_equal(test_results, assert_results)

  finally:
    if audio_a_tmp_path.exists():
      os.remove(audio_a_tmp_path)
    if audio_b_tmp_path.exists():
      os.remove(audio_b_tmp_path)


def test_diff_sr_resamples_to_smaller_sr() -> None:
  new_sr = 16000
  assert_mcd = 7.7502037992418265
  assert_pen = 0.16913946587537088

  # create tmp file with different sample rate
  with NamedTemporaryFile(
    suffix=".wav", delete=False, prefix="test_compare_audio_files"
  ) as file_a_tmp:
    audio_a_tmp_path = Path(file_a_tmp.name)

  with NamedTemporaryFile(
    suffix=".wav", delete=False, prefix="test_compare_audio_files"
  ) as file_b_tmp:
    audio_b_tmp_path = Path(file_b_tmp.name)

  try:
    sr_a, audio_a = wavfile.read(AUDIO_A)
    assert sr_a == 22050

    resampled_audio = resample_if_necessary(audio_a, sr_a, new_sr)
    wavfile.write(audio_a_tmp_path, new_sr, resampled_audio)

    sr_b, audio_b = wavfile.read(AUDIO_B)
    assert sr_b == 22050

    resampled_audio = resample_if_necessary(audio_b, sr_b, new_sr)
    wavfile.write(audio_b_tmp_path, new_sr, resampled_audio)

    for a, b, should_be_assert_result in [
      (AUDIO_A, audio_b_tmp_path, True),  # 16000 Hz vs 22050 Hz
      (audio_a_tmp_path, AUDIO_B, True),  # 22050 Hz vs 16000 Hz
      (audio_a_tmp_path, audio_b_tmp_path, True),  # 16000 Hz vs 16000 Hz
      (AUDIO_A, AUDIO_B, False),  # 22050 Hz vs 22050 Hz
    ]:
      # set default params
      mcd, pen = compare_audio_files(
        a,
        b,
        sample_rate=None,
        align_target="mel",
        aligning="dtw",
        remove_silence="no",
        norm_audio=True,
        M=20,
        s=1,
        D=16,
        fmin=0,
        fmax=new_sr // 2,
        n_fft=32,
        win_len=32,
        hop_len=16,
        window="hanning",
        dtw_radius=1,
      )

      if should_be_assert_result:
        np.testing.assert_almost_equal(mcd, assert_mcd)
        np.testing.assert_almost_equal(pen, assert_pen)
      else:
        with np.testing.assert_raises(AssertionError):
          np.testing.assert_almost_equal(mcd, assert_mcd)
          np.testing.assert_almost_equal(pen, assert_pen)

  finally:
    if audio_a_tmp_path.exists():
      os.remove(audio_a_tmp_path)
    if audio_b_tmp_path.exists():
      os.remove(audio_b_tmp_path)


def test_aligning_with_pad_returns_same_for_spec_mel_mfcc() -> None:
  res = []
  for align_target in ["spec", "mel", "mfcc"]:
    mcd, pen = compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      align_target=align_target,
      aligning="pad",
      dtw_radius=None,
      sample_rate=22050,
      remove_silence="no",
      norm_audio=True,
      M=20,
      s=1,
      D=16,
      fmin=0,
      fmax=8000,
      n_fft=32,
      win_len=32,
      hop_len=16,
      window="hanning",
    )
    res.append((mcd, pen))
  np.testing.assert_almost_equal(res[0], res[1])
  np.testing.assert_almost_equal(res[0], res[2])
  np.testing.assert_almost_equal(res[1], res[2])


def test_result_changes_after_silence_removal_before_padding_spec() -> None:
  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    align_target="spec",
    aligning="pad",
    dtw_radius=None,
    remove_silence="sig",
    silence_threshold_A=0.01,
    silence_threshold_B=0.01,
    sample_rate=22050,
    norm_audio=True,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  mcd2, pen2 = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    align_target="spec",
    aligning="pad",
    dtw_radius=None,
    remove_silence="no",
    sample_rate=22050,
    norm_audio=True,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )

  assert not np.allclose(mcd, mcd2)
  assert not np.allclose(pen, pen2)


def test_result_changes_after_silence_removal_before_padding_mel() -> None:
  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    align_target="mel",
    aligning="pad",
    dtw_radius=None,
    remove_silence="spec",
    silence_threshold_A=0.01,
    silence_threshold_B=0.01,
    sample_rate=22050,
    norm_audio=True,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  mcd2, pen2 = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    align_target="mel",
    aligning="pad",
    dtw_radius=None,
    remove_silence="no",
    sample_rate=22050,
    norm_audio=True,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )

  assert not np.allclose(mcd, mcd2)
  assert not np.allclose(pen, pen2)


def test_result_changes_after_silence_removal_before_padding_mfcc() -> None:
  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    align_target="mfcc",
    aligning="pad",
    dtw_radius=None,
    remove_silence="mel",
    silence_threshold_A=0.01,
    silence_threshold_B=0.01,
    sample_rate=22050,
    norm_audio=True,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  mcd2, pen2 = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    align_target="mfcc",
    aligning="pad",
    dtw_radius=None,
    remove_silence="no",
    sample_rate=22050,
    norm_audio=True,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )

  assert not np.allclose(mcd, mcd2)
  assert not np.allclose(pen, pen2)


def test_same_file_returns_zero() -> None:
  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_A,
    align_target="mel",
    aligning="dtw",
    dtw_radius=1,
    remove_silence="no",
    sample_rate=22050,
    norm_audio=True,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  assert mcd == 0
  assert pen == 0


def test_invalid_silence_removal_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, remove_silence="none")


def test_invalid_aligning_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, aligning="none")


def test_invalid_align_target_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, align_target="none")


def test_invalid_sample_rate_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, sample_rate=0)


def test_invalid_n_fft_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, n_fft=0)


def test_invalid_win_len_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, win_len=0)


def test_invalid_hop_len_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, hop_len=0)


def test_invalid_window_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, window="none")


def test_invalid_fmin_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, fmin=-1)


def test_invalid_fmax_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, fmax=0)


def test_invalid_remove_silence_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, remove_silence="none")


def test_invalid_radius_raises_error() -> None:
  with pytest.raises(
    ValueError, match="dtw_radius must be None or greater than or equal to 1"
  ):
    compare_audio_files(AUDIO_A, AUDIO_B, aligning="dtw", dtw_radius=0)


def test_no_silence_threshold_raises_error() -> None:
  # A None
  with pytest.raises(ValueError):
    compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      remove_silence="sig",
      silence_threshold_A=None,
      silence_threshold_B=0.01,
    )

  with pytest.raises(ValueError):
    compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      remove_silence="spec",
      silence_threshold_A=None,
      silence_threshold_B=0.01,
    )

  with pytest.raises(ValueError):
    compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      remove_silence="mel",
      silence_threshold_A=None,
      silence_threshold_B=0.01,
    )

  with pytest.raises(ValueError):
    compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      remove_silence="mfcc",
      silence_threshold_A=None,
      silence_threshold_B=0.01,
    )
  # B None
  with pytest.raises(ValueError):
    compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      remove_silence="sig",
      silence_threshold_A=0.01,
      silence_threshold_B=None,
    )

  with pytest.raises(ValueError):
    compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      remove_silence="spec",
      silence_threshold_A=0.01,
      silence_threshold_B=None,
    )

  with pytest.raises(ValueError):
    compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      remove_silence="mel",
      silence_threshold_A=0.01,
      silence_threshold_B=None,
    )

  with pytest.raises(ValueError):
    compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      remove_silence="mfcc",
      silence_threshold_A=0.01,
      silence_threshold_B=None,
    )


def test_removing_silence_from_sig_too_hard_returns_nan_nan() -> None:
  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    remove_silence="sig",
    silence_threshold_A=10000,
    silence_threshold_B=0,
    align_target="mel",
    aligning="dtw",
    dtw_radius=1,
    norm_audio=False,
    sample_rate=22050,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)

  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    remove_silence="sig",
    silence_threshold_A=0,
    silence_threshold_B=10000,
    align_target="mel",
    aligning="dtw",
    dtw_radius=1,
    norm_audio=False,
    sample_rate=22050,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)

  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    remove_silence="sig",
    silence_threshold_A=10000,
    silence_threshold_B=10000,
    align_target="mel",
    aligning="dtw",
    dtw_radius=1,
    norm_audio=False,
    sample_rate=22050,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)


def test_removing_silence_from_spec_too_hard_returns_nan_nan() -> None:
  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    remove_silence="spec",
    silence_threshold_A=100000,
    silence_threshold_B=-100000,
    align_target="mel",
    aligning="dtw",
    dtw_radius=1,
    norm_audio=False,
    sample_rate=22050,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)

  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    remove_silence="spec",
    silence_threshold_A=-100000,
    silence_threshold_B=100000,
    align_target="mel",
    aligning="dtw",
    dtw_radius=1,
    norm_audio=False,
    sample_rate=22050,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)

  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    remove_silence="spec",
    silence_threshold_A=100000,
    silence_threshold_B=100000,
    align_target="mel",
    aligning="dtw",
    dtw_radius=1,
    norm_audio=False,
    sample_rate=22050,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)


def test_removing_silence_from_mel_too_hard_returns_nan_nan() -> None:
  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    remove_silence="mel",
    silence_threshold_A=100000,
    silence_threshold_B=-100000,
    align_target="mel",
    aligning="dtw",
    dtw_radius=1,
    norm_audio=False,
    sample_rate=22050,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)

  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    remove_silence="mel",
    silence_threshold_A=-100000,
    silence_threshold_B=100000,
    align_target="mel",
    aligning="dtw",
    dtw_radius=1,
    norm_audio=False,
    sample_rate=22050,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)

  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    remove_silence="mel",
    silence_threshold_A=100000,
    silence_threshold_B=100000,
    align_target="mel",
    aligning="dtw",
    dtw_radius=1,
    norm_audio=False,
    sample_rate=22050,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)


def test_removing_silence_from_mfcc_too_hard_returns_nan_nan() -> None:
  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    remove_silence="mfcc",
    silence_threshold_A=100000,
    silence_threshold_B=-100000,
    align_target="mfcc",
    aligning="dtw",
    dtw_radius=1,
    norm_audio=False,
    sample_rate=22050,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)

  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    remove_silence="mfcc",
    silence_threshold_A=-100000,
    silence_threshold_B=100000,
    align_target="mfcc",
    aligning="dtw",
    dtw_radius=1,
    norm_audio=False,
    sample_rate=22050,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)

  mcd, pen = compare_audio_files(
    AUDIO_A,
    AUDIO_B,
    remove_silence="mfcc",
    silence_threshold_A=100000,
    silence_threshold_B=100000,
    align_target="mfcc",
    aligning="dtw",
    dtw_radius=1,
    norm_audio=False,
    sample_rate=22050,
    M=20,
    s=1,
    D=16,
    fmin=0,
    fmax=8000,
    n_fft=32,
    win_len=32,
    hop_len=16,
    window="hanning",
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)


def test_invalid_sig_sil_thres_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      remove_silence="sig",
      silence_threshold_A=-1,
      silence_threshold_B=0,
    )

  with pytest.raises(ValueError):
    compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      remove_silence="sig",
      silence_threshold_A=0,
      silence_threshold_B=-1,
    )

  with pytest.raises(ValueError):
    compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      remove_silence="sig",
      silence_threshold_A=-1,
      silence_threshold_B=-1,
    )


def test_removing_silence_after_aligning_raises_error() -> None:
  # mel after spec was aligned
  with pytest.raises(ValueError):
    compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      remove_silence="mel",
      silence_threshold_A=0.01,
      silence_threshold_B=1,
      align_target="spec",
      aligning="dtw",
      dtw_radius=1,
    )

  # mfcc after spec was aligned
  with pytest.raises(ValueError):
    compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      remove_silence="mfcc",
      silence_threshold_A=0.01,
      silence_threshold_B=0.01,
      align_target="spec",
      aligning="dtw",
      dtw_radius=1,
    )

  # mfcc after mel was aligned
  with pytest.raises(ValueError):
    compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      remove_silence="mfcc",
      silence_threshold_A=0.01,
      silence_threshold_B=0.01,
      align_target="mel",
      aligning="dtw",
      dtw_radius=1,
    )


def test_D_greater_than_M_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, M=10, D=11)


def test_invalid_D_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, D=0)

  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, D=1)


def test_invalid_M_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, M=0)


def test_invalid_s_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, s=-1)


def test_s_equals_D_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, s=12, D=12)


def test_s_bigger_than_D_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_files(AUDIO_A, AUDIO_B, s=13, D=12)


def test_empty_audio_returns_nan_nan() -> None:
  # create empty audio in tmp dir
  with NamedTemporaryFile(
    suffix=".wav", delete=False, prefix="test_compare_audio_files"
  ) as f:
    empty_audio_path = Path(f.name)

  try:
    data = np.array([], dtype=np.int16)
    wavfile.write(empty_audio_path, 22050, data)

    mcd, pen = compare_audio_files(
      AUDIO_A,
      empty_audio_path,
      sample_rate=22050,
      n_fft=512,
      win_len=512,
      hop_len=512,
      window="hanning",
      fmin=0,
      fmax=8000,
      M=80,
      s=1,
      D=13,
      norm_audio=True,
      align_target="mel",
      aligning="dtw",
      remove_silence="no",
      dtw_radius=1,
    )
    assert np.isnan(mcd)
    assert np.isnan(pen)

    mcd, pen = compare_audio_files(
      empty_audio_path,
      AUDIO_B,
      sample_rate=22050,
      n_fft=512,
      win_len=512,
      hop_len=512,
      window="hanning",
      fmin=0,
      fmax=8000,
      M=80,
      s=1,
      D=13,
      norm_audio=True,
      align_target="mel",
      aligning="dtw",
      remove_silence="no",
      dtw_radius=1,
    )
    assert np.isnan(mcd)
    assert np.isnan(pen)

    mcd, pen = compare_audio_files(
      empty_audio_path,
      empty_audio_path,
      sample_rate=22050,
      n_fft=512,
      win_len=512,
      hop_len=512,
      window="hanning",
      fmin=0,
      fmax=8000,
      M=80,
      s=1,
      D=13,
      norm_audio=True,
      align_target="mel",
      aligning="dtw",
      remove_silence="no",
      dtw_radius=1,
    )
    assert np.isnan(mcd)
    assert np.isnan(pen)

  finally:
    if empty_audio_path.exists():
      os.remove(empty_audio_path)


def create_other_outputs() -> None:
  size512 = samples_to_ms(512, 22050)
  size128 = samples_to_ms(128, 22050)

  targets = []

  # sample rate
  for sr in [None, 22050, 16000, 8000, 4000]:
    sr_val = 22050 if sr is None else sr

    targets.append(
      (
        sr,
        samples_to_ms(512, sr_val),
        samples_to_ms(512, sr_val),
        samples_to_ms(128, sr_val),
        "hanning",
        0,
        sr_val // 2,
        80,
        1,
        13,
        True,
        1,
      )
    )

  # n_fft, win_len, hop_len
  for n_ffts, win_lens, hop_lens in [
    (512, 512, 256),  # win len == nfft
    (512, 256, 256),  # win len < nfft
    (512, 1024, 256),  # win len > nfft
    (512, 512, 128),
    (1024, 1024, 128),
    (1025, 1025, 129),  # odd
    (1023, 1023, 127),  # odd
  ]:
    targets.append(
      (
        22050,
        samples_to_ms(n_ffts, 22050),
        samples_to_ms(win_lens, 22050),
        samples_to_ms(hop_lens, 22050),
        "hanning",
        0,
        8000,
        80,
        1,
        13,
        True,
        1,
      )
    )

  # fmax
  targets.extend(
    [
      (22050, size512, size512, size128, "hanning", 0, fmax, 80, 1, 13, True, 1)
      for fmax in [None, 8000, 6000, 4000, 2000]
    ]
  )

  # fmin
  targets.extend(
    [
      (22050, size512, size512, size128, "hanning", fmin, 8000, 80, 1, 13, True, 1)
      for fmin in [0, 1000, 2000, 4000]
    ]
  )

  # window
  for window in ["hanning", "hamming"]:
    targets.extend(
      [(22050, size512, size512, size128, window, 0, 8000, 80, 1, 13, True, 1)]
    )

  # norm
  targets.extend(
    [
      (22050, size512, size512, size128, "hanning", 0, 8000, 80, 1, 13, norm, 1)
      for norm in [True, False]
    ]
  )

  # N
  targets.extend(
    [(22050, size512, size512, size128, "hanning", 0, 8000, n, 1, 13, True, 1)]
    for n in [20, 40, 60, 80]
  )

  # s, D
  for s, d in [
    (0, 1),
    (0, 1),
    (0, 2),
    (0, 5),
    (0, 13),
    (0, 16),
    (0, 80),
    (1, 2),
    (1, 5),
    (1, 13),
    (1, 16),
    (1, 80),
    (2, 3),
    (2, 13),
    (2, 80),
    (79, 80),
  ]:
    targets.append(
      (22050, size512, size512, size128, "hanning", 0, 8000, 80, s, d, True, 1)
    )

  # dtw_radius
  targets.extend(
    [
      (
        22050,
        size512,
        size512,
        size128,
        "hanning",
        0,
        8000,
        80,
        1,
        13,
        True,
        dtw_radius,
      )
      for dtw_radius in [1, 10, 20, None]
    ]
  )

  targets.extend(
    [
      (22050, size512, size512, size128, "hanning", 0, 8000, 1, 0, 1, True, 1),
      (22050, size512, size512, size128, "hanning", 0, 8000, 2, 1, 2, True, 1),
    ]
  )

  outputs = []

  for (
    sample_rate,
    n_fft,
    win_len,
    hop_len,
    window,
    fmin,
    fmax,
    n,
    s,
    d,
    norm,
    dtw_radius,
  ) in targets:
    mcd, pen = compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      sample_rate=sample_rate,
      n_fft=n_fft,
      win_len=win_len,
      hop_len=hop_len,
      window=window,
      fmin=fmin,
      fmax=fmax,
      M=n,
      s=s,
      D=d,
      norm_audio=norm,
      align_target="mel",
      aligning="dtw",
      remove_silence="no",
      dtw_radius=dtw_radius,
    )
    outputs.append(
      (
        sample_rate,
        n_fft,
        win_len,
        hop_len,
        window,
        fmin,
        fmax,
        n,
        s,
        d,
        norm,
        dtw_radius,
        mcd,
        pen,
      )
    )

  logger = getLogger(__name__)
  for vals in outputs:
    logger.info("\t".join(str(i) for i in vals))
  (TEST_DIR / "test_compare_audio_files_other.pkl").write_bytes(pickle.dumps(outputs))


def test_other_outputs() -> None:
  outputs = pickle.loads((TEST_DIR / "test_compare_audio_files_other.pkl").read_bytes())
  for (
    sample_rate,
    n_fft,
    win_len,
    hop_len,
    window,
    fmin,
    fmax,
    n,
    s,
    d,
    norm,
    dtw_radius,
    expected_mcd,
    expected_pen,
  ) in outputs:
    mcd, pen = compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      sample_rate=sample_rate,
      n_fft=n_fft,
      win_len=win_len,
      hop_len=hop_len,
      window=window,
      fmin=fmin,
      fmax=fmax,
      M=n,
      s=s,
      D=d,
      norm_audio=norm,
      align_target="mel",
      aligning="dtw",
      remove_silence="no",
      dtw_radius=dtw_radius,
    )
    np.testing.assert_almost_equal(mcd, expected_mcd)
    np.testing.assert_almost_equal(pen, expected_pen)


def create_sil_outputs() -> None:
  sig_sil = 0.001
  spec_sil = 0.001
  mel_sil = -7
  mfcc_sil = 0.001

  targets = [
    ("no", None, None, "pad", "spec", None),
    ("no", None, None, "pad", "mel", None),
    ("no", None, None, "pad", "mfcc", None),
    ("sig", sig_sil, sig_sil, "pad", "spec", None),
    ("sig", sig_sil, sig_sil, "pad", "mel", None),
    ("sig", sig_sil, sig_sil, "pad", "mfcc", None),
    ("spec", spec_sil, spec_sil, "pad", "spec", None),
    ("spec", spec_sil, spec_sil, "pad", "mel", None),
    ("spec", spec_sil, spec_sil, "pad", "mfcc", None),
    ("mel", mel_sil, mel_sil, "pad", "mel", None),
    ("mel", mel_sil, mel_sil, "pad", "mfcc", None),
    ("mfcc", mfcc_sil, mfcc_sil, "pad", "mfcc", None),
  ]
  for dtw_radius in [1, 20]:
    targets.extend(
      [
        ("no", None, None, "dtw", "spec", dtw_radius),
        ("no", None, None, "dtw", "mel", dtw_radius),
        ("no", None, None, "dtw", "mfcc", dtw_radius),
        ("sig", sig_sil, sig_sil, "dtw", "spec", dtw_radius),
        ("sig", sig_sil, sig_sil, "dtw", "mel", dtw_radius),
        ("sig", sig_sil, sig_sil, "dtw", "mfcc", dtw_radius),
        ("spec", spec_sil, spec_sil, "dtw", "spec", dtw_radius),
        ("spec", spec_sil, spec_sil, "dtw", "mel", dtw_radius),
        ("spec", spec_sil, spec_sil, "dtw", "mfcc", dtw_radius),
        ("mel", mel_sil, mel_sil, "dtw", "mel", dtw_radius),
        ("mel", mel_sil, mel_sil, "dtw", "mfcc", dtw_radius),
        ("mfcc", mfcc_sil, mfcc_sil, "dtw", "mfcc", dtw_radius),
      ]
    )

  outputs = []

  for remove_silence, sil_a, sil_b, aligning, target, dtw_radius in targets:
    mcd, pen = compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      sample_rate=22050,
      n_fft=samples_to_ms(512, 22050),
      win_len=samples_to_ms(512, 22050),
      hop_len=samples_to_ms(512 // 4, 22050),
      align_target=target,
      aligning=aligning,
      remove_silence=remove_silence,
      silence_threshold_A=sil_a,
      silence_threshold_B=sil_b,
      dtw_radius=dtw_radius,
      norm_audio=True,
      M=20,
      s=1,
      D=16,
      fmin=0,
      fmax=22050 // 2,
      window="hanning",
    )
    outputs.append(
      (remove_silence, sil_a, sil_b, aligning, target, dtw_radius, mcd, pen)
    )

  logger = getLogger(__name__)
  for vals in outputs:
    logger.info("\t".join(str(i) for i in vals))
  (TEST_DIR / "test_compare_audio_files_sil.pkl").write_bytes(pickle.dumps(outputs))


def test_sil_outputs() -> None:
  outputs = pickle.loads((TEST_DIR / "test_compare_audio_files_sil.pkl").read_bytes())
  for (
    remove_silence,
    sil_a,
    sil_b,
    aligning,
    target,
    dtw_radius,
    expected_mcd,
    expected_pen,
  ) in outputs:
    mcd, pen = compare_audio_files(
      AUDIO_A,
      AUDIO_B,
      sample_rate=22050,
      n_fft=samples_to_ms(512, 22050),
      win_len=samples_to_ms(512, 22050),
      hop_len=samples_to_ms(512 // 4, 22050),
      align_target=target,
      aligning=aligning,
      remove_silence=remove_silence,
      silence_threshold_A=sil_a,
      silence_threshold_B=sil_b,
      dtw_radius=dtw_radius,
      norm_audio=True,
      M=20,
      s=1,
      D=16,
      fmin=0,
      fmax=22050 // 2,
      window="hanning",
    )
    np.testing.assert_almost_equal(mcd, expected_mcd)
    np.testing.assert_almost_equal(pen, expected_pen)


if __name__ == "__main__":
  create_other_outputs()
  create_sil_outputs()
