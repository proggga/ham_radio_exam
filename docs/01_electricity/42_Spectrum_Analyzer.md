# Spectrum Analyzer

A Spectrum Analyzer displays signals in the **Frequency Domain**.
*   **X-Axis:** Frequency.
*   **Y-Axis:** Amplitude (usually logarithmic/[dB](../00_basic_skills.md)).

## Architecture
It functions like a scanning superheterodyne receiver.
*   **Local Oscillator**: Sweeps across a frequency range (Ramp generator).
*   **Display**: Shows the output of the detector as the LO sweeps.

## Usage
*   **Harmonics**: Checking a transmitter for spurious emissions or harmonics (required to be -60dBc or similar).
*   **[Bandwidth](../03_circuits/07_Bandwidth.md)**: Measuring the occupied bandwidth of a modulated signal.
*   **[Modulation](31_Modulation_&_Digital_Signals.md)**: Visualizing sidebands ([AM](32_Analogue_Modulation_&_AM.md)/[FM](35_Frequency_Modulation_FM.md)).

## Comparison with Oscilloscope
*   **[Oscilloscope](41_Oscilloscope.md):** Time Domain (Voltage vs Time). Good for waveform shape.
*   **Spectrum Analyzer:** Frequency Domain (Amplitude vs Frequency). Good for harmonic content and spectral purity.

---
[< Back to Section Index](README.md)