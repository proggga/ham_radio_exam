# Digital Signal Processing (DSP)

DSP involves processing signals in the digital domain (as numbers) rather than using analog components (R, L, C).

## Sampling (Bemonstering)
*   **[ADC](40_Digital_Processing_Techniques.md) (Analog-to-Digital Converter)**: Measures the analog voltage at regular intervals.
*   **[Sampling](41_Sampling_Theory.md) Rate ($f_s$)**: How many samples per second.
*   **Nyquist-Shannon Theorem**: To accurately reconstruct a signal, the sampling rate must be **at least twice** the highest frequency in the signal.
    *   $f_s \ge 2 \times f_{max}$.
*   **Aliasing**: If $f_{signal} > f_s / 2$, the signal is "folded back" and appears as a lower, false frequency (alias).
    *   *Prevention:* Use an **Anti-Aliasing [Filter](../03_circuits/03_Filters_&_Resonance.md)** (Low Pass) before the ADC to block frequencies $> f_s / 2$.

## Reconstruction (Digital to Analog)
*   **[DAC](40_Digital_Processing_Techniques.md) (Digital-to-Analog Converter)**: Converts the stream of numbers back into a stepped voltage.
*   **Reconstruction [Filter](../03_circuits/03_Filters_&_Resonance.md)**: A Low Pass Filter placed *after* the DAC.
    *   **Purpose**: Smoothes the "stairsteps" from the DAC output and removes the high-frequency sampling images (harmonics at $f_s, 2f_s$, etc.).

## Quantization
*   **Resolution (Bit Depth)**: The number of bits used to represent each sample value.
*   **Quantization [Noise](26_AC_Signals_&_Noise.md)**: The error between the real analog value and the nearest digital step.
    *   More bits = Less noise, higher [Dynamic Range](../04_receivers/03_Receiver_Performance.md). (~6 [dB](../00_basic_skills.md) per bit).

## Digital Filters
*   **Convolution**: The mathematical operation used to apply filters ([Convolution](42_Convolution.md)).
*   **FIR (Finite Impulse Response)**:
    *   No feedback. Inherently stable.
    *   Linear phase response (good for data).
*   **IIR (Infinite Impulse Response)**:
    *   Uses feedback. Can be unstable like analog filters.
    *   More efficient (fewer calculations) for steep slopes.

### Block Diagrams (Exam Topic)
*   **FIR Structure**: Input signal flows through a series of **Delays** ($Z^{-1}$). Taps are taken after each delay, multiplied by **Coefficients** (weights), and **Summed** to create the output. **No feedback loops.**
*   **IIR Structure**: Similar to FIR but includes **Feedback** loops where previous *outputs* are also delayed, weighted, and summed back into the input stream.

## FFT (Fast Fourier Transform)
*   Converts a signal from **Time Domain** ([Oscilloscope](43_Oscilloscope.md) view) to **Frequency Domain** ([Spectrum Analyzer](44_Spectrum_Analyzer.md) view).
*   Used for filtering, spectral display, and modulation/demodulation.

## DDS (Direct Digital Synthesis)
*   **[Direct Digital Synthesis (DDS)](../03_circuits/25_Direct_Digital_Synthesis_DDS.md)**: Generating waveforms directly from a digital look-up table (Sine table) and a [DAC](40_Digital_Processing_Techniques.md).
*   Very fast frequency switching and high resolution.

---
[< Back to Section Index](README.md)