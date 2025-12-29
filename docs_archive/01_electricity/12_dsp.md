# Digital Signal Processing (DSP)

## 1. Digitization
Converting analogue signals to digital data.
*   **ADC:** Analogue-to-Digital Converter.
*   **DAC:** Digital-to-Analogue Converter.

## 2. Sampling
Taking snapshots of the signal voltage at regular intervals.
*   **Nyquist-Shannon Theorem:** Sample rate must be at least **twice** the highest frequency component of the signal ($f_s > 2 \cdot f_{max}$).
*   **Aliasing:** If sampling is too slow, high frequencies appear as false low frequencies.
    *   **Solution:** **Anti-Aliasing Filter** (Low Pass) before the ADC. See [Filters](../03_circuits/03_filters.md).

## 3. Quantisation
Assigning a discrete digital value to each sample.
*   **Bit Depth:** Number of bits per sample determines resolution. See [Digital Components](../02_components/07_digital_components.md).
*   **Quantisation Noise:** The error between the actual analog value and the digital step.

## 4. Processing
*   **DDS (Direct Digital Synthesis):** Generating waveforms (Sine, etc.) using a lookup table and DAC. Precise frequency control.
*   **FFT (Fast Fourier Transform):** Converting Time-domain data to Frequency-domain data (Spectrum Scope).
*   **Digital Filters:**
    *   **FIR (Finite Impulse Response):** Stable, linear phase.
    *   **IIR (Infinite Impulse Response):** Uses feedback, mimics analog filters.

---
[Back to Index](../INDEX.md) | [Back to Dashboard](../../README.md)
