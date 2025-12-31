---
id: 202301011211
title: "Map: Digital Signal Processing (DSP)"
tags:
  - ham-radio
  - dsp
  - map
created: 2025-12-29
type: index
modified: 2025-12-29
---

# Digital Signal Processing (DSP)

DSP involves processing signals in the digital domain (as numbers) rather than using analog components (R, L, C).

## Sampling (Bemonstering)
*   **[[Digital Processing Techniques|ADC]] (Analog-to-Digital Converter)**: Measures the analog voltage at regular intervals.
*   **[[Sampling Theory|Sampling]] Rate ($f_s$)**: How many samples per second.
*   **Nyquist-Shannon Theorem**: To accurately reconstruct a signal, the sampling rate must be **at least twice** the highest frequency in the signal.
    *   $f_s \ge 2 \times f_{max}$.
*   **Aliasing**: If $f_{signal} > f_s / 2$, the signal is "folded back" and appears as a lower, false frequency (alias).
    *   *Prevention:* Use an **Anti-Aliasing [[Filters & Resonance|Filter]]** (Low Pass) before the ADC to block frequencies $> f_s / 2$.

## Quantization
*   **Resolution (Bit Depth)**: The number of bits used to represent each sample value.
*   **Quantization [[AC Signals & Noise|Noise]]**: The error between the real analog value and the nearest digital step.
    *   More bits = Less noise, higher [[Receiver Performance|Dynamic Range]]. (~6 [[Decibels & Logarithms|dB]] per bit).

## Digital Filters
*   **FIR (Finite Impulse Response)**:
    *   No feedback. Inherently stable.
    *   Linear phase response (good for data).
*   **IIR (Infinite Impulse Response)**:
    *   Uses feedback. Can be unstable like analog filters.
    *   More efficient (fewer calculations) for steep slopes.

## FFT (Fast Fourier Transform)
*   Converts a signal from **Time Domain** ([[Oscilloscope]] view) to **Frequency Domain** ([[Spectrum Analyzer]] view).
*   Used for filtering, spectral display, and modulation/demodulation.

## DDS (Direct Digital Synthesis)
*   Generating waveforms directly from a digital look-up table (Sine table) and a [[Digital Processing Techniques|DAC]].
*   Very fast frequency switching and high resolution.

## Related
*   **Nyquist-Shannon Theorem**: To accurately reconstruct a signal, the sampling rate must be **at least twice** the highest frequency in the signal.
    *   $f_s \ge 2 \times f_{max}$.
*   **Aliasing**: If $f_{signal} > f_s / 2$, the signal is "folded back" and appears as a lower, false frequency (alias).
    *   *Prevention:* Use an **Anti-Aliasing [[Filters & Resonance|Filter]]** (Low Pass) before the ADC to block frequencies $> f_s / 2$.
*   **FIR (Finite Impulse Response)**:
    *   No feedback. Inherently stable.
    *   Linear phase response (good for data).
*   **IIR (Infinite Impulse Response)**:
    *   Uses feedback. Can be unstable like analog filters.
    *   More efficient (fewer calculations) for steep slopes.
