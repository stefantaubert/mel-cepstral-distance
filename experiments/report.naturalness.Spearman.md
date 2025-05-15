# Analysis of MCD and naturalness MOS Spearman correlation

## Metrics

| obj_metric      |   mean |   median |
|-----------------|--------|----------|
| mcd*(pen+1)     | -0.23  |   -0.242 |
| mcd*(pen+0.5)   | -0.229 |   -0.239 |
| mcd*(pen+2)     | -0.223 |   -0.24  |
| mcd*(pen+0.25)  | -0.22  |   -0.229 |
| mcd+pen         | -0.215 |   -0.232 |
| sqrt(mcd²+pen²) | -0.207 |   -0.224 |
| mcd             | -0.206 |   -0.224 |
| mcd*(pen+0.1)   | -0.203 |   -0.21  |
| mcd-pen         | -0.194 |   -0.216 |
| mcd*pen         | -0.181 |   -0.181 |
| pen*(mcd+1)     | -0.176 |   -0.175 |
| pen             | -0.137 |   -0.14  |
| mcd*(pen-1)     |  0.121 |    0.135 |

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
  - Spearman -0.273: 96000
  - Spearman -0.240: 88200
  - Spearman -0.230: 48000
  - Spearman -0.218: 32000
  - Spearman -0.200: 44100
  - Spearman -0.196: 192000
  - Spearman -0.183: 22050, 24000
  - Spearman -0.157: 16000
  - Spearman -0.119: 8000
  - Spearman -0.002: 4000

## Experiment - Minimum frequency

- Experimented parameter(s):
  - fmin = 0, 100, 500, 1000, 2000, 4000, 8000, 16000, 22050, 44100
- Results (format = {fmin}):
  - Spearman -0.273: 0
  - Spearman -0.256: 500
  - Spearman -0.251: 100
  - Spearman -0.190: 1000
  - Spearman -0.189: 4000
  - Spearman -0.162: 2000
  - Spearman -0.161: 8000
  - Spearman -0.027: 22050
  - Spearman 0.005: 44100
  - Spearman 0.071: 16000

## Experiment - Maximum frequency

- Changed parameter(s): sample_rate=192000
- Experimented parameter(s):
  - fmax = 4000, 8000, 11025, 16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000
- Results (format = {fmax}):
  - Spearman -0.273: 48000
  - Spearman -0.265: 88200
  - Spearman -0.263: 44100
  - Spearman -0.240: 32000
  - Spearman -0.231: 24000
  - Spearman -0.227: 16000
  - Spearman -0.198: 22050
  - Spearman -0.196: 96000
  - Spearman -0.176: 11025
  - Spearman -0.157: 8000
  - Spearman -0.119: 4000

## Experiment - Number of mel filterbanks

- Changed parameter(s): D=10
- Experimented parameter(s):
  - M = 10, 11, 12, 13, 20, 30, 40, 50, 60, 70, 80
- Results (format = {M}):
  - Spearman -0.286: 11
  - Spearman -0.270: 20
  - Spearman -0.259: 40
  - Spearman -0.255: 50, 70
  - Spearman -0.250: 80
  - Spearman -0.249: 12, 60
  - Spearman -0.227: 13
  - Spearman -0.225: 10
  - Spearman -0.224: 30

## Experiment - Starting index

- Experimented parameter(s):
  - s = 0, 1, 2, 3, 4, 5, 6, 7, 8
- Results (format = {s}):
  - Spearman -0.256: 1
  - Spearman -0.253: 0
  - Spearman -0.232: 3
  - Spearman -0.214: 8
  - Spearman -0.212: 2
  - Spearman -0.203: 7
  - Spearman -0.199: 6
  - Spearman -0.189: 5
  - Spearman -0.175: 4

## Experiment - Number of MFCC coefficients (M=80)

- Changed parameter(s): M=80
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 30, 40, 50, 60, 70, 80
- Results (format = {D}):
  - Spearman -0.266: 13
  - Spearman -0.265: 12, 15
  - Spearman -0.263: 14
  - Spearman -0.261: 17, 19
  - Spearman -0.260: 16
  - Spearman -0.259: 11
  - Spearman -0.258: 18
  - Spearman -0.250: 10
  - Spearman -0.243: 9
  - Spearman -0.239: 30, 8
  - Spearman -0.231: 7
  - Spearman -0.225: 6
  - Spearman -0.213: 40
  - Spearman -0.207: 5
  - Spearman -0.194: 4
  - Spearman -0.192: 50
  - Spearman -0.185: 60
  - Spearman -0.184: 70
  - Spearman -0.181: 80
  - Spearman -0.155: 2
  - Spearman -0.149: 3

## Experiment - Number of MFCC coefficients (M=40)

- Changed parameter(s): M=40
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 25, 30, 35, 40
- Results (format = {D}):
  - Spearman -0.270: 13
  - Spearman -0.267: 15
  - Spearman -0.266: 12, 14
  - Spearman -0.263: 11, 18, 19
  - Spearman -0.262: 17
  - Spearman -0.261: 16
  - Spearman -0.259: 10
  - Spearman -0.246: 25
  - Spearman -0.244: 9
  - Spearman -0.239: 8
  - Spearman -0.237: 7
  - Spearman -0.230: 6
  - Spearman -0.229: 30
  - Spearman -0.224: 35
  - Spearman -0.223: 40
  - Spearman -0.213: 5
  - Spearman -0.211: 4
  - Spearman -0.150: 3
  - Spearman -0.140: 2

## Experiment - Number of MFCC coefficients (M=20)

- Changed parameter(s): M=20
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
- Results (format = {D}):
  - Spearman -0.277: 13, 18
  - Spearman -0.276: 12, 14
  - Spearman -0.275: 19, 20
  - Spearman -0.274: 11, 17
  - Spearman -0.273: 16
  - Spearman -0.271: 15
  - Spearman -0.270: 10
  - Spearman -0.267: 8
  - Spearman -0.263: 9
  - Spearman -0.255: 7
  - Spearman -0.251: 6
  - Spearman -0.244: 5
  - Spearman -0.230: 4
  - Spearman -0.168: 3
  - Spearman -0.140: 2

## Experiment - Number of MFCC coefficients (M=10)

- Changed parameter(s): M=10
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10
- Results (format = {D}):
  - Spearman -0.239: 6
  - Spearman -0.232: 7
  - Spearman -0.230: 5
  - Spearman -0.225: 10, 8, 9
  - Spearman -0.210: 4
  - Spearman -0.205: 3
  - Spearman -0.136: 2

## Experiment - Number of MFCC coefficients (M=5)

- Changed parameter(s): M=5
- Experimented parameter(s):
  - D = 2, 3, 4, 5
- Results (format = {D}):
  - Spearman -0.188: 4, 5
  - Spearman -0.176: 3
  - Spearman -0.158: 2

## Experiment - Silence removal

- Experimented parameter(s):
  - remove_silence = mel, no
  - silence_threshold_A = -3, None, -4, -3.5
  - silence_threshold_B = -4.5, -4, -3.5, None
- Results (format = {remove_silence:silence_threshold_A:silence_threshold_B}):
  - Spearman -0.273: no:None:None
  - Spearman -0.214: mel:-3.5:-4
  - Spearman -0.207: mel:-4:-4.5
  - Spearman -0.191: mel:-3:-3.5

## Experiment - Normalize audio

- Experimented parameter(s):
  - norm_audio = False, True
- Results (format = {norm_audio}):
  - Spearman -0.274: False
  - Spearman -0.273: True

## Experiment - Alignment method

- Experimented parameter(s):
  - align_method = dtw, pad
  - align_target = mel, mfcc, spec
- Results (format = {align_method:align_target}):
  - Spearman -0.279: dtw:mel
  - Spearman -0.273: dtw:mfcc
  - Spearman -0.215: dtw:spec
  - Spearman -0.067: pad:mel, pad:mfcc, pad:spec

## Experiment - Sakoe-Chiba radius

- Experimented parameter(s):
  - dtw_radius = 1, 2, 3, 10, 20, None, 40
- Results (format = {dtw_radius}):
  - Spearman -0.273: 1, 10, 2, 20, 3, 40, None

## Experiment - Window function

- Experimented parameter(s):
  - window = hamming, hanning
- Results (format = {window}):
  - Spearman -0.273: hanning
  - Spearman -0.253: hamming

## Experiment - FFT window length

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {n_fft}):
  - Spearman -0.273: 128
  - Spearman -0.261: 8
  - Spearman -0.253: 64
  - Spearman -0.243: 32
  - Spearman -0.233: 256
  - Spearman -0.230: 16
  - Spearman -0.224: 1024, 512

## Experiment - Window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len}):
  - Spearman -0.273: 128
  - Spearman -0.267: 256
  - Spearman -0.258: 64
  - Spearman -0.250: 1024, 512
  - Spearman -0.239: 32
  - Spearman -0.200: 16
  - Spearman -0.169: 8

## Experiment - Hop length

- Experimented parameter(s):
  - hop_len = 8, 16, 32, 64, 128
- Results (format = {hop_len}):
  - Spearman -0.273: 32
  - Spearman -0.241: 16
  - Spearman -0.233: 8
  - Spearman -0.221: 64
  - Spearman -0.189: 128

## Experiment - Equal FFT window length and window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len:n_fft}):
  - Spearman -0.273: 128:128
  - Spearman -0.247: 8:8
  - Spearman -0.245: 64:64
  - Spearman -0.239: 256:256
  - Spearman -0.231: 32:32
  - Spearman -0.222: 16:16
  - Spearman -0.204: 512:512
  - Spearman -0.172: 1024:1024

## Experiment - FFT window length, window length and hop length with ratio 4:4:1

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {win_len:n_fft:hop_len}):
  - Spearman -0.273: 128:128:32
  - Spearman -0.243: 16:16:4
  - Spearman -0.238: 32:32:8
  - Spearman -0.237: 8:8:2
  - Spearman -0.226: 64:64:16
  - Spearman -0.200: 256:256:64
  - Spearman -0.194: 512:512:128
  - Spearman -0.153: 1024:1024:256

## Experiment - FFT window length, window length and hop length with ratio 9:3:1

- Experimented parameter(s):
  - n_fft = 16, 32, 64, 128, 256, 512, 1024
  - win_len = 5, 5.33, 10, 10.67, 21, 21.33, 42, 42.67, 85, 85.33, 170, 170.67, 341, 341.33
  - hop_len = 1, 1.78, 3, 3.56, 7, 7.11, 14, 14.22, 28, 28.44, 56, 56.89, 113, 113.78
- Results (format = {n_fft:win_len:hop_len}):
  - Spearman -0.264: 64:21.33:7.11
  - Spearman -0.261: 128:42:14
  - Spearman -0.252: 32:10:3
  - Spearman -0.249: 64:21:7
  - Spearman -0.247: 128:42.67:14.22, 256:85:28
  - Spearman -0.236: 256:85.33:28.44
  - Spearman -0.235: 32:10.67:3.56
  - Spearman -0.221: 16:5:1
  - Spearman -0.204: 16:5.33:1.78
  - Spearman -0.138: 512:170:56
  - Spearman -0.096: 1024:341:113
  - Spearman -0.092: 512:170.67:56.89
  - Spearman -0.079: 1024:341.33:113.78

## Experiment - FFT window length, window length and hop length with ratio 4:2:1

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 64, 128, 256, 512
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - Spearman -0.305: 64:32:16
  - Spearman -0.277: 32:16:8
  - Spearman -0.258: 128:64:32
  - Spearman -0.248: 16:8:4
  - Spearman -0.214: 8:4:2
  - Spearman -0.187: 512:256:128
  - Spearman -0.162: 256:128:64
  - Spearman -0.119: 1024:512:256

## Experiment - FFT window length, window length and hop length with different ratios

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 46.44, 64, 85.33, 100, 120, 128, 170.67, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 46.44, 50, 60, 64, 85.33, 100, 120, 128, 170.67, 256, 512
  - hop_len = 2, 4, 8, 11.61, 16, 21.33, 25, 30, 32, 42.67, 48, 50, 60, 64, 85.33, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - Spearman -0.305: 64:32:16
  - Spearman -0.296: 128:64:16
  - Spearman -0.292: 64:32:8
  - Spearman -0.287: 128:32:8
  - Spearman -0.285: 100:50:25, 256:64:8
  - Spearman -0.277: 32:16:8
  - Spearman -0.273: 100:100:50, 128:128:32, 128:64:8
  - Spearman -0.267: 128:256:32
  - Spearman -0.258: 128:64:32
  - Spearman -0.255: 120:120:30
  - Spearman -0.254: 46.44:46.44:11.61
  - Spearman -0.252: 256:128:16
  - Spearman -0.251: 100:100:25
  - Spearman -0.249: 85.33:85.33:21.33
  - Spearman -0.245: 256:128:8, 64:64:32
  - Spearman -0.243: 16:16:4, 8:8:4
  - Spearman -0.242: 16:16:8
  - Spearman -0.241: 128:128:16
  - Spearman -0.239: 256:256:32, 64:64:8
  - Spearman -0.238: 170.67:170.67:42.67, 32:32:8
  - Spearman -0.237: 8:8:2
  - Spearman -0.233: 256:128:32
  - Spearman -0.230: 512:256:32
  - Spearman -0.228: 85.33:85.33:42.67
  - Spearman -0.222: 128:256:64
  - Spearman -0.221: 128:128:64
  - Spearman -0.214: 8:4:2
  - Spearman -0.212: 64:64:48
  - Spearman -0.209: 120:120:60, 120:60:30
  - Spearman -0.198: 170.67:170.67:85.33
  - Spearman -0.194: 512:512:128
  - Spearman -0.119: 1024:512:256

## Experiment - Finding optimal Pearson parameters (baseline)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = True
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - Spearman -0.292: 128:64:16:12:mel:True

## Experiment - Finding optimal Pearson parameters (norm=False)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = False
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - Spearman -0.276: 128:64:16:12:mel:False

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
  - Spearman -0.301: 128:64:16:12:mel:True:3, 128:64:16:12:mel:True:4
  - Spearman -0.292: 128:64:16:12:mel:True:10
  - Spearman -0.290: 128:64:16:12:mel:True:2
  - Spearman -0.269: 128:64:16:12:mel:True:1

## Experiment - Finding optimal Spearman parameters (baseline)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 10
  - M = 11
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - Spearman -0.279: 64:32:16:10:11:mel

## Experiment - Finding optimal Spearman parameters (D, M)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 12, 13
  - M = 20
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - Spearman -0.307: 64:32:16:12:20:mel, 64:32:16:13:20:mel

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
  - Spearman -0.274: 64:32:16:13:20:mel:False

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
  - Spearman -0.309: 64:32:16:13:20:mel:2
  - Spearman -0.308: 64:32:16:13:20:mel:4
  - Spearman -0.307: 64:32:16:13:20:mel:10, 64:32:16:13:20:mel:3
  - Spearman -0.291: 64:32:16:13:20:mel:1

## Best experiments

### 1. Place

- Spearman: -0.3089277132823951
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

- Spearman: -0.3076200298281067
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

- Spearman: -0.3073647554058694
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
