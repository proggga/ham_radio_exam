---
id: 202501151315
title: Admittance
tags:
  - ham-radio
  - circuits
  - ac-theory
created: 2026-01-15
type: permanent-note
modified: 2026-01-15
aliases: ["Admittantie", "Y", "Susceptance", "Susceptantie"]
---

# Admittance ($Y$)

**Admittance** is the measure of how easily a circuit or device will allow a current to flow. It is the reciprocal (inverse) of [[Impedance|Impedance]] ($Z$).

## Definition
*   **Symbol**: $Y$
*   **Unit**: **Siemens** (S) or Mho ($\mho$).
*   **Formula**:
    $$Y = \frac{1}{Z}$$

Just as Impedance is a complex combination of Resistance and Reactance, Admittance is a complex combination of **Conductance** and **Susceptance**.

$$Y = G + jB$$

Where:
*   **$G$** = [[Conductance]] (Real part, inverse of Resistance $R$ in parallel circuits)
*   **$B$** = **Susceptance** (Imaginary part, inverse of Reactance $X$ in parallel circuits)

## Susceptance ($B$)
**Susceptance** is the reciprocal of [[Reactance|Reactance]] ($X$). It represents the ease with which an AC current passes through a capacitor or inductor.
*   **Unit**: Siemens (S).
*   **Formula**: $B = 1/X$ (Note: Sign changes may apply depending on convention).

## Applications
Admittance is primarily used when analyzing **[[Parallel Circuits]]**.
*   In series circuits, Impedances add up: $Z_{tot} = Z_1 + Z_2$.
*   In parallel circuits, Admittances add up: $Y_{tot} = Y_1 + Y_2$.
    *   This makes calculation much simpler than using the complex impedance parallel formula ($1/Z_{tot} = 1/Z_1 + \dots$).

## Smith Chart
On the [[Smith Chart]], Admittance is often used for matching stubs in parallel with the transmission line. The chart can be "rotated" to convert Impedance coordinates to Admittance coordinates.

## Related Notes
*   [[Impedance]]
*   [[Conductance]]
*   [[Reactance]]
*   [[Parallel Circuits]]
