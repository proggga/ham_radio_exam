---
id: 202512302360
title: Spectrum Analyzer
tags: ["ham-radio", "measurements", "equipment"]
created: 2025-12-30
type: permanent-note
modified: 2025-12-30
---

# Spectrum Analyzer

A Spectrum Analyzer displays signals in the **Frequency Domain**.
*   **X-Axis:** Frequency.
*   **Y-Axis:** Amplitude (usually logarithmic/dB).

## Architecture
It functions like a scanning superheterodyne receiver.
*   **Local Oscillator**: Sweeps across a frequency range (Ramp generator).
*   **Display**: Shows the output of the detector as the LO sweeps.

## Usage
*   **Harmonics**: Checking a transmitter for spurious emissions or harmonics (required to be -60dBc or similar).
*   **Bandwidth**: Measuring the occupied bandwidth of a modulated signal.
*   **Modulation**: Visualizing sidebands (AM/FM).

## Comparison with Oscilloscope
*   **Oscilloscope:** Time Domain (Voltage vs Time). Good for waveform shape.
*   **Spectrum Analyzer:** Frequency Domain (Amplitude vs Frequency). Good for harmonic content and spectral purity.

## Related
*   [[Measurements]]
*   [[Complex Waveforms & Fourier]]
