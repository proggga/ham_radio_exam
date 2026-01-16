id: 202301011205
title: "Measurements"
tags: ["electricity", "formulas", "math", "modes", "safety", "transmission-lines"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29

aliases: ["Metingen", "Meetinstrumenten"]

# Measurements

Accurate measurement is essential for testing equipment, verifying compliance, and troubleshooting.

## 1. Basic Parameters (Voltage, Current, Resistance)
*   **Instrument:** [Multimeters](../08_measurements/01_Multimeters.md).
*   **[Key](../04_receivers/07_Station_Accessories.md) Concepts:**
    *   **[Loading Effect](../08_measurements/02_Measurement_Errors.md)**: A voltmeter with low impedance loads the circuit, giving a reading *lower* than the actual voltage.
    *   **AC Measurements:** Standard meters measure **Average** value but are calibrated for **RMS** (Sine wave).
        *   *[Exam](../12_regulations/05_Licensing_in_the_Netherlands.md) Trap:* For non-sine waves (square, triangle), the reading is incorrect. See [Measurement Errors](../08_measurements/02_Measurement_Errors.md).
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
*   **Transmitter Load:** [Dummy Load](../06_antennas/15_Dummy_Load.md). Non-radiating $50 \Omega$ load.
*   **Power:** Measured with an RF Power Meter or derived from Voltage ($P = U^2/R$) on a scope/dummy load.
    *   **PEP Measurement:** Requires a Peak-Reading meter (capacitor hold) or Oscilloscope.

---
[< Back to Section Index](README.md)