# Analysis of MCD values depending on the parameters

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
  - MCD 6.420: 8000
  - MCD 6.708: 16000
  - MCD 6.712: 22050
  - MCD 6.757: 24000
  - MCD 7.458: 32000
  - MCD 7.477: 88200
  - MCD 7.625: 48000
  - MCD 7.751: 96000
  - MCD 7.952: 4000
  - MCD 10.689: 192000
  - MCD 12.189: 44100

## Experiment - Minimum frequency

- Experimented parameter(s):
  - fmin = 0, 100, 500, 1000, 2000, 4000, 8000, 16000, 22050, 44100
- Results (format = {fmin}):
  - MCD 0.003: 44100
  - MCD 0.364: 22050
  - MCD 0.707: 16000
  - MCD 5.505: 8000
  - MCD 7.207: 2000
  - MCD 7.279: 100
  - MCD 7.653: 4000
  - MCD 7.655: 500
  - MCD 7.751: 0
  - MCD 8.879: 1000

## Experiment - Maximum frequency

- Changed parameter(s): sample_rate=192000
- Experimented parameter(s):
  - fmax = 4000, 8000, 11025, 16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000
- Results (format = {fmax}):
  - MCD 6.419: 4000
  - MCD 6.712: 11025
  - MCD 6.714: 8000
  - MCD 7.247: 88200
  - MCD 7.538: 16000
  - MCD 7.544: 44100
  - MCD 7.648: 32000
  - MCD 7.791: 24000
  - MCD 7.817: 48000
  - MCD 10.689: 96000
  - MCD 12.241: 22050

## Experiment - Number of mel filterbanks

- Changed parameter(s): D=10
- Experimented parameter(s):
  - M = 10, 11, 12, 13, 20, 30, 40, 50, 60, 70, 80
- Results (format = {M}):
  - MCD 3.208: 10
  - MCD 3.855: 12
  - MCD 4.070: 11
  - MCD 4.286: 13
  - MCD 7.134: 20
  - MCD 10.690: 30
  - MCD 14.422: 40
  - MCD 18.115: 50
  - MCD 21.497: 60
  - MCD 25.773: 70
  - MCD 28.938: 80

## Experiment - Starting index

- Experimented parameter(s):
  - s = 0, 1, 2, 3, 4, 5, 6, 7, 8
- Results (format = {s}):
  - MCD 1.037: 8
  - MCD 1.466: 7
  - MCD 1.952: 6
  - MCD 2.474: 5
  - MCD 3.088: 4
  - MCD 3.569: 3
  - MCD 4.231: 2
  - MCD 5.382: 1
  - MCD 6.333: 0

## Experiment - Number of MFCC coefficients (M=80)

- Changed parameter(s): M=80
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 30, 40, 50, 60, 70, 80
- Results (format = {D}):
  - MCD 8.880: 2
  - MCD 15.749: 3
  - MCD 20.117: 4
  - MCD 23.043: 5
  - MCD 24.963: 6
  - MCD 26.421: 7
  - MCD 27.368: 8
  - MCD 28.263: 9
  - MCD 28.938: 10
  - MCD 29.717: 11
  - MCD 30.211: 12
  - MCD 30.716: 13
  - MCD 31.102: 14
  - MCD 31.560: 15
  - MCD 31.931: 16
  - MCD 32.305: 17
  - MCD 32.646: 18
  - MCD 32.916: 19
  - MCD 35.702: 30
  - MCD 38.261: 40
  - MCD 40.395: 50
  - MCD 41.531: 60
  - MCD 42.038: 70
  - MCD 42.352: 80

## Experiment - Number of MFCC coefficients (M=40)

- Changed parameter(s): M=40
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 25, 30, 35, 40
- Results (format = {D}):
  - MCD 4.515: 2
  - MCD 7.781: 3
  - MCD 9.731: 4
  - MCD 11.321: 5
  - MCD 12.449: 6
  - MCD 13.181: 7
  - MCD 13.646: 8
  - MCD 14.087: 9
  - MCD 14.422: 10
  - MCD 14.759: 11
  - MCD 15.033: 12
  - MCD 15.261: 13
  - MCD 15.460: 14
  - MCD 15.685: 15
  - MCD 15.875: 16
  - MCD 16.010: 17
  - MCD 16.164: 18
  - MCD 16.311: 19
  - MCD 17.093: 25
  - MCD 17.594: 30
  - MCD 18.017: 35
  - MCD 18.289: 40

## Experiment - Number of MFCC coefficients (M=20)

- Changed parameter(s): M=20
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
- Results (format = {D}):
  - MCD 2.278: 2
  - MCD 3.853: 3
  - MCD 4.752: 4
  - MCD 5.565: 5
  - MCD 6.092: 6
  - MCD 6.530: 7
  - MCD 6.795: 8
  - MCD 6.941: 9
  - MCD 7.134: 10
  - MCD 7.272: 11
  - MCD 7.382: 12
  - MCD 7.455: 13
  - MCD 7.580: 14
  - MCD 7.702: 15
  - MCD 7.751: 16
  - MCD 7.798: 17
  - MCD 7.923: 18
  - MCD 8.015: 19, 20

## Experiment - Number of MFCC coefficients (M=10)

- Changed parameter(s): M=10
- Experimented parameter(s):
  - D = 2, 3, 4, 5, 6, 7, 8, 9, 10
- Results (format = {D}):
  - MCD 1.157: 2
  - MCD 2.022: 3
  - MCD 2.438: 4
  - MCD 2.687: 5
  - MCD 2.816: 6
  - MCD 2.988: 7
  - MCD 3.126: 8
  - MCD 3.208: 10, 9

## Experiment - Number of MFCC coefficients (M=5)

- Changed parameter(s): M=5
- Experimented parameter(s):
  - D = 2, 3, 4, 5
- Results (format = {D}):
  - MCD 0.689: 2
  - MCD 1.164: 3
  - MCD 1.366: 4, 5

## Experiment - Silence removal

- Experimented parameter(s):
  - remove_silence = mel, no
  - silence_threshold_A = -4, -3.5, -3, None
  - silence_threshold_B = -4.5, -4, -3.5, None
- Results (format = {remove_silence:silence_threshold_A:silence_threshold_B}):
  - MCD 7.434: mel:-3:-3.5
  - MCD 7.453: mel:-3.5:-4
  - MCD 7.500: mel:-4:-4.5
  - MCD 7.751: no:None:None

## Experiment - Normalize audio

- Experimented parameter(s):
  - norm_audio = False, True
- Results (format = {norm_audio}):
  - MCD 7.751: True
  - MCD 7.963: False

## Experiment - Alignment method

- Experimented parameter(s):
  - align_method = dtw, pad
  - align_target = mel, mfcc, spec
- Results (format = {align_method:align_target}):
  - MCD 7.751: dtw:mfcc
  - MCD 7.922: dtw:mel
  - MCD 8.553: dtw:spec
  - MCD 15.028: pad:mel, pad:mfcc, pad:spec

## Experiment - Sakoe-Chiba radius

- Experimented parameter(s):
  - dtw_radius = 1, 2, 3, 10, 20, None, 40
- Results (format = {dtw_radius}):
  - MCD 7.751: 10, 2, 20, 3, 40, None
  - MCD 7.752: 1

## Experiment - Window function

- Experimented parameter(s):
  - window = hamming, hanning
- Results (format = {window}):
  - MCD 6.749: hamming
  - MCD 7.751: hanning

## Experiment - FFT window length

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {n_fft}):
  - MCD 5.831: 1024
  - MCD 5.863: 512
  - MCD 6.024: 256
  - MCD 7.751: 128
  - MCD 8.453: 64
  - MCD 8.661: 32
  - MCD 9.198: 8
  - MCD 9.233: 16

## Experiment - Window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len}):
  - MCD 5.097: 8
  - MCD 5.252: 16
  - MCD 5.466: 32
  - MCD 5.924: 64
  - MCD 7.673: 1024
  - MCD 7.689: 512
  - MCD 7.721: 256
  - MCD 7.751: 128

## Experiment - Hop length

- Experimented parameter(s):
  - hop_len = 8, 16, 32, 64, 128
- Results (format = {hop_len}):
  - MCD 7.266: 8
  - MCD 7.440: 16
  - MCD 7.751: 32
  - MCD 8.424: 64
  - MCD 9.568: 128

## Experiment - Equal FFT window length and window length

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
- Results (format = {win_len:n_fft}):
  - MCD 4.551: 1024:1024
  - MCD 5.699: 512:512
  - MCD 6.892: 256:256
  - MCD 7.751: 128:128
  - MCD 8.483: 64:64
  - MCD 8.703: 32:32
  - MCD 9.256: 8:8
  - MCD 9.293: 16:16

## Experiment - FFT window length, window length and hop length with ratio 4:4:1

- Experimented parameter(s):
  - win_len = 8, 16, 32, 64, 128, 256, 512, 1024
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {win_len:n_fft:hop_len}):
  - MCD 5.245: 1024:1024:256
  - MCD 6.406: 512:512:128
  - MCD 7.293: 256:256:64
  - MCD 7.751: 128:128:32
  - MCD 8.100: 64:64:16
  - MCD 8.120: 32:32:8
  - MCD 8.481: 8:8:2
  - MCD 8.653: 16:16:4

## Experiment - FFT window length, window length and hop length with ratio 9:3:1

- Experimented parameter(s):
  - n_fft = 16, 32, 64, 128, 256, 512, 1024
  - win_len = 5, 10, 21, 42, 85, 170, 341
  - hop_len = 1, 3, 7, 14, 28, 56, 113
- Results (format = {n_fft:win_len:hop_len}):
  - MCD 4.359: 16:5:1
  - MCD 4.539: 32:10:3
  - MCD 4.825: 64:21:7
  - MCD 5.216: 128:42:14
  - MCD 5.729: 256:85:28
  - MCD 6.318: 512:170:56
  - MCD 6.649: 1024:341:113

## Experiment - FFT window length, window length and hop length with ratio 4:2:1

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 64, 128, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 64, 128, 256, 512
  - hop_len = 2, 4, 8, 16, 32, 64, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - MCD 4.731: 8:4:2
  - MCD 4.743: 16:8:4
  - MCD 4.946: 32:16:8
  - MCD 5.344: 64:32:16
  - MCD 5.924: 128:64:32
  - MCD 6.623: 256:128:64
  - MCD 7.102: 512:256:128
  - MCD 7.229: 1024:512:256

## Experiment - FFT window length, window length and hop length with different ratios

- Experimented parameter(s):
  - n_fft = 8, 16, 32, 46.44, 64, 85.33, 100, 120, 128, 170.67, 256, 512, 1024
  - win_len = 4, 8, 16, 32, 46.44, 50, 60, 64, 85.33, 100, 120, 128, 170.67, 256, 512
  - hop_len = 2, 4, 8, 11.61, 16, 21.33, 25, 30, 32, 42.67, 48, 50, 60, 64, 85.33, 128, 256
- Results (format = {n_fft:win_len:hop_len}):
  - MCD 4.731: 8:4:2
  - MCD 4.918: 128:32:8
  - MCD 4.946: 32:16:8
  - MCD 5.111: 64:32:8
  - MCD 5.126: 256:64:8
  - MCD 5.319: 128:64:8
  - MCD 5.344: 64:32:16
  - MCD 5.427: 256:128:8
  - MCD 5.563: 128:64:16
  - MCD 5.665: 256:128:16
  - MCD 5.688: 100:50:25
  - MCD 5.801: 512:256:32
  - MCD 5.861: 120:60:30
  - MCD 5.924: 128:64:32
  - MCD 6.024: 256:128:32
  - MCD 6.406: 512:512:128
  - MCD 6.892: 256:256:32
  - MCD 7.229: 1024:512:256
  - MCD 7.440: 128:128:16
  - MCD 7.611: 46.44:46.44:11.61
  - MCD 7.616: 120:120:30
  - MCD 7.686: 170.67:170.67:42.67
  - MCD 7.721: 128:256:32
  - MCD 7.751: 128:128:32
  - MCD 7.895: 64:64:8
  - MCD 7.900: 85.33:85.33:21.33
  - MCD 7.979: 100:100:25
  - MCD 8.120: 32:32:8
  - MCD 8.280: 120:120:60
  - MCD 8.387: 85.33:85.33:42.67
  - MCD 8.397: 128:256:64
  - MCD 8.404: 170.67:170.67:85.33
  - MCD 8.424: 128:128:64
  - MCD 8.481: 8:8:2
  - MCD 8.483: 64:64:32
  - MCD 8.522: 100:100:50
  - MCD 8.595: 8:8:4
  - MCD 8.653: 16:16:4
  - MCD 8.779: 16:16:8
  - MCD 8.831: 64:64:48

## Experiment - Finding optimal Pearson parameters (baseline)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = True
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - MCD 5.773: 128:64:16:12:mel:True

## Experiment - Finding optimal Pearson parameters (norm=False)

- Experimented parameter(s):
  - n_fft = 128
  - win_len = 64
  - hop_len = 16
  - D = 12
  - align_target = mel
  - norm_audio = False
- Results (format = {n_fft:win_len:hop_len:D:align_target:norm_audio}):
  - MCD 5.804: 128:64:16:12:mel:False

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
  - MCD 5.771: 128:64:16:12:mel:True:4
  - MCD 5.772: 128:64:16:12:mel:True:3
  - MCD 5.773: 128:64:16:12:mel:True:10
  - MCD 5.774: 128:64:16:12:mel:True:2
  - MCD 5.780: 128:64:16:12:mel:True:1

## Experiment - Finding optimal Spearman parameters (baseline)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 10
  - M = 11
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - MCD 2.872: 64:32:16:10:11:mel

## Experiment - Finding optimal Spearman parameters (D, M)

- Experimented parameter(s):
  - n_fft = 64
  - win_len = 32
  - hop_len = 16
  - D = 12, 13
  - M = 20
  - align_target = mel
- Results (format = {n_fft:win_len:hop_len:D:M:align_target}):
  - MCD 5.545: 64:32:16:12:20:mel
  - MCD 5.605: 64:32:16:13:20:mel

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
  - MCD 5.634: 64:32:16:13:20:mel:False

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
  - MCD 5.604: 64:32:16:13:20:mel:3
  - MCD 5.605: 64:32:16:13:20:mel:10, 64:32:16:13:20:mel:2, 64:32:16:13:20:mel:4
  - MCD 5.618: 64:32:16:13:20:mel:1
