# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.4] - 2025-04-14

### Changed

- Complete refactoring of the codebase
- Support for Python 3.8-3.13
- Support removal of pause
- Improved MCD calculation

## [0.0.3] - 2024-01-25

### Added

- MCD calculation for Mel spectrograms via CLI using `from-mel`
- batch processing for `from-mel` via `from-mel-batch`
- `get_metrics_mels_pairwise`
- logging to file
- Support for Python 3.11

### Changed

- Changed usage of CLI for wav files, now via `from-wav`
- Improved input validation for CLI
- Logging method

## [0.0.2] - 2022-08-17

### Added

- missing init files
- pylint
- tox config
- acknowledgments

### Changed

- updated dependency restrictions
- renamed some metavars

## [0.0.1] - 2022-04-26

- Initial release

[unreleased]: https://github.com/stefantaubert/mel-cepstral-distance/compare/v0.0.4...HEAD
[0.0.4]: https://github.com/stefantaubert/mel-cepstral-distance/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/stefantaubert/mel-cepstral-distance/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/stefantaubert/mel-cepstral-distance/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/stefantaubert/mel-cepstral-distance/releases/tag/v0.0.1
