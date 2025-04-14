import logging


def pytest_configure() -> None:
  logger = logging.getLogger("numba")
  logger.disabled = True
  logger.propagate = False
