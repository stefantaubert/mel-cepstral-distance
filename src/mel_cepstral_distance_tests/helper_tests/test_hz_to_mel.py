import numpy as np

from mel_cepstral_distance.helper import hz_to_mel


def test_hz_to_mel_zero_frequency() -> None:
  hz = 0
  expected = 0
  result = hz_to_mel(hz)
  assert result == expected, f"Expected {expected}, but got {result}."


def test_hz_to_mel_typical_value() -> None:
  hz = 1000
  expected = 2595 * np.log10(1 + 1000 / 700.0)
  result = hz_to_mel(hz)
  assert np.isclose(result, expected), f"Expected {expected}, but got {result}."


def test_hz_to_mel_large_value() -> None:
  hz = 20000
  expected = 2595 * np.log10(1 + 20000 / 700.0)
  result = hz_to_mel(hz)
  assert np.isclose(result, expected), f"Expected {expected}, but got {result}."


def test_hz_to_mel_small_value() -> None:
  hz = 10
  expected = 2595 * np.log10(1 + 10 / 700.0)
  result = hz_to_mel(hz)
  assert np.isclose(result, expected), f"Expected {expected}, but got {result}."


def test_hz_to_mel_decimal_value() -> None:
  hz = 432.5
  expected = 2595 * np.log10(1 + 432.5 / 700.0)
  result = hz_to_mel(hz)
  assert np.isclose(result, expected), f"Expected {expected}, but got {result}."
