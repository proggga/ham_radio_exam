---
id: 202501112055
title: Conductance
tags:
  - ham-radio
  - electricity
  - theory
created: 2026-01-11
type: permanent-note
modified: 2026-01-11
dutch_title: "Geleidbaarheid"
aliases: ["Geleidbaarheid", "G"]
---

# Conductance

**Conductance** ($G$) is a measure of how easily an electrical current flows through a component or circuit. It is the reciprocal (inverse) of [[Voltage, Current, and Ohm's Law|Resistance]] ($R$).

## Definition

*   **Symbol**: $G$
*   **Unit**: **Siemens** (S).
    *   *Old Unit*: **Mho** ($\mho$) - "Ohm" spelled backwards.
*   **Formula**:
    $$G = \frac{1}{R}$$

## Application in Circuits

Conductance is particularly useful when calculating [[Parallel Circuits]]. While resistances in parallel follow a complex formula ($1/R_{tot} = 1/R_1 + \dots$), conductances simply **add up**.

*   **Parallel Formula**:
    $$G_{total} = G_1 + G_2 + G_3 + \dots$$

### Example
Two resistors in parallel: $R_1 = 10 \Omega$, $R_2 = 20 \Omega$.
1.  Calculate Conductances:
    *   $G_1 = 1 / 10 = 0.1 \text{ S}$
    *   $G_2 = 1 / 20 = 0.05 \text{ S}$
2.  Add Conductances:
    *   $G_{total} = 0.1 + 0.05 = 0.15 \text{ S}$
3.  Convert back to Resistance (if needed):
    *   $R_{total} = 1 / 0.15 \approx 6.67 \Omega$

## RF Context
In AC circuits and transmission lines, conductance is the real part of **[[Reactance & Impedance|Admittance]]** ($Y$), representing the resistive loss in the dielectric of a transmission line or capacitor.

## Related Notes
*   [[Voltage, Current, and Ohm's Law]]
*   [[Parallel Circuits]]
*   [[Resistivity (Soortelijke Weerstand)]]
*   [[Reactance & Impedance]]
