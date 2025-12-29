# Circuits and Kirchhoff's Laws

## 1. Kirchhoff's Laws

### First Law: Current Law (KCL)
**"The sum of currents flowing into a node equals the sum of currents flowing out."**
*   $\Sigma I_{in} = \Sigma I_{out}$
*   Based on conservation of charge.
*   *Application:* Used in [Parallel Circuits](#3-parallel-circuits).

### Second Law: Voltage Law (KVL)
**"The sum of all voltage rises and drops in a closed loop is zero."**
*   $\Sigma U = 0$
*   Applied: Source Voltage = Sum of Voltage Drops across components.
*   *Note:* Voltage drops are determined by [Ohm's Law](02_ohm_law.md) ($U = I \times R$).
*   *Application:* Used in [Series Circuits](#2-series-circuits).

## 2. Series Circuits
Components arranged in a chain.
*   **Current ($I$):** Same through all components.
*   **Voltage ($U$):** Divides across components ($U_{total} = U_1 + U_2 + \dots$).
*   **Total Resistance ($R_{tot}$):**
    $$R_{tot} = R_1 + R_2 + R_3 + \dots$$
    *   $R_{tot}$ is always **larger** than the largest individual resistor.

## 3. Parallel Circuits
Components arranged side-by-side (ladder rungs).
*   **Voltage ($U$):** Same across all components.
*   **Current ($I$):** Divides among branches ($I_{total} = I_1 + I_2 + \dots$).
*   **Total Resistance ($R_{tot}$):**
    $$\frac{1}{R_{tot}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots$$
    *   $R_{tot}$ is always **smaller** than the smallest individual resistor.

### Special Cases for Parallel
*   **Two Resistors:**
    $$R_{tot} = \frac{R_1 \cdot R_2}{R_1 + R_2} \quad (\frac{\text{Product}}{\text{Sum}})$$
*   **$N$ Equal Resistors ($R$):**
    $$R_{tot} = \frac{R}{N}$$

## 4. Voltage Dividers
A series circuit used to tap off a lower voltage.
Two resistors $R_1$ and $R_2$ in series connected to source $U_{in}$. Output voltage $U_{out}$ taken across $R_2$.

$$U_{out} = U_{in} \times \frac{R_2}{R_1 + R_2}$$

*   **Potentiometer:** A variable voltage divider.

---
[Back to Index](../INDEX.md) | [Back to Dashboard](../../README.md)
