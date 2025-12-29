---
id: 202512292133
title: Voltage Dividers
tags:
  - ham-radio
  - electricity
  - circuits
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Voltage Dividers

A voltage divider is a simple linear circuit that produces an output voltage ($U_{out}$) that is a fraction of its input voltage ($U_{in}$).

## Construction
It consists of two resistors ($R_1$ and $R_2$) connected in [[Series Circuits]].
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

## Loading Effect
Ideally, a voltage divider drives a high-impedance load. If the load has low resistance (draws current), it acts as a parallel resistor to $R_2$, dropping the output voltage further.

## Related Notes
- [[Series Circuits]] - The underlying topology.
- [[Kirchhoff's Laws]] - Explains the voltage drops.
- [[Resistor Types]] - Fixed and variable resistors.
- [[Voltage Regulation]] - For stable voltage references.
