import numpy as np
import pytest

from mel_cepstral_distance.api import compare_audio_arrays

SIGNAL_A = np.array([])
SIGNAL_B = np.array([])
SR_A = 16000
SR_B = 16000


def test_invalid_silence_removal_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_arrays(SIGNAL_A, SIGNAL_B, SR_A, SR_B, remove_silence="none")


def test_invalid_sample_rate_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_arrays(SIGNAL_A, SIGNAL_B, SR_A, SR_B, sample_rate=0)


def test_invalid_n_fft_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_arrays(SIGNAL_A, SIGNAL_B, SR_A, SR_B, n_fft=0)


def test_invalid_win_len_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_arrays(SIGNAL_A, SIGNAL_B, SR_A, SR_B, win_len=0)


def test_invalid_hop_len_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_arrays(SIGNAL_A, SIGNAL_B, SR_A, SR_B, hop_len=0)


def test_invalid_window_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_audio_arrays(SIGNAL_A, SIGNAL_B, SR_A, SR_B, window="none")
