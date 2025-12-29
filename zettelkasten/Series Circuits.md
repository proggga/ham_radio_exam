---
id: 202512292131
title: Series Circuits
tags:
  - ham-radio
  - electricity
  - circuits
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Series Circuits

In a series circuit, components are arranged in a single continuous chain. There is only one path for the current to flow.

## Characteristics

1.  **Current ($I$)**: The current is the **same** through all components.
    *   $I_{total} = I_1 = I_2 = \dots$
2.  **Voltage ($U$)**: The source voltage divides across the components.
    *   $U_{total} = U_1 + U_2 + U_3 + \dots$
    *   The voltage drop across each component is proportional to its resistance (Ohm's Law: $U = I \times R$).
3.  **Resistance ($R$)**: The total resistance is the **sum** of individual resistances.
    *   $R_{tot} = R_1 + R_2 + R_3 + \dots$
    *   **Note**: $R_{tot}$ is always *larger* than the largest individual resistor.

## Failure Mode
If one component in a series circuit opens (fails), the current stops for the entire circuit. This is why "Christmas tree lights" often fail together.

## Applications
- [[Voltage Dividers]] - Used to tap off a specific voltage.
- Fuses are placed in series to protect the circuit.
- Switches are placed in series to control flow.

## Related Notes
- [[Kirchhoff's Laws]] - Specifically KVL.
- [[Parallel Circuits]] - The opposite configuration.
- [[Voltage, Current, and Ohm's Law]]
- [[Resistors]]
