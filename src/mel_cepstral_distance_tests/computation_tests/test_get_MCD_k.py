import numpy as np

from mel_cepstral_distance.computation import get_MCD_k


def get_MCD_k_from_paper(
  MC_X_ik: np.ndarray, MC_Y_ik: np.ndarray, s: int, D: int
) -> np.ndarray:
  assert MC_X_ik.shape == MC_Y_ik.shape
  assert 0 <= s < D
  K = MC_X_ik.shape[1]

  MCD_k = np.zeros(K)
  for k in range(K):
    diff_square_sum = 0
    for i in range(s, D):
      diff_square_sum += (MC_X_ik[i, k] - MC_Y_ik[i, k]) ** 2
    MCD_k[k] = np.sqrt(diff_square_sum)

  return MCD_k


def test_basic_case_zero_three() -> None:
  MC_X_ik = np.array([[1, 2], [3, 4], [5, 6]])
  MC_Y_ik = np.array([[1, 2], [3, 5], [5, 8]])
  s, D = 0, 3
  expected = np.array(
    [
      np.sqrt(abs(1 - 1) ** 2 + abs(3 - 3) ** 2 + abs(5 - 5) ** 2),
      np.sqrt(abs(2 - 2) ** 2 + abs(4 - 5) ** 2 + abs(6 - 8) ** 2),
    ]
  )
  result = get_MCD_k(MC_X_ik, MC_Y_ik, s, D)
  assert np.allclose(result, expected), f"Expected {expected}, but got {result}."
  # Compare with the paper's implementation
  assert np.allclose(result, get_MCD_k_from_paper(MC_X_ik, MC_Y_ik, s, D))


def test_basic_case_one_three_returns_same_as_zero_three_in_this_case() -> None:
  MC_X_ik = np.array([[1, 2], [3, 4], [5, 6]])
  MC_Y_ik = np.array([[1, 2], [3, 5], [5, 8]])
  s, D = 1, 3
  expected = np.array(
    [
      np.sqrt(abs(3 - 3) ** 2 + abs(5 - 5) ** 2),
      np.sqrt(abs(4 - 5) ** 2 + abs(6 - 8) ** 2),
    ]
  )
  result = get_MCD_k(MC_X_ik, MC_Y_ik, s, D)
  assert np.allclose(result, expected), f"Expected {expected}, but got {result}."
  # Compare with the paper's implementation
  assert np.allclose(result, get_MCD_k_from_paper(MC_X_ik, MC_Y_ik, s, D))


def test_basic_case_zero_two() -> None:
  MC_X_ik = np.array([[1, 2], [3, 4], [5, 6]])
  MC_Y_ik = np.array([[1, 2], [3, 5], [5, 8]])
  s, D = 0, 2
  expected = np.array(
    [
      np.sqrt(abs(1 - 1) ** 2 + abs(3 - 3) ** 2),
      np.sqrt(abs(2 - 2) ** 2 + abs(4 - 5) ** 2),
    ]
  )
  result = get_MCD_k(MC_X_ik, MC_Y_ik, s, D)
  assert np.allclose(result, expected), f"Expected {expected}, but got {result}."
  # Compare with the paper's implementation
  assert np.allclose(result, get_MCD_k_from_paper(MC_X_ik, MC_Y_ik, s, D))


def test_case_with_nonzero_start_index() -> None:
  MC_X_ik = np.array([[0, 1], [2, 3], [4, 5], [6, 7]])
  MC_Y_ik = np.array([[0, 1], [1, 2], [3, 5], [5, 8]])
  s, D = 1, 4
  expected = np.array(
    [
      np.sqrt(abs(2 - 1) ** 2 + abs(4 - 3) ** 2 + abs(6 - 5) ** 2),
      np.sqrt(abs(3 - 2) ** 2 + abs(5 - 5) ** 2 + abs(7 - 8) ** 2),
    ]
  )
  result = get_MCD_k(MC_X_ik, MC_Y_ik, s, D)
  assert np.allclose(result, expected), f"Expected {expected}, but got {result}."
  # Compare with the paper's implementation
  assert np.allclose(result, get_MCD_k_from_paper(MC_X_ik, MC_Y_ik, s, D))


def test_large_values_case() -> None:
  MC_X_ik = np.array([[1e10, 2e10], [3e10, 4e10], [5e10, 6e10]])
  MC_Y_ik = np.array([[1e10, 2e10], [3e10, 5e10], [5e10, 8e10]])
  s, D = 0, 3
  expected = np.array(
    [
      np.sqrt(
        abs(1e10 - 1e10) ** 2 + abs(3e10 - 3e10) ** 2 + abs(5e10 - 5e10) ** 2
      ),  # Should result in 0
      np.sqrt(abs(2e10 - 2e10) ** 2 + abs(4e10 - 5e10) ** 2 + abs(6e10 - 8e10) ** 2),
    ]
  )
  result = get_MCD_k(MC_X_ik, MC_Y_ik, s, D)
  assert np.allclose(result, expected), f"Expected {expected}, but got {result}."
  # Compare with the paper's implementation
  assert np.allclose(result, get_MCD_k_from_paper(MC_X_ik, MC_Y_ik, s, D))


def test_mixed_values_case() -> None:
  MC_X_ik = np.array([[1, -2], [-3, 4], [5, -6]])
  MC_Y_ik = np.array([[1, -2], [-3, 5], [5, -8]])
  s, D = 0, 3
  expected = np.array(
    [
      np.sqrt(
        abs(1 - 1) ** 2 + abs(-3 - (-3)) ** 2 + abs(5 - 5) ** 2
      ),  # Should result in 0
      np.sqrt(abs(-2 - (-2)) ** 2 + abs(4 - 5) ** 2 + abs(-6 - (-8)) ** 2),
    ]
  )
  result = get_MCD_k(MC_X_ik, MC_Y_ik, s, D)
  assert np.allclose(result, expected), f"Expected {expected}, but got {result}."
  # Compare with the paper's implementation
  assert np.allclose(result, get_MCD_k_from_paper(MC_X_ik, MC_Y_ik, s, D))
