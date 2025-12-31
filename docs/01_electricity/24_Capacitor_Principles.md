# Capacitor Principles

A capacitor stores electrical energy in an **electric field**.

## Structure
*   **Construction**: Two conductive plates (electrodes) separated by an insulating material called the **dielectric** (diëlektricum).
*   **Symbol**: Two parallel lines.

## Capacitance ($C$)
The ability to store charge.
*   **Unit**: Farad ($F$).
    *   $1 \text{ F} = 1 \text{ [Coulomb](03_Electrical_Charge_Coulomb.md) per Volt} (C/V)$.
    *   Typical values: $\mu F$, $nF$, $pF$.

### Formula
$$C \approx 0.0885 \cdot \varepsilon_r \cdot \frac{A}{d}$$
*(Where C is in pF, A in $cm^2$, d in cm)*

**Factors increasing Capacitance**:
1.  **Larger Plate Area ($A$)**
2.  **Smaller Distance ($d$)** between plates.
3.  **Higher Dielectric Constant ($\varepsilon_r$)** of the insulator.
    *   Vacuum/Air: $\varepsilon_r \approx 1$.
    *   Solids (Plastic, Ceramic): $\varepsilon_r > 1$.
    *   *[Exam](../12_regulations/02_Licensing_in_the_Netherlands.md) Tip:* Inserting a dielectric with $\varepsilon_r = 5$ into an air capacitor increases capacitance by **5x**.

## Variable Capacitors
*   Often specified with a **minimum** and **variation** (swing).
*   *Example:* Min 10pF, Variation 500pF.
    *   Range = 10pF to 510pF (10 + 500).
*   **Parallel Padding:** Adding a fixed capacitor in parallel shifts the entire range up.
    *   +250pF fixed parallel -> Range becomes 260pF to 760pF.

## Temperature Coefficient
*   Unlike resistors (which usually have a specific PTC or NTC behavior), capacitors can have **Positive**, **Negative**, or **Zero** (NP0) temperature coefficients depending on the dielectric.
*   *Exam Tip:* The temperature coefficient of a capacitor can be both positive and negative.

## Circuit Combinations (Opposite of Resistors!)
*   **Parallel:** $C_{tot} = C_1 + C_2 + \dots$ (Capacitance Adds).
    *   *Logic:* Effectively increasing the Plate Area ($A$).
*   **Series:** $\frac{1}{C_{tot}} = \frac{1}{C_1} + \frac{1}{C_2} + \dots$ (Total is smaller than smallest).
    *   *Logic:* Effectively increasing the Distance ($d$).
    *   *Two Caps:* $C_{tot} = \frac{C_1 \cdot C_2}{C_1 + C_2}$.

## Charge Relationship
*   **Formula**: $Q = C \times U$
    *   $Q$ = Charge (Coulombs)
    *   $U$ = Voltage (Volts)

---
[< Back to Section Index](README.md)