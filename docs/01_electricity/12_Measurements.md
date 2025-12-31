# Measurements

Accurate measurement is essential for testing equipment, verifying compliance, and troubleshooting.

## 1. Basic Parameters (Voltage, Current, Resistance)
*   **Instrument:** [Multimeters (Universeelmeters)](../08_measurements/01_Multimeters_Universeelmeters.md).
*   **Key Concepts:**
    *   **Loading Effect:** A voltmeter with low impedance loads the circuit, giving a reading *lower* than the actual voltage.
    *   **AC Measurements:** Standard meters measure **Average** value but are calibrated for **RMS** (Sine wave).
        *   *Exam Trap:* For non-sine waves (square, triangle), the reading is incorrect.
        *   *Rectified Sine:* Meter reads Average ($\approx 0.637 \times Peak$).

## 2. Signal Visualization
*   **Time Domain:** [Oscilloscope](39_Oscilloscope.md). Shows Voltage vs Time.
    *   Used for: Waveform shape, Amplitude ($U_{pp}$), Period ($T$).
*   **Frequency Domain:** [Spectrum Analyzer](40_Spectrum_Analyzer.md). Shows Amplitude vs Frequency.
    *   Used for: Harmonics, [Bandwidth](../03_circuits/07_Bandwidth.md), Spurious emissions.

## 3. Radio Frequency (RF) Measurements
*   **Frequency:** [Frequency Counter](../08_measurements/06_Frequency_Counter.md). Measures precise frequency.
    *   *Accuracy:* Depends on the internal timebase (Crystal/OCXO).
*   **[Resonance](../03_circuits/05_Resonance.md):** [Dip Meter](../08_measurements/05_Dip_Meter.md). Finds resonant frequency of unpowered LC circuits.
*   **Signal Injection:** [Signal Generator](../08_measurements/07_Signal_Generator.md). Produces stable RF signals for receiver testing.
    *   *Critical Feature:* Calibrated Attenuator for sensitivity measurements.

## 4. Transmission & Antenna
*   **[Impedance](21_Impedance_Impedantie.md) Matching:** [SWR Meter](../08_measurements/04_SWR_Meter.md). Measures [Standing Wave Ratio](../06_antennas/16_Standing_Wave_Ratio_SWR.md).
*   **Transmitter Load:** [Dummy Load](../06_antennas/08_Dummy_Load.md). Non-radiating $50 \Omega$ load.
*   **Power:** Measured with an RF Power Meter or derived from Voltage ($P = U^2/R$) on a scope/dummy load.
    *   **[PEP](32_Analogue_Modulation_&_AM.md) Measurement:** Requires a Peak-Reading meter (capacitor hold) or [Oscilloscope](39_Oscilloscope.md).

---
[< Back to Section Index](README.md)