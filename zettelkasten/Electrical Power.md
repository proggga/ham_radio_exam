---
id: 202512292170
title: Electrical Power
tags:
  - ham-radio
  - electricity
  - physics
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Electrical Power (Vermogen)

Power is the rate at which electrical energy is transferred or used.

## Definition
*   **Symbol**: $P$
*   **Unit**: Watt ($W$).
    *   $1 \text{ Watt} = 1 \text{ Joule per second} (J/s)$.

## Formulas
Derived from [[Voltage, Current, and Ohm's Law|Ohm's Law]]:

1.  **Fundamental**: $P = U \times I$
    *   (Voltage $\times$ Current)
2.  **Resistive Load (Current known)**: $P = I^2 \times R$
    *   Used to calculate heat loss in cables or resistors.
3.  **Resistive Load (Voltage known)**: $P = \frac{U^2}{R}$
    *   Used to calculate power in a dummy load or speaker.

## Proportionality Rules
For comparing power dissipation in components:

1.  **In Series ($I$ is constant):**
    *   $P \propto R$ (Power is proportional to Resistance).
    *   A $200\Omega$ resistor dissipates **2x** the power of a $100\Omega$ resistor in series.

2.  **In Parallel ($U$ is constant):**
    *   $P \propto \frac{1}{R}$ (Power is inversely proportional to Resistance).
    *   A $100\Omega$ resistor dissipates **2x** the power of a $200\Omega$ resistor in parallel.

3.  **Changing State:**
    *   If Voltage doubles ($2x$), Power quadruples ($4x$) ($P = U^2/R$).
    *   If Current doubles ($2x$), Power quadruples ($4x$) ($P = I^2R$).

## Related Notes
*   [[Electrical Energy]]
*   [[Electrical Dissipation]]
*   [[Voltage, Current, and Ohm's Law]]
