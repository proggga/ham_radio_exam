# Digital Processing Techniques

Once a signal is digital, mathematical algorithms can manipulate it in ways impossible for analog circuits.

## DDS (Direct Digital Synthesis)
A method for generating waveforms (Sine, Triangle, etc.) mathematically.
*   Uses a **Phase Accumulator** and a **Lookup Table** (Sine table) feeding a DAC.
*   **Advantage**: Extremely precise frequency control and fast switching.

## FFT (Fast Fourier Transform)
An algorithm that converts Time-domain data (Voltage vs Time) into Frequency-domain data (Amplitude vs Frequency).
*   **Application**: Creating the "Spectrum Scope" or Waterfall display on modern transceivers.

## Digital Filters
*   **Convolution**: The mathematical operation used to apply a filter to a signal. It involves multiplying overlapping samples of the signal and the filter kernel (impulse response) and summing the results.
*   **FIR (Finite Impulse Response)**: Inherently stable, linear phase. Good for sharp brick-wall filters.
*   **IIR (Infinite Impulse Response)**: Uses feedback. Mimics behavior of analog filters but can be unstable.

---
[< Back to Section Index](README.md)