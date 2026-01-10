# Impedance Transformation

A transmission line can act as an impedance transformer depending on its electrical length.

## Half-Wave Line ($\lambda/2$)
Repeats the load impedance at the input.
*   **Effect**: $Z_{in} = Z_{load}$ (1:1 transformation).
*   **Use**: Measuring antenna impedance from the shack (line length doesn't matter if it's a multiple of $\lambda/2$).

## Quarter-Wave Line ($\lambda/4$)
Inverts the impedance relative to the line's characteristic impedance ($Z_0$). Acts as a transformer.
*   **Formula**: $$Z_{in} = \frac{Z_0^2}{Z_{load}}$$
    *   *Alternative Form:* $Z_{in} : Z_0 = Z_0 : Z_{load}$

### Applications
1.  **Matching Transformer (Q-Match)**: Can match two resistive impedances.
    *   To match Load ($Z_{load}$) to Source ($Z_{in}$), use a line with impedance:
    *   $$Z_0 = \sqrt{Z_{in} \cdot Z_{load}}$$
    *   *Example:* Matching a $100 \Omega$ Quad loop to $50 \Omega$ coax.
        *   $Z_{stub} = \sqrt{50 \times 100} = \sqrt{5000} \approx 71 \Omega$. (Use $75 \Omega$ coax).
2.  **[Impedance](../01_electricity/21_Impedance_Impedantie.md) Inversion**:
    *   **Short Circuit** at end ($Z_L=0$) $\rightarrow$ **Open Circuit** ($\infty \Omega$) at input. (Parallel Resonant Circuit / Trap).
    *   **Open Circuit** at end ($Z_L=\infty$) $\rightarrow$ **Short Circuit** ($0 \Omega$) at input. (Series Resonant Circuit).

---
[< Back to Section Index](README.md)