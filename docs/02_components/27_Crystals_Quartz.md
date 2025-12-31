# Crystals (Quartz)

Crystals are components made of quartz that vibrate at a precise frequency due to the **Piezoelectric effect**.

## Characteristics
*   **[Resonance](../03_circuits/05_Resonance.md):** A crystal behaves like a resonant circuit with two closely spaced resonance frequencies:
    *   **Series [Resonance](../03_circuits/05_Resonance.md) ($f_s$):** Lower frequency. [Impedance](../01_electricity/21_Impedance_Impedantie.md) is very low (Dip).
    *   **Parallel [Resonance](../03_circuits/05_Resonance.md) ($f_p$):** Higher frequency. [Impedance](../01_electricity/21_Impedance_Impedantie.md) is very high (Peak).
    *   *Caveat:* When scanning frequency from low to high, you see a voltage **dip** (series) followed by a **peak** (parallel).
*   **Equivalent Circuit:** Series L, C, and R, all in parallel with a holder capacitance ($C_p$).
*   **Stability**: Provides very high frequency stability for oscillators and filters compared to LC circuits.
*   **Q-Factor**: Extremely high Q ([Quality Factor](../03_circuits/06_Quality_Factor_Q.md)), resulting in sharp resonance.

## Types
*   **AT-cut**: The standard cut for good temperature stability over a wide range.
*   **TCXO (Temperature Compensated Crystal Oscillator)**: Contains a circuit that compensates for frequency drift due to temperature changes.
*   **OCXO (Oven Controlled Crystal Oscillator)**: The crystal is kept in a heated chamber (oven) at a constant temperature. Highest stability, but consumes more power.

---
[< Back to Section Index](README.md)