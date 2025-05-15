# Analysis of MCD and intelligibility MOS Kendall_tau correlation

## Metrics

| obj_metric      |   mean |   median |
|-----------------|--------|----------|
| mcd*(pen+0.5)   | -0.081 |   -0.085 |
| mcd*(pen+0.25)  | -0.08  |   -0.084 |
| mcd*(pen+0.1)   | -0.077 |   -0.081 |
| mcd*(pen+1)     | -0.076 |   -0.08  |
| mcd*pen         | -0.072 |   -0.076 |
| pen*(mcd+1)     | -0.07  |   -0.075 |
| mcd*(pen+2)     | -0.07  |   -0.073 |
| pen             | -0.062 |   -0.068 |
| mcd+pen         | -0.06  |   -0.064 |
| mcd             | -0.057 |   -0.06  |
| sqrt(mcd²+pen²) | -0.056 |   -0.06  |
| mcd-pen         | -0.051 |   -0.052 |
| mcd*(pen-1)     |  0.01  |    0.008 |

## Default parameters for experiments

- obj_metric = mcd*(pen+0.5)
- sample_rate = 96000
- n_fft = 128
- win_len = 128
- hop_len = 32
- window = hanning
- fmin = 0
- fmax = 48000
- s = 1
- M = 20
- D = 16
- align_method = dtw
- align_target = mfcc
- remove_silence = no
- silence_threshold_A = None
- silence_threshold_B = None
- norm_audio = True
- dtw_radius = 10

## Experiment - Sample rate

- Experimented parameter(s):
  - sample_rate = 4000, 8000, 16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000, 192000
- Results (format = {sample_rate}):
  - Kendall_tau -0.098: 44100
  - Kendall_tau -0.092: 96000
  - Kendall_tau -0.086: 24000
  - Kendall_tau -0.085: 88200
  - Kendall_tau -0.084: 32000
  - Kendall_tau -0.083: 22050, 8000
  - Kendall_tau -0.082: 192000
  - Kendall_tau -0.081: 48000
  - Kendall_tau -0.070: 16000
  - Kendall_tau -0.042: 4000

## Experiment - Minimum frequency

- Experimented parameter(s):
  - fmin = 0, 100, 500, 1000, 2000, 4000, 8000, 16000, 22050, 44100
- Results (format = {fmin}):
  - Kendall_tau -0.109: 1000
  - Kendall_tau -0.105: 8000
  - Kendall_tau -0.100: 500
  - Kendall_tau -0.092: 0
  - Kendall_tau -0.090: 100
  - Kendall_tau -0.081: 2000
  - Kendall_tau -0.057: 22050
  - Kendall_tau -0.055: 4000
  - Kendall_tau -0.047: 44100
  - Kendall_tau 0.026: 16000

## Experiment - Maximum frequency

- Changed parameter(s): sample_rate=192000
- Experimented parameter(s):
  - fmax = 4000, 8000, 11025, 16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000
- Results (format = {fmax}):
  - Kendall_tau -0.097: 88200
  - Kendall_tau -0.096: 22050
  - Kendall_tau -0.091: 48000
  - Kendall_tau -0.086: 11025
  - Kendall_tau -0.084: 32000, 44100
  - Kendall_tau -0.082: 4000, 96000
  - Kendall_tau -0.081: 24000
  - Kendall_tau -0.080: 16000
  - Kendall_tau -0.068: 8000

## Experiment - Number of mel filterbanks

- Changed parameter(s): D=10
- Experimented parameter(s):
  - M = 10, 11, 12, 13, 20, 30, 40, 50, 60, 70, 80
- Results (format = {M}):
  - Kendall_tau -0.089: 80
  - Kendall_tau -0.087: 70
  - Kendall_tau -0.083: 30
  - Kendall_tau -0.082: 50
  - Kendall_tau -0.080: 13, 60
  - Kendall_tau -0.077: 20
  - Kendall_tau -0.075: 40
  - Kendall_tau -0.070: 10
  - Kendall_tau -0.069: 12
  - Kendall_tau -0.061: 11

## Experiment - Starting index

- Experimented parameter(s):
  - s = 0, 1, 2, 3, 4, 5, 6, 7, 8
- Results (format = {s}):
  - Kendall_tau -0.166: 5
  - Kendall_tau -0.163: 6
  - Kendall_tau -0.133: 8
  - Kendall_tau -0.131: 7
  - Kendall_tau -0.130: 4
  - Kendall_tau -0.121: 3
  - Kendall_tau -0.108: 2
  - Kendall_tau -0.093: 0
  - Kendall_tau -0.086: 1

## Experiment - Number of MFCC coefficients (M=80)

- Changed parameter(s): M=80
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 30, 40, 50, 60, 70, 80
- Results (format = {D}):
  - Kendall_tau -0.096: 16
  - Kendall_tau -0.093: 13, 15
  - Kendall_tau -0.091: 14, 60, 80
  - Kendall_tau -0.090: 30, 50, 70
  - Kendall_tau -0.089: 10, 19
  - Kendall_tau -0.088: 17, 18
  - Kendall_tau -0.087: 12
  - Kendall_tau -0.084: 11, 40
  - Kendall_tau -0.083: 8
  - Kendall_tau -0.080: 9
  - Kendall_tau -0.076: 7
  - Kendall_tau -0.070: 6
  - Kendall_tau -0.058: 5
  - Kendall_tau -0.055: 2
  - Kendall_tau -0.038: 4
  - Kendall_tau -0.015: 3

## Experiment - Number of MFCC coefficients (M=40)

- Changed parameter(s): M=40
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 25, 30, 35, 40
- Results (format = {D}):
  - Kendall_tau -0.092: 17
  - Kendall_tau -0.089: 35
  - Kendall_tau -0.088: 14, 16, 18, 25, 30
  - Kendall_tau -0.087: 19
  - Kendall_tau -0.086: 15, 40
  - Kendall_tau -0.085: 12
  - Kendall_tau -0.084: 13
  - Kendall_tau -0.082: 11
  - Kendall_tau -0.077: 8
  - Kendall_tau -0.075: 10
  - Kendall_tau -0.067: 6
  - Kendall_tau -0.064: 9
  - Kendall_tau -0.063: 7
  - Kendall_tau -0.053: 2
  - Kendall_tau -0.043: 5
  - Kendall_tau -0.033: 4
  - Kendall_tau -0.029: 3

## Experiment - Number of MFCC coefficients (M=20)

- Changed parameter(s): M=20
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
- Results (format = {D}):
  - Kendall_tau -0.092: 15, 16
  - Kendall_tau -0.089: 17
  - Kendall_tau -0.085: 14, 19, 20
  - Kendall_tau -0.084: 13
  - Kendall_tau -0.083: 12
  - Kendall_tau -0.082: 18
  - Kendall_tau -0.081: 11
  - Kendall_tau -0.079: 8
  - Kendall_tau -0.077: 10
  - Kendall_tau -0.076: 7
  - Kendall_tau -0.075: 9
  - Kendall_tau -0.071: 6
  - Kendall_tau -0.064: 2
  - Kendall_tau -0.056: 4
  - Kendall_tau -0.052: 3
  - Kendall_tau -0.051: 5

## Experiment - Number of MFCC coefficients (M=10)

- Changed parameter(s): M=10
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10
- Results (format = {D}):
  - Kendall_tau -0.075: 8
  - Kendall_tau -0.073: 2
  - Kendall_tau -0.070: 10, 9
  - Kendall_tau -0.068: 7
  - Kendall_tau -0.065: 6
  - Kendall_tau -0.055: 5
  - Kendall_tau -0.049: 3
  - Kendall_tau -0.035: 4

## Experiment - Number of MFCC coefficients (M=5)

- Changed parameter(s): M=5
- Experimented parameter(s):
  - D = 2, 3, 4, 5
- Results (format = {D}):
  - Kendall_tau -0.084: 2
  - Kendall_tau -0.054: 3
  - Kendall_tau -0.028: 4, 5

## Experiment - Silence removal

- Experimented parameter(s):
  - remove_silence = mel, no
  - silence_threshold_A = -4, -3.5, -3, None
  - silence_threshold_B = None, -4.5, -4, -3.5
- Results (format = {remove_silence:silence_threshold_A:silence_threshold_B}):
  - Kendall_tau -0.092: no:None:None
  - Kendall_tau -0.077: mel:-3.5:-4
  - Kendall_tau -0.065: mel:-4:-4.5
  - Kendall_tau -0.042: mel:-3:-3.5

## Experiment - Normalize audio

- Experimented parameter(s):
  - norm_audio = False, True
- Results (format = {norm_audio}):
  - Kendall_tau -0.094: False
  - Kendall_tau -0.092: True

## Experiment - Alignment method

- Experimented parameter(s):
  - align_method = dtw, pad
  - align_target = mel, mfcc, spec
- Results (format = {align_method:align_target}):
  - Kendall_tau -0.095: dtw:mel
  - Kendall_tau -0.092: dtw:mfcc
  - Kendall_tau -0.053: dtw:spec
  - Kendall_tau 0.002: pad:mel, pad:mfcc, pad:spec

## Experiment - Sakoe-Chiba radius

- Experimented parameter(s):
  - dtw_radius = 1, 2, 3, 10, 20, 40, None
- Results (format = {dtw_radius}):
  - Kendall_tau -0.092: 1, 10, 2, 20, 3, 40, None

## Experiment - Window function

- Experimented parameter(s):
  - window = hamming, hanning
- Results (format = {window}):
  - Kendall_tau -0.092: hanning
  - Kendall_tau -0.081: hamming

## Experiment - FFT window length

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {n_fft}):
  - Kendall_tau -0.112: 16
  - Kendall_tau -0.100: 256
  - Kendall_tau -0.098: 32
  - Kendall_tau -0.095: 8
  - Kendall_tau -0.092: 128
  - Kendall_tau -0.091: 512
  - Kendall_tau -0.090: 64
  - Kendall_tau -0.086: 1024

## Experiment - Window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len}):
  - Kendall_tau -0.096: 1024
  - Kendall_tau -0.092: 128
  - Kendall_tau -0.086: 256
  - Kendall_tau -0.084: 512
  - Kendall_tau -0.073: 64
  - Kendall_tau -0.064: 16
  - Kendall_tau -0.047: 32
  - Kendall_tau -0.033: 8

## Experiment - Hop length

- Experimented parameter(s):
  - hop_len = 8, 16, 32, 64, 128
- Results (format = {hop_len}):
  - Kendall_tau -0.125: 64
  - Kendall_tau -0.099: 8
  - Kendall_tau -0.092: 32
  - Kendall_tau -0.091: 16
  - Kendall_tau -0.047: 128

## Experiment - Equal FFT window length and window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len:n_fft}):
  - Kendall_tau -0.106: 16:16
  - Kendall_tau -0.097: 8:8
  - Kendall_tau -0.094: 32:32
  - Kendall_tau -0.092: 128:128
  - Kendall_tau -0.089: 64:64
  - Kendall_tau -0.087: 256:256
  - Kendall_tau -0.083: 1024:1024
  - Kendall_tau -0.077: 512:512

## Experiment - FFT window length, window length and hop length with ratio 4:4:1

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {win_len:n_fft:hop_len}):
  - Kendall_tau -0.111: 64:64:16
  - Kendall_tau -0.108: 32:32:8
  - Kendall_tau -0.105: 16:16:4
  - Kendall_tau -0.099: 8:8:2
  - Kendall_tau -0.092: 128:128:32
  - Kendall_tau -0.088: 256:256:64
  - Kendall_tau -0.069: 512:512:128
  - Kendall_tau -0.040: 1024:1024:256

## Experiment - FFT window length, window length and hop length with ratio 9:3:1

- Experimented parameter(s):
  - n_fft = 16, 32, 64, 128, 256, 512, 1024
  - win_len = 5, 10, 21, 42, 85, 170, 341
  - hop_len = 1, 3, 7, 14, 28, 56, 113
- Results (format = {n_fft:win_len:hop_len}):
  - Kendall_tau -0.094: 512:170:56
  - Kendall_tau -0.083: 128:42:14
  - Kendall_tau -0.074: 64:21:7
  - Kendall_tau -0.072: 256:85:28
  - Kendall_tau -0.054: 32:10:3
  - Kendall_tau -0.046: 16:5:1
  - Kendall_tau -0.021: 1024:341:113

## Experiment - FFT window length, window length and hop length with ratio 4:2:1

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 64, 128, 256, 512
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - Kendall_tau -0.090: 32:16:8, 64:32:16
  - Kendall_tau -0.085: 256:128:64
  - Kendall_tau -0.073: 128:64:32
  - Kendall_tau -0.068: 512:256:128
  - Kendall_tau -0.059: 16:8:4
  - Kendall_tau -0.045: 8:4:2
  - Kendall_tau 0.012: 1024:512:256

## Experiment - FFT window length, window length and hop length with different ratios

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 46.44, 64, 85.33, 100, 120, 128, 170.67, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 46.44, 50, 60, 64, 85.33, 100, 120, 128, 170.67, 256, 512
  - hop_len = 2, 4, 8, 11.61, 16, 21.33, 25, 30, 32, 42.67, 48, 50, 60, 64, 85.33, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - Kendall_tau -0.129: 256:128:16
  - Kendall_tau -0.126: 100:50:25
  - Kendall_tau -0.125: 128:128:64
  - Kendall_tau -0.119: 128:256:64
  - Kendall_tau -0.116: 16:16:8
  - Kendall_tau -0.115: 256:128:8
  - Kendall_tau -0.114: 128:64:16
  - Kendall_tau -0.113: 100:100:50
  - Kendall_tau -0.111: 64:64:8
  - Kendall_tau -0.110: 100:100:25
  - Kendall_tau -0.108: 32:32:8, 512:256:32
  - Kendall_tau -0.106: 120:120:30
  - Kendall_tau -0.105: 16:16:4
  - Kendall_tau -0.103: 128:64:8
  - Kendall_tau -0.101: 8:8:4
  - Kendall_tau -0.100: 256:128:32, 256:64:8, 85.33:85.33:21.33
  - Kendall_tau -0.099: 85.33:85.33:42.67, 8:8:2
  - Kendall_tau -0.094: 170.67:170.67:42.67
  - Kendall_tau -0.093: 120:60:30, 128:32:8
  - Kendall_tau -0.092: 128:128:32, 64:32:8
  - Kendall_tau -0.091: 128:128:16
  - Kendall_tau -0.090: 32:16:8, 64:32:16
  - Kendall_tau -0.089: 64:64:32
  - Kendall_tau -0.088: 64:64:48
  - Kendall_tau -0.087: 256:256:32
  - Kendall_tau -0.086: 128:256:32
  - Kendall_tau -0.084: 120:120:60
  - Kendall_tau -0.080: 46.44:46.44:11.61
  - Kendall_tau -0.073: 128:64:32
  - Kendall_tau -0.069: 512:512:128
  - Kendall_tau -0.045: 8:4:2
  - Kendall_tau -0.040: 170.67:170.67:85.33
  - Kendall_tau 0.012: 1024:512:256

## Experiment - Finding optimal Pearson parameters (baseline)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = True
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - Kendall_tau -0.068: 128:64:16:12:mel:True

## Experiment - Finding optimal Pearson parameters (norm=False)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = False
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - Kendall_tau -0.086: 128:64:16:12:mel:False

## Experiment - Finding optimal Pearson parameters (radius)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = True
  - dtw_radius = 1, 2, 3, 4, 10
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio:dtw_radius}):
  - Kendall_tau -0.074: 128:64:16:12:mel:True:3, 128:64:16:12:mel:True:4
  - Kendall_tau -0.069: 128:64:16:12:mel:True:2
  - Kendall_tau -0.068: 128:64:16:12:mel:True:10
  - Kendall_tau -0.060: 128:64:16:12:mel:True:1

## Experiment - Finding optimal Spearman parameters (baseline)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 10
  - M = 11
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - Kendall_tau -0.061: 64:32:16:10:11:mel

## Experiment - Finding optimal Spearman parameters (D, M)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 12, 13
  - M = 20
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - Kendall_tau -0.070: 64:32:16:13:20:mel
  - Kendall_tau -0.069: 64:32:16:12:20:mel

## Experiment - Finding optimal Spearman parameters (norm)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 13
  - M = 20
  - align_target = mel
  - norm_audio = False
- Results (format = {n_fft:win_len:hop_len:D:M:align_target:norm_audio}):
  - Kendall_tau -0.096: 64:32:16:13:20:mel:False

## Experiment - Finding optimal Spearman parameters (radius)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 13
  - M = 20
  - align_target = mel
  - dtw_radius = 1, 2, 3, 4, 10
- Results (format = {n_fft:win_len:hop_len:D:M:align_target:dtw_radius}):
  - Kendall_tau -0.070: 64:32:16:13:20:mel:10, 64:32:16:13:20:mel:3, 64:32:16:13:20:mel:4
  - Kendall_tau -0.068: 64:32:16:13:20:mel:1
  - Kendall_tau -0.066: 64:32:16:13:20:mel:2

## Best experiments

### 1. Place

- Kendall_tau: -0.1663373744000734
- Experiments with that score (#1):
  - 'Starting index' with parameters:
    - sample_rate = 96000
    - n_fft = 128
    - win_len = 128
    - hop_len = 32
    - window = hanning
    - fmin = 0
    - fmax = 48000
    - s = 5
    - M = 16
    - D = 10
    - align_method = dtw
    - align_target = mfcc
    - remove_silence = no
    - silence_threshold_A = None
    - silence_threshold_B = None
    - norm_audio = True
    - dtw_radius = 10

### 2. Place

- Kendall_tau: -0.1631913409278046
- Experiments with that score (#1):
  - 'Starting index' with parameters:
    - sample_rate = 96000
    - n_fft = 128
    - win_len = 128
    - hop_len = 32
    - window = hanning
    - fmin = 0
    - fmax = 48000
    - s = 6
    - M = 16
    - D = 10
    - align_method = dtw
    - align_target = mfcc
    - remove_silence = no
    - silence_threshold_A = None
    - silence_threshold_B = None
    - norm_audio = True
    - dtw_radius = 10

### 3. Place

- Kendall_tau: -0.1333406047258121
- Experiments with that score (#1):
  - 'Starting index' with parameters:
    - sample_rate = 96000
    - n_fft = 128
    - win_len = 128
    - hop_len = 32
    - window = hanning
    - fmin = 0
    - fmax = 48000
    - s = 8
    - M = 16
    - D = 10
    - align_method = dtw
    - align_target = mfcc
    - remove_silence = no
    - silence_threshold_A = None
    - silence_threshold_B = None
    - norm_audio = True
    - dtw_radius = 10
