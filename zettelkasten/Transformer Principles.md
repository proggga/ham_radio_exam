---
id: 202512292022
title: Transformer Principles
tags: ["ham-radio", "components", "transformers"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Transformer Principles

A transformer transfers electrical energy between two or more circuits through electromagnetic induction. It is used to transform Voltage, Current, and Impedance.

## Operation
*   **Induction**: A changing current in the **Primary Winding** creates a changing magnetic field, which induces a voltage in the **Secondary Winding**.
*   **DC**: Transformers do **not** work with DC (Direct Current) because a steady current creates a static magnetic field.

## Formulas
The transformation depends on the **Turns Ratio** ($\frac{N_{prim}}{N_{sec}}$).

### Voltage & Current
*   **Voltage**: $\frac{U_{sec}}{U_{prim}} = \frac{N_{sec}}{N_{prim}}$
*   **Current**: $\frac{I_{sec}}{I_{prim}} = \frac{N_{prim}}{N_{sec}}$
    *   **Step-up**: More turns on secondary $\rightarrow$ Higher Voltage, Lower Current.
    *   **Step-down**: Fewer turns on secondary $\rightarrow$ Lower Voltage, Higher Current.

### Phasing (Windings in Series)
When connecting two windings (e.g., secondaries) in series, the **Phase** matters (Dot convention).
*   **In Phase (Boosting)**: Voltages add up ($U_{total} = U_1 + U_2$).
*   **Out of Phase (Bucking)**: Voltages subtract ($U_{total} = |U_1 - U_2|$).
    *   *Example*: Connecting a 24V and 18V winding in anti-series results in $24 - 18 = 6V$.

### Impedance Transformation
Transformers can match source and load impedances.
*   **Formula**: $Z_{prim} = Z_{sec} \times (\frac{N_{prim}}{N_{sec}})^2$
*   The impedance ratio is the **square** of the turns ratio.
*   *Example*: To match $4 \Omega$ to $400 \Omega$ (ratio 1:100), you need a turns ratio of $\sqrt{100} = 10:1$.

## Construction
*   **Core**: Directs magnetic flux.
    *   **Laminated Iron**: For Mains/Audio (Low freq). Laminations reduce Eddy Currents (Kernverliezen).
    *   **Ferrite / Powdered Iron**: For RF (High freq). Powdered iron (insulated particles) increases Inductance ($L$) and Quality Factor ($Q$) compared to air, unlike solid iron which would cause high losses.
    *   **Toroid (Ringkern)**: Ring-shaped core with low flux leakage (self-shielding).
*   **Shielding**: Placing a conductive shield (Aluminium/Copper) around a coil reduces its Inductance ($L$) and Quality Factor ($Q$) due to induced eddy currents.

## Related
*   [[Inductors (Spoelen)]]
*   [[Transformer Losses]]
