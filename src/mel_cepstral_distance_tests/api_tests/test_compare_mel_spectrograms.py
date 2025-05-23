import pickle
from logging import getLogger
from pathlib import Path

import numpy as np
import numpy.typing as npt
import pytest
from scipy.io import wavfile

from mel_cepstral_distance.api import compare_mel_spectrograms
from mel_cepstral_distance.computation import get_w_n_m, get_X_km, get_X_kn
from mel_cepstral_distance.helper import norm_audio_signal

TEST_DIR = Path("src/mel_cepstral_distance_tests/api_tests")

AUDIO_A = TEST_DIR / "A.wav"
AUDIO_B = TEST_DIR / "B.wav"

M = 80


def test_zero_dim_spec_raise_error() -> None:
  with pytest.raises(ValueError):
    compare_mel_spectrograms(get_X_kn_A(), np.empty((305, 0)))

  with pytest.raises(ValueError):
    compare_mel_spectrograms(np.empty((305, 0)), get_X_kn_A())

  with pytest.raises(ValueError):
    compare_mel_spectrograms(np.empty((305, 0)), np.empty((305, 0)))


def test_one_dim_spec_raise_error() -> None:
  with pytest.raises(ValueError):
    compare_mel_spectrograms(get_X_kn_A(), np.empty(305))

  with pytest.raises(ValueError):
    compare_mel_spectrograms(np.empty(305), get_X_kn_A())

  with pytest.raises(ValueError):
    compare_mel_spectrograms(np.empty(305), np.empty(305))


def test_three_dim_spec_raise_error() -> None:
  with pytest.raises(ValueError):
    compare_mel_spectrograms(get_X_kn_A(), np.empty((305, 20, 10)))

  with pytest.raises(ValueError):
    compare_mel_spectrograms(np.empty((305, 20, 10)), get_X_kn_A())

  with pytest.raises(ValueError):
    compare_mel_spectrograms(np.empty((305, 20, 10)), np.empty((305, 20, 10)))


def get_X_kn_A() -> npt.NDArray:
  sr1, signalA = wavfile.read(AUDIO_A)
  signalA = norm_audio_signal(signalA)
  X_km = get_X_km(signalA, 512, 512, 128, "hamming")
  w_n_m = get_w_n_m(sr1, 512, M, 0, sr1 // 2)
  X_kn = get_X_kn(X_km, w_n_m)
  return X_kn


def get_X_kn_B() -> npt.NDArray:
  sr2, signalB = wavfile.read(AUDIO_B)
  signalB = norm_audio_signal(signalB)
  X_km = get_X_km(signalB, 512, 512, 128, "hamming")
  w_n_m = get_w_n_m(sr2, 512, M, 0, sr2 // 2)
  X_kn = get_X_kn(X_km, w_n_m)
  return X_kn


def test_aligning_with_pad_returns_same_for_mel_mfcc() -> None:
  res = []
  for align_target in ["mel", "mfcc"]:
    mcd, pen = compare_mel_spectrograms(
      get_X_kn_A(),
      get_X_kn_B(),
      align_target=align_target,
      aligning="pad",
      dtw_radius=None,
      D=16,
      s=1,
      remove_silence="no",
    )
    res.append((mcd, pen))
  np.testing.assert_almost_equal(res[0], res[1])


def test_result_changes_after_silence_removal_before_padding_mfcc() -> None:
  mcd, pen = compare_mel_spectrograms(
    get_X_kn_A(),
    get_X_kn_B(),
    align_target="mfcc",
    aligning="pad",
    dtw_radius=None,
    remove_silence="mel",
    silence_threshold_A=0.01,
    silence_threshold_B=0.01,
    s=1,
    D=16,
  )
  mcd2, pen2 = compare_mel_spectrograms(
    get_X_kn_A(),
    get_X_kn_B(),
    align_target="mfcc",
    aligning="pad",
    dtw_radius=None,
    remove_silence="no",
    s=1,
    D=16,
  )

  assert not np.allclose(mcd, mcd2)
  assert not np.allclose(pen, pen2)


def test_same_spec_returns_zero() -> None:
  mcd, pen = compare_mel_spectrograms(
    get_X_kn_A(),
    get_X_kn_A(),
    D=16,
    s=1,
    align_target="mfcc",
    aligning="pad",
    dtw_radius=None,
    remove_silence="no",
  )
  assert mcd == 0
  assert pen == 0


def test_invalid_radius_raises_error() -> None:
  with pytest.raises(
    ValueError, match="dtw_radius must be None or greater than or equal to 1"
  ):
    compare_mel_spectrograms(
      get_X_kn_A(), get_X_kn_B(), aligning="dtw", align_target="mel", dtw_radius=0
    )


def test_removing_silence_from_mel_too_hard_returns_nan_nan() -> None:
  mcd, pen = compare_mel_spectrograms(
    get_X_kn_A(),
    get_X_kn_B(),
    remove_silence="mel",
    silence_threshold_A=100,
    silence_threshold_B=0,
    align_target="mfcc",
    aligning="pad",
    dtw_radius=None,
    D=16,
    s=1,
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)

  mcd, pen = compare_mel_spectrograms(
    get_X_kn_A(),
    get_X_kn_B(),
    remove_silence="mel",
    silence_threshold_A=0,
    silence_threshold_B=100,
    align_target="mfcc",
    aligning="pad",
    dtw_radius=None,
    D=16,
    s=1,
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)

  mcd, pen = compare_mel_spectrograms(
    get_X_kn_A(),
    get_X_kn_B(),
    remove_silence="mel",
    silence_threshold_A=100,
    silence_threshold_B=100,
    align_target="mfcc",
    aligning="pad",
    dtw_radius=None,
    D=16,
    s=1,
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)


def test_removing_silence_from_mfcc_too_hard_returns_nan_nan() -> None:
  mcd, pen = compare_mel_spectrograms(
    get_X_kn_A(),
    get_X_kn_B(),
    remove_silence="mfcc",
    silence_threshold_A=100,
    silence_threshold_B=0,
    align_target="mfcc",
    D=16,
    s=1,
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)

  mcd, pen = compare_mel_spectrograms(
    get_X_kn_A(),
    get_X_kn_B(),
    remove_silence="mfcc",
    silence_threshold_A=0,
    silence_threshold_B=100,
    align_target="mfcc",
    aligning="pad",
    dtw_radius=None,
    D=16,
    s=1,
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)

  mcd, pen = compare_mel_spectrograms(
    get_X_kn_A(),
    get_X_kn_B(),
    remove_silence="mfcc",
    silence_threshold_A=100,
    silence_threshold_B=100,
    align_target="mfcc",
    aligning="pad",
    dtw_radius=None,
    D=16,
    s=1,
  )
  assert np.isnan(mcd)
  assert np.isnan(pen)


def test_empty_spec_returns_nan_nan() -> None:
  X_km_empty = np.empty((0, M))
  mcd, pen = compare_mel_spectrograms(X_km_empty, get_X_kn_B())
  assert np.isnan(mcd)
  assert np.isnan(pen)

  mcd, pen = compare_mel_spectrograms(get_X_kn_A(), X_km_empty)
  assert np.isnan(mcd)
  assert np.isnan(pen)

  mcd, pen = compare_mel_spectrograms(X_km_empty, X_km_empty)
  assert np.isnan(mcd)
  assert np.isnan(pen)


def test_invalid_silence_removal_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_mel_spectrograms(get_X_kn_A(), get_X_kn_B(), remove_silence="none")


def test_invalid_aligning_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_mel_spectrograms(get_X_kn_A(), get_X_kn_B(), aligning="none")


def test_invalid_align_target_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_mel_spectrograms(get_X_kn_A(), get_X_kn_B(), align_target="none")


def test_invalid_remove_silence_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_mel_spectrograms(get_X_kn_A(), get_X_kn_B(), remove_silence="none")


def test_invalid_silence_threshold_raises_error() -> None:
  # A None
  with pytest.raises(ValueError):
    compare_mel_spectrograms(
      get_X_kn_A(),
      get_X_kn_B(),
      remove_silence="mel",
      silence_threshold_A=None,
      silence_threshold_B=0.01,
    )

  with pytest.raises(ValueError):
    compare_mel_spectrograms(
      get_X_kn_A(),
      get_X_kn_B(),
      remove_silence="mfcc",
      silence_threshold_A=None,
      silence_threshold_B=0.01,
    )
  # B None
  with pytest.raises(ValueError):
    compare_mel_spectrograms(
      get_X_kn_A(),
      get_X_kn_B(),
      remove_silence="mel",
      silence_threshold_A=0.01,
      silence_threshold_B=None,
    )

  with pytest.raises(ValueError):
    compare_mel_spectrograms(
      get_X_kn_A(),
      get_X_kn_B(),
      remove_silence="mfcc",
      silence_threshold_A=0.01,
      silence_threshold_B=None,
    )


def test_removing_silence_after_aligning_raises_error() -> None:
  # mfcc after mel was aligned
  with pytest.raises(ValueError):
    compare_mel_spectrograms(
      get_X_kn_A(),
      get_X_kn_B(),
      remove_silence="mfcc",
      silence_threshold_A=0.01,
      silence_threshold_B=0.01,
      align_target="mel",
      aligning="dtw",
      dtw_radius=1,
    )


def test_D_greater_than_M_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_mel_spectrograms(get_X_kn_A(), get_X_kn_B(), D=M + 1)


def test_invalid_D_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_mel_spectrograms(get_X_kn_A(), get_X_kn_B(), D=0)

  with pytest.raises(ValueError):
    compare_mel_spectrograms(get_X_kn_A(), get_X_kn_B(), D=1)


def test_invalid_s_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_mel_spectrograms(get_X_kn_A(), get_X_kn_B(), s=-1)


def test_s_equals_D_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_mel_spectrograms(get_X_kn_A(), get_X_kn_B(), s=12, D=12)


def test_s_bigger_than_D_raises_error() -> None:
  with pytest.raises(ValueError):
    compare_mel_spectrograms(get_X_kn_A(), get_X_kn_B(), s=13, D=12)


def create_other_outputs() -> None:
  targets = []

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
    targets.append((s, d, 1))

  # dtw_radius
  targets.extend([(1, 13, dtw_radius) for dtw_radius in [1, 10, 20, None]])

  outputs = []

  for s, d, dtw_radius in targets:
    mcd, pen = compare_mel_spectrograms(
      get_X_kn_A(),
      get_X_kn_B(),
      s=s,
      D=d,
      align_target="mel",
      aligning="dtw",
      remove_silence="no",
      dtw_radius=dtw_radius,
    )
    outputs.append((s, d, dtw_radius, mcd, pen))

  logger = getLogger(__name__)
  for vals in outputs:
    logger.info("\t".join(str(i) for i in vals))
  (TEST_DIR / "test_compare_mel_spectrograms_other.pkl").write_bytes(
    pickle.dumps(outputs)
  )


def test_other_outputs() -> None:
  outputs = pickle.loads(
    (TEST_DIR / "test_compare_mel_spectrograms_other.pkl").read_bytes()
  )
  for s, d, dtw_radius, expected_mcd, expected_pen in outputs:
    mcd, pen = compare_mel_spectrograms(
      get_X_kn_A(),
      get_X_kn_B(),
      s=s,
      D=d,
      align_target="mel",
      aligning="dtw",
      remove_silence="no",
      dtw_radius=dtw_radius,
    )
    np.testing.assert_almost_equal(mcd, expected_mcd)
    np.testing.assert_almost_equal(pen, expected_pen)


def create_sil_outputs() -> None:
  mel_sil = -7
  mfcc_sil = 0.001

  targets = [
    ("no", None, None, "pad", "mel", None),
    ("no", None, None, "pad", "mfcc", None),
    ("mel", mel_sil, mel_sil, "pad", "mel", None),
    ("mel", mel_sil, mel_sil, "pad", "mfcc", None),
    ("mfcc", mfcc_sil, mfcc_sil, "pad", "mfcc", None),
  ]

  for dtw_radius in [1, 20]:
    targets.extend(
      [
        ("no", None, None, "dtw", "mel", dtw_radius),
        ("no", None, None, "dtw", "mfcc", dtw_radius),
        ("mel", mel_sil, mel_sil, "dtw", "mel", dtw_radius),
        ("mel", mel_sil, mel_sil, "dtw", "mfcc", dtw_radius),
        ("mfcc", mfcc_sil, mfcc_sil, "dtw", "mfcc", dtw_radius),
      ]
    )

  outputs = []

  for remove_silence, sil_a, sil_b, aligning, target, dtw_radius in targets:
    mcd, pen = compare_mel_spectrograms(
      get_X_kn_A(),
      get_X_kn_B(),
      align_target=target,
      aligning=aligning,
      remove_silence=remove_silence,
      silence_threshold_A=sil_a,
      silence_threshold_B=sil_b,
      dtw_radius=dtw_radius,
      s=1,
      D=13,
    )
    outputs.append(
      (remove_silence, sil_a, sil_b, aligning, target, dtw_radius, mcd, pen)
    )
  logger = getLogger(__name__)
  for vals in outputs:
    logger.info("\t".join(str(i) for i in vals))
  (TEST_DIR / "test_compare_mel_spectrograms_sil.pkl").write_bytes(
    pickle.dumps(outputs)
  )


def test_sil_outputs() -> None:
  outputs = pickle.loads(
    (TEST_DIR / "test_compare_mel_spectrograms_sil.pkl").read_bytes()
  )
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
    mcd, pen = compare_mel_spectrograms(
      get_X_kn_A(),
      get_X_kn_B(),
      align_target=target,
      aligning=aligning,
      remove_silence=remove_silence,
      silence_threshold_A=sil_a,
      silence_threshold_B=sil_b,
      dtw_radius=dtw_radius,
      s=1,
      D=13,
    )
    np.testing.assert_almost_equal(mcd, expected_mcd)
    np.testing.assert_almost_equal(pen, expected_pen)


if __name__ == "__main__":
  create_other_outputs()
  create_sil_outputs()
