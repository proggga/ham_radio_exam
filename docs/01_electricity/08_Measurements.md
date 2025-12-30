# Measurements

Accurate measurement is essential for testing equipment, verifying compliance, and troubleshooting.

## 1. Basic Parameters (Voltage, Current, Resistance)
*   **Instrument:** Multimeters (Universeelmeters).
*   **Key Concepts:**
    *   **Loading Effect:** A voltmeter with low impedance loads the circuit, giving a reading *lower* than the actual voltage.
    *   **AC Measurements:** Standard meters measure **Average** value but are calibrated for **RMS** (Sine wave).
        *   *Exam Trap:* For non-sine waves (square, triangle), the reading is incorrect.
        *   *Rectified Sine:* Meter reads Average ($\approx 0.637 \times Peak$).

## 2. Signal Visualization
*   **Time Domain:** Oscilloscope. Shows Voltage vs Time.
    *   Used for: Waveform shape, Amplitude ($U_{pp}$), Period ($T$).
*   **Frequency Domain:** Spectrum Analyzer. Shows Amplitude vs Frequency.
    *   Used for: Harmonics, Bandwidth, Spurious emissions.

## 3. Radio Frequency (RF) Measurements
*   **Frequency:** Frequency Counter. Measures precise frequency.
    *   *Accuracy:* Depends on the internal timebase (Crystal/OCXO).
*   **Resonance:** Dip Meter. Finds resonant frequency of unpowered LC circuits.
*   **Signal Injection:** Signal Generator. Produces stable RF signals for receiver testing.
    *   *Critical Feature:* Calibrated Attenuator for sensitivity measurements.

## 4. Transmission & Antenna
*   **Impedance Matching:** SWR Meter. Measures Standing Wave Ratio.
*   **Transmitter Load:** Dummy Load. Non-radiating $50 \Omega$ load.
*   **Power:** Measured with an RF Power Meter or derived from Voltage ($P = U^2/R$) on a scope/dummy load.
    *   **PEP Measurement:** Requires a Peak-Reading meter (capacitor hold) or Oscilloscope.

---
[< Back to Section Index](README.md)