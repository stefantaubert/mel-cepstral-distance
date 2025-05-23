import numpy as np

from mel_cepstral_distance.helper import mel_to_hz


def test_mel_to_hz_zero() -> None:
  mel = 0
  expected = 0
  result = mel_to_hz(mel)
  assert result == expected, f"Expected {expected}, but got {result}."


def test_mel_to_hz_typical_value() -> None:
  mel = 1000
  expected = 700 * (10 ** (1000 / 2595) - 1)
  result = mel_to_hz(mel)
  assert np.isclose(result, expected), f"Expected {expected}, but got {result}."


def test_mel_to_hz_large_value() -> None:
  mel = 4000
  expected = 700 * (10 ** (4000 / 2595) - 1)
  result = mel_to_hz(mel)
  assert np.isclose(result, expected), f"Expected {expected}, but got {result}."


def test_mel_to_hz_small_value() -> None:
  mel = 10
  expected = 700 * (10 ** (10 / 2595) - 1)
  result = mel_to_hz(mel)
  assert np.isclose(result, expected), f"Expected {expected}, but got {result}."


def test_mel_to_hz_decimal_value() -> None:
  mel = 432.5
  expected = 700 * (10 ** (432.5 / 2595) - 1)
  result = mel_to_hz(mel)
  assert np.isclose(result, expected), f"Expected {expected}, but got {result}."
