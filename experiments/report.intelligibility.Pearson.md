# Analysis of MCD and intelligibility MOS Pearson correlation

## Metrics

| obj_metric      |   mean |   median |
|-----------------|--------|----------|
| mcd*(pen+0.1)   | -0.127 |   -0.137 |
| mcd*pen         | -0.126 |   -0.135 |
| mcd*(pen+0.25)  | -0.125 |   -0.133 |
| pen*(mcd+1)     | -0.124 |   -0.134 |
| mcd*(pen+0.5)   | -0.118 |   -0.124 |
| pen             | -0.117 |   -0.127 |
| mcd*(pen+1)     | -0.105 |   -0.11  |
| mcd*(pen+2)     | -0.092 |   -0.095 |
| mcd+pen         | -0.076 |   -0.079 |
| mcd             | -0.071 |   -0.073 |
| sqrt(mcd²+pen²) | -0.07  |   -0.073 |
| mcd-pen         | -0.063 |   -0.07  |
| mcd*(pen-1)     |  0.001 |    0.01  |

## Default parameters for experiments

- obj_metric = mcd*(pen+0.1)
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
  - Pearson -0.158: 192000
  - Pearson -0.143: 96000
  - Pearson -0.137: 44100
  - Pearson -0.127: 88200
  - Pearson -0.125: 48000
  - Pearson -0.121: 8000
  - Pearson -0.116: 32000
  - Pearson -0.102: 16000
  - Pearson -0.089: 24000
  - Pearson -0.087: 22050
  - Pearson -0.052: 4000

## Experiment - Minimum frequency

- Experimented parameter(s):
  - fmin = 0, 100, 500, 1000, 2000, 4000, 8000, 16000, 22050, 44100
- Results (format = {fmin}):
  - Pearson -0.185: 1000
  - Pearson -0.157: 500
  - Pearson -0.145: 100
  - Pearson -0.143: 0
  - Pearson -0.106: 8000
  - Pearson -0.104: 2000
  - Pearson -0.059: 4000
  - Pearson -0.038: 44100
  - Pearson -0.017: 22050
  - Pearson 0.005: 16000

## Experiment - Maximum frequency

- Changed parameter(s): sample_rate=192000
- Experimented parameter(s):
  - fmax = 4000, 8000, 11025, 16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000
- Results (format = {fmax}):
  - Pearson -0.173: 22050
  - Pearson -0.158: 96000
  - Pearson -0.139: 32000, 88200
  - Pearson -0.135: 24000, 48000
  - Pearson -0.118: 4000
  - Pearson -0.113: 16000
  - Pearson -0.111: 8000
  - Pearson -0.104: 11025
  - Pearson -0.095: 44100

## Experiment - Number of mel filterbanks

- Changed parameter(s): D=10
- Experimented parameter(s):
  - M = 10, 11, 12, 13, 20, 30, 40, 50, 60, 70, 80
- Results (format = {M}):
  - Pearson -0.157: 80
  - Pearson -0.151: 70
  - Pearson -0.144: 50
  - Pearson -0.131: 60
  - Pearson -0.116: 40
  - Pearson -0.115: 30
  - Pearson -0.114: 20
  - Pearson -0.110: 13
  - Pearson -0.104: 11, 12
  - Pearson -0.050: 10

## Experiment - Starting index

- Experimented parameter(s):
  - s = 0, 1, 2, 3, 4, 5, 6, 7, 8
- Results (format = {s}):
  - Pearson -0.216: 5
  - Pearson -0.215: 6
  - Pearson -0.195: 8
  - Pearson -0.169: 0
  - Pearson -0.162: 4
  - Pearson -0.145: 7
  - Pearson -0.141: 3
  - Pearson -0.128: 2
  - Pearson -0.097: 1

## Experiment - Number of MFCC coefficients (M=80)

- Changed parameter(s): M=80
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 30, 40, 50, 60, 70, 80
- Results (format = {D}):
  - Pearson -0.157: 10
  - Pearson -0.155: 15
  - Pearson -0.153: 13, 16
  - Pearson -0.150: 12
  - Pearson -0.146: 14
  - Pearson -0.143: 11
  - Pearson -0.141: 9
  - Pearson -0.139: 17
  - Pearson -0.138: 18, 19
  - Pearson -0.133: 8
  - Pearson -0.127: 30
  - Pearson -0.126: 7
  - Pearson -0.125: 60
  - Pearson -0.120: 50
  - Pearson -0.119: 70
  - Pearson -0.117: 40, 80
  - Pearson -0.114: 6
  - Pearson -0.104: 5
  - Pearson -0.076: 2
  - Pearson -0.039: 3, 4

## Experiment - Number of MFCC coefficients (M=40)

- Changed parameter(s): M=40
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 25, 30, 35, 40
- Results (format = {D}):
  - Pearson -0.148: 17
  - Pearson -0.146: 18
  - Pearson -0.141: 12, 19
  - Pearson -0.140: 16
  - Pearson -0.139: 14
  - Pearson -0.137: 15
  - Pearson -0.134: 13
  - Pearson -0.133: 11
  - Pearson -0.132: 25
  - Pearson -0.128: 30, 8
  - Pearson -0.124: 35
  - Pearson -0.117: 40
  - Pearson -0.116: 10
  - Pearson -0.110: 6
  - Pearson -0.106: 7
  - Pearson -0.103: 9
  - Pearson -0.057: 2
  - Pearson -0.056: 5
  - Pearson -0.044: 3
  - Pearson -0.030: 4

## Experiment - Number of MFCC coefficients (M=20)

- Changed parameter(s): M=20
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
- Results (format = {D}):
  - Pearson -0.146: 17
  - Pearson -0.145: 15
  - Pearson -0.143: 16
  - Pearson -0.141: 14
  - Pearson -0.137: 13, 19, 20
  - Pearson -0.135: 12, 18
  - Pearson -0.129: 11
  - Pearson -0.124: 8
  - Pearson -0.122: 9
  - Pearson -0.115: 7
  - Pearson -0.114: 10
  - Pearson -0.098: 6
  - Pearson -0.074: 4
  - Pearson -0.067: 3
  - Pearson -0.066: 5
  - Pearson -0.053: 2

## Experiment - Number of MFCC coefficients (M=10)

- Changed parameter(s): M=10
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10
- Results (format = {D}):
  - Pearson -0.065: 6
  - Pearson -0.062: 8
  - Pearson -0.059: 7
  - Pearson -0.058: 2
  - Pearson -0.050: 10, 9
  - Pearson -0.042: 5
  - Pearson -0.041: 3
  - Pearson -0.010: 4

## Experiment - Number of MFCC coefficients (M=5)

- Changed parameter(s): M=5
- Experimented parameter(s):
  - D = 2, 3, 4, 5
- Results (format = {D}):
  - Pearson -0.120: 2
  - Pearson -0.043: 3
  - Pearson -0.006: 4, 5

## Experiment - Silence removal

- Experimented parameter(s):
  - remove_silence = mel, no
  - silence_threshold_A = -4, None, -3.5, -3
  - silence_threshold_B = -4.5, -4, -3.5, None
- Results (format = {remove_silence:silence_threshold_A:silence_threshold_B}):
  - Pearson -0.143: no:None:None
  - Pearson -0.118: mel:-3.5:-4
  - Pearson -0.083: mel:-4:-4.5
  - Pearson -0.041: mel:-3:-3.5

## Experiment - Normalize audio

- Experimented parameter(s):
  - norm_audio = False, True
- Results (format = {norm_audio}):
  - Pearson -0.153: False
  - Pearson -0.143: True

## Experiment - Alignment method

- Experimented parameter(s):
  - align_method = dtw, pad
  - align_target = mel, mfcc, spec
- Results (format = {align_method:align_target}):
  - Pearson -0.173: dtw:mel
  - Pearson -0.143: dtw:mfcc
  - Pearson -0.076: pad:mel, pad:mfcc, pad:spec
  - Pearson -0.069: dtw:spec

## Experiment - Sakoe-Chiba radius

- Experimented parameter(s):
  - dtw_radius = 1, 2, 3, 10, 20, 40, None
- Results (format = {dtw_radius}):
  - Pearson -0.143: 10, 2, 20, 3, 40, None
  - Pearson -0.140: 1

## Experiment - Window function

- Experimented parameter(s):
  - window = hamming, hanning
- Results (format = {window}):
  - Pearson -0.143: hanning
  - Pearson -0.142: hamming

## Experiment - FFT window length

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {n_fft}):
  - Pearson -0.221: 32
  - Pearson -0.198: 16
  - Pearson -0.176: 8
  - Pearson -0.167: 64
  - Pearson -0.149: 512
  - Pearson -0.144: 1024
  - Pearson -0.143: 128, 256

## Experiment - Window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len}):
  - Pearson -0.144: 16
  - Pearson -0.143: 128
  - Pearson -0.134: 256
  - Pearson -0.133: 1024
  - Pearson -0.123: 64
  - Pearson -0.122: 512
  - Pearson -0.106: 8
  - Pearson -0.094: 32

## Experiment - Hop length

- Experimented parameter(s):
  - hop_len = 8, 16, 32, 64, 128
- Results (format = {hop_len}):
  - Pearson -0.192: 64
  - Pearson -0.164: 8
  - Pearson -0.143: 32
  - Pearson -0.140: 16
  - Pearson -0.119: 128

## Experiment - Equal FFT window length and window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len:n_fft}):
  - Pearson -0.215: 32:32
  - Pearson -0.191: 16:16
  - Pearson -0.174: 8:8
  - Pearson -0.171: 1024:1024
  - Pearson -0.165: 64:64
  - Pearson -0.143: 128:128
  - Pearson -0.126: 512:512
  - Pearson -0.117: 256:256

## Experiment - FFT window length, window length and hop length with ratio 4:4:1

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {win_len:n_fft:hop_len}):
  - Pearson -0.206: 16:16:4
  - Pearson -0.203: 32:32:8
  - Pearson -0.195: 8:8:2
  - Pearson -0.178: 64:64:16
  - Pearson -0.143: 128:128:32
  - Pearson -0.125: 256:256:64
  - Pearson -0.121: 512:512:128
  - Pearson -0.093: 1024:1024:256

## Experiment - FFT window length, window length and hop length with ratio 9:3:1

- Experimented parameter(s):
  - n_fft = 16, 32, 64, 128, 256, 512, 1024
  - win_len = 5, 10, 21, 42, 85, 170, 341
  - hop_len = 1, 3, 7, 14, 28, 56, 113
- Results (format = {n_fft:win_len:hop_len}):
  - Pearson -0.144: 64:21:7
  - Pearson -0.140: 128:42:14
  - Pearson -0.134: 256:85:28
  - Pearson -0.103: 512:170:56
  - Pearson -0.102: 32:10:3
  - Pearson -0.090: 16:5:1
  - Pearson -0.025: 1024:341:113

## Experiment - FFT window length, window length and hop length with ratio 4:2:1

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 64, 128, 256, 512
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - Pearson -0.149: 32:16:8
  - Pearson -0.140: 512:256:128
  - Pearson -0.130: 16:8:4, 64:32:16
  - Pearson -0.125: 256:128:64
  - Pearson -0.123: 128:64:32
  - Pearson -0.102: 8:4:2
  - Pearson -0.005: 1024:512:256

## Experiment - FFT window length, window length and hop length with different ratios

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 46.44, 64, 85.33, 100, 120, 128, 170.67, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 46.44, 50, 60, 64, 85.33, 100, 120, 128, 170.67, 256, 512
  - hop_len = 2, 4, 8, 11.61, 16, 21.33, 25, 30, 32, 42.67, 48, 50, 60, 64, 85.33, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - Pearson -0.206: 16:16:4
  - Pearson -0.205: 16:16:8
  - Pearson -0.203: 32:32:8
  - Pearson -0.200: 8:8:4
  - Pearson -0.195: 8:8:2
  - Pearson -0.192: 128:128:64, 64:64:8
  - Pearson -0.187: 128:256:64, 85.33:85.33:21.33
  - Pearson -0.180: 120:60:30
  - Pearson -0.179: 256:128:16
  - Pearson -0.174: 120:120:30
  - Pearson -0.172: 100:100:25
  - Pearson -0.171: 100:50:25
  - Pearson -0.169: 128:64:16
  - Pearson -0.165: 64:64:32
  - Pearson -0.163: 128:64:8
  - Pearson -0.157: 256:64:8, 64:32:8
  - Pearson -0.156: 256:128:8
  - Pearson -0.153: 128:32:8, 85.33:85.33:42.67
  - Pearson -0.152: 100:100:50
  - Pearson -0.149: 32:16:8
  - Pearson -0.145: 46.44:46.44:11.61
  - Pearson -0.143: 128:128:32, 256:128:32
  - Pearson -0.140: 128:128:16, 512:256:32
  - Pearson -0.138: 64:64:48
  - Pearson -0.134: 128:256:32
  - Pearson -0.130: 64:32:16
  - Pearson -0.123: 128:64:32
  - Pearson -0.121: 120:120:60, 512:512:128
  - Pearson -0.117: 256:256:32
  - Pearson -0.110: 170.67:170.67:42.67
  - Pearson -0.102: 8:4:2
  - Pearson -0.073: 170.67:170.67:85.33
  - Pearson -0.005: 1024:512:256

## Experiment - Finding optimal Pearson parameters (baseline)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = True
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - Pearson -0.140: 128:64:16:12:mel:True

## Experiment - Finding optimal Pearson parameters (norm=False)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = False
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - Pearson -0.115: 128:64:16:12:mel:False

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
  - Pearson -0.150: 128:64:16:12:mel:True:3
  - Pearson -0.148: 128:64:16:12:mel:True:4
  - Pearson -0.144: 128:64:16:12:mel:True:2
  - Pearson -0.140: 128:64:16:12:mel:True:10
  - Pearson -0.125: 128:64:16:12:mel:True:1

## Experiment - Finding optimal Spearman parameters (baseline)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 10
  - M = 11
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - Pearson -0.133: 64:32:16:10:11:mel

## Experiment - Finding optimal Spearman parameters (D, M)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 12, 13
  - M = 20
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - Pearson -0.149: 64:32:16:13:20:mel
  - Pearson -0.148: 64:32:16:12:20:mel

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
  - Pearson -0.152: 64:32:16:13:20:mel:False

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
  - Pearson -0.167: 64:32:16:13:20:mel:1
  - Pearson -0.153: 64:32:16:13:20:mel:3
  - Pearson -0.151: 64:32:16:13:20:mel:2, 64:32:16:13:20:mel:4
  - Pearson -0.149: 64:32:16:13:20:mel:10

## Best experiments

### 1. Place

- Pearson: -0.2213719616212097
- Experiments with that score (#1):
  - 'FFT window length' with parameters:
    - sample_rate = 96000
    - n_fft = 32
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

### 2. Place

- Pearson: -0.2160685642034554
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

### 3. Place

- Pearson: -0.2153991452078824
- Experiments with that score (#1):
  - 'Equal FFT window length and window length' with parameters:
    - sample_rate = 96000
    - n_fft = 32
    - win_len = 32
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
