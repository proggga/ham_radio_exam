# Transmission Lines

## 1. Types
*   **Coaxial Cable (Asymmetric):**
    *   Structure: Inner conductor, Dielectric, Shield/Braid, Jacket.
    *   Impedance ($Z_0$): Typically $50 \Omega$ (RG58, RG213) or $75 \Omega$ (TV coax). See [Impedance](../03_circuits/07_reactance_impedance.md).
    *   Shielding: Keeps RF inside, interference out.
*   **Open Wire / Twin Lead (Symmetric):**
    *   Structure: Two parallel wires separated by spacers ("Ladder line" or "Kippenladder").
    *   Impedance ($Z_0$): Typically $300 \Omega$, $450 \Omega$, or $600 \Omega$.
    *   Loss: Very low loss, even at high SWR.

## 2. Velocity Factor (Verkortingsfactor)
Radio waves travel slower in a cable than in a vacuum due to the dielectric material.
*   **Formula:** $VF = \frac{v_{cable}}{c}$.
*   **Typical Values:**
    *   Open Wire: ~0.95 (Air dielectric).
    *   Foam Coax: ~0.80.
    *   Solid PE Coax (RG58): ~0.66.
*   **Physical Length:** $L_{phys} = L_{elect} \times VF$.
    *   A "quarter wave" of coax is physically shorter than a quarter wave in free space.

## 3. Impedance Transformation
A transmission line can act as an impedance transformer depending on its length.
*   **$\lambda/2$ Line:** Repeats the load impedance at the input ($Z_{in} = Z_{load}$).
*   **$\lambda/4$ Line:** Inverts the impedance.
    *   $$Z_{in} = \frac{Z_0^2}{Z_{load}}$$
    *   *Short* at end becomes *Open* at input.
    *   *Open* at end becomes *Short* at input.
    *   Used to match different impedances (Quarter-wave transformer).

## 4. Attenuation (Verzwakking)
Loss of signal strength as it travels through the line.
*   Increases with **Frequency**.
*   Increases with **Length**.
*   Increases with **SWR** (Standing waves cause additional heat loss). See [Matching](04_matching.md).

---
[Back to Index](../INDEX.md) | [Back to Dashboard](../../README.md)
