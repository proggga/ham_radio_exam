# Oscilloscope

An oscilloscope visualizes electrical signals (Voltage) over Time.

## Basic Structure (Analogue)
*   **Cathode Ray Tube (CRT):** Electron beam draws the trace on a phosphorescent screen.
*   **Vertical Amplifier (Y):** Deflects the beam Up/Down based on Input Voltage.
*   **Horizontal Amplifier (X) / Timebase:** Deflects the beam Left/Right based on Time (Sawtooth wave).
*   **Trigger:** Synchronizes the timebase start with the signal to create a stable image.

## Controls & Reading
*   **Vertical Scale (Volts/Div):** Determines amplitude.
    *   *Reading:* Count divisions peak-to-peak $\times$ Setting.
    *   $U_{pp} = \text{Divisions}_{vert} \times \text{Volts/Div}$.
    *   $U_{peak} = U_{pp} / 2$.
    *   $U_{eff} (RMS) = U_{peak} \times 0.707$ (for Sine wave).
*   **Horizontal Scale (Time/Div):** Determines frequency/period.
    *   *Reading:* Count divisions for one full cycle $\times$ Setting.
    *   $Period (T) = \text{Divisions}_{horiz} \times \text{Time/Div}$.
    *   $Frequency (f) = 1 / T$.

## Probes
*   **Input [Impedance](21_Impedance_Impedantie.md):** Typically $1 M\Omega$ parallel with $\approx 20 pF$.
*   **10:1 Probe:** Attenuates signal by 10x. Increases input impedance to $10 M\Omega$ and lowers capacitance (less loading).
    *   *Note:* Remember to multiply the voltage reading by 10!

## Exam Calculations
**Scenario:** Scope set to 5V/div and 10 $\mu$s/div. Waveform is 4 divisions high and 1 cycle covers 5 divisions.
1.  **Voltage:** $4 \text{ div} \times 5 \text{ V/div} = 20 V_{pp}$.
    *   Amplitude ($U_{max}$) = 10 V.
    *   RMS ($U_{eff}$) = 7.07 V.
2.  **Time:** $5 \text{ div} \times 10 \mu\text{s/div} = 50 \mu\text{s}$.
3.  **Frequency:** $f = 1 / 50 \mu\text{s} = 1 / (50 \times 10^{-6}) = 20,000 \text{ Hz} = 20 \text{ kHz}$.

---
[< Back to Section Index](README.md)