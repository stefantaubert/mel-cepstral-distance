"""
This module provides functions for processing and analyzing audio data, including
the computation of spectrograms, extraction of Mel-Frequency Cepstral Coefficients
(MFCCs), and calculation of the Mel-Cepstral Distance (MCD) between audio signals.

Functions
---------
- `get_amplitude_spectrogram`: Computes the Short-Time Fourier Transform (STFT)
  of an audio signal and returns the amplitude spectrogram.
- `get_mel_spectrogram`: Converts an amplitude spectrogram to a Mel spectrogram
  using mel filterbanks.
- `get_mfccs`: Extracts MFCCs from a Mel spectrogram.
- `compare_audio_files`: Compares two audio files by calculating the MCD and
  alignment penalty.
- `compare_amplitude_spectrograms`: Compares two amplitude spectrograms.
- `compare_mel_spectrograms`: Compares two Mel spectrograms.
- `compare_mfccs`: Compares two sets of MFCCs.

The `get_*` functions, while not directly invoked elsewhere in the module, can be used
independently to experiment with silence removal and parameter configurations. This
enables detailed analysis of how preprocessing affects subsequent alignment and distance
computations. For instance, with `get_amplitude_spectrogram`, you can test different
silence thresholds and window lengths to observe their impact on the resulting
spectrogram. Once you have generated spectrograms for both audio files, you can use the
`compare_amplitude_spectrograms` function to calculate the MCD and alignment penalty.
This approach can be similarly applied to the other `get_*`
functions and their corresponding `compare_*` functions.

Features
--------
- Silence removal at various stages of the processing pipeline.
- Alignment of spectrograms or MFCCs using zero-padding or Dynamic Time Warping (DTW).
- Flexible configuration of FFT parameters, mel filterbanks, and alignment strategies.

Notes
-----
- The module assumes that input audio files are mono WAV files. If the audio files
  contain multiple channels, preprocessing is required to convert them to mono.
- For optimal performance, FFT window lengths should be powers of 2 in samples.
- Silence removal is applied based on energy thresholds, either in the time domain
  or at different spectral levels (e.g., Mel spectrogram or MFCCs).
- The Mel-Cepstral Distance (MCD) is a commonly used metric for evaluating the
  similarity between two audio signals, particularly in speech synthesis and
  voice conversion tasks.
"""

from mel_cepstral_distance.api import (
  compare_amplitude_spectrograms,
  compare_audio_files,
  compare_mel_spectrograms,
  compare_mfccs,
  get_amplitude_spectrogram,
  get_mel_spectrogram,
  get_mfccs,
)

__all__ = [
  "get_mfccs",
  "get_mel_spectrogram",
  "get_amplitude_spectrogram",
  "compare_amplitude_spectrograms",
  "compare_mel_spectrograms",
  "compare_audio_files",
  "compare_mfccs",
]
