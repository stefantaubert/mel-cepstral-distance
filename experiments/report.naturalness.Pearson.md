# Analysis of MCD and naturalness MOS Pearson correlation

## Metrics

| obj_metric      |   mean |   median |
|-----------------|--------|----------|
| mcd*(pen+1)     | -0.27  |   -0.286 |
| mcd*(pen+2)     | -0.267 |   -0.285 |
| mcd*(pen+0.5)   | -0.263 |   -0.275 |
| mcd+pen         | -0.261 |   -0.279 |
| sqrt(mcd²+pen²) | -0.253 |   -0.274 |
| mcd             | -0.251 |   -0.274 |
| mcd*(pen+0.25)  | -0.245 |   -0.259 |
| mcd-pen         | -0.239 |   -0.268 |
| mcd*(pen+0.1)   | -0.221 |   -0.227 |
| mcd*pen         | -0.195 |   -0.194 |
| pen*(mcd+1)     | -0.19  |   -0.189 |
| pen             | -0.143 |   -0.143 |
| mcd*(pen-1)     |  0.155 |    0.178 |

## Default parameters for experiments

- obj_metric = mcd*(pen+1)
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
  - Pearson -0.318: 96000
  - Pearson -0.287: 88200
  - Pearson -0.272: 48000
  - Pearson -0.238: 32000
  - Pearson -0.226: 192000, 44100
  - Pearson -0.196: 24000
  - Pearson -0.195: 22050
  - Pearson -0.171: 16000
  - Pearson -0.123: 8000
  - Pearson -0.006: 4000

## Experiment - Minimum frequency

- Experimented parameter(s):
  - fmin = 0, 100, 500, 1000, 2000, 4000, 8000, 16000, 22050, 44100
- Results (format = {fmin}):
  - Pearson -0.318: 0
  - Pearson -0.303: 500
  - Pearson -0.300: 100
  - Pearson -0.236: 1000
  - Pearson -0.206: 2000
  - Pearson -0.199: 4000
  - Pearson -0.196: 8000
  - Pearson -0.022: 22050
  - Pearson -0.016: 44100
  - Pearson 0.058: 16000

## Experiment - Maximum frequency

- Changed parameter(s): sample_rate=192000
- Experimented parameter(s):
  - fmax = 4000, 8000, 11025, 16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000
- Results (format = {fmax}):
  - Pearson -0.319: 48000
  - Pearson -0.315: 88200
  - Pearson -0.306: 44100
  - Pearson -0.285: 32000
  - Pearson -0.271: 24000
  - Pearson -0.251: 16000
  - Pearson -0.228: 22050
  - Pearson -0.226: 96000
  - Pearson -0.188: 11025
  - Pearson -0.167: 8000
  - Pearson -0.122: 4000

## Experiment - Number of mel filterbanks

- Changed parameter(s): D=10
- Experimented parameter(s):
  - M = 10, 11, 12, 13, 20, 30, 40, 50, 60, 70, 80
- Results (format = {M}):
  - Pearson -0.318: 20
  - Pearson -0.308: 11
  - Pearson -0.305: 40
  - Pearson -0.299: 50
  - Pearson -0.297: 70
  - Pearson -0.296: 12
  - Pearson -0.293: 80
  - Pearson -0.291: 60
  - Pearson -0.277: 30
  - Pearson -0.273: 13
  - Pearson -0.268: 10

## Experiment - Starting index

- Experimented parameter(s):
  - s = 0, 1, 2, 3, 4, 5, 6, 7, 8
- Results (format = {s}):
  - Pearson -0.296: 1
  - Pearson -0.294: 0
  - Pearson -0.268: 3
  - Pearson -0.253: 8
  - Pearson -0.248: 2
  - Pearson -0.244: 7
  - Pearson -0.224: 6
  - Pearson -0.212: 4
  - Pearson -0.210: 5

## Experiment - Number of MFCC coefficients (M=80)

- Changed parameter(s): M=80
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 30, 40, 50, 60, 70, 80
- Results (format = {D}):
  - Pearson -0.308: 12, 13
  - Pearson -0.304: 14, 15
  - Pearson -0.303: 19
  - Pearson -0.302: 11, 18
  - Pearson -0.300: 17
  - Pearson -0.298: 16
  - Pearson -0.293: 10
  - Pearson -0.285: 9
  - Pearson -0.282: 8
  - Pearson -0.277: 30, 7
  - Pearson -0.271: 6
  - Pearson -0.249: 5
  - Pearson -0.245: 40
  - Pearson -0.240: 4
  - Pearson -0.230: 50
  - Pearson -0.223: 60
  - Pearson -0.221: 70
  - Pearson -0.219: 80
  - Pearson -0.210: 2
  - Pearson -0.208: 3

## Experiment - Number of MFCC coefficients (M=40)

- Changed parameter(s): M=40
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 25, 30, 35, 40
- Results (format = {D}):
  - Pearson -0.313: 13
  - Pearson -0.310: 12, 14
  - Pearson -0.309: 11
  - Pearson -0.308: 15, 19
  - Pearson -0.307: 18
  - Pearson -0.305: 10, 17
  - Pearson -0.303: 16
  - Pearson -0.293: 9
  - Pearson -0.291: 25
  - Pearson -0.290: 8
  - Pearson -0.285: 7
  - Pearson -0.280: 6
  - Pearson -0.274: 30
  - Pearson -0.268: 35
  - Pearson -0.267: 40
  - Pearson -0.258: 5
  - Pearson -0.255: 4
  - Pearson -0.216: 3
  - Pearson -0.193: 2

## Experiment - Number of MFCC coefficients (M=20)

- Changed parameter(s): M=20
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
- Results (format = {D}):
  - Pearson -0.324: 12
  - Pearson -0.323: 13
  - Pearson -0.322: 14
  - Pearson -0.321: 18
  - Pearson -0.320: 11, 17
  - Pearson -0.319: 15, 19, 20
  - Pearson -0.318: 10, 16
  - Pearson -0.314: 8, 9
  - Pearson -0.307: 6
  - Pearson -0.299: 7
  - Pearson -0.296: 5
  - Pearson -0.280: 4
  - Pearson -0.232: 3
  - Pearson -0.169: 2

## Experiment - Number of MFCC coefficients (M=10)

- Changed parameter(s): M=10
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10
- Results (format = {D}):
  - Pearson -0.281: 6
  - Pearson -0.273: 7
  - Pearson -0.271: 5, 8
  - Pearson -0.268: 10, 9
  - Pearson -0.255: 4
  - Pearson -0.232: 3
  - Pearson -0.143: 2

## Experiment - Number of MFCC coefficients (M=5)

- Changed parameter(s): M=5
- Experimented parameter(s):
  - D = 2, 3, 4, 5
- Results (format = {D}):
  - Pearson -0.219: 4, 5
  - Pearson -0.201: 3
  - Pearson -0.179: 2

## Experiment - Silence removal

- Experimented parameter(s):
  - remove_silence = mel, no
  - silence_threshold_A = -4, -3.5, -3, None
  - silence_threshold_B = -4.5, -4, -3.5, None
- Results (format = {remove_silence:silence_threshold_A:silence_threshold_B}):
  - Pearson -0.318: no:None:None
  - Pearson -0.252: mel:-4:-4.5
  - Pearson -0.246: mel:-3.5:-4
  - Pearson -0.215: mel:-3:-3.5

## Experiment - Normalize audio

- Experimented parameter(s):
  - norm_audio = False, True
- Results (format = {norm_audio}):
  - Pearson -0.323: False
  - Pearson -0.318: True

## Experiment - Alignment method

- Experimented parameter(s):
  - align_method = dtw, pad
  - align_target = mel, mfcc, spec
- Results (format = {align_method:align_target}):
  - Pearson -0.330: dtw:mel
  - Pearson -0.318: dtw:mfcc
  - Pearson -0.270: dtw:spec
  - Pearson -0.060: pad:mel, pad:mfcc, pad:spec

## Experiment - Sakoe-Chiba radius

- Experimented parameter(s):
  - dtw_radius = 1, 2, 3, 10, 20, 40, None
- Results (format = {dtw_radius}):
  - Pearson -0.318: 1, 10, 2, 20, 3, 40, None

## Experiment - Window function

- Experimented parameter(s):
  - window = hamming, hanning
- Results (format = {window}):
  - Pearson -0.318: hanning
  - Pearson -0.294: hamming

## Experiment - FFT window length

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {n_fft}):
  - Pearson -0.318: 128
  - Pearson -0.287: 64
  - Pearson -0.279: 8
  - Pearson -0.276: 256
  - Pearson -0.274: 32
  - Pearson -0.265: 512
  - Pearson -0.262: 1024
  - Pearson -0.260: 16

## Experiment - Window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len}):
  - Pearson -0.318: 128
  - Pearson -0.306: 256
  - Pearson -0.291: 512
  - Pearson -0.279: 1024
  - Pearson -0.273: 64
  - Pearson -0.247: 32
  - Pearson -0.228: 16
  - Pearson -0.168: 8

## Experiment - Hop length

- Experimented parameter(s):
  - hop_len = 8, 16, 32, 64, 128
- Results (format = {hop_len}):
  - Pearson -0.318: 32
  - Pearson -0.300: 16
  - Pearson -0.290: 8
  - Pearson -0.273: 64
  - Pearson -0.223: 128

## Experiment - Equal FFT window length and window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len:n_fft}):
  - Pearson -0.318: 128:128
  - Pearson -0.305: 256:256
  - Pearson -0.283: 64:64
  - Pearson -0.278: 512:512
  - Pearson -0.271: 8:8
  - Pearson -0.270: 32:32
  - Pearson -0.254: 16:16
  - Pearson -0.220: 1024:1024

## Experiment - FFT window length, window length and hop length with ratio 4:4:1

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {win_len:n_fft:hop_len}):
  - Pearson -0.318: 128:128:32
  - Pearson -0.288: 16:16:4
  - Pearson -0.287: 32:32:8
  - Pearson -0.284: 8:8:2
  - Pearson -0.278: 64:64:16
  - Pearson -0.273: 512:512:128
  - Pearson -0.255: 256:256:64
  - Pearson -0.193: 1024:1024:256

## Experiment - FFT window length, window length and hop length with ratio 9:3:1

- Experimented parameter(s):
  - n_fft = 16, 32, 64, 128, 256, 512, 1024
  - win_len = 5, 10, 21, 42, 85, 170, 341
  - hop_len = 1, 3, 7, 14, 28, 56, 113
- Results (format = {n_fft:win_len:hop_len}):
  - Pearson -0.300: 128:42:14
  - Pearson -0.290: 64:21:7
  - Pearson -0.279: 32:10:3
  - Pearson -0.267: 256:85:28
  - Pearson -0.252: 16:5:1
  - Pearson -0.202: 512:170:56
  - Pearson -0.130: 1024:341:113

## Experiment - FFT window length, window length and hop length with ratio 4:2:1

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 64, 128, 256, 512
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - Pearson -0.319: 64:32:16
  - Pearson -0.291: 32:16:8
  - Pearson -0.286: 16:8:4
  - Pearson -0.273: 128:64:32
  - Pearson -0.251: 8:4:2
  - Pearson -0.240: 512:256:128
  - Pearson -0.199: 256:128:64
  - Pearson -0.137: 1024:512:256

## Experiment - FFT window length, window length and hop length with different ratios

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 46.44, 64, 85.33, 100, 120, 128, 170.67, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 46.44, 50, 60, 64, 85.33, 100, 120, 128, 170.67, 256, 512
  - hop_len = 2, 4, 8, 11.61, 16, 21.33, 25, 30, 32, 42.67, 48, 50, 60, 64, 85.33, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - Pearson -0.326: 128:64:16
  - Pearson -0.322: 100:50:25
  - Pearson -0.319: 64:32:16
  - Pearson -0.318: 128:128:32
  - Pearson -0.312: 100:100:50
  - Pearson -0.311: 256:64:8
  - Pearson -0.310: 64:32:8
  - Pearson -0.306: 120:120:30, 128:256:32, 128:64:8
  - Pearson -0.305: 256:256:32
  - Pearson -0.302: 128:32:8
  - Pearson -0.300: 128:128:16
  - Pearson -0.298: 256:128:16
  - Pearson -0.297: 100:100:25
  - Pearson -0.295: 170.67:170.67:42.67, 512:256:32
  - Pearson -0.294: 64:64:8
  - Pearson -0.292: 16:16:8, 46.44:46.44:11.61
  - Pearson -0.291: 256:128:8, 32:16:8
  - Pearson -0.288: 16:16:4
  - Pearson -0.287: 32:32:8
  - Pearson -0.286: 8:8:4
  - Pearson -0.284: 85.33:85.33:21.33, 8:8:2
  - Pearson -0.283: 64:64:32
  - Pearson -0.276: 256:128:32
  - Pearson -0.273: 128:128:64, 128:64:32, 512:512:128
  - Pearson -0.271: 120:60:30
  - Pearson -0.264: 170.67:170.67:85.33
  - Pearson -0.263: 128:256:64
  - Pearson -0.251: 8:4:2
  - Pearson -0.246: 64:64:48
  - Pearson -0.241: 85.33:85.33:42.67
  - Pearson -0.234: 120:120:60
  - Pearson -0.137: 1024:512:256

## Experiment - Finding optimal Pearson parameters (baseline)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = True
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - Pearson -0.353: 128:64:16:12:mel:True

## Experiment - Finding optimal Pearson parameters (norm=False)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = False
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - Pearson -0.298: 128:64:16:12:mel:False

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
  - Pearson -0.360: 128:64:16:12:mel:True:3, 128:64:16:12:mel:True:4
  - Pearson -0.353: 128:64:16:12:mel:True:10, 128:64:16:12:mel:True:2
  - Pearson -0.339: 128:64:16:12:mel:True:1

## Experiment - Finding optimal Spearman parameters (baseline)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 10
  - M = 11
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - Pearson -0.315: 64:32:16:10:11:mel

## Experiment - Finding optimal Spearman parameters (D, M)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 12, 13
  - M = 20
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - Pearson -0.341: 64:32:16:13:20:mel
  - Pearson -0.340: 64:32:16:12:20:mel

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
  - Pearson -0.294: 64:32:16:13:20:mel:False

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
  - Pearson -0.348: 64:32:16:13:20:mel:2
  - Pearson -0.345: 64:32:16:13:20:mel:3
  - Pearson -0.342: 64:32:16:13:20:mel:4
  - Pearson -0.341: 64:32:16:13:20:mel:10
  - Pearson -0.329: 64:32:16:13:20:mel:1

## Best experiments

### 1. Place

- Pearson: -0.3598736819026922
- Experiments with that score (#1):
  - 'Finding optimal Pearson parameters (radius)' with parameters:
    - sample_rate = 96000
    - n_fft = 128
    - win_len = 64
    - hop_len = 16
    - window = hanning
    - fmin = 0
    - fmax = 48000
    - s = 1
    - M = 20
    - D = 12
    - align_method = dtw
    - align_target = mel
    - remove_silence = no
    - silence_threshold_A = None
    - silence_threshold_B = None
    - norm_audio = True
    - dtw_radius = 3

### 2. Place

- Pearson: -0.3595394692511479
- Experiments with that score (#1):
  - 'Finding optimal Pearson parameters (radius)' with parameters:
    - sample_rate = 96000
    - n_fft = 128
    - win_len = 64
    - hop_len = 16
    - window = hanning
    - fmin = 0
    - fmax = 48000
    - s = 1
    - M = 20
    - D = 12
    - align_method = dtw
    - align_target = mel
    - remove_silence = no
    - silence_threshold_A = None
    - silence_threshold_B = None
    - norm_audio = True
    - dtw_radius = 4

### 3. Place

- Pearson: -0.3534082312870614
- Experiments with that score (#1):
  - 'Finding optimal Pearson parameters (radius)' with parameters:
    - sample_rate = 96000
    - n_fft = 128
    - win_len = 64
    - hop_len = 16
    - window = hanning
    - fmin = 0
    - fmax = 48000
    - s = 1
    - M = 20
    - D = 12
    - align_method = dtw
    - align_target = mel
    - remove_silence = no
    - silence_threshold_A = None
    - silence_threshold_B = None
    - norm_audio = True
    - dtw_radius = 2
