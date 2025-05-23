# mel-cepstral-distance

[![CI](https://github.com/stefantaubert/mel-cepstral-distance/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/stefantaubert/mel-cepstral-distance/actions/workflows/ci.yml)
[![codecov](https://codecov.io/github/stefantaubert/mel-cepstral-distance/branch/main/graph/badge.svg?token=DZ8LB2Q5I0)](https://codecov.io/github/stefantaubert/mel-cepstral-distance)
[![PyPI](https://img.shields.io/pypi/v/mel-cepstral-distance.svg)](https://pypi.python.org/pypi/mel-cepstral-distance)
[![PyPI](https://img.shields.io/pypi/pyversions/mel-cepstral-distance.svg)](https://pypi.python.org/pypi/mel-cepstral-distance)
[![MIT](https://img.shields.io/github/license/stefantaubert/mel-cepstral-distance.svg)](https://github.com/stefantaubert/mel-cepstral-distance/blob/main/LICENSE)
[![PyPI](https://img.shields.io/github/commits-since/stefantaubert/mel-cepstral-distance/latest/main.svg)](https://github.com/stefantaubert/mel-cepstral-distance/compare/v0.0.4...main)
[![PyPI Downloads](https://img.shields.io/pypi/dm/mel-cepstral-distance.svg?label=PyPI%20downloads)](https://pypi.org/project/mel-cepstral-distance)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15213012.svg)](https://doi.org/10.5281/zenodo.15213012)

A Python library for computing the Mel-Cepstral Distance (also known as Mel-Cepstral Distortion, MCD) between two inputs. This implementation is based on the method proposed by Robert F. Kubichek in [*Mel-Cepstral Distance Measure for Objective Speech Quality Assessment*](https://ieeexplore.ieee.org/document/407206).

- Compute MCD between two inputs: audio files, amplitude spectrograms, Mel spectrograms, or MFCCs.
- Calculate an alignment penalty (PEN) as an additional metric to indicate the extent of alignment applied.
- Remove pauses from audio files or feature representations (amplitude spectrograms, Mel spectrograms, or MFCCs) using a threshold.
- Align feature representations using either Dynamic Time Warping (DTW) or zero-padding.
- Experimental results show a moderate negative correlation with naturalness (Spearman: –0.31) and a weak negative correlation with intelligibility (–0.24). For a detailed analysis of parameter configurations and their impact on correlation strength, see the [experiment report](https://github.com/stefantaubert/mel-cepstral-distance/blob/main/experiments/README.md).

## Getting Started

### Installation

```sh
pip install mel-cepstral-distance
```

### Example usage

Compare two audio files with default parameters:

```py
from mel_cepstral_distance import compare_audio_files

mcd, penalty = compare_audio_files(
  'examples/GT.wav',
  'examples/Tacotron-2.wav',
)

print(f'MCD: {mcd:.2f}, Penalty: {penalty:.4f}')
# MCD: 7.45, Penalty: 0.1087
```

## Calculation

### Spectrogram

$$
X(k, m) = \text{FFT of } x_k(n), \text{ for real input.}
$$

Where:

- $X(k, m)$: The result (amplitude spectrogram) of the real-valued FFT for the $k$-th frame at frequency index $m$.
- $x_k(n)$: The time-domain signal of the $k$-th frame.
- $\text{FFT}$: The real-valued discrete Fourier transform, computed using `np.fft.rfft`.

### Mel spectrogram

$$
X_{k,n} = \log_{10}\left\lbrace\sum_m^M |X(k, m)|^2 \cdot w_n(m)\right\rbrace
$$

Where:

- $X_{k,n}$: The logarithmic Mel-scaled power spectrogram for the $k$-th frame at Mel frequency $n$.
- $X(k, m)$: The amplitude spectrum of the $k$-th frame at frequency $m$.
- $M$: The total number of Mel frequency bins.
- $w_n(m)$: The Mel filter bank weights for Mel frequency $n$ and frequency bin $m$.

### Mel-frequency cepstral coefficients

$$
MC_X(i, k) = \sum_{n=1}^{M} X_{k,n} \cos\left[i\left(n - \frac{1}{2}\right)\frac{\pi}{M}\right]
$$

Where:

- $MC_X(i, k)$: The $i$-th Mel-frequency cepstral coefficient (MFCC) for the $k$-th frame.
- $X_{k,n}$: The logarithmic Mel-scaled power spectrogram for the $k$-th frame at Mel frequency $n$.
- $M$: The total number of Mel frequency bins.
- $i$: The index of the MFCC being computed.

### Mel-cepstral distance

#### Per frame

$$
MCD(k) = \alpha\sqrt{\sum_{i=s}^{D} \left(MC_X(i, k) - MC_Y(i, k)\right)^2}
$$

Where:

- $MCD(k)$: The Mel-cepstral distance for the $k$-th frame.
- $MC_X(i, k)$: The $i$-th MFCC of the reference signal for the $k$-th frame.
- $MC_Y(i, k)$: The $i$-th MFCC of the target signal for the $k$-th frame.
- $D$: The number of MFCCs used in the computation.
- $\alpha$: Optional scaling factor used in some literature, e.g. $\frac{10\sqrt{2}}{\ln 10}$.
  - Note: Kubichek didn't use it, so it has value 1
- $s$: Parameter to exclude the 0th coefficient (corresponding to energy):
  - $s = 0$: Includes the 0th coefficient
  - $s = 1$: Excludes the 0th coefficient

#### Mean over all frames

$$
MCD = \frac{1}{N} \sum_{k=1}^{N} MCD(k)
$$

Where:

- $MCD$: The mean Mel-cepstral distance over all frames.
- $N$: The total number of frames.
- $MCD(k)$: The Mel-cepstral distance for the $k$-th frame.

### Alignment penalty during Dynamic Time Warping (DTW)

$$
PEN = 2 - \frac{N_X + N_Y}{N_{XY}}
$$

Where:

- $N_X$: The number of frames in the reference sequence.
- $N_Y$: The number of frames in the target sequence.
- $N_{XY}$: The number of frames after alignment (same for X and Y).
- $PEN$: A value in interval $[0, 1)$, where a smaller value indicates less alignment.

### Used parameters in literature

| Literature | Sampling Rate | Window Size           | Hop Length           | FFT Size     | Window Function | $M$ | Min Frequency | Max Frequency | $s$ | $D$ | Pause | DTW | $\alpha$                      | Smallest MCD | Largest MCD | Citation MCD | Domain  |
| ---------- | ------------- | --------------------- | -------------------- | ------------ | --------------- | --- | ------------- | ------------- | --- | --- | ----- | --- | ----------------------------- | ------------ | ----------- | ------------ | ------- |
| [1]        | 8kHz          | 32ms/256              | <16ms/128*           | 32ms/256*    | ?               | 20  | 0Hz*          | 4kHz*         | 1   | 16  | no    | no  | 1                             | ~0.8         | ~1.05       | original     | generic |
| [2]        | ?             | ?                     | ?                    | ?            | ?               | 80* | 80Hz*         | 12kHz*        | 1   | 13  | yes*  | no  | 1                             | 0.294        | 0.518       | [3]          | TTS     |
| [3]        | 24kHz*        | ?                     | ?                    | ?            | ?               | 80  | 80Hz          | 12kHz         | 1   | 13  | yes*  | no  | 1                             | 6.99         | 12.37       | [1]          | TTS     |
| [4]        | 16kHz*        | 25ms                  | 5ms                  | ?            | ?               | ?   | 0Hz*          | 8kHz*         | 1   | 24  | yes*  | no  | $\frac{10}{\ln(10)}$          | ~2.5dB       | ~12.5dB     | [5]          | TTS     |
| [5]        | ?             | 30ms                  | 10ms                 | ?            | Hamming         | ?   | ?             | ?             | 1   | 10  | yes*  | yes | 1                             | 3.415        | 4.066       | [1]          | TTS     |
| [6]        | ?             | >10ms*                | 5ms                  | >10ms*       | Gaussian*       | ?   | ?             | 8kHz*         | 1   | 24  | no    | no  | $\frac{10 \sqrt{2}}{\ln(10)}$ | ~4.75        | ~6          | [7]          | VC      |
| [7]        | 16kHz         | 40ms*                 | 5ms                  | 64ms/1024    | Gaussian        | ?   | ?             | 12kHz         | 1   | 40  | yes   | no  | $\frac{10 \sqrt{2}}{\ln(10)}$ | 2.32dB       | 3.53dB      | none         | TTS     |
| [8]        | 24kHz         | 50ms/1200             | 12.5ms/300           | 2048/~85.3ms | Hann            | 80  | 80Hz          | 12kHz         | 1   | 13  | yes*  | yes | 1                             | 4.83         | 5.68        | [1]          | TTS     |
| [9]        | 16kHz         | 64ms/1024             | 16ms/256             | 128ms/2048   | Hann            | 80  | 125Hz         | 7.6kHz        | 1*  | 16* | yes*  | yes | 1*                            | 10.62        | 14.38       | [1]          | TTS     |
| [10]       | 16kHz         | ?                     | ?                    | ?            | ?               | ?   | ?             | ?             | 1   | 16* | yes*  | yes | 1*                            | 8.67         | 19.41       | none         | TTS     |
| [11]       | 16kHz*        | 64ms* (at 16kHz)/1024 | 16ms* (at 16kHz)/256 | 64ms*/1024*  | Hann*           | 80  | 0Hz           | 8kHz          | 1   | 60  | yes*  | no  | $\frac{10 \sqrt{2}}{\ln(10)}$ | 5.32dB       | 6.78dB      | [12]         | TTS     |

*Parameters are not explicitly stated, but were estimated from the information in the literature.
  
**Literature:**

- [1] Kubichek, R. (1993). Mel-cepstral distance measure for objective speech quality assessment. Proceedings of IEEE Pacific Rim Conference on Communications Computers and Signal Processing, 1, 125–128. https://doi.org/10.1109/PACRIM.1993.407206 
- [2] Lee, Y., & Kim, T. (2019). Robust and Fine-grained Prosody Control of End-to-end Speech Synthesis. ICASSP 2019 - 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 5911–5915. https://doi.org/10.1109/ICASSP.2019.8683501
- [3] **Ref-Tacotron** -> Skerry-Ryan, R. J., Battenberg, E., Xiao, Y., Wang, Y., Stanton, D., Shor, J., Weiss, R., Clark, R., & Saurous, R. A. (2018). Towards End-to-End Prosody Transfer for Expressive Speech Synthesis with Tacotron. Proceedings of the 35th International Conference on Machine Learning, 4693–4702. https://proceedings.mlr.press/v80/skerry-ryan18a.html
- [4] Nature/ansp19-503 Anumanchipalli, G. K., Chartier, J., & Chang, E. F. (2019). Speech synthesis from neural decoding of spoken sentences. Nature, 568(7753), Article 7753. https://doi.org/10.1038/s41586-019-1119-1
- [5] Shah, N. J., Vachhani, B. B., Sailor, H. B., & Patil, H. A. (2014). Effectiveness of PLP-based phonetic segmentation for speech synthesis. 2014 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 270–274. https://doi.org/10.1109/ICASSP.2014.6853600
- [6] Kominek, J., Schultz, T., & Black, A. W. (2008). Synthesizer voice quality of new languages calibrated with mean Mel cepstral distortion. SLTU, 63–68. http://www.cs.cmu.edu/~./awb/papers/sltu2008/kominek_black.sltu_2008.pdf
- [7] Mashimo, M., Toda, T., Shikano, K., & Campbell, N. (2001). Evaluation of cross-language voice conversion based on GMM and straight. 7th European Conference on Speech Communication and Technology (Eurospeech 2001), 361–364. https://doi.org/10.21437/Eurospeech.2001-111
- [8] **Capacitron** -> Battenberg, E., Mariooryad, S., Stanton, D., Skerry-Ryan, R. J., Shannon, M., Kao, D., & Bagby, T. (2019). Effective Use of Variational Embedding Capacity in Expressive End-to-End Speech Synthesis (No. arXiv:1906.03402). arXiv. http://arxiv.org/abs/1906.03402
- [9] **Attentron** -> Choi, S., Han, S., Kim, D., & Ha, S. (2020). Attentron: Few-Shot Text-to-Speech Utilizing Attention-Based Variable-Length Embedding. Interspeech 2020, 2007–2011. https://doi.org/10.21437/Interspeech.2020-2096
- [10] **VoiceLoop** -> Taigman, Y., Wolf, L., Polyak, A., & Nachmani, E. (2018). VoiceLoop: Voice Fitting and Synthesis via a Phonological Loop. 6th International Conference on Learning Representations (ICLR 2018), 2, 1374–1387. https://openreview.net/forum?id=SkFAWax0-
- [11] **MIST-Tacotron** -> Moon, S., Kim, S., & Choi, Y.-H. (2022). MIST-Tacotron: End-to-End Emotional Speech Synthesis Using Mel-Spectrogram Image Style Transfer. IEEE Access, 10, 25455–25463. IEEE Access. https://doi.org/10.1109/ACCESS.2022.3156093
- [12] Kim, J., Choi, H., Park, J., Hahn, M., Kim, S., & Kim, J.-J. (2018). Korean Singing Voice Synthesis Based on an LSTM Recurrent Neural Network. Interspeech 2018, 1551–1555. https://doi.org/10.21437/Interspeech.2018-1575

### Default parameters

Based on the values in the literature the default parameters were set:

- Hop Length (hop_len): 8 ms
  - Note: should be 1/2 or 1/4 of the window size
- Window Size (win_len): 32 ms
- FFT Size (n_fft): 32 ms
  - For faster computation, the sample equivalent should be a power of 2.
- Window Function (window): Hanning
- Sampling Rate (sample_rate): is taken from the audio file
- Minimum Frequency (fmin): 0 Hz
- Maximum Frequency (fmax): sampling rate / 2
  - Cannot exceed half the sampling rate.
- Num. Mel-Bands ($M$): 20
  - Increasing the number will increase the resulting MCD values.
- $s$: 1
- $D$: 16
- $\alpha$: 1 (alternate values can be applied by multiplying the MCD with a custom factor)
- Aligning: DTW
- Align Target (align_target): MFCC
- Remove Silence: No
  - Silence can be removed from Mel spectrograms before computing the MCD, with dataset-specific thresholds.

### Suggested parameters

Based on the conducted [experiments](https://github.com/stefantaubert/mel-cepstral-distance/blob/main/experiments/README.md), the following parameter settings are recommended to achieve the strongest correlation with subjective ratings:

```
sample_rate = 96000 Hz
n_fft = 64 ms
win_len = 32 ms
hop_len = 16 ms
window = 'hanning'
fmin = 0 Hz
fmax = 48000 Hz
M = 20
s = 1
D = 13
align_method = 'dtw'
align_target = 'mel'
remove_silence = 'no'
silence_threshold_A = None
silence_threshold_B = None
norm_audio = True
dtw_radius = 2
```

Furthermore, combining MCD and PEN using the formula `MCD*(PEN+1)` yield the strongest correlation with subjective ratings, according to the experimental results.

**Note:** To enable meaningful cross-paper comparisons, it is strongly recommended that users of this library—whether adopting it directly or implementing their own version—explicitly report all parameter settings used for feature extraction and distance calculation, as inconsistent or undocumented configurations remain a major issue in the current literature.


## License

MIT License

## Citation

If you want to cite this repo, you can use the BibTeX-entry generated by GitHub (see *About => Cite this repository*).

```txt
Taubert, S., & Sternkopf, J. (2025). mel-cepstral-distance (Version 0.0.4) [Computer software]. https://doi.org/10.5281/zenodo.15213012
```

## Acknowledgments

Funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – Project-ID 416228727 – CRC 1410
