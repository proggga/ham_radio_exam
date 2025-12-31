---
id: 202301011215
title: "Transformers"
tags: ["ham-radio", "components", "index"]
created: 2025-12-29
type: index
modified: 2025-12-29
---

# Transformers

This map covers transformers and their applications in radio.

## Theory
*   **[[Transformer Principles]]** - Operation, turns ratio, and impedance matching.
*   **[[Transformer Losses]]** - Eddy currents, hysteresis, and copper loss.

### Impedance Transformation
Transformers can match source and load impedances.
*   **Formula**: $Z_{prim} = Z_{sec} \times (\frac{N_{prim}}{N_{sec}})^2$
*   The impedance ratio is the **square** of the turns ratio.
*   *Example*: To match $4 \Omega$ to $400 \Omega$ (ratio 1:100), you need a turns ratio of $\sqrt{100} = 10:1$.
*   *Exam Example*: A transformer has a winding ratio of 1:2 (Primary:Secondary). A $200 \Omega$ resistor is connected to the secondary. What is the impedance seen at the primary?
    *   Ratio $N_p/N_s = 1/2$.
    *   $Z_p = 200 \Omega \times (1/2)^2 = 200 \times 1/4 = 50 \Omega$.

### Shielding
*   **Magnetic [[Shielding (Afscherming)|Shielding]] (Low Freq):** High-permeability materials (Soft Iron, Mu-Metal) **conduct/divert** the magnetic field lines.
*   **RF Shielding (High Freq):** Conductive materials (Aluminium, Copper) create **Eddy Currents** that generate an opposing field, canceling the original field outside the can.
*   **Electrostatic Shielding:** A grounded copper/aluminum foil between windings (Faraday Shield) blocks capacitive coupling of noise.

## Types
*   **[[Special Transformers]]** - Autotransformers and [[Baluns]].

## Related
*   **[[Inductors (Spoelen)]]** - The fundamental component.
*   **[[Power Supply]]** - Major application of transformers.
