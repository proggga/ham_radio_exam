# Distortion and Dissipation

## Dissipation
Power lost as heat in the active device.
*   **Formula**: $P_{diss} = U_{DS} \times I_D$ (or $U_{CE} \times I_C$).
*   **[Exam](../12_regulations/02_Licensing_in_the_Netherlands.md) Topic: Dissipation Hyperbola**: A curve plotted on the $I_D - U_{DS}$ graph representing constant power ($P = C$).
    *   The Operating Point and the entire Load Line must ideally stay **below** this curve to avoid destroying the component.
    *   Check: Calculate $P$ at the operating point and compare to $P_{max}$.

## Harmonic Distortion
Non-linearity in an amplifier creates multiples of the fundamental frequency.
*   Example: A 14 MHz signal generates harmonics at 28 MHz ($2^{nd}$), 42 MHz ($3^{rd}$), etc.
*   Push-Pull amplifiers cancel even harmonics.
*   Low Pass [Filters](03_Filters_&_Resonance.md) are used to suppress harmonics at the output.

## Intermodulation Distortion (IMD)
Occurs when two or more signals mix in a non-linear device.
*   Creates sum and difference products: $2f_1 - f_2$, $2f_2 - f_1$.
*   **Problem**: These "third-order" products often fall close to the desired frequency and cannot be filtered out easily.
*   Causes "splatter" in [SSB](../01_electricity/34_Single_Sideband_SSB.md) transmissions.

---
[< Back to Section Index](README.md)