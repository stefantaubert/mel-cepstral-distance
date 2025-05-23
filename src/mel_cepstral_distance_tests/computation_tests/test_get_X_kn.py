import numpy as np

from mel_cepstral_distance.computation import get_w_n_m, get_X_kn


def get_X_kn_from_paper(X_km: np.ndarray, w_n_m: np.ndarray) -> np.ndarray:
  """Calculates the energy Mel spectrogram (Bel) of the linear amplitude spectrogram
  returns Mel spectrogram with shape (#frames, N)
  """
  # M = n mels
  assert X_km.shape[1] == w_n_m.shape[1], (
    f"Expected {w_n_m.shape[1]} columns, but got {X_km.shape[1]}"
  )

  K = X_km.shape[0]
  M = w_n_m.shape[0]

  # same as np.dot(energy_spec, w_n_m.T)
  X_kn_energy = np.zeros((K, M))
  for k in range(K):
    for n in range(w_n_m.shape[0]):
      X_kn_energy[k, n] = np.sum(abs(X_km[k, :]) ** 2 * w_n_m[n, :])

  X_kn_energy_bel = np.log10(X_kn_energy + np.finfo(float).eps)
  return X_kn_energy_bel


def test_imag_part() -> None:
  X_km = np.array(
    [[3.75 + 0.0j, -2.25 - 1.5j, 0.75 + 0.0j], [6.75 + 0.0j, -3.75 - 3.0j, 0.75 + 0.0j]]
  )

  sample_rate = 8000
  M = 2
  n_fft = 4  # adjust n_fft to ensure dimensions match
  fmin = 0
  fmax = 4000
  w_n_m = get_w_n_m(sample_rate, n_fft, M, fmin, fmax)
  result = get_X_kn(X_km, w_n_m)

  # Expected shape based on X_km shape and N
  expected_shape = (X_km.shape[0], M)
  assert result.shape == expected_shape, (
    f"Expected shape {expected_shape}, but got {result.shape}."
  )
  assert np.allclose(
    result, np.array([[1.14806254, 0.86406588], [1.65860755, 1.36290638]])
  )
  # Compare with the paper's implementation
  assert np.allclose(result, get_X_kn_from_paper(X_km, w_n_m))


def test_mel_spectrogram_dimension_fix() -> None:
  X_km = np.array([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9]])
  sample_rate = 8000
  M = 2
  n_fft = 8  # adjust n_fft to ensure dimensions match
  fmin = 0
  fmax = 4000
  w_n_m = get_w_n_m(sample_rate, n_fft, M, fmin, fmax)
  result = get_X_kn(X_km, w_n_m)

  # Expected shape based on X_km shape and N
  expected_shape = (X_km.shape[0], M)
  assert result.shape == expected_shape, (
    f"Expected shape {expected_shape}, but got {result.shape}."
  )
  assert np.allclose(
    result, np.array([[0.47712125, 1.2787536], [1.63346846, 1.99563519]])
  )
  # Compare with the paper's implementation
  assert np.allclose(result, get_X_kn_from_paper(X_km, w_n_m))


def test_single_mel_band() -> None:
  X_km = np.array([[1, 2], [3, 4]])
  sample_rate = 16000
  M = 1
  n_fft = 2
  fmin = 0
  fmax = 8000
  w_n_m = get_w_n_m(sample_rate, n_fft, M, fmin, fmax)
  result = get_X_kn(X_km, w_n_m)

  # Expected shape
  expected_shape = (X_km.shape[0], M)
  assert result.shape == expected_shape, (
    f"Expected shape {expected_shape}, but got {result.shape}."
  )
  assert np.allclose(result, np.array([[9.64327467e-17], [0.95424251]]))
  # Compare with the paper's implementation
  assert np.allclose(result, get_X_kn_from_paper(X_km, w_n_m))


def test_large_values_input() -> None:
  X_km = np.array([[1e10, 2e10, 3e10], [3e10, 4e10, 5e10]])
  sample_rate = 44100
  M = 3
  n_fft = 4
  fmin = 0
  fmax = 22050
  w_n_m = get_w_n_m(sample_rate, n_fft, M, fmin, fmax)
  result = get_X_kn(X_km, w_n_m)

  # Ensure the shape is correct
  expected_shape = (X_km.shape[0], M)
  assert result.shape == expected_shape, (
    f"Expected shape {expected_shape}, but got {result.shape}."
  )

  # Check for finite values
  assert np.all(np.isfinite(result)), "Expected all values to be finite."
  assert np.allclose(
    result,
    np.array(
      [[-15.65355977, 20.0, 20.60205999], [-15.65355977, 20.95424251, 21.20411998]]
    ),
  )
  # Compare with the paper's implementation
  assert np.allclose(result, get_X_kn_from_paper(X_km, w_n_m))


def test_zero_input() -> None:
  X_km = np.zeros((30, 3), dtype=np.complex128)
  sample_rate = 16000
  M = 2
  n_fft = 4
  fmin = 0
  fmax = 8000
  w_n_m = get_w_n_m(sample_rate, n_fft, M, fmin, fmax)
  result = get_X_kn(X_km, w_n_m)

  # Check that the result is -inf due to log10 of
  # zero input energy (with small eps added)
  assert np.allclose(result, -15.65355977), (
    "Expected all values to be < 0 due to log10 of zero input energy."
  )
  # Compare with the paper's implementation
  assert np.allclose(result, get_X_kn_from_paper(X_km, w_n_m))


def test_high_and_fminuencies() -> None:
  X_km = np.random.rand(12, 5)
  sample_rate = 48000
  M = 4
  n_fft = 8
  fmin = 100
  fmax = 12000
  w_n_m = get_w_n_m(sample_rate, n_fft, M, fmin, fmax)
  result = get_X_kn(X_km, w_n_m)

  # Expected shape
  expected_shape = (X_km.shape[0], M)
  assert result.shape == expected_shape, (
    f"Expected shape {expected_shape}, but got {result.shape}."
  )
  # Compare with the paper's implementation
  assert np.allclose(result, get_X_kn_from_paper(X_km, w_n_m))
