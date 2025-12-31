---
id: 202512302220
title: Zener Diode
tags: ["ham-radio", "components", "semiconductors", "power-supply"]
created: 2025-12-30
type: permanent-note
modified: 2025-12-30
---

# Zener Diode

A diode designed to operate in the **reverse breakdown** region.

## Operation
*   **Forward Bias**: Acts like a normal diode ($U_F \approx 0.7V$).
*   **Reverse Bias**: Conducts current when the voltage exceeds the **Zener Voltage ($U_Z$)**.
    *   The voltage across the diode remains nearly constant at $U_Z$ over a wide range of currents.

## Mechanisms
1.  **Zener Effect**: (Low voltage, $< 5V$). Quantum tunneling. Negative temperature coefficient (Voltage drops as Temp rises).
2.  **Avalanche Effect**: (High voltage, $> 5V$). Impact ionization. Positive temperature coefficient (Voltage rises as Temp rises).
    *   *Note:* Around 5V, these effects cancel out, making 5V Zeners very temperature stable.

## Application
*   **[[Voltage Regulation]]**: Used as a simple voltage reference or regulator.
*   **Protection**: Used to limit voltage spikes (overvoltage protection).

## Calculations
*   **Series [[Resistors|Resistor]] ($R_s$)**: Required to limit current.
    *   $$R_s = \frac{U_{in} - U_{Z}}{I_{total}}$$
    *   Where $I_{total} = I_{Zener} + I_{Load}$.
*   **Dissipation ($P_Z$)**:
    *   $$P_Z = U_Z \times I_Z$$
    *   Must not exceed the diode's power rating (e.g., 400mW, 1W).

## Related
*   [[Diodes]]
*   [[Power Supply]]
