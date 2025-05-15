# Analysis of MCD and intelligibility MOS Spearman correlation

## Metrics

| obj_metric      |   mean |   median |
|-----------------|--------|----------|
| mcd*(pen+0.5)   | -0.113 |   -0.12  |
| mcd*(pen+0.25)  | -0.113 |   -0.117 |
| mcd*(pen+0.1)   | -0.109 |   -0.116 |
| mcd*(pen+1)     | -0.108 |   -0.113 |
| mcd*pen         | -0.102 |   -0.108 |
| pen*(mcd+1)     | -0.099 |   -0.107 |
| mcd*(pen+2)     | -0.098 |   -0.102 |
| pen             | -0.089 |   -0.096 |
| mcd+pen         | -0.085 |   -0.089 |
| mcd             | -0.081 |   -0.083 |
| sqrt(mcd²+pen²) | -0.079 |   -0.083 |
| mcd-pen         | -0.073 |   -0.073 |
| mcd*(pen-1)     |  0.014 |    0.012 |

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
  - Spearman -0.140: 44100
  - Spearman -0.128: 96000
  - Spearman -0.121: 24000
  - Spearman -0.119: 32000
  - Spearman -0.117: 8000, 88200
  - Spearman -0.116: 22050
  - Spearman -0.113: 48000
  - Spearman -0.112: 192000
  - Spearman -0.101: 16000
  - Spearman -0.056: 4000

## Experiment - Minimum frequency

- Experimented parameter(s):
  - fmin = 0, 100, 500, 1000, 2000, 4000, 8000, 16000, 22050, 44100
- Results (format = {fmin}):
  - Spearman -0.157: 1000
  - Spearman -0.150: 8000
  - Spearman -0.142: 500
  - Spearman -0.128: 0
  - Spearman -0.125: 100
  - Spearman -0.114: 2000
  - Spearman -0.079: 22050
  - Spearman -0.077: 4000
  - Spearman -0.068: 44100
  - Spearman 0.045: 16000

## Experiment - Maximum frequency

- Changed parameter(s): sample_rate=192000
- Experimented parameter(s):
  - fmax = 4000, 8000, 11025, 16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000
- Results (format = {fmax}):
  - Spearman -0.139: 22050
  - Spearman -0.134: 88200
  - Spearman -0.128: 48000
  - Spearman -0.121: 11025
  - Spearman -0.117: 32000
  - Spearman -0.116: 4000
  - Spearman -0.114: 44100
  - Spearman -0.113: 24000
  - Spearman -0.112: 16000, 96000
  - Spearman -0.099: 8000

## Experiment - Number of mel filterbanks

- Changed parameter(s): D=10
- Experimented parameter(s):
  - M = 10, 11, 12, 13, 20, 30, 40, 50, 60, 70, 80
- Results (format = {M}):
  - Spearman -0.122: 80
  - Spearman -0.120: 70
  - Spearman -0.115: 50
  - Spearman -0.113: 30
  - Spearman -0.112: 60
  - Spearman -0.111: 13
  - Spearman -0.107: 20
  - Spearman -0.104: 40
  - Spearman -0.098: 10
  - Spearman -0.097: 12
  - Spearman -0.087: 11

## Experiment - Starting index

- Experimented parameter(s):
  - s = 0, 1, 2, 3, 4, 5, 6, 7, 8
- Results (format = {s}):
  - Spearman -0.241: 5
  - Spearman -0.235: 6
  - Spearman -0.194: 8
  - Spearman -0.190: 7
  - Spearman -0.184: 4
  - Spearman -0.175: 3
  - Spearman -0.151: 2
  - Spearman -0.127: 0
  - Spearman -0.117: 1

## Experiment - Number of MFCC coefficients (M=80)

- Changed parameter(s): M=80
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 30, 40, 50, 60, 70, 80
- Results (format = {D}):
  - Spearman -0.134: 80
  - Spearman -0.133: 70
  - Spearman -0.132: 60
  - Spearman -0.131: 16
  - Spearman -0.129: 13, 50
  - Spearman -0.128: 15
  - Spearman -0.126: 14, 30
  - Spearman -0.124: 19
  - Spearman -0.123: 12, 17, 18
  - Spearman -0.122: 10
  - Spearman -0.120: 40
  - Spearman -0.117: 11
  - Spearman -0.113: 8
  - Spearman -0.110: 9
  - Spearman -0.106: 7
  - Spearman -0.098: 6
  - Spearman -0.080: 5
  - Spearman -0.076: 2
  - Spearman -0.053: 4
  - Spearman -0.022: 3

## Experiment - Number of MFCC coefficients (M=40)

- Changed parameter(s): M=40
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 25, 30, 35, 40
- Results (format = {D}):
  - Spearman -0.129: 17
  - Spearman -0.125: 35
  - Spearman -0.124: 14, 25
  - Spearman -0.123: 18, 30
  - Spearman -0.122: 16, 40
  - Spearman -0.121: 19
  - Spearman -0.120: 15
  - Spearman -0.119: 12
  - Spearman -0.117: 13
  - Spearman -0.115: 11
  - Spearman -0.104: 10, 8
  - Spearman -0.092: 6
  - Spearman -0.089: 9
  - Spearman -0.086: 7
  - Spearman -0.076: 2
  - Spearman -0.060: 5
  - Spearman -0.048: 4
  - Spearman -0.040: 3

## Experiment - Number of MFCC coefficients (M=20)

- Changed parameter(s): M=20
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
- Results (format = {D}):
  - Spearman -0.129: 15
  - Spearman -0.128: 16
  - Spearman -0.127: 17
  - Spearman -0.120: 14
  - Spearman -0.119: 19, 20
  - Spearman -0.118: 13
  - Spearman -0.116: 12, 18
  - Spearman -0.115: 11
  - Spearman -0.107: 10, 7, 8
  - Spearman -0.104: 9
  - Spearman -0.099: 6
  - Spearman -0.089: 2
  - Spearman -0.080: 4
  - Spearman -0.073: 3
  - Spearman -0.072: 5

## Experiment - Number of MFCC coefficients (M=10)

- Changed parameter(s): M=10
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10
- Results (format = {D}):
  - Spearman -0.104: 8
  - Spearman -0.103: 2
  - Spearman -0.098: 10, 9
  - Spearman -0.097: 7
  - Spearman -0.093: 6
  - Spearman -0.078: 5
  - Spearman -0.069: 3
  - Spearman -0.050: 4

## Experiment - Number of MFCC coefficients (M=5)

- Changed parameter(s): M=5
- Experimented parameter(s):
  - D = 2, 3, 4, 5
- Results (format = {D}):
  - Spearman -0.117: 2
  - Spearman -0.077: 3
  - Spearman -0.040: 4, 5

## Experiment - Silence removal

- Experimented parameter(s):
  - remove_silence = mel, no
  - silence_threshold_A = -3, None, -4, -3.5
  - silence_threshold_B = -4.5, None, -4, -3.5
- Results (format = {remove_silence:silence_threshold_A:silence_threshold_B}):
  - Spearman -0.128: no:None:None
  - Spearman -0.112: mel:-3.5:-4
  - Spearman -0.095: mel:-4:-4.5
  - Spearman -0.054: mel:-3:-3.5

## Experiment - Normalize audio

- Experimented parameter(s):
  - norm_audio = False, True
- Results (format = {norm_audio}):
  - Spearman -0.131: False
  - Spearman -0.128: True

## Experiment - Alignment method

- Experimented parameter(s):
  - align_method = dtw, pad
  - align_target = mel, mfcc, spec
- Results (format = {align_method:align_target}):
  - Spearman -0.132: dtw:mel
  - Spearman -0.128: dtw:mfcc
  - Spearman -0.077: dtw:spec
  - Spearman 0.001: pad:mel, pad:mfcc, pad:spec

## Experiment - Sakoe-Chiba radius

- Experimented parameter(s):
  - dtw_radius = 1, 2, 3, 10, 20, 40, None
- Results (format = {dtw_radius}):
  - Spearman -0.129: 1
  - Spearman -0.128: 10, 2, 20, 3, 40, None

## Experiment - Window function

- Experimented parameter(s):
  - window = hamming, hanning
- Results (format = {window}):
  - Spearman -0.128: hanning
  - Spearman -0.116: hamming

## Experiment - FFT window length

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {n_fft}):
  - Spearman -0.157: 16
  - Spearman -0.143: 256
  - Spearman -0.141: 32
  - Spearman -0.135: 8
  - Spearman -0.130: 512
  - Spearman -0.128: 128
  - Spearman -0.127: 64
  - Spearman -0.123: 1024

## Experiment - Window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len}):
  - Spearman -0.130: 1024
  - Spearman -0.128: 128
  - Spearman -0.122: 256
  - Spearman -0.116: 512
  - Spearman -0.103: 64
  - Spearman -0.092: 16
  - Spearman -0.068: 32
  - Spearman -0.048: 8

## Experiment - Hop length

- Experimented parameter(s):
  - hop_len = 8, 16, 32, 64, 128
- Results (format = {hop_len}):
  - Spearman -0.178: 64
  - Spearman -0.138: 8
  - Spearman -0.128: 32
  - Spearman -0.127: 16
  - Spearman -0.066: 128

## Experiment - Equal FFT window length and window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len:n_fft}):
  - Spearman -0.149: 16:16
  - Spearman -0.138: 8:8
  - Spearman -0.136: 32:32
  - Spearman -0.128: 128:128
  - Spearman -0.126: 64:64
  - Spearman -0.124: 1024:1024
  - Spearman -0.123: 256:256
  - Spearman -0.113: 512:512

## Experiment - FFT window length, window length and hop length with ratio 4:4:1

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {win_len:n_fft:hop_len}):
  - Spearman -0.156: 64:64:16
  - Spearman -0.154: 32:32:8
  - Spearman -0.149: 16:16:4
  - Spearman -0.139: 8:8:2
  - Spearman -0.128: 128:128:32
  - Spearman -0.125: 256:256:64
  - Spearman -0.097: 512:512:128
  - Spearman -0.062: 1024:1024:256

## Experiment - FFT window length, window length and hop length with ratio 9:3:1

- Experimented parameter(s):
  - n_fft = 16, 32, 64, 128, 256, 512, 1024
  - win_len = 5, 10, 21, 42, 85, 170, 341
  - hop_len = 1, 3, 7, 14, 28, 56, 113
- Results (format = {n_fft:win_len:hop_len}):
  - Spearman -0.132: 512:170:56
  - Spearman -0.117: 128:42:14
  - Spearman -0.105: 64:21:7
  - Spearman -0.100: 256:85:28
  - Spearman -0.076: 32:10:3
  - Spearman -0.066: 16:5:1
  - Spearman -0.032: 1024:341:113

## Experiment - FFT window length, window length and hop length with ratio 4:2:1

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 64, 128, 256, 512
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - Spearman -0.128: 64:32:16
  - Spearman -0.127: 32:16:8
  - Spearman -0.117: 256:128:64
  - Spearman -0.103: 128:64:32
  - Spearman -0.096: 512:256:128
  - Spearman -0.085: 16:8:4
  - Spearman -0.062: 8:4:2
  - Spearman 0.019: 1024:512:256

## Experiment - FFT window length, window length and hop length with different ratios

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 46.44, 64, 85.33, 100, 120, 128, 170.67, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 46.44, 50, 60, 64, 85.33, 100, 120, 128, 170.67, 256, 512
  - hop_len = 2, 4, 8, 11.61, 16, 21.33, 25, 30, 32, 42.67, 48, 50, 60, 64, 85.33, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - Spearman -0.181: 256:128:16
  - Spearman -0.178: 128:128:64
  - Spearman -0.174: 100:50:25
  - Spearman -0.172: 128:256:64
  - Spearman -0.162: 128:64:16, 16:16:8, 256:128:8
  - Spearman -0.158: 512:256:32
  - Spearman -0.156: 64:64:8
  - Spearman -0.155: 100:100:50
  - Spearman -0.154: 120:120:30, 32:32:8
  - Spearman -0.153: 100:100:25
  - Spearman -0.149: 16:16:4
  - Spearman -0.146: 128:64:8
  - Spearman -0.143: 256:128:32
  - Spearman -0.142: 8:8:4
  - Spearman -0.141: 256:64:8
  - Spearman -0.140: 85.33:85.33:42.67
  - Spearman -0.139: 8:8:2
  - Spearman -0.137: 120:60:30, 85.33:85.33:21.33
  - Spearman -0.131: 170.67:170.67:42.67
  - Spearman -0.130: 128:32:8
  - Spearman -0.129: 64:32:8
  - Spearman -0.128: 128:128:32, 64:32:16, 64:64:48
  - Spearman -0.127: 128:128:16, 32:16:8
  - Spearman -0.126: 64:64:32
  - Spearman -0.123: 256:256:32
  - Spearman -0.122: 128:256:32
  - Spearman -0.118: 120:120:60
  - Spearman -0.111: 46.44:46.44:11.61
  - Spearman -0.103: 128:64:32
  - Spearman -0.097: 512:512:128
  - Spearman -0.062: 8:4:2
  - Spearman -0.056: 170.67:170.67:85.33
  - Spearman 0.019: 1024:512:256

## Experiment - Finding optimal Pearson parameters (baseline)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = True
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - Spearman -0.094: 128:64:16:12:mel:True

## Experiment - Finding optimal Pearson parameters (norm=False)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = False
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - Spearman -0.124: 128:64:16:12:mel:False

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
  - Spearman -0.102: 128:64:16:12:mel:True:3, 128:64:16:12:mel:True:4
  - Spearman -0.094: 128:64:16:12:mel:True:10, 128:64:16:12:mel:True:2
  - Spearman -0.083: 128:64:16:12:mel:True:1

## Experiment - Finding optimal Spearman parameters (baseline)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 10
  - M = 11
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - Spearman -0.088: 64:32:16:10:11:mel

## Experiment - Finding optimal Spearman parameters (D, M)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 12, 13
  - M = 20
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - Spearman -0.098: 64:32:16:13:20:mel
  - Spearman -0.095: 64:32:16:12:20:mel

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
  - Spearman -0.140: 64:32:16:13:20:mel:False

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
  - Spearman -0.099: 64:32:16:13:20:mel:3, 64:32:16:13:20:mel:4
  - Spearman -0.098: 64:32:16:13:20:mel:10
  - Spearman -0.097: 64:32:16:13:20:mel:1
  - Spearman -0.093: 64:32:16:13:20:mel:2

## Best experiments

### 1. Place

- Spearman: -0.2409050925699912
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

- Spearman: -0.2345127554433395
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

- Spearman: -0.1939310206601931
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
