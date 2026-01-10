# Measurement Errors (Meetfouten)

Understanding the limitations of your test equipment is crucial for accurate results.

## 1. Influence of Waveform
Most analog AC voltmeters are calibrated to read **RMS** values, but they actually measure the **Average** value (rectified sine).
*   **Sine Wave**: Reading is correct.
*   **Square/Triangle Wave**: Reading is **incorrect** (Systematic Error).
*   *Solution:* Use a "True RMS" meter.

## 2. Influence of Frequency
Every meter has a limited bandwidth.
*   **Multimeters**: typically accurate only for 50/60 Hz mains. At RF frequencies, they read zero or nonsense.
*   **Probes**: Oscilloscope probes have capacitance. At high frequencies, this loads the circuit and distorts the signal.

## 3. Loading Effect (Internal Impedance)
Connecting a meter changes the circuit being measured.
*   **Ideal Voltmeter**: Infinite input impedance ($Z_{in} = \infty$).
*   **Real Voltmeter**: Finite impedance (e.g., $10 M\Omega$ for DMM, $20 k\Omega/V$ for analog).
*   **Effect**: The meter acts as a parallel resistor. If the circuit has high impedance, the voltage drops when you connect the meter.
    *   *Example:* Measuring a 10V drop across a $1 M\Omega$ resistor with a $1 M\Omega$ meter yields 6.6V (Error!).

## 4. Types of Errors
*   **Systematic Error**: Consistent deviation (e.g., calibration drift, zero offset, waveform error). Can be corrected if known.
*   **Random Error**: Unpredictable noise or reading fluctuations. Reduced by averaging multiple measurements.

---
[< Back to Section Index](README.md)