# Multimeters (Universeelmeters)

## 1. Analogue Multimeter (Moving Coil)
Uses a moving coil mechanism (Draaispoelmeter) which deflects a needle proportional to current.
*   **Mechanism:** A coil in a magnetic field rotates when current flows (Lorentz force). Spring provides counter-force.
*   **Measurement Types:**
    *   **Current (DC):** Direct measurement. Shunt [Resistors](../02_components/01_resistors.md) used to extend range.
    *   **Voltage (DC):** Measured as current through a known series resistor.
        *   **Sensitivity:** Expressed in $k\Omega/V$ (e.g., $20 k\Omega/V$). See [Ohm's Law](../01_electricity/02_ohm_law.md).
        *   *Input Resistance:* $R_{in} = Sensitivity \times Range$.
        *   *Loading Effect:* Low input resistance can load the circuit, affecting the measurement.
    *   **Voltage (AC):** Uses a rectifier ([Diode](../02_components/05_semiconductors.md)). Scale is calibrated for Sine waves (Average -> RMS).
    *   **Resistance:** Uses an internal battery. Zero-adjustment required (short probes, set to 0 $\Omega$). Scale is non-linear (logarithmic-like).

## 2. Digital Multimeter (DMM)
Uses an Analog-to-Digital Converter (ADC).
*   **Input Impedance:** Very high (typically $10-11 M\Omega$). Does not load the circuit.
*   **Features:** Auto-ranging, Diode test, Transistor $h_{FE}$, Capacitance.
*   **Accuracy vs Resolution:** High number of digits (resolution) does not guarantee high accuracy.

## 3. Measurement Techniques
*   **Voltage:** Connect **Parallel** to the component.
*   **Current:** Connect **Series** (break the circuit).
    *   *Warning:* Connecting an ammeter in parallel will cause a short circuit!
*   **Resistance:** Connect to component **Isolated** from the circuit (Power OFF).

---
[Back to Index](../INDEX.md) | [Back to Dashboard](../../README.md)
