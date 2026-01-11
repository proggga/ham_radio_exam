# Amplifier Coupling

Coupling methods describe how amplifier stages are connected to each other or to a load.

## Methods
*   **RC Coupling (Resistance-Capacitance)**:
    *   **Components**: Collector/Drain resistor converts current to voltage. [Capacitor](../02_components/05_Capacitors.md) ($C_k$) blocks DC. Grid/Base resistor sets bias for next stage.
    *   **Calculation**: The capacitor forms a [High Pass Filter](03_Filters_&_Resonance.md) with the input resistance ($R_{in}$) of the next stage.
    *   **Rule of Thumb**: The reactance $X_C$ at the lowest frequency ($f_{min}$) must be less than the input resistance ($R_{in}$).
        *   $X_C < R_{in} \rightarrow \frac{1}{2\pi f C} < R_{in}$
    *   **Application**: Audio amplifiers (requires wide bandwidth).
*   **Transformer Coupling**:
    *   **Components**: Transformer primary is the load.
    *   **Pros**: [Impedance](../01_electricity/21_Impedance_Impedantie.md) matching ($Z_p/Z_s = n^2$), high efficiency (no DC voltage drop in load resistor).
    *   **Cons**: Heavy, expensive, limited bandwidth. Rare in modern audio, common in RF.
*   **Choke Coupling (Smoorspoel)**:
    *   **Components**: [Inductor](../02_components/09_Inductors_Spoelen.md) (Choke) replaces the load resistor.
    *   **Pros**: Low DC resistance (full $U_b$ at anode/collector), High AC impedance ($\omega L$) increasing with frequency.
    *   **Application**: RF amplifiers. Not for Audio (impedance varies too much with frequency).

---
[< Back to Section Index](README.md)