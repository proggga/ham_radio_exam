---
id: 202301011240
title: "Multimeters (Universeelmeters)"
tags: ["ham-radio", "measurements"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Multimeters (Universeelmeters)

## 1. Analogue Multimeter (Moving Coil)
Uses a moving coil mechanism (Draaispoelmeter) which deflects a needle proportional to current.
*   **Mechanism:** A coil in a magnetic field rotates when current flows (Lorentz force). Spring provides counter-force.
*   **Damping:** To prevent needle overshoot/oscillation.
*   **Protection:** Often has anti-parallel diodes across the meter movement to limit voltage/current during overload.

### Voltage Measurement (DC)
Measured as current through a known series resistor.
*   **Multiplier Formula:** $R_{series} = \frac{U_{range}}{I_{fsd}} - R_{meter}$ (where $I_{fsd}$ is full scale deflection current).
*   **[[Receiver Performance|Sensitivity]] ($S$):** Expressed in $k\Omega/V$ (e.g., $20 k\Omega/V$). $S = 1 / I_{fsd}$.
    *   *Example:* $50 \mu A$ movement $\rightarrow 20 k\Omega/V$.
*   **Input Resistance:** $R_{in} = S \times Range$.
    *   *Example:* On 10V range with $20 k\Omega/V$ sensitivity, $R_{in} = 200 k\Omega$.
*   **Loading Effect (Belastingseffect):**
    *   Ideally, a voltmeter has infinite impedance. Real meters draw current.
    *   If $R_{in}$ is not $\gg$ Circuit [[Impedance (Impedantie)|Impedance]], the meter loads the circuit, reading **lower** than the actual voltage.
    *   *[[Licensing in the Netherlands|Exam]] Tip:* Always check if the meter resistance is comparable to the circuit resistors. If so, calculate the parallel equivalent.

### Current Measurement (DC)
Measured directly or with a shunt.
*   **Ideal:** Zero impedance.
*   **Shunt Formula:** $R_{shunt} = R_{meter} \cdot \frac{I_{meter}}{I_{total} - I_{meter}}$
    *   Most current flows through the shunt (low resistance), small fraction through the meter.

### AC Measurement
Uses a rectifier ([[Semiconductors|Diode]]).
*   **Average vs RMS:** Moving coil meters respond to the **Average** value of the rectified current.
*   **Calibration:** The scale is calibrated to show **RMS** (Effectieve waarde) assuming a **pure Sine wave**.
    *   $U_{rms} \approx 1.11 \times U_{avg}$.
*   **Sensitivity:** AC sensitivity is typically lower than DC sensitivity (e.g., DC $20 k\Omega/V$, AC $9 k\Omega/V$) due to rectifier characteristics.

### Resistance Measurement
Uses an internal battery.
*   **Zero-adjustment:** Short probes, adjust knob for $0 \Omega$ (Full Scale Current).
*   **Scale:** Non-linear (logarithmic-like). $0 \Omega$ is at full scale (right), $\infty$ is at rest (left).

## 2. Digital Multimeter (DMM)
Uses an Analog-to-Digital Converter ([[Digital Processing Techniques|ADC]]).
*   **Input [[Impedance (Impedantie)|Impedance]]:** Very high and constant (typically $10-11 M\Omega$). Does not load the circuit significantly.
*   **Power:** Requires a battery for all measurements (unlike analogue which only needs it for Ohms).
*   **Features:** Auto-ranging, [[Diodes|Diode]] test, [[Transistors (BJT & FET)|Transistor]] $h_{FE}$, Capacitance.

## Related
*   [[Measurements]]
*   [[Voltage, Current, and Ohm's Law]]