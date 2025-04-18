import pickle
from logging import getLogger
from pathlib import Path

import numpy as np
import numpy.typing as npt
import pytest

from mel_cepstral_distance.api import get_amplitude_spectrogram, get_mel_spectrogram
from mel_cepstral_distance.helper import get_n_fft_bins, samples_to_ms
from mel_cepstral_distance.silence import get_loudness_vals_X_km

TEST_DIR = Path("src/mel_cepstral_distance_tests/api_tests")

AUDIO_A = TEST_DIR / "A.wav"

N_FFT = samples_to_ms(512, 22050)
SR = 22050


def test_one_dim_raises_error() -> None:
  with pytest.raises(ValueError):
    get_mel_spectrogram(np.zeros(302), SR, N_FFT)


def test_three_dim_raises_error() -> None:
  with pytest.raises(ValueError):
    get_mel_spectrogram(np.zeros((302, 353, 3)), SR, N_FFT)


def test_no_freq_bins_raises_error() -> None:
  with pytest.raises(ValueError):
    get_mel_spectrogram(np.zeros((302, 0)), SR, N_FFT)


def get_X_km() -> npt.NDArray[np.complex128]:
  return get_amplitude_spectrogram(
    AUDIO_A,
    sample_rate=SR,
    n_fft=N_FFT,
    window="hamming",
    hop_len=16,
    norm_audio=False,
    remove_silence=False,
    win_len=N_FFT,
  )


def test_result_changes_after_silence_removal() -> None:
  res = get_mel_spectrogram(
    get_X_km(),
    SR,
    N_FFT,
    remove_silence=False,
    fmin=0,
    fmax=SR // 2,
    M=20,
  )

  assert res.shape == (303, 20)

  mean = get_loudness_vals_X_km(get_X_km()).mean()

  res = get_mel_spectrogram(
    get_X_km(),
    SR,
    N_FFT,
    remove_silence=True,
    silence_threshold=mean,
    fmax=SR // 2,
    fmin=0,
    M=20,
  )

  assert res.shape == (124, 20)


def test_invalid_n_fft_raises_error() -> None:
  with pytest.raises(ValueError):
    get_mel_spectrogram(get_X_km(), SR, 0)

  with pytest.raises(ValueError):
    get_mel_spectrogram(get_X_km(), SR, samples_to_ms(512 - 1, 22050))


def test_n_fft_one_larger_raises_no_error() -> None:
  get_mel_spectrogram(get_X_km(), SR, samples_to_ms(512 + 1, 22050))


def test_invalid_M_raises_error() -> None:
  with pytest.raises(ValueError):
    get_mel_spectrogram(get_X_km(), SR, N_FFT, M=0)


def test_invalid_fmin_raises_error() -> None:
  with pytest.raises(ValueError):
    get_mel_spectrogram(get_X_km(), SR, N_FFT, fmin=-1)


def test_invalid_fmax_raises_error() -> None:
  with pytest.raises(ValueError):
    get_mel_spectrogram(get_X_km(), SR, N_FFT, fmax=0)


def test_invalid_sample_rate_raises_error() -> None:
  with pytest.raises(ValueError):
    get_mel_spectrogram(get_X_km(), 0, N_FFT)


def test_no_silence_threshold_raises_error() -> None:
  with pytest.raises(ValueError):
    get_mel_spectrogram(
      get_X_km(), SR, N_FFT, remove_silence=True, silence_threshold=None
    )


def test_removing_silence_from_sig_too_hard_returns_empty() -> None:
  loudness_max = get_loudness_vals_X_km(get_X_km()).max()
  res = get_mel_spectrogram(
    get_X_km(),
    SR,
    N_FFT,
    remove_silence=True,
    silence_threshold=loudness_max + 1,
    fmax=SR // 2,
    fmin=0,
    M=20,
  )

  assert res.shape == (0, 20)


def test_empty_spec_returns_empty() -> None:
  empty_spec = np.empty((0, get_n_fft_bins(512)), dtype=np.int16)

  res = get_mel_spectrogram(
    empty_spec,
    SR,
    N_FFT,
    remove_silence=False,
    fmax=SR // 2,
    fmin=0,
    M=20,
  )

  assert res.shape == (0, 20)


def create_outputs() -> None:
  targets = []

  # fmax
  targets.extend([(0, fmax, 80, None) for fmax in [None, 8000, 6000, 4000, 2000]])

  # fmin
  targets.extend([(fmin, 8000, 80, None) for fmin in [0, 1000, 2000, 4000]])

  # N
  targets.extend(
    [
      (
        0,
        8000,
        n,
        None,
      )
      for n in [20, 40, 60, 80]
    ]
  )

  # silence removal
  for sil_rem in [None, 70, 8000, 100000]:
    targets.extend(((0, 8000, 80, sil_rem),))

  outputs = []

  for fmin, fmax, n, sil_removal in targets:
    spec = get_mel_spectrogram(
      get_X_km(),
      SR,
      N_FFT,
      fmin=fmin,
      fmax=fmax,
      M=n,
      remove_silence=sil_removal is not None,
      silence_threshold=sil_removal,
    )
    outputs.append((fmin, fmax, n, sil_removal, spec))

  logger = getLogger(__name__)
  for vals in outputs:
    logger.info(
      "\t".join(
        str(i) if not isinstance(i, np.ndarray) else str(np.mean(i)) for i in vals
      )
    )
  (TEST_DIR / "test_get_mel_spectrogram.pkl").write_bytes(pickle.dumps(outputs))


def test_outputs() -> None:
  outputs = pickle.loads((TEST_DIR / "test_get_mel_spectrogram.pkl").read_bytes())
  for fmin, fmax, n, sil_removal, expected_spec in outputs:
    spec = get_mel_spectrogram(
      get_X_km(),
      SR,
      N_FFT,
      fmin=fmin,
      fmax=fmax,
      M=n,
      remove_silence=sil_removal is not None,
      silence_threshold=sil_removal,
    )
    np.testing.assert_almost_equal(spec, expected_spec)


if __name__ == "__main__":
  create_outputs()
