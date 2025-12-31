---
id: 202301011242
title: "RF Measurements"
tags: ["ham-radio", "measurements", "index"]
created: 2025-12-29
type: index
modified: 2025-12-29
---

# RF Measurements

This map covers the instruments used to test and maintain radio equipment.

## Transmitter Testing
*   **[[SWR Meter]]** - Checking antenna match.
*   **[[Dummy Load]]** - Safe non-radiating test load.
*   **Antenna Analyzer** - A handheld instrument that generates a low-power signal to measure [[Standing Wave Ratio (SWR)|SWR]], resistance ($R$), and reactance ($X$) of an antenna system across a range of frequencies without using a transmitter.

## Circuit Analysis
*   **[[Dip Meter]]** - Finding resonance of passive circuits.
*   **[[Frequency Counter]]** - Measuring exact frequency.

## Receiver Testing
*   **[[Signal Generator]]** - Injecting test signals.

### Calculation Example: Power Measurement
**Scenario:** You measure 8 Watts on a power meter. The setup includes an attenuator (10 [[Decibels & Logarithms|dB]]), a disabled amplifier acting as a load (1 dB loss), and cable/connector losses (2 dB). What is the transmitter output power?
1.  **Total Loss/Attenuation:** $10 \text{ dB} + 1 \text{ dB} + 2 \text{ dB} = 13 \text{ dB}$.
2.  **Calculate Factor:** $13 \text{ dB} \approx 20\times$ ($10 \text{ dB} = 10\times$, $3 \text{ dB} = 2\times$, so $10 \times 2 = 20$).
3.  **Calculate Source Power:** $P_{source} = P_{measured} \times \text{Factor} = 8 \text{ W} \times 20 = 160 \text{ W}$.

## Related
*   **[[Multimeters (Universeelmeters)]]** - DC/AC Voltage and Resistance.
    *   *Voltmeter:* Should have **High** impedance to avoid loading the circuit.
    *   *Ammeter:* Should have **Low** impedance.
    *   *AC Measurement:* Standard moving-coil meters measure **Average** value. For sine waves, the scale is calibrated to RMS ($U_{rms} \approx 1.11 \times U_{avg}$). If rectifying a sine wave without a smoothing capacitor, the meter reads average ($2 U_{peak} / \pi$). With a capacitor, it reads peak.
*   **[[Analogue Modulation & AM|PEP]] Measurement:** To measure Peak Envelope Power with a simple meter, a capacitor is needed to hold the peak voltage (time constant ~seconds).
