# Digital Signal Processing (DSP)

DSP involves processing signals in the digital domain (as numbers) rather than using analog components (R, L, C).

## Sampling (Bemonstering)
*   **ADC (Analog-to-Digital Converter)**: Measures the analog voltage at regular intervals.
*   **Sampling Rate ($f_s$)**: How many samples per second.
*   **Nyquist-Shannon Theorem**: To accurately reconstruct a signal, the sampling rate must be **at least twice** the highest frequency in the signal.
    *   $f_s \ge 2 \times f_{max}$.
*   **Aliasing**: If $f_{signal} > f_s / 2$, the signal is "folded back" and appears as a lower, false frequency (alias).
    *   *Prevention:* Use an **Anti-Aliasing [Filter](../03_circuits/03_Filters_&_Resonance.md)** (Low Pass) before the ADC to block frequencies $> f_s / 2$.

## Quantization
*   **Resolution (Bit Depth)**: The number of bits used to represent each sample value.
*   **Quantization [Noise](26_AC_Signals_&_Noise.md)**: The error between the real analog value and the nearest digital step.
    *   More bits = Less noise, higher Dynamic Range. (~6 [dB](../00_basic_skills.md) per bit).

## Digital Filters
*   **FIR (Finite Impulse Response)**:
    *   No feedback. Inherently stable.
    *   Linear phase response (good for data).
*   **IIR (Infinite Impulse Response)**:
    *   Uses feedback. Can be unstable like analog filters.
    *   More efficient (fewer calculations) for steep slopes.

## FFT (Fast Fourier Transform)
*   Converts a signal from **Time Domain** ([Oscilloscope](39_Oscilloscope.md) view) to **Frequency Domain** ([Spectrum Analyzer](40_Spectrum_Analyzer.md) view).
*   Used for filtering, spectral display, and modulation/demodulation.

## DDS (Direct Digital Synthesis)
*   Generating waveforms directly from a digital look-up table (Sine table) and a DAC.
*   Very fast frequency switching and high resolution.

---
[< Back to Section Index](README.md)