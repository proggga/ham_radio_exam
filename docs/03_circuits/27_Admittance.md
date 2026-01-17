# Admittance ($Y$)

**Admittance** is the measure of how easily a circuit or device will allow a current to flow. It is the reciprocal (inverse) of [Impedance](../01_electricity/22_Impedance.md) ($Z$).

## Definition
*   **Symbol**: $Y$
*   **Unit**: **Siemens** (S) or Mho ($\mho$).
*   **Formula**:
    $$Y = \frac{1}{Z}$$

Just as Impedance is a complex combination of Resistance and Reactance, Admittance is a complex combination of **Conductance** and **Susceptance**.

$$Y = G + jB$$

Where:
*   **$G$** = [Conductance](../01_electricity/08_Conductance.md) (Real part, inverse of Resistance $R$ in parallel circuits)
*   **$B$** = **Susceptance** (Imaginary part, inverse of Reactance $X$ in parallel circuits)

## Susceptance ($B$)
**Susceptance** is the reciprocal of [Reactance](../02_components/07_Reactance.md) ($X$). It represents the ease with which an AC current passes through a capacitor or inductor.
*   **Unit**: Siemens (S).
*   **Formula**: $B = 1/X$ (Note: Sign changes may apply depending on convention).

## Applications
Admittance is primarily used when analyzing **[Parallel Circuits](../01_electricity/17_Parallel_Circuits.md)**.
*   In series circuits, Impedances add up: $Z_{tot} = Z_1 + Z_2$.
*   In parallel circuits, Admittances add up: $Y_{tot} = Y_1 + Y_2$.
    *   This makes calculation much simpler than using the complex impedance parallel formula ($1/Z_{tot} = 1/Z_1 + \dots$).

## Smith Chart
On the [Smith Chart](../06_antennas/25_Smith_Chart.md), Admittance is often used for matching stubs in parallel with the transmission line. The chart can be "rotated" to convert Impedance coordinates to Admittance coordinates.

---
[< Back to Section Index](README.md)