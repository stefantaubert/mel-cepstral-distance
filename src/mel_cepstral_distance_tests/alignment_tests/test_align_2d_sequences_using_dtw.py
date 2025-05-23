import numpy as np

from mel_cepstral_distance.alignment import align_2d_sequences_using_dtw


def test_2d_identical_sequences() -> None:
  seq_1 = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
  seq_2 = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
  aligned_seq_1, aligned_seq_2, paths = align_2d_sequences_using_dtw(
    seq_1, seq_2, custom_radius=1
  )
  expected_aligned_seq_1 = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
  expected_aligned_seq_2 = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
  assert np.array_equal(aligned_seq_1, expected_aligned_seq_1), (
    "Aligned sequence 1 does not match expected output"
  )
  assert np.array_equal(aligned_seq_2, expected_aligned_seq_2), (
    "Aligned sequence 2 does not match expected output"
  )


def test_2d_different_lengths() -> None:
  seq_1 = np.array([[1, 3, 5], [5, 3, 1]])
  seq_2 = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
  aligned_seq_1, aligned_seq_2, paths = align_2d_sequences_using_dtw(
    seq_1, seq_2, custom_radius=1
  )
  expected_aligned_seq_1 = np.array([[1, 3, 3, 5, 5], [5, 3, 3, 1, 1]])
  expected_aligned_seq_2 = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
  assert np.array_equal(aligned_seq_1, expected_aligned_seq_1), (
    "Aligned sequence 1 does not match expected output"
  )
  assert np.array_equal(aligned_seq_2, expected_aligned_seq_2), (
    "Aligned sequence 2 does not match expected output"
  )


def test_2d_different_lengths_max_radius() -> None:
  seq_1 = np.array([[1, 3, 5], [5, 3, 1]])
  seq_2 = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
  aligned_seq_1, aligned_seq_2, paths = align_2d_sequences_using_dtw(
    seq_1, seq_2, custom_radius=None
  )
  expected_aligned_seq_1 = np.array([[1, 3, 3, 5, 5], [5, 3, 3, 1, 1]])
  expected_aligned_seq_2 = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
  assert np.array_equal(aligned_seq_1, expected_aligned_seq_1), (
    "Aligned sequence 1 does not match expected output"
  )
  assert np.array_equal(aligned_seq_2, expected_aligned_seq_2), (
    "Aligned sequence 2 does not match expected output"
  )


def test_2d_with_noise() -> None:
  seq_1 = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
  seq_2 = np.array([[1, 2, 2.5, 3, 4, 5], [5, 4, 3, 2.5, 2, 1]])
  aligned_seq_1, aligned_seq_2, paths = align_2d_sequences_using_dtw(
    seq_1, seq_2, custom_radius=1
  )
  expected_aligned_seq_1 = np.array([[1, 2, 3, 3, 4, 5], [5, 4, 3, 3, 2, 1]])
  expected_aligned_seq_2 = np.array([[1, 2, 2.5, 3, 4, 5], [5, 4, 3, 2.5, 2, 1]])
  assert np.array_equal(aligned_seq_1, expected_aligned_seq_1), (
    "Aligned sequence 1 does not match expected output"
  )
  assert np.array_equal(aligned_seq_2, expected_aligned_seq_2), (
    "Aligned sequence 2 does not match expected output"
  )


def test_2d_reverse_order() -> None:
  seq_1 = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
  seq_2 = np.array([[5, 4, 3, 2, 1], [1, 2, 3, 4, 5]])
  aligned_seq_1, aligned_seq_2, paths = align_2d_sequences_using_dtw(
    seq_1, seq_2, custom_radius=1
  )
  expected_aligned_seq_1 = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
  expected_aligned_seq_2 = np.array([[5, 4, 3, 2, 1], [1, 2, 3, 4, 5]])
  assert np.array_equal(aligned_seq_1, expected_aligned_seq_1), (
    "Aligned sequence 1 does not match expected output"
  )
  assert np.array_equal(aligned_seq_2, expected_aligned_seq_2), (
    "Aligned sequence 2 does not match expected output"
  )
