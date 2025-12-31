# Receiver Overload

Receiver overload occurs when a very strong signal (even if off-frequency) enters the RF front-end of a receiver.

## Blocking (Blokkering)
*   **Effect**: The receiver goes "deaf" (desensitized) or the gain fluctuates wildly.
*   **Mechanism**:
    *   A strong RF signal drives the input transistor/FET/Tube into non-linearity.
    *   The input junction acts as a **rectifier** (diode), creating a DC voltage from the RF signal.
    *   This DC voltage shifts the **Operating Point** (Instelpunt/Bias) of the amplifier.
    *   *Result:* The amplifier gain drops or cuts off completely (Class C operation).
*   **[Mitigation](07_Mitigation_Ontstoring.md)**:
    *   **Attenuator (Verzwakker)**: Reducing the input signal moves the stage back into its linear range.
    *   **Preselector**: Better filtering before the first amplifier.
    *   **[Antenna](../10_safety/03_Antenna_&_Tower_Safety.md) Orientation**: Rotating a directional antenna ([Yagi](../06_antennas/08_Directional_Antennas_Beams.md)) to null the interference.

---
[< Back to Section Index](README.md)