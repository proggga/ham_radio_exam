# Smith Chart

The **Smith Chart** is a graphical calculator for radio frequency engineering, used to plot impedance, [SWR](16_Standing_Wave_Ratio_SWR.md), and design matching networks.

## Structure
It maps the complex impedance plane onto a circular grid.
*   **Horizontal Axis**: Resistance ($R$).
    *   **Center**: System [Impedance](../01_electricity/21_Impedance_Impedantie.md) ($Z_0$, usually $50 \Omega$). Perfect match.
    *   **Right Edge**: Open Circuit ($\infty \Omega$).
    *   **Left Edge**: Short Circuit ($0 \Omega$).
*   **Curves/Circles**:
    *   **Circles**: Constant Resistance.
    *   **Arcs**: Constant [Reactance](../02_components/07_Reactance_Reactantie.md) ($X$).
        *   **Top Half**: Inductive ($+jX$).
        *   **Bottom Half**: Capacitive ($-jX$).

## Use
*   Visualizing how impedance changes with frequency or line length.
*   Designing matching networks (adding series/parallel L or C components moves the point along specific circles).

## Normalization
The chart is "normalized" to make it universal.
*   **Formula**: $Z_{normalized} = \frac{Z_{actual}}{Z_0}$
*   *Example*: If system $Z_0 = 50\Omega$ and load is $100\Omega$, plot $2.0$ on the resistance axis.

## Radially Scaled Parameters
Scales at the bottom of the chart provide derived data based on the plotted impedance radius (distance from center).
*   **SWR**: Standing Wave Ratio.
*   **Return Loss**: Power reflected back in dB.
*   **Reflection Coefficient**: Voltage ($\Gamma$) or Power ($\Gamma_{pwr}$).
*   **Transmission Loss**: Attenuation due to mismatch.

---
[< Back to Section Index](README.md)