---
id: 202512292017
title: Amplifier Coupling
tags: ["ham-radio", "circuits", "amplifiers"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Amplifier Coupling

Coupling methods describe how amplifier stages are connected to each other or to a load.

## Methods
*   **RC Coupling (Resistance-Capacitance)**:
    *   **Components**: Collector/Drain resistor converts current to voltage. [[Capacitors|Capacitor]] ($C_k$) blocks DC. Grid/Base resistor sets bias for next stage.
    *   **Calculation**: The capacitor forms a [[Filters & Resonance|High Pass Filter]] with the input resistance ($R_{in}$) of the next stage.
    *   **Rule of Thumb**: The reactance $X_C$ at the lowest frequency ($f_{min}$) must be less than the input resistance ($R_{in}$).
        *   $X_C < R_{in} \rightarrow \frac{1}{2\pi f C} < R_{in}$
    *   **Application**: Audio amplifiers (requires wide bandwidth).
*   **Transformer Coupling**:
    *   **Components**: Transformer primary is the load.
    *   **Pros**: [[Impedance (Impedantie)|Impedance]] matching ($Z_p/Z_s = n^2$), high efficiency (no DC voltage drop in load resistor).
    *   **Cons**: Heavy, expensive, limited bandwidth. Rare in modern audio, common in RF.
*   **Choke Coupling (Smoorspoel)**:
    *   **Components**: [[Inductors (Spoelen)|Inductor]] (Choke) replaces the load resistor.
    *   **Pros**: Low DC resistance (full $U_b$ at anode/collector), High AC impedance ($\omega L$) increasing with frequency.
    *   **Application**: RF amplifiers. Not for Audio (impedance varies too much with frequency).

## Related
*   [[Filters & Resonance]]
*   [[Transformers]]
