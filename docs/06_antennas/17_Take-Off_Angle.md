# Take-Off Angle (Opstraalhoek)

The **Take-Off Angle** (also called **Radiation Angle** or **Elevation Angle**) is the angle above the horizon at which an antenna radiates the maximum amount of energy.

## Importance
The take-off angle determines the distance a [Sky Wave](../07_propagation/06_Sky_Wave_Propagation.md) signal will travel.
*   **Low Angle ($5^\circ - 15^\circ$):** Required for **DX** (Long Distance). The signal hits the ionosphere at a shallow angle, resulting in a longer "skip" distance and fewer hops to reach the destination.
*   **High Angle ($> 45^\circ$):** Used for Short Range communications ($0 - 500 \text{ km}$). This is known as **[Near Vertical Incidence Skywave (NVIS)](../07_propagation/13_Near_Vertical_Incidence_Skywave_NVIS.md)**.
    *   The signal is sent almost straight up and reflected back down nearby, filling the [Dead Zone](../07_propagation/12_Dead_Zone_Skip_Zone.md).

## Factors Influencing Take-Off Angle
1.  **Height Above Ground:**
    *   Generally, raising an antenna **lowers** the take-off angle (better for DX).
    *   For a horizontal dipole, a height of $\lambda/2$ (half wavelength) produces a pattern suitable for general use ($~30^\circ$).
    *   A height of $\lambda$ or more creates significantly lower lobes ($~15^\circ$).
2.  **Ground Quality:** The conductivity of the ground affects the reflection of the wave, reinforcing or cancelling the signal at certain angles.
3.  **Antenna Type:**
    *   **Vertical Antennas:** Naturally have a **low take-off angle** (good for DX), even when mounted close to the ground.
    *   **Horizontal Antennas:** Require height to achieve a low angle. If mounted low ($< \lambda/4$), they radiate mostly straight up (NVIS).

---
[< Back to Section Index](README.md)