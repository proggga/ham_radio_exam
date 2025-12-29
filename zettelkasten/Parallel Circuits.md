---
id: 202512292132
title: Parallel Circuits
tags:
  - ham-radio
  - electricity
  - circuits
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Parallel Circuits

In a parallel circuit, components are arranged side-by-side like the rungs of a ladder. The current has multiple paths to flow through.

## Characteristics

1.  **Voltage ($U$)**: The voltage is the **same** across all parallel components.
    *   $U_{total} = U_1 = U_2 = \dots$
2.  **Current ($I$)**: The total current splits among the branches.
    *   $I_{total} = I_1 + I_2 + I_3 + \dots$
    *   Current follows the path of least resistance (higher current in lower resistance branches).
3.  **Resistance ($R$)**: Adding resistors in parallel **reduces** the total resistance.
    *   Formula: $\frac{1}{R_{tot}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots$
    *   **Note**: $R_{tot}$ is always *smaller* than the smallest individual resistor.

## Special Calculation Cases

### Two Resistors
$$R_{tot} = \frac{R_1 \cdot R_2}{R_1 + R_2}$$
*(Product over Sum)*

### N Equal Resistors
$$R_{tot} = \frac{R}{N}$$
*(Resistance divided by number of resistors)*

## Applications
- Mains wiring (all outlets are parallel).
- [[Ampere Meter]] shunts.
- Reducing component values (e.g., two $100\Omega$ in parallel = $50\Omega$).

## Related Notes
- [[Kirchhoff's Laws]] - Specifically KCL.
- [[Series Circuits]]
- [[Voltage, Current, and Ohm's Law]]
- [[Conductance]] - The inverse of resistance ($G = 1/R$) adds in parallel.
