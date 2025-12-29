---
id: 202512292027
title: Voltage Regulation
tags: ["ham-radio", "circuits", "power-supply"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Voltage Regulation

Regulation keeps the output voltage constant despite changes in Load Current or Mains Voltage.

## Zener Diode Regulator
*   **Setup**: Zener diode in reverse bias (parallel to load) + Series Resistor.
*   **Operation**: Zener maintains constant breakdown voltage.
*   **Resistor**: $R_{series} = \frac{U_{in} - U_{zener}}{I_{zener} + I_{load}}$
*   **Use**: Low power reference voltages.

## Linear Series Regulator
Uses a transistor to control output voltage.
*   **Operation**: Transistor acts as a variable resistor adjusting voltage drop to maintain constant output.
*   **Dissipation**: Excess power is lost as heat.
    *   $P = (U_{in} - U_{out}) \times I_{load}$

## IC Regulators
Integrated circuits simplifying regulation.
*   **78xx Series**: Positive voltage (e.g., 7812 for +12V).
*   **79xx Series**: Negative voltage (e.g., 7905 for -5V).

## Related
*   [[Semiconductors]]
*   [[Physics Principles]] (Dissipation)
