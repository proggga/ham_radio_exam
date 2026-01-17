# Measurements

Accurate measurement is essential for testing equipment, verifying compliance, and troubleshooting.

## 1. Basic Parameters (Voltage, Current, Resistance)
*   **Instrument:** [Multimeters](../08_measurements/01_Multimeters.md).
*   **[Key](../04_receivers/11_Station_Accessories.md) Concepts:**
    *   **[Loading Effect](../08_measurements/02_Measurement_Errors.md)**: A voltmeter with low impedance loads the circuit, giving a reading *lower* than the actual voltage.
    *   **AC Measurements:** Standard meters measure **Average** value but are calibrated for **RMS** (Sine wave).
        *   *[Exam](../12_regulations/05_Licensing_in_the_Netherlands.md) Trap:* For non-sine waves (square, triangle), the reading is incorrect. See [Measurement Errors](../08_measurements/02_Measurement_Errors.md).
        *   *Rectified Sine:* Meter reads Average ($\approx 0.637 \times Peak$).

## 2. Signal Visualization
*   **Time Domain:** [Oscilloscope](44_Oscilloscope.md). Shows Voltage vs Time.
    *   Used for: Waveform shape, Amplitude ($U_{pp}$), Period ($T$).
*   **Frequency Domain:** [Spectrum Analyzer](45_Spectrum_Analyzer.md). Shows Amplitude vs Frequency.
    *   Used for: Harmonics, [Bandwidth](../03_circuits/07_Bandwidth.md), Spurious emissions.

## 3. Radio Frequency (RF) Measurements
*   **Frequency:** [Frequency Counter](../08_measurements/07_Frequency_Counter.md). Measures precise frequency.
    *   *Accuracy:* Depends on the internal timebase (Crystal/OCXO).
*   **[Resonance](../03_circuits/05_Resonance.md):** [Dip Meter](../08_measurements/06_Dip_Meter.md). Finds resonant frequency of unpowered LC circuits.
*   **Signal Injection:** [Signal Generator](../08_measurements/08_Signal_Generator.md). Produces stable RF signals for receiver testing.
    *   *Critical Feature:* Calibrated Attenuator for sensitivity measurements.

## 4. Transmission & Antenna
*   **[Impedance](22_Impedance.md) Matching:** [SWR Meter](../08_measurements/05_SWR_Meter.md). Measures [Standing Wave Ratio](../06_antennas/24_Standing_Wave_Ratio_SWR.md).
*   **Transmitter Load:** [Dummy Load](../06_antennas/15_Dummy_Load.md). Non-radiating $50 \Omega$ load.
*   **Power:** Measured with an RF Power Meter or derived from Voltage ($P = U^2/R$) on a scope/dummy load.
    *   **[PEP](33_Analogue_Modulation_&_AM.md) Measurement:** Requires a Peak-Reading meter (capacitor hold) or [Oscilloscope](44_Oscilloscope.md).

---
[< Back to Section Index](README.md)