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
*   **RC Coupling**: A capacitor blocks DC bias voltages but passes AC signal. Resistors set the bias.
    *   *Calculation*: The capacitor forms a [[Filters & Resonance|High Pass Filter]] with the input impedance of the next stage. $X_c$ must be low at the lowest frequency ($f_{min}$).
*   **Transformer Coupling**: Uses a transformer to link stages.
    *   *Pros*: Can match impedance ($Z_p/Z_s = (N_p/N_s)^2$). Efficient.
    *   *Cons*: Heavy, bandwidth limited.
*   **LC/Choke Coupling**: Uses an inductor (choke) as the collector load instead of a resistor.
    *   *Pros*: High efficiency for RF because there is no DC voltage drop (DC voltage at collector $\approx V_{supply}$).
*   **Direct Coupling**: DC connection (no capacitor).
    *   Used in **Op-amps** and DC amplifiers.
    *   Requires careful thermal stabilization as DC drift is amplified.

## Related
*   [[Filters & Resonance]]
*   [[Transformers]]
