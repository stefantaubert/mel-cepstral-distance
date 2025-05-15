# Analysis of PEN values depending on the parameters

## Default parameters for experiments

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
  - PEN 0.079: 44100
  - PEN 0.083: 192000
  - PEN 0.090: 32000
  - PEN 0.091: 22050, 24000, 8000
  - PEN 0.092: 4000
  - PEN 0.094: 16000
  - PEN 0.104: 48000
  - PEN 0.107: 96000
  - PEN 0.110: 88200

## Experiment - Minimum frequency

- Experimented parameter(s):
  - fmin = 0, 100, 500, 1000, 2000, 4000, 8000, 16000, 22050, 44100
- Results (format = {fmin}):
  - PEN 0.094: 1000
  - PEN 0.104: 4000
  - PEN 0.107: 0, 500
  - PEN 0.111: 2000
  - PEN 0.113: 100
  - PEN 0.219: 8000
  - PEN 0.387: 16000
  - PEN 0.412: 22050
  - PEN 0.569: 44100

## Experiment - Maximum frequency

- Changed parameter(s): sample_rate=192000
- Experimented parameter(s):
  - fmax = 4000, 8000, 11025, 16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000
- Results (format = {fmax}):
  - PEN 0.080: 22050
  - PEN 0.083: 96000
  - PEN 0.090: 16000
  - PEN 0.091: 11025, 4000
  - PEN 0.094: 8000
  - PEN 0.106: 24000
  - PEN 0.110: 48000
  - PEN 0.114: 32000, 88200
  - PEN 0.115: 44100

## Experiment - Number of mel filterbanks

- Changed parameter(s): D=10
- Experimented parameter(s):
  - M = 10, 11, 12, 13, 20, 30, 40, 50, 60, 70, 80
- Results (format = {M}):
  - PEN 0.106: 70, 80
  - PEN 0.108: 50, 60
  - PEN 0.110: 40
  - PEN 0.112: 30
  - PEN 0.116: 20
  - PEN 0.130: 11
  - PEN 0.137: 13
  - PEN 0.142: 12
  - PEN 0.154: 10

## Experiment - Starting index

- Experimented parameter(s):
  - s = 0, 1, 2, 3, 4, 5, 6, 7, 8
- Results (format = {s}):
  - PEN 0.113: 2
  - PEN 0.115: 3
  - PEN 0.118: 0
  - PEN 0.127: 1
  - PEN 0.136: 4
  - PEN 0.161: 5
  - PEN 0.173: 6
  - PEN 0.205: 7
  - PEN 0.306: 8

## Experiment - Number of MFCC coefficients (M=80)

- Changed parameter(s): M=80
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 30, 40, 50, 60, 70, 80
- Results (format = {D}):
  - PEN 0.083: 70, 80
  - PEN 0.084: 60
  - PEN 0.085: 50
  - PEN 0.087: 40
  - PEN 0.090: 30
  - PEN 0.096: 18, 19
  - PEN 0.097: 17
  - PEN 0.098: 15, 16
  - PEN 0.100: 13, 14
  - PEN 0.102: 12
  - PEN 0.103: 11
  - PEN 0.106: 10
  - PEN 0.109: 9
  - PEN 0.114: 8
  - PEN 0.121: 7
  - PEN 0.132: 6
  - PEN 0.150: 5
  - PEN 0.186: 4
  - PEN 0.253: 3
  - PEN 0.445: 2

## Experiment - Number of MFCC coefficients (M=40)

- Changed parameter(s): M=40
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 25, 30, 35, 40
- Results (format = {D}):
  - PEN 0.091: 35, 40
  - PEN 0.093: 30
  - PEN 0.094: 25
  - PEN 0.098: 19
  - PEN 0.099: 17, 18
  - PEN 0.100: 16
  - PEN 0.101: 15
  - PEN 0.103: 14
  - PEN 0.104: 13
  - PEN 0.106: 12
  - PEN 0.107: 11
  - PEN 0.110: 10
  - PEN 0.113: 9
  - PEN 0.118: 8
  - PEN 0.124: 7
  - PEN 0.138: 6
  - PEN 0.164: 5
  - PEN 0.204: 4
  - PEN 0.264: 3
  - PEN 0.439: 2

## Experiment - Number of MFCC coefficients (M=20)

- Changed parameter(s): M=20
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
- Results (format = {D}):
  - PEN 0.105: 18, 19, 20
  - PEN 0.107: 16, 17
  - PEN 0.108: 15
  - PEN 0.110: 14
  - PEN 0.111: 13
  - PEN 0.112: 12
  - PEN 0.113: 11
  - PEN 0.116: 10
  - PEN 0.120: 9
  - PEN 0.123: 8
  - PEN 0.131: 7
  - PEN 0.147: 6
  - PEN 0.170: 5
  - PEN 0.210: 4
  - PEN 0.272: 3
  - PEN 0.425: 2

## Experiment - Number of MFCC coefficients (M=10)

- Changed parameter(s): M=10
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10
- Results (format = {D}):
  - PEN 0.154: 10, 9
  - PEN 0.158: 8
  - PEN 0.165: 7
  - PEN 0.179: 6
  - PEN 0.191: 5
  - PEN 0.229: 4
  - PEN 0.298: 3
  - PEN 0.420: 2

## Experiment - Number of MFCC coefficients (M=5)

- Changed parameter(s): M=5
- Experimented parameter(s):
  - D = 2, 3, 4, 5
- Results (format = {D}):
  - PEN 0.317: 4, 5
  - PEN 0.375: 3
  - PEN 0.480: 2

## Experiment - Silence removal

- Experimented parameter(s):
  - remove_silence = mel, no
  - silence_threshold_A = -3, None, -4, -3.5
  - silence_threshold_B = -4.5, None, -4, -3.5
- Results (format = {remove_silence:silence_threshold_A:silence_threshold_B}):
  - PEN 0.104: mel:-4:-4.5
  - PEN 0.107: no:None:None
  - PEN 0.110: mel:-3.5:-4
  - PEN 0.135: mel:-3:-3.5

## Experiment - Normalize audio

- Experimented parameter(s):
  - norm_audio = False, True
- Results (format = {norm_audio}):
  - PEN 0.107: True
  - PEN 0.112: False

## Experiment - Alignment method

- Experimented parameter(s):
  - align_method = dtw, pad
  - align_target = mel, mfcc, spec
- Results (format = {align_method:align_target}):
  - PEN 0.042: pad:mel, pad:mfcc, pad:spec
  - PEN 0.106: dtw:spec
  - PEN 0.107: dtw:mfcc
  - PEN 0.114: dtw:mel

## Experiment - Sakoe-Chiba radius

- Experimented parameter(s):
  - dtw_radius = 1, 2, 3, 10, 20, 40, None
- Results (format = {dtw_radius}):
  - PEN 0.107: 1, 10, 2, 20, 3, 40, None

## Experiment - Window function

- Experimented parameter(s):
  - window = hamming, hanning
- Results (format = {window}):
  - PEN 0.107: hanning
  - PEN 0.148: hamming

## Experiment - FFT window length

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {n_fft}):
  - PEN 0.106: 16
  - PEN 0.107: 128
  - PEN 0.108: 8
  - PEN 0.109: 32, 64
  - PEN 0.148: 1024
  - PEN 0.149: 512
  - PEN 0.151: 256

## Experiment - Window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len}):
  - PEN 0.107: 128
  - PEN 0.109: 256
  - PEN 0.111: 512
  - PEN 0.118: 1024
  - PEN 0.137: 32
  - PEN 0.138: 16
  - PEN 0.139: 64, 8

## Experiment - Hop length

- Experimented parameter(s):
  - hop_len = 8, 16, 32, 64, 128
- Results (format = {hop_len}):
  - PEN 0.085: 128
  - PEN 0.091: 64
  - PEN 0.107: 32
  - PEN 0.123: 16
  - PEN 0.139: 8

## Experiment - Equal FFT window length and window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len:n_fft}):
  - PEN 0.101: 256:256
  - PEN 0.102: 512:512
  - PEN 0.105: 16:16
  - PEN 0.107: 128:128, 8:8
  - PEN 0.108: 32:32
  - PEN 0.109: 64:64
  - PEN 0.110: 1024:1024

## Experiment - FFT window length, window length and hop length with ratio 4:4:1

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {win_len:n_fft:hop_len}):
  - PEN 0.062: 1024:1024:256
  - PEN 0.074: 512:512:128
  - PEN 0.088: 256:256:64
  - PEN 0.107: 128:128:32
  - PEN 0.124: 64:64:16
  - PEN 0.138: 32:32:8
  - PEN 0.141: 16:16:4
  - PEN 0.158: 8:8:2

## Experiment - FFT window length, window length and hop length with ratio 9:3:1

- Experimented parameter(s):
  - n_fft = 16, 32, 64, 128, 256, 512, 1024
  - win_len = 5, 10, 21, 42, 85, 170, 341
  - hop_len = 1, 3, 7, 14, 28, 56, 113
- Results (format = {n_fft:win_len:hop_len}):
  - PEN 0.120: 1024:341:113
  - PEN 0.131: 512:170:56
  - PEN 0.148: 256:85:28
  - PEN 0.172: 128:42:14
  - PEN 0.192: 64:21:7
  - PEN 0.211: 32:10:3
  - PEN 0.229: 16:5:1

## Experiment - FFT window length, window length and hop length with ratio 4:2:1

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 64, 128, 256, 512
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - PEN 0.101: 1024:512:256
  - PEN 0.109: 512:256:128
  - PEN 0.120: 256:128:64
  - PEN 0.139: 128:64:32
  - PEN 0.166: 64:32:16
  - PEN 0.188: 32:16:8
  - PEN 0.205: 16:8:4
  - PEN 0.212: 8:4:2

## Experiment - FFT window length, window length and hop length with different ratios

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 46.44, 64, 85.33, 100, 120, 128, 170.67, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 46.44, 50, 60, 64, 85.33, 100, 120, 128, 170.67, 256, 512
  - hop_len = 2, 4, 8, 11.61, 16, 21.33, 25, 30, 32, 42.67, 48, 50, 60, 64, 85.33, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - PEN 0.074: 512:512:128
  - PEN 0.085: 170.67:170.67:85.33
  - PEN 0.091: 128:128:64
  - PEN 0.092: 128:256:64
  - PEN 0.096: 120:120:60
  - PEN 0.097: 170.67:170.67:42.67
  - PEN 0.099: 100:100:50
  - PEN 0.100: 64:64:48
  - PEN 0.101: 1024:512:256, 256:256:32
  - PEN 0.102: 85.33:85.33:42.67
  - PEN 0.107: 128:128:32
  - PEN 0.109: 128:256:32, 64:64:32
  - PEN 0.111: 120:120:30
  - PEN 0.114: 100:100:25
  - PEN 0.118: 85.33:85.33:21.33
  - PEN 0.123: 128:128:16
  - PEN 0.129: 16:16:8
  - PEN 0.138: 32:32:8
  - PEN 0.139: 128:64:32, 46.44:46.44:11.61
  - PEN 0.140: 64:64:8
  - PEN 0.141: 16:16:4
  - PEN 0.144: 120:60:30
  - PEN 0.146: 8:8:4
  - PEN 0.147: 100:50:25
  - PEN 0.151: 256:128:32
  - PEN 0.158: 8:8:2
  - PEN 0.166: 64:32:16
  - PEN 0.171: 128:64:16
  - PEN 0.176: 512:256:32
  - PEN 0.184: 256:128:16
  - PEN 0.188: 32:16:8
  - PEN 0.192: 128:32:8, 64:32:8
  - PEN 0.196: 256:64:8
  - PEN 0.197: 128:64:8
  - PEN 0.210: 256:128:8
  - PEN 0.212: 8:4:2

## Experiment - Finding optimal Pearson parameters (baseline)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = True
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - PEN 0.236: 128:64:16:12:mel:True

## Experiment - Finding optimal Pearson parameters (norm=False)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = False
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - PEN 0.226: 128:64:16:12:mel:False

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
  - PEN 0.235: 128:64:16:12:mel:True:1
  - PEN 0.236: 128:64:16:12:mel:True:10, 128:64:16:12:mel:True:2, 128:64:16:12:mel:True:3, 128:64:16:12:mel:True:4

## Experiment - Finding optimal Spearman parameters (baseline)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 10
  - M = 11
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - PEN 0.258: 64:32:16:10:11:mel

## Experiment - Finding optimal Spearman parameters (D, M)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 12, 13
  - M = 20
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - PEN 0.247: 64:32:16:12:20:mel, 64:32:16:13:20:mel

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
  - PEN 0.240: 64:32:16:13:20:mel:False

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
  - PEN 0.246: 64:32:16:13:20:mel:1
  - PEN 0.247: 64:32:16:13:20:mel:10, 64:32:16:13:20:mel:2, 64:32:16:13:20:mel:3, 64:32:16:13:20:mel:4
