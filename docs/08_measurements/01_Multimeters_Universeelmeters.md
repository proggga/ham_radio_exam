# Multimeters (Universeelmeters)

## 1. Analogue Multimeter (Moving Coil)
Uses a moving coil mechanism (Draaispoelmeter) which deflects a needle proportional to current.
*   **Mechanism:** A coil in a magnetic field rotates when current flows (Lorentz force). Spring provides counter-force.
*   **Measurement Types:**
    *   **Current (DC):** Direct measurement. Shunt Resistors used to extend range.
        *   **Shunt Formula:** $R_{shunt} = R_{meter} \cdot \frac{I_{meter}}{I_{total} - I_{meter}}$
    *   **Voltage (DC):** Measured as current through a known series resistor.
        *   **Multiplier Formula:** $R_{series} = \frac{U_{range}}{I_{fsd}} - R_{meter}$ (where $I_{fsd}$ is full scale deflection current).
        *   **Sensitivity:** Expressed in $k\Omega/V$ (e.g., $20 k\Omega/V$). See Ohm's Law.
        *   *Input Resistance:* $R_{in} = Sensitivity \times Range$.
        *   *Loading Effect:* Low input resistance can load the circuit (parallel resistance), causing the measured voltage to be **lower** than the actual voltage.
            *   *Example:* Measuring a high-impedance divider with a low-impedance meter changes the divider ratio.
    *   **Voltage (AC):** Uses a rectifier (Diode). Scale is calibrated for Sine waves (Average -> RMS).
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
[< Back to Section Index](README.md)