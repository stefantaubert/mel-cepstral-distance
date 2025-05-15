# Analysis of MCD and intelligibility MOS Spearman correlation

## Metrics

| obj_metric      |   mean |   median |
|-----------------|--------|----------|
| mcd*(pen+0.25)  | -0.113 |   -0.117 |
| mcd*(pen+0.5)   | -0.113 |   -0.119 |
| mcd*(pen+0.1)   | -0.109 |   -0.116 |
| mcd*(pen+1)     | -0.107 |   -0.113 |
| mcd*pen         | -0.102 |   -0.108 |
| pen*(mcd+1)     | -0.1   |   -0.107 |
| mcd*(pen+2)     | -0.098 |   -0.102 |
| pen             | -0.089 |   -0.098 |
| mcd+pen         | -0.084 |   -0.088 |
| mcd             | -0.08  |   -0.083 |
| sqrt(mcd²+pen²) | -0.078 |   -0.083 |
| mcd-pen         | -0.072 |   -0.073 |
| mcd*(pen-1)     |  0.013 |    0.012 |

## Default parameters for experiments

- obj_metric = mcd*(pen+0.25)
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
  - Spearman -0.136: 44100
  - Spearman -0.128: 96000
  - Spearman -0.123: 192000
  - Spearman -0.122: 8000
  - Spearman -0.117: 88200
  - Spearman -0.114: 32000
  - Spearman -0.112: 48000
  - Spearman -0.104: 24000
  - Spearman -0.103: 16000
  - Spearman -0.102: 22050
  - Spearman -0.075: 4000

## Experiment - Minimum frequency

- Experimented parameter(s):
  - fmin = 0, 100, 500, 1000, 2000, 4000, 8000, 16000, 22050, 44100
- Results (format = {fmin}):
  - Spearman -0.150: 1000
  - Spearman -0.133: 500
  - Spearman -0.128: 0
  - Spearman -0.125: 8000
  - Spearman -0.124: 100
  - Spearman -0.090: 2000
  - Spearman -0.056: 44100
  - Spearman -0.052: 22050
  - Spearman -0.039: 4000
  - Spearman 0.048: 16000

## Experiment - Maximum frequency

- Changed parameter(s): sample_rate=192000
- Experimented parameter(s):
  - fmax = 4000, 8000, 11025, 16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000
- Results (format = {fmax}):
  - Spearman -0.141: 22050
  - Spearman -0.125: 88200
  - Spearman -0.123: 48000, 96000
  - Spearman -0.120: 4000
  - Spearman -0.119: 32000
  - Spearman -0.114: 11025
  - Spearman -0.103: 24000
  - Spearman -0.101: 16000
  - Spearman -0.097: 8000
  - Spearman -0.095: 44100

## Experiment - Number of mel filterbanks

- Changed parameter(s): D=10
- Experimented parameter(s):
  - M = 10, 11, 12, 13, 20, 30, 40, 50, 60, 70, 80
- Results (format = {M}):
  - Spearman -0.128: 80
  - Spearman -0.126: 70
  - Spearman -0.117: 50
  - Spearman -0.111: 60
  - Spearman -0.106: 30
  - Spearman -0.104: 13
  - Spearman -0.096: 40
  - Spearman -0.095: 20
  - Spearman -0.086: 11
  - Spearman -0.077: 12
  - Spearman -0.069: 10

## Experiment - Starting index

- Experimented parameter(s):
  - s = 0, 1, 2, 3, 4, 5, 6, 7, 8
- Results (format = {s}):
  - Spearman -0.221: 5, 6
  - Spearman -0.202: 8
  - Spearman -0.160: 7
  - Spearman -0.149: 3
  - Spearman -0.146: 4
  - Spearman -0.138: 0
  - Spearman -0.128: 2
  - Spearman -0.103: 1

## Experiment - Number of MFCC coefficients (M=80)

- Changed parameter(s): M=80
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 30, 40, 50, 60, 70, 80
- Results (format = {D}):
  - Spearman -0.134: 60
  - Spearman -0.132: 30
  - Spearman -0.131: 15, 16
  - Spearman -0.130: 70
  - Spearman -0.129: 80
  - Spearman -0.128: 10, 18, 50
  - Spearman -0.127: 13, 19
  - Spearman -0.126: 17
  - Spearman -0.125: 12, 14
  - Spearman -0.120: 40
  - Spearman -0.119: 11
  - Spearman -0.115: 8
  - Spearman -0.114: 9
  - Spearman -0.112: 7
  - Spearman -0.111: 6
  - Spearman -0.094: 5
  - Spearman -0.076: 2
  - Spearman -0.049: 4
  - Spearman -0.025: 3

## Experiment - Number of MFCC coefficients (M=40)

- Changed parameter(s): M=40
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 25, 30, 35, 40
- Results (format = {D}):
  - Spearman -0.123: 30
  - Spearman -0.122: 17, 35
  - Spearman -0.120: 25
  - Spearman -0.119: 18
  - Spearman -0.117: 19
  - Spearman -0.114: 16, 40
  - Spearman -0.112: 12
  - Spearman -0.111: 14
  - Spearman -0.110: 11
  - Spearman -0.108: 15
  - Spearman -0.107: 8
  - Spearman -0.104: 13
  - Spearman -0.101: 6
  - Spearman -0.096: 10
  - Spearman -0.087: 7
  - Spearman -0.084: 9
  - Spearman -0.066: 2
  - Spearman -0.061: 5
  - Spearman -0.037: 4
  - Spearman -0.033: 3

## Experiment - Number of MFCC coefficients (M=20)

- Changed parameter(s): M=20
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
- Results (format = {D}):
  - Spearman -0.128: 16, 17
  - Spearman -0.127: 15
  - Spearman -0.122: 14
  - Spearman -0.117: 13, 19, 20
  - Spearman -0.116: 12
  - Spearman -0.115: 18, 7
  - Spearman -0.112: 11
  - Spearman -0.108: 8
  - Spearman -0.101: 9
  - Spearman -0.099: 6
  - Spearman -0.095: 10
  - Spearman -0.071: 5
  - Spearman -0.070: 2
  - Spearman -0.068: 4
  - Spearman -0.064: 3

## Experiment - Number of MFCC coefficients (M=10)

- Changed parameter(s): M=10
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10
- Results (format = {D}):
  - Spearman -0.093: 2
  - Spearman -0.084: 8
  - Spearman -0.082: 6
  - Spearman -0.078: 7
  - Spearman -0.069: 10, 9
  - Spearman -0.066: 5
  - Spearman -0.062: 3
  - Spearman -0.034: 4

## Experiment - Number of MFCC coefficients (M=5)

- Changed parameter(s): M=5
- Experimented parameter(s):
  - D = 2, 3, 4, 5
- Results (format = {D}):
  - Spearman -0.099: 2
  - Spearman -0.060: 3
  - Spearman -0.023: 4, 5

## Experiment - Silence removal

- Experimented parameter(s):
  - remove_silence = mel, no
  - silence_threshold_A = -4, -3.5, -3, None
  - silence_threshold_B = -4.5, None, -4, -3.5
- Results (format = {remove_silence:silence_threshold_A:silence_threshold_B}):
  - Spearman -0.128: no:None:None
  - Spearman -0.101: mel:-3.5:-4
  - Spearman -0.072: mel:-4:-4.5
  - Spearman -0.033: mel:-3:-3.5

## Experiment - Normalize audio

- Experimented parameter(s):
  - norm_audio = False, True
- Results (format = {norm_audio}):
  - Spearman -0.128: True
  - Spearman -0.119: False

## Experiment - Alignment method

- Experimented parameter(s):
  - align_method = dtw, pad
  - align_target = mel, mfcc, spec
- Results (format = {align_method:align_target}):
  - Spearman -0.135: dtw:mel
  - Spearman -0.128: dtw:mfcc
  - Spearman -0.072: dtw:spec
  - Spearman -0.008: pad:mel, pad:mfcc, pad:spec

## Experiment - Sakoe-Chiba radius

- Experimented parameter(s):
  - dtw_radius = 1, 2, 3, 20, 40, None, 10
- Results (format = {dtw_radius}):
  - Spearman -0.128: 1, 10, 2, 20, 3, 40, None

## Experiment - Window function

- Experimented parameter(s):
  - window = hamming, hanning
- Results (format = {window}):
  - Spearman -0.128: hanning
  - Spearman -0.114: hamming

## Experiment - FFT window length

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {n_fft}):
  - Spearman -0.169: 32
  - Spearman -0.167: 16
  - Spearman -0.157: 256
  - Spearman -0.153: 8
  - Spearman -0.142: 512
  - Spearman -0.131: 1024
  - Spearman -0.130: 64
  - Spearman -0.128: 128

## Experiment - Window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len}):
  - Spearman -0.128: 128
  - Spearman -0.125: 1024
  - Spearman -0.121: 256
  - Spearman -0.109: 512, 64
  - Spearman -0.104: 16
  - Spearman -0.078: 32
  - Spearman -0.072: 8

## Experiment - Hop length

- Experimented parameter(s):
  - hop_len = 8, 16, 32, 64, 128
- Results (format = {hop_len}):
  - Spearman -0.187: 64
  - Spearman -0.151: 8
  - Spearman -0.133: 16
  - Spearman -0.128: 32
  - Spearman -0.068: 128

## Experiment - Equal FFT window length and window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len:n_fft}):
  - Spearman -0.161: 32:32
  - Spearman -0.157: 16:16
  - Spearman -0.152: 8:8
  - Spearman -0.131: 1024:1024
  - Spearman -0.128: 128:128
  - Spearman -0.127: 64:64
  - Spearman -0.114: 256:256
  - Spearman -0.107: 512:512

## Experiment - FFT window length, window length and hop length with ratio 4:4:1

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {win_len:n_fft:hop_len}):
  - Spearman -0.174: 32:32:8
  - Spearman -0.168: 64:64:16
  - Spearman -0.163: 16:16:4
  - Spearman -0.152: 8:8:2
  - Spearman -0.128: 128:128:32
  - Spearman -0.125: 256:256:64
  - Spearman -0.091: 512:512:128
  - Spearman -0.042: 1024:1024:256

## Experiment - FFT window length, window length and hop length with ratio 9:3:1

- Experimented parameter(s):
  - n_fft = 16, 32, 64, 128, 256, 512, 1024
  - win_len = 5, 5.33, 10, 10.67, 21, 21.33, 42, 42.67, 85, 85.33, 170, 170.67, 341, 341.33
  - hop_len = 1, 1.78, 3, 3.56, 7, 7.11, 14, 14.22, 28, 28.44, 56, 56.89, 113, 113.78
- Results (format = {n_fft:win_len:hop_len}):
  - Spearman -0.145: 256:85.33:28.44
  - Spearman -0.140: 128:42:14
  - Spearman -0.132: 512:170.67:56.89
  - Spearman -0.123: 16:5.33:1.78
  - Spearman -0.120: 64:21:7
  - Spearman -0.119: 64:21.33:7.11
  - Spearman -0.116: 128:42.67:14.22, 512:170:56
  - Spearman -0.114: 32:10.67:3.56
  - Spearman -0.111: 256:85:28
  - Spearman -0.095: 32:10:3
  - Spearman -0.083: 16:5:1
  - Spearman -0.027: 1024:341:113
  - Spearman -0.016: 1024:341.33:113.78

## Experiment - FFT window length, window length and hop length with ratio 4:2:1

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 64, 128, 256, 512
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - Spearman -0.147: 32:16:8
  - Spearman -0.120: 64:32:16
  - Spearman -0.113: 256:128:64
  - Spearman -0.109: 128:64:32
  - Spearman -0.097: 16:8:4
  - Spearman -0.093: 512:256:128
  - Spearman -0.073: 8:4:2
  - Spearman 0.020: 1024:512:256

## Experiment - FFT window length, window length and hop length with different ratios

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 46.44, 64, 85.33, 100, 120, 128, 170.67, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 46.44, 50, 60, 64, 85.33, 100, 120, 128, 170.67, 256, 512
  - hop_len = 2, 4, 8, 11.61, 16, 21.33, 25, 30, 32, 42.67, 48, 50, 60, 64, 85.33, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - Spearman -0.187: 128:128:64
  - Spearman -0.185: 256:128:16
  - Spearman -0.183: 128:256:64
  - Spearman -0.182: 100:50:25
  - Spearman -0.174: 32:32:8
  - Spearman -0.170: 16:16:8
  - Spearman -0.169: 120:60:30
  - Spearman -0.166: 120:120:30
  - Spearman -0.164: 256:128:8
  - Spearman -0.163: 16:16:4
  - Spearman -0.162: 128:64:8
  - Spearman -0.161: 128:64:16, 64:64:8
  - Spearman -0.158: 8:8:4
  - Spearman -0.157: 128:32:8, 256:128:32
  - Spearman -0.154: 100:100:25
  - Spearman -0.152: 8:8:2
  - Spearman -0.151: 256:64:8
  - Spearman -0.150: 64:32:8
  - Spearman -0.149: 85.33:85.33:42.67
  - Spearman -0.147: 100:100:50, 32:16:8
  - Spearman -0.145: 85.33:85.33:21.33
  - Spearman -0.144: 512:256:32
  - Spearman -0.133: 128:128:16
  - Spearman -0.128: 128:128:32
  - Spearman -0.127: 64:64:32
  - Spearman -0.126: 46.44:46.44:11.61
  - Spearman -0.123: 170.67:170.67:42.67
  - Spearman -0.122: 64:64:48
  - Spearman -0.121: 128:256:32
  - Spearman -0.120: 64:32:16
  - Spearman -0.114: 256:256:32
  - Spearman -0.112: 120:120:60
  - Spearman -0.109: 128:64:32
  - Spearman -0.091: 512:512:128
  - Spearman -0.073: 8:4:2
  - Spearman -0.045: 170.67:170.67:85.33
  - Spearman 0.020: 1024:512:256

## Experiment - Finding optimal Pearson parameters (baseline)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = True
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - Spearman -0.108: 128:64:16:12:mel:True

## Experiment - Finding optimal Pearson parameters (norm=False)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = False
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - Spearman -0.111: 128:64:16:12:mel:False

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
  - Spearman -0.115: 128:64:16:12:mel:True:3, 128:64:16:12:mel:True:4
  - Spearman -0.108: 128:64:16:12:mel:True:10, 128:64:16:12:mel:True:2
  - Spearman -0.091: 128:64:16:12:mel:True:1

## Experiment - Finding optimal Spearman parameters (baseline)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 10
  - M = 11
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - Spearman -0.101: 64:32:16:10:11:mel

## Experiment - Finding optimal Spearman parameters (D, M)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 12, 13
  - M = 20
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - Spearman -0.109: 64:32:16:13:20:mel
  - Spearman -0.106: 64:32:16:12:20:mel

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
  - Spearman -0.129: 64:32:16:13:20:mel:False

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
  - Spearman -0.111: 64:32:16:13:20:mel:4
  - Spearman -0.110: 64:32:16:13:20:mel:1, 64:32:16:13:20:mel:3
  - Spearman -0.109: 64:32:16:13:20:mel:10
  - Spearman -0.105: 64:32:16:13:20:mel:2

## Best experiments

### 1. Place

- Spearman: -0.2210281552054716
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

- Spearman: -0.2207399760727127
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

- Spearman: -0.2022467351804856
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
