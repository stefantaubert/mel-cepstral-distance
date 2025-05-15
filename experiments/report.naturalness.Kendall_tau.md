# Analysis of MCD and naturalness MOS Kendall_tau correlation

## Metrics

| obj_metric      |   mean |   median |
|-----------------|--------|----------|
| mcd*(pen+1)     | -0.162 |   -0.17  |
| mcd*(pen+0.5)   | -0.161 |   -0.168 |
| mcd*(pen+2)     | -0.157 |   -0.169 |
| mcd*(pen+0.25)  | -0.154 |   -0.16  |
| mcd+pen         | -0.15  |   -0.162 |
| sqrt(mcd²+pen²) | -0.144 |   -0.157 |
| mcd             | -0.144 |   -0.156 |
| mcd*(pen+0.1)   | -0.141 |   -0.147 |
| mcd-pen         | -0.136 |   -0.152 |
| mcd*pen         | -0.126 |   -0.125 |
| pen*(mcd+1)     | -0.123 |   -0.121 |
| pen             | -0.095 |   -0.097 |
| mcd*(pen-1)     |  0.084 |    0.092 |

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
  - Kendall_tau -0.193: 96000
  - Kendall_tau -0.168: 88200
  - Kendall_tau -0.161: 48000
  - Kendall_tau -0.153: 32000
  - Kendall_tau -0.139: 44100
  - Kendall_tau -0.138: 192000
  - Kendall_tau -0.128: 24000
  - Kendall_tau -0.126: 22050
  - Kendall_tau -0.112: 16000
  - Kendall_tau -0.086: 8000
  - Kendall_tau -0.003: 4000

## Experiment - Minimum frequency

- Experimented parameter(s):
  - fmin = 0, 100, 500, 1000, 2000, 4000, 8000, 16000, 22050, 44100
- Results (format = {fmin}):
  - Kendall_tau -0.193: 0
  - Kendall_tau -0.181: 500
  - Kendall_tau -0.176: 100
  - Kendall_tau -0.133: 1000
  - Kendall_tau -0.131: 4000
  - Kendall_tau -0.113: 2000
  - Kendall_tau -0.111: 8000
  - Kendall_tau -0.020: 22050
  - Kendall_tau -0.000: 44100
  - Kendall_tau 0.049: 16000

## Experiment - Maximum frequency

- Changed parameter(s): sample_rate=192000
- Experimented parameter(s):
  - fmax = 4000, 8000, 11025, 16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000
- Results (format = {fmax}):
  - Kendall_tau -0.194: 48000
  - Kendall_tau -0.185: 88200
  - Kendall_tau -0.184: 44100
  - Kendall_tau -0.169: 32000
  - Kendall_tau -0.160: 24000
  - Kendall_tau -0.158: 16000
  - Kendall_tau -0.139: 22050
  - Kendall_tau -0.138: 96000
  - Kendall_tau -0.123: 11025
  - Kendall_tau -0.111: 8000
  - Kendall_tau -0.085: 4000

## Experiment - Number of mel filterbanks

- Changed parameter(s): D=10
- Experimented parameter(s):
  - M = 10, 11, 12, 13, 20, 30, 40, 50, 60, 70, 80
- Results (format = {M}):
  - Kendall_tau -0.201: 11
  - Kendall_tau -0.191: 20
  - Kendall_tau -0.185: 40
  - Kendall_tau -0.184: 50, 70
  - Kendall_tau -0.179: 60
  - Kendall_tau -0.178: 80
  - Kendall_tau -0.174: 12
  - Kendall_tau -0.159: 13
  - Kendall_tau -0.158: 10, 30

## Experiment - Starting index

- Experimented parameter(s):
  - s = 0, 1, 2, 3, 4, 5, 6, 7, 8
- Results (format = {s}):
  - Kendall_tau -0.180: 0
  - Kendall_tau -0.179: 1
  - Kendall_tau -0.161: 3
  - Kendall_tau -0.148: 2
  - Kendall_tau -0.147: 8
  - Kendall_tau -0.141: 7
  - Kendall_tau -0.137: 6
  - Kendall_tau -0.133: 5
  - Kendall_tau -0.123: 4

## Experiment - Number of MFCC coefficients (M=80)

- Changed parameter(s): M=80
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 30, 40, 50, 60, 70, 80
- Results (format = {D}):
  - Kendall_tau -0.189: 13
  - Kendall_tau -0.188: 12, 15
  - Kendall_tau -0.187: 14
  - Kendall_tau -0.186: 11, 17, 19
  - Kendall_tau -0.185: 16
  - Kendall_tau -0.184: 18
  - Kendall_tau -0.178: 10
  - Kendall_tau -0.173: 9
  - Kendall_tau -0.170: 8
  - Kendall_tau -0.169: 30
  - Kendall_tau -0.163: 7
  - Kendall_tau -0.159: 6
  - Kendall_tau -0.149: 40
  - Kendall_tau -0.146: 5
  - Kendall_tau -0.136: 4, 50
  - Kendall_tau -0.131: 60
  - Kendall_tau -0.129: 70
  - Kendall_tau -0.126: 80
  - Kendall_tau -0.108: 2
  - Kendall_tau -0.104: 3

## Experiment - Number of MFCC coefficients (M=40)

- Changed parameter(s): M=40
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 25, 30, 35, 40
- Results (format = {D}):
  - Kendall_tau -0.193: 13
  - Kendall_tau -0.190: 14, 15
  - Kendall_tau -0.189: 12
  - Kendall_tau -0.188: 11
  - Kendall_tau -0.186: 17
  - Kendall_tau -0.185: 10, 16, 18, 19
  - Kendall_tau -0.175: 25
  - Kendall_tau -0.173: 9
  - Kendall_tau -0.169: 8
  - Kendall_tau -0.167: 7
  - Kendall_tau -0.163: 6
  - Kendall_tau -0.161: 30
  - Kendall_tau -0.157: 35
  - Kendall_tau -0.156: 40
  - Kendall_tau -0.151: 5
  - Kendall_tau -0.147: 4
  - Kendall_tau -0.102: 3
  - Kendall_tau -0.096: 2

## Experiment - Number of MFCC coefficients (M=20)

- Changed parameter(s): M=20
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
- Results (format = {D}):
  - Kendall_tau -0.196: 13, 14, 18
  - Kendall_tau -0.195: 12, 17, 19, 20
  - Kendall_tau -0.193: 11, 16
  - Kendall_tau -0.192: 15
  - Kendall_tau -0.191: 10
  - Kendall_tau -0.189: 8
  - Kendall_tau -0.186: 9
  - Kendall_tau -0.179: 7
  - Kendall_tau -0.177: 6
  - Kendall_tau -0.173: 5
  - Kendall_tau -0.160: 4
  - Kendall_tau -0.115: 3
  - Kendall_tau -0.099: 2

## Experiment - Number of MFCC coefficients (M=10)

- Changed parameter(s): M=10
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10
- Results (format = {D}):
  - Kendall_tau -0.167: 6
  - Kendall_tau -0.163: 7
  - Kendall_tau -0.160: 5
  - Kendall_tau -0.158: 10, 9
  - Kendall_tau -0.156: 8
  - Kendall_tau -0.147: 4
  - Kendall_tau -0.141: 3
  - Kendall_tau -0.095: 2

## Experiment - Number of MFCC coefficients (M=5)

- Changed parameter(s): M=5
- Experimented parameter(s):
  - D = 2, 3, 4, 5
- Results (format = {D}):
  - Kendall_tau -0.130: 4, 5
  - Kendall_tau -0.121: 3
  - Kendall_tau -0.108: 2

## Experiment - Silence removal

- Experimented parameter(s):
  - remove_silence = mel, no
  - silence_threshold_A = -4, -3.5, -3, None
  - silence_threshold_B = -4.5, -4, -3.5, None
- Results (format = {remove_silence:silence_threshold_A:silence_threshold_B}):
  - Kendall_tau -0.193: no:None:None
  - Kendall_tau -0.149: mel:-3.5:-4
  - Kendall_tau -0.145: mel:-4:-4.5
  - Kendall_tau -0.133: mel:-3:-3.5

## Experiment - Normalize audio

- Experimented parameter(s):
  - norm_audio = False, True
- Results (format = {norm_audio}):
  - Kendall_tau -0.194: False
  - Kendall_tau -0.193: True

## Experiment - Alignment method

- Experimented parameter(s):
  - align_method = dtw, pad
  - align_target = mel, mfcc, spec
- Results (format = {align_method:align_target}):
  - Kendall_tau -0.200: dtw:mel
  - Kendall_tau -0.193: dtw:mfcc
  - Kendall_tau -0.153: dtw:spec
  - Kendall_tau -0.046: pad:mel, pad:mfcc, pad:spec

## Experiment - Sakoe-Chiba radius

- Experimented parameter(s):
  - dtw_radius = 1, 2, 3, 10, 20, 40, None
- Results (format = {dtw_radius}):
  - Kendall_tau -0.194: 1
  - Kendall_tau -0.193: 10, 2, 20, 3, 40, None

## Experiment - Window function

- Experimented parameter(s):
  - window = hamming, hanning
- Results (format = {window}):
  - Kendall_tau -0.193: hanning
  - Kendall_tau -0.179: hamming

## Experiment - FFT window length

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {n_fft}):
  - Kendall_tau -0.193: 128
  - Kendall_tau -0.183: 8
  - Kendall_tau -0.180: 64
  - Kendall_tau -0.172: 32
  - Kendall_tau -0.162: 256
  - Kendall_tau -0.160: 16
  - Kendall_tau -0.154: 512
  - Kendall_tau -0.153: 1024

## Experiment - Window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len}):
  - Kendall_tau -0.193: 128
  - Kendall_tau -0.188: 256
  - Kendall_tau -0.180: 64
  - Kendall_tau -0.176: 1024, 512
  - Kendall_tau -0.167: 32
  - Kendall_tau -0.137: 16
  - Kendall_tau -0.122: 8

## Experiment - Hop length

- Experimented parameter(s):
  - hop_len = 8, 16, 32, 64, 128
- Results (format = {hop_len}):
  - Kendall_tau -0.193: 32
  - Kendall_tau -0.168: 16
  - Kendall_tau -0.162: 8
  - Kendall_tau -0.155: 64
  - Kendall_tau -0.134: 128

## Experiment - Equal FFT window length and window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len:n_fft}):
  - Kendall_tau -0.193: 128:128
  - Kendall_tau -0.174: 64:64, 8:8
  - Kendall_tau -0.167: 256:256
  - Kendall_tau -0.163: 32:32
  - Kendall_tau -0.155: 16:16
  - Kendall_tau -0.142: 512:512
  - Kendall_tau -0.119: 1024:1024

## Experiment - FFT window length, window length and hop length with ratio 4:4:1

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {win_len:n_fft:hop_len}):
  - Kendall_tau -0.193: 128:128:32
  - Kendall_tau -0.174: 16:16:4
  - Kendall_tau -0.168: 8:8:2
  - Kendall_tau -0.167: 32:32:8
  - Kendall_tau -0.160: 64:64:16
  - Kendall_tau -0.139: 256:256:64
  - Kendall_tau -0.138: 512:512:128
  - Kendall_tau -0.108: 1024:1024:256

## Experiment - FFT window length, window length and hop length with ratio 9:3:1

- Experimented parameter(s):
  - n_fft = 16, 32, 64, 128, 256, 512, 1024
  - win_len = 5, 5.33, 10, 10.67, 21, 21.33, 42, 42.67, 85, 85.33, 170, 170.67, 341, 341.33
  - hop_len = 1, 1.78, 3, 3.56, 7, 7.11, 14, 14.22, 28, 28.44, 56, 56.89, 113, 113.78
- Results (format = {n_fft:win_len:hop_len}):
  - Kendall_tau -0.184: 128:42:14, 64:21.33:7.11
  - Kendall_tau -0.180: 32:10:3
  - Kendall_tau -0.176: 256:85:28
  - Kendall_tau -0.174: 64:21:7
  - Kendall_tau -0.172: 128:42.67:14.22
  - Kendall_tau -0.170: 32:10.67:3.56
  - Kendall_tau -0.167: 256:85.33:28.44
  - Kendall_tau -0.157: 16:5:1
  - Kendall_tau -0.143: 16:5.33:1.78
  - Kendall_tau -0.092: 512:170:56
  - Kendall_tau -0.071: 1024:341:113
  - Kendall_tau -0.065: 512:170.67:56.89
  - Kendall_tau -0.052: 1024:341.33:113.78

## Experiment - FFT window length, window length and hop length with ratio 4:2:1

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 64, 128, 256, 512
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - Kendall_tau -0.212: 64:32:16
  - Kendall_tau -0.194: 32:16:8
  - Kendall_tau -0.180: 128:64:32
  - Kendall_tau -0.176: 16:8:4
  - Kendall_tau -0.151: 8:4:2
  - Kendall_tau -0.129: 512:256:128
  - Kendall_tau -0.113: 256:128:64
  - Kendall_tau -0.084: 1024:512:256

## Experiment - FFT window length, window length and hop length with different ratios

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 46.44, 64, 85.33, 100, 120, 128, 170.67, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 46.44, 50, 60, 64, 85.33, 100, 120, 128, 170.67, 256, 512
  - hop_len = 2, 4, 8, 11.61, 16, 21.33, 25, 30, 32, 42.67, 48, 50, 60, 64, 85.33, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - Kendall_tau -0.212: 64:32:16
  - Kendall_tau -0.205: 64:32:8
  - Kendall_tau -0.203: 128:32:8, 128:64:16
  - Kendall_tau -0.200: 256:64:8
  - Kendall_tau -0.197: 100:50:25
  - Kendall_tau -0.194: 32:16:8
  - Kendall_tau -0.193: 128:128:32
  - Kendall_tau -0.191: 128:64:8
  - Kendall_tau -0.189: 100:100:50
  - Kendall_tau -0.188: 128:256:32
  - Kendall_tau -0.181: 120:120:30
  - Kendall_tau -0.180: 128:64:32
  - Kendall_tau -0.178: 46.44:46.44:11.61
  - Kendall_tau -0.176: 85.33:85.33:21.33
  - Kendall_tau -0.174: 100:100:25, 16:16:4, 64:64:32
  - Kendall_tau -0.173: 16:16:8, 256:128:16
  - Kendall_tau -0.172: 8:8:4
  - Kendall_tau -0.170: 256:128:8
  - Kendall_tau -0.169: 64:64:8
  - Kendall_tau -0.168: 128:128:16, 170.67:170.67:42.67, 8:8:2
  - Kendall_tau -0.167: 256:256:32, 32:32:8
  - Kendall_tau -0.162: 256:128:32
  - Kendall_tau -0.160: 512:256:32
  - Kendall_tau -0.159: 85.33:85.33:42.67
  - Kendall_tau -0.157: 128:256:64
  - Kendall_tau -0.155: 128:128:64
  - Kendall_tau -0.151: 8:4:2
  - Kendall_tau -0.148: 64:64:48
  - Kendall_tau -0.147: 120:60:30
  - Kendall_tau -0.146: 120:120:60
  - Kendall_tau -0.138: 170.67:170.67:85.33, 512:512:128
  - Kendall_tau -0.084: 1024:512:256

## Experiment - Finding optimal Pearson parameters (baseline)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = True
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - Kendall_tau -0.203: 128:64:16:12:mel:True

## Experiment - Finding optimal Pearson parameters (norm=False)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = False
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - Kendall_tau -0.191: 128:64:16:12:mel:False

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
  - Kendall_tau -0.210: 128:64:16:12:mel:True:3, 128:64:16:12:mel:True:4
  - Kendall_tau -0.203: 128:64:16:12:mel:True:10, 128:64:16:12:mel:True:2
  - Kendall_tau -0.188: 128:64:16:12:mel:True:1

## Experiment - Finding optimal Spearman parameters (baseline)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 10
  - M = 11
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - Kendall_tau -0.195: 64:32:16:10:11:mel

## Experiment - Finding optimal Spearman parameters (D, M)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 12, 13
  - M = 20
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - Kendall_tau -0.215: 64:32:16:12:20:mel, 64:32:16:13:20:mel

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
  - Kendall_tau -0.190: 64:32:16:13:20:mel:False

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
  - Kendall_tau -0.217: 64:32:16:13:20:mel:2
  - Kendall_tau -0.216: 64:32:16:13:20:mel:4
  - Kendall_tau -0.215: 64:32:16:13:20:mel:10, 64:32:16:13:20:mel:3
  - Kendall_tau -0.205: 64:32:16:13:20:mel:1

## Best experiments

### 1. Place

- Kendall_tau: -0.2168261756461208
- Experiments with that score (#1):
  - 'Finding optimal Spearman parameters (radius)' with parameters:
    - sample_rate = 96000
    - n_fft = 64
    - win_len = 32
    - hop_len = 16
    - window = hanning
    - fmin = 0
    - fmax = 48000
    - s = 1
    - M = 20
    - D = 13
    - align_method = dtw
    - align_target = mel
    - remove_silence = no
    - silence_threshold_A = None
    - silence_threshold_B = None
    - norm_audio = True
    - dtw_radius = 2

### 2. Place

- Kendall_tau: -0.2157522470891811
- Experiments with that score (#1):
  - 'Finding optimal Spearman parameters (radius)' with parameters:
    - sample_rate = 96000
    - n_fft = 64
    - win_len = 32
    - hop_len = 16
    - window = hanning
    - fmin = 0
    - fmax = 48000
    - s = 1
    - M = 20
    - D = 13
    - align_method = dtw
    - align_target = mel
    - remove_silence = no
    - silence_threshold_A = None
    - silence_threshold_B = None
    - norm_audio = True
    - dtw_radius = 4

### 3. Place

- Kendall_tau: -0.2152510804292759
- Experiments with that score (#1):
  - 'Finding optimal Spearman parameters (radius)' with parameters:
    - sample_rate = 96000
    - n_fft = 64
    - win_len = 32
    - hop_len = 16
    - window = hanning
    - fmin = 0
    - fmax = 48000
    - s = 1
    - M = 20
    - D = 13
    - align_method = dtw
    - align_target = mel
    - remove_silence = no
    - silence_threshold_A = None
    - silence_threshold_B = None
    - norm_audio = True
    - dtw_radius = 3
