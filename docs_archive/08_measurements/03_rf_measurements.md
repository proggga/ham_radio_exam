# RF Measurements

## 1. SWR Meter (Staandegolfmeter)
Measures the [Standing Wave Ratio](../06_antennas/04_matching.md) on a transmission line.
*   **Placement:** Between Transmitter and Antenna (or Tuner).
*   **Operation:** Directional couplers sample Forward ($P_{fwd}$) and Reflected ($P_{ref}$) power.
*   **Usage:**
    1.  Select FWD (Forward).
    2.  Key Transmitter (FM/CW).
    3.  Adjust calibration knob to "SET" (Full scale).
    4.  Select REF (Reflected).
    5.  Read SWR value.
*   **Values:** 1:1 is perfect. > 2:1 usually requires attention.

## 2. Frequency Counter
Measures precise frequency.
*   **Operation:** Counts cycles (pulses) within a precise time window (Gate time).
*   **Accuracy:** Depends on the stability of the internal reference oscillator ([Crystal/TCXO/OCXO](../02_components/07_digital_components.md)).
*   **Sensitivity:** Needs sufficient signal level to trigger the counter.

## 3. Dip Meter (Grid Dipper)
A variable oscillator with an external coil. Used to find the resonant frequency of **unpowered** [LC circuits](../03_circuits/03_filters.md).
*   **Operation:**
    1.  Bring the Dip Meter coil close to the circuit under test.
    2.  Tune the Dip Meter frequency.
    3.  At resonance, the external circuit absorbs energy from the Dip Meter.
    4.  The meter needle "dips" (Oscillator amplitude drops).
*   **Uses:** Measuring unknown L or C, Tuning antennas, checking traps.

## 4. Dummy Load (Kunstantenne)
A non-radiating resistive load.
*   **Impedance:** $50 \Omega$ pure [Resistance](../01_electricity/02_ohm_law.md).
*   **Construction:** Carbon resistors (Non-inductive). Wirewound resistors are **unsuitable** due to inductance.
*   **Purpose:** Testing transmitters without causing interference (QRM) on the bands.
*   **Rating:** Must be able to dissipate the transmitter power as heat.

## 5. Signal Generator
Produces stable RF signals for testing receivers.
*   **Features:** Precise frequency, Accurate attenuation (output level), Modulation (AM/FM).

---
[Back to Index](../INDEX.md) | [Back to Dashboard](../../README.md)
