# Systematic analysis of parameter combinations to optimize the correlation between MCD/PEN and MOS ratings

To investigate the correlation between Mel-Cepstral Distance (MCD) and Penalty (PEN) with subjective ratings, 230 experiments were conducted. The main objective was to identify how various parameters influence the computation of MCD and PEN and their correlation strength with subjective assessments.

## Utilization of the LJS-MOS-120 dataset

The experiments utilized the [LJS-MOS-120 dataset](https://huggingface.co/datasets/stefantaubert/ljs-mos-120), containing Mean Opinion Scores (MOS) for naturalness and intelligibility of various conditions across 120 sentences from the [LJ-Speech dataset](https://keithito.com/LJ-Speech-Dataset). These conditions include ground-truth and synthesized outputs from two neural text-to-speech (TTS) models. The evaluation was conducted in mid-2022 using [Amazon Mechanical Turk (MTurk)](https://www.mturk.com), involving ratings from six demographic groups divided by gender (male/female) and age (18–29, 30–49, 50+). A total of 33 subjects participated, with only ratings obtained using headphones considered. Participants were required to pass a general qualification test, a language proficiency test  with North American English as their native language, and an auditory test.

## Objectives

### 1. Correlation analysis

Several correlation measures were evaluated to examine the relationship between different parameters and subjective ratings, including Pearson’s correlation coefficient, Spearman’s rank correlation, and Kendall’s tau coefficient. All three coefficients range from -1 to 1, with 1 indicating a perfect positive correlation, -1 a perfect negative correlation, and 0 indicating no correlation.

- **Pearson’s coefficient** quantifies the linear relationship between the objective metric (e.g., MCD) and the subjective ratings (MOS). Since the MOS values are averaged over 12 listeners per utterance, they can be reasonably treated as interval-scaled, allowing Pearson’s r to capture subtle proportional relationships between acoustic distortion and perceived quality. It is sensitive to outliers and assumes homoscedasticity.
- **Spearman’s coefficient** assesses the monotonic relationship between the ranked values of the objective and subjective metrics. It does not assume normal distribution or linearity and is robust to non-linear trends and outliers. This makes it particularly suitable for MOS data, even when aggregated, as it captures consistent ordinal tendencies between metrics and ratings.
- **Kendall’s tau** evaluates the rank concordance by comparing the number of concordant and discordant pairs across samples. It is more conservative than Spearman’s ρ, especially in the presence of tied ranks. Although averaging MOS reduces the number of ties compared to raw Likert scores, Kendall’s tau remains useful for cross-validating monotonic relationships under stricter assumptions.

Spearman’s rank correlation was chosen as the primary measure of association due to its robustness with ordinal-scaled MOS ratings, while Pearson’s coefficient was additionally reported under the assumption of approximately interval-scaled mean scores. Kendall’s tau was included as a supplementary metric for completeness.

Correlations were calculated separately for naturalness and intelligibility, combining IMPL and EXPL conditions and comparing them to the respective MOS values.

### 2. Analysis of optimal objective metrics

Different combinations of MCD and PEN metrics were evaluated:

- `MCD`, `PEN`, `MCD+PEN`, `MCD-PEN`, `MCD*PEN`, `SQRT(MCD²+PEN²)`, `MCD*(PEN-1)`, `MCD*(PEN+0.1)`, `MCD*(PEN+0.25)`, `MCD*(PEN+0.5)`, `MCD*(PEN+1)`, `MCD*(PEN+2)`, `PEN*(MCD+1)`

### 3. Analysis of parameter effects on MCD and PEN values

The impact of varying individual parameters on the numerical values of MCD and PEN was assessed, e.g., analyzing if longer window lengths systematically correspond to higher MCD values.

## Input data

Input audio files from the LJ-Speech dataset had a sampling rate of 22050 Hz. Synthesized spectrograms were generated using Tacotron with the following parameters and subsequently converted to audio files using WaveGlow:

```
sample_rate = 22050 Hz
n_fft = 1024 samples (= 46.44 ms)
win_len = 1024 samples (= 46.44 ms)
hop_len = 256 samples (= 11.61 ms)
window = 'hanning'
fmin = 0 Hz
fmax = 8000 Hz
M = 80
```

## Experimental configuration

Standard experimental configurations were based on the following parameters, upscaled to a sampling rate of 96000 Hz, determined optimal through preliminary tests:

```
sample_rate = 96000 Hz
n_fft = 128 ms
win_len = 128 ms
hop_len = 32 ms
window = 'hanning'
fmin = 0 Hz
fmax = 48000 Hz
M = 20
s = 1
D = 16
align_method = 'dtw'
align_target = 'mfcc'
remove_silence = 'no'
silence_threshold_a = None
silence_threshold_b = None
norm_audio = True
dtw_radius = 10
```

Parameters were individually varied to examine their effect on correlations with subjective ratings.

## Results

Full results are documented in the respective report files (`report.{subjective_metric}.{correlation_measure}.md` and `report.{MCD|PEN}.md`), with [report.naturalness.Spearman.md](https://github.com/stefantaubert/mel-cepstral-distance/blob/main/experiments/report.naturalness.Spearman.md) and [report.MCD.md](https://github.com/stefantaubert/mel-cepstral-distance/blob/main/experiments/report.MCD.md) providing the most informative summaries.

### 1. Correlation analysis

- Moderate negative Spearman correlation of up to -0.31 for naturalness but weak negative correlation for intelligibility (-0.24).
  * Moderate negative Pearson correlation of up to -0.36 for naturalness but weak negative correlation for intelligibility (-0.22). The resulting coefficient suggests a meaningful linear relationship between the objective measure and perceived naturalness.
- Removing pauses reduced correlation.
- Upsampling to 96 kHz improved correlation; higher rates offered no additional benefit.
- Optimal Mel-spectrogram upper frequency limit was half the sampling rate (48 kHz).
- Optimal lower frequency limit was 0 Hz.
- Best Spearman results with 32 ms window length, 64 ms FFT length, and 16 ms hop length.
  * Best Pearson results with 64 ms window length, 128 ms FFT length, and 16 ms hop length.
- Hanning window slightly outperformed Hamming.
- DTW alignment of Mel-spectrograms outperformed linear or MFCC alignment.
  * DTW radius had minor impact, recommended >1.
  * Padding severely degraded correlation.
- 20 Mel bands were optimal.
- Computing first 13 MFCC coefficients was optimal for Spearman correlation.
  * Computing first 12 MFCC coefficients was optimal for Pearson correlation.
- Skipping the first MFCC coefficient (s = 1) improved correlation.

**Best parameter configuration (Spearman):**

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

### 2. Optimal objective metric analysis

- Combination `MCD*(PEN+1)` showed highest average correlation with naturalness ratings across experiments.

### 3. Parameter impact on MCD/PEN

- Increasing Mel bands or MFCC coefficients increased MCD values.
- Smaller FFT windows, longer window lengths, and larger hop lengths generally led to higher MCD values.
