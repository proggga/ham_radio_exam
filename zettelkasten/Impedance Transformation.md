---
id: 202512292182
title: Impedance Transformation
tags:
  - ham-radio
  - antennas
  - circuits
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Impedance Transformation

A transmission line can act as an impedance transformer depending on its electrical length.

## Half-Wave Line ($\lambda/2$)
Repeats the load impedance at the input.
*   **Effect**: $Z_{in} = Z_{load}$
*   **Use**: Carrying an impedance to the shack unchanged (e.g., measuring antenna impedance).

## Quarter-Wave Line ($\lambda/4$)
Inverts the impedance relative to the line's characteristic impedance ($Z_0$).
*   **Formula**: $$Z_{in} = \frac{Z_0^2}{Z_{load}}$$

### Behaviors
1.  **Short Circuit** at end $\rightarrow$ **Open Circuit** ($\infty \Omega$) at input.
    *   *Use*: Parallel resonant circuit equivalent (Trap).
2.  **Open Circuit** at end $\rightarrow$ **Short Circuit** ($0 \Omega$) at input.
    *   *Use*: Series resonant circuit equivalent.
3.  **Matching**: Can match two resistive impedances.
    *   *Example*: Matching $100 \Omega$ antenna to $50 \Omega$ coax requires a $\sqrt{50 \times 100} = 71 \Omega$ quarter-wave section.

## Related Notes
*   [[Velocity Factor]] - Critical for cutting lines to exact length.
*   [[Transmission Lines]]
*   [[Reactance & Impedance]]
