---
id: 202301011221
title: "Filters & Resonance"
tags: ["ham-radio", "circuits", "index"]
created: 2025-12-29
type: index
modified: 2025-12-29
---

# Filters & Resonance

This map covers frequency selective circuits.

## Fundamentals
*   **[[Filter Types]]** - LPF, HPF, BPF, Notch.
*   **[[Resonance]]** - Series vs Parallel resonance ( = X_C$).

## Characteristics
*   **[[Quality Factor (Q)]]** - Q factor.
    *   *Caveat:* Adding a parallel resistor (damping) to an LC circuit **lowers** the Q-factor, **increases** the Bandwidth, and **lowers** the impedance/gain.
*   **[[Bandwidth]]** - -3dB bandwidth and selectivity.
## 3. Bandwidth and Selectivity
*   **Bandwidth ($B$):** $B = \frac{f_{res}}{Q}$.
*   **Parallel RLC:**
    *   Lower $R$ (more damping? No, in parallel, Lower R = More Load = Lower Q).
    *   Wait, parallel resistor acts as load. $Q = R_p / X$.
    *   If $R_p$ decreases (more loading), $Q$ decreases, Bandwidth **Increases**.
    *   *Mnemonic (Dutch):* **BeROEP** (Bandbreedte en R Omgekeerd Evenredig bij Parallelkring).
        *   $R$ half $\rightarrow$ $Q$ half $\rightarrow$ Bandwidth double.
*   **Series RLC:**
    *   Higher $R$ (more damping). $Q = X / R_s$.
    *   If $R_s$ increases, $Q$ decreases, Bandwidth **Increases**.
    *   *Mnemonic (Dutch):* **BRES** (Bandbreedte en R Evenredig bij Seriekring).
    *   Relationship: $R \propto B$.

## Advanced
*   **[[High-Performance Filters]]** - Crystal and Mechanical filters.

## 4. Impedance at Resonance
*   **Series LC:** $X_L$ and $X_C$ cancel out ($X_{total} = 0$). Impedance is minimal ($Z = R_{loss}$). Acts as a short circuit.
    *   **Off-Resonance Behavior:**
        *   $f < f_{res}$: **Capacitive** ($X_C > X_L$). Voltage lags current.
        *   $f > f_{res}$: **Inductive** ($X_L > X_C$). Voltage leads current.
*   **Parallel LC:** Currents cancel out. Impedance is maximal ($Z_{res} = L / (C \cdot R_{loss})$ or $Q \cdot X_L$). Acts as an open circuit.
    *   **Off-Resonance Behavior:**
        *   $f < f_{res}$: **Inductive** (behaves like a coil).
        *   $f > f_{res}$: **Capacitive** (behaves like a capacitor).
    *   *Phase Difference:* In a parallel LC circuit, the current through the coil and capacitor are $180^\circ$ out of phase.

## 6. Bandpass Filter Coupling (Coupled Circuits)
When two tuned circuits are coupled (e.g., in an IF transformer), the response changes based on the coupling coefficient ($k$) and Q-factor ($Q$).
*   **Undercritical Coupling ($kQ < 1$):** Single peak, lower amplitude. Narrow bandwidth.
*   **Critical Coupling ($kQ = 1$):** Maximum transfer of energy. Flattest top without a dip.
*   **Overcritical Coupling ($kQ > 1$):** Double peak ("Camel hump" or "Oortjes"). Broader bandwidth but with a dip in the center. Used to widen the passband for FM/Audio.

## Related
*   **[[Reactance & Impedance]]** - Underlying theory.
*   **[[Inductors (Spoelen)]]** - Component.
*   **[[Capacitors]]** - Component.
*   **[[High-Performance Filters]]** - Crystal/Mechanical.
