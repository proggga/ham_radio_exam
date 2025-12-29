---
id: 202301011203
title: "Resistivity (Soortelijke Weerstand)"
tags: ["ham-radio", "electricity"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Resistivity (Soortelijke Weerstand)

## Factors Affecting Resistance
The resistance of a conductor depends on four factors:
1.  **Material:** Different materials conduct differently (e.g., Copper vs Iron).
2.  **Length ($L$):** Longer wire = Higher resistance.
3.  **Cross-sectional Area ($A$):** Thicker wire = Lower resistance.
4.  **Temperature:** 
    *   **Metals (PTC):** Resistance **increases** as temperature rises.
    *   **Carbon/Semiconductors (NTC):** Resistance **decreases** as temperature rises.

## Specific Resistance Formula
The resistance $R$ of a wire can be calculated using the specific resistance (resistivity) of the material, denoted by the Greek letter Rho ($\rho$).

$$R = \rho \cdot \frac{L}{A}$$

*   $R$ = Resistance in Ohm ($\Omega$)
*   $\rho$ (rho) = Specific resistance in Ohm-meter ($\Omega \cdot m$)
*   $L$ = Length in meters ($m$)
*   $A$ = Cross-sectional area in square meters ($m^2$)

> **Note on Area:** For a round wire, Area $A = \pi \cdot r^2$ or $A = \frac{\pi \cdot d^2}{4}$. 
> Do not confuse Diameter ($d$) with Area ($A$). If diameter doubles, Area quadruples ($2^2=4$), so Resistance becomes $1/4$.

### Stretching a Wire
If you stretch a wire to **2x** its length:
1.  Length $L$ doubles ($2L$).
2.  Area $A$ halves ($0.5A$) (assuming volume stays constant).
3.  New Resistance $R_{new} \propto \frac{2L}{0.5A} = 4 \times \frac{L}{A}$.
    *   **Result:** Resistance becomes **4x** higher.