---
id: 202512292193
title: Smith Chart
tags:
  - ham-radio
  - antennas
  - measurements
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Smith Chart

The **Smith Chart** is a graphical calculator for radio frequency engineering, used to plot impedance, SWR, and design matching networks.

## Structure
It maps the complex impedance plane onto a circular grid.
*   **Horizontal Axis**: Resistance ($R$).
    *   **Center**: System Impedance ($Z_0$, usually $50 \Omega$). Perfect match.
    *   **Right Edge**: Open Circuit ($\infty \Omega$).
    *   **Left Edge**: Short Circuit ($0 \Omega$).
*   **Curves/Circles**:
    *   **Circles**: Constant Resistance.
    *   **Arcs**: Constant Reactance ($X$).
        *   **Top Half**: Inductive ($+jX$).
        *   **Bottom Half**: Capacitive ($-jX$).

## Use
*   Visualizing how impedance changes with frequency or line length.
*   Designing matching networks (adding series/parallel L or C components moves the point along specific circles).

## Related Notes
*   [[Impedance (Impedantie)]]
*   [[Standing Wave Ratio (SWR)]]
