# Voltage Dividers

A voltage divider is a simple linear circuit that produces an output voltage ($U_{out}$) that is a fraction of its input voltage ($U_{in}$).

## Construction
It consists of two resistors ($R_1$ and $R_2$) connected in [Series Circuits](15_Series_Circuits.md).
*   $U_{in}$ is applied across both resistors.
*   $U_{out}$ is taken across $R_2$ (typically the resistor connected to ground).

## Formula
$$U_{out} = U_{in} \times \frac{R_2}{R_1 + R_2}$$

*   If $R_1 = R_2$, then $U_{out} = 0.5 \times U_{in}$ (Halves the voltage).
*   If $R_2$ is much larger than $R_1$, $U_{out} \approx U_{in}$.

## Potentiometer
A **Potentiometer** is a variable resistor with three terminals functioning as an adjustable voltage divider.
*   The wiper moves along the resistive track, changing the ratio of $R_1$ to $R_2$.
*   Used for volume controls, tuning, and calibration.

## Node Potentials (Potentials relative to Ground)
In circuit analysis, voltages are often defined at a specific point (Node) relative to a common reference (Ground, 0V).
*   **Example:** A voltage divider between +4V and -2V.
    *   Total Voltage across resistors = $4V - (-2V) = 6V$.
    *   Calculate current $I = 6V / R_{tot}$.
    *   Calculate voltage drop across the first resistor ($U_1 = I \times R_1$).
    *   Potential at the midpoint = $+4V - U_1$ (or $-2V + U_2$).
*   If resistors are equal, the midpoint potential is the **average** of the two end potentials: $\frac{U_{top} + U_{bottom}}{2}$.

## Loading Effect
Ideally, a voltage divider drives a high-impedance load. If the load has low resistance (draws current), it acts as a parallel resistor to $R_2$, dropping the output voltage further.

---
[< Back to Section Index](README.md)