# Switch Mode Power Supply (SMPS)

## Operation
1.  Rectifies mains to high voltage DC.
2.  Switches this DC at high frequency (kHz to MHz).
3.  Transforms/Regulates using an [Inductor](../02_components/09_Inductors_Spoelen.md)/Transformer.
4.  Rectifies and filters output.
*   **Regulation**: Uses **PWM** (Pulse Width [Modulation](../01_electricity/31_Modulation_&_Digital_Signals.md)) to adjust duty cycle ($D$).

## Topologies
Identify these by the arrangement of the [Inductor](../02_components/09_Inductors_Spoelen.md) (L), Switch (T), and [Diode](../02_components/17_Diodes.md) (D).
*   **Step-Down (Buck)**: Output < Input.
    *   Formula: $U_{out} \approx D \times U_{in}$
    *   *Circuit:* Switch in series, then [Diode](../02_components/17_Diodes.md) to ground, [Inductor](../02_components/09_Inductors_Spoelen.md) to output.
*   **Step-Up (Boost)**: Output > Input.
    *   *Circuit:* Inductor in series, Switch to ground, [Diode](../02_components/17_Diodes.md) to output.
*   **Inverting**: Output polarity opposite to input.
    *   *Circuit:* Switch in series, Inductor to ground, Diode reverse biased to output.

## Characteristics
*   **Pros**: High efficiency (> 80%), small, lightweight.
*   **Cons**: Generates **RF [Noise](../01_electricity/26_AC_Signals_&_Noise.md) (QRM)** due to fast switching transients.
    *   Requires extensive EMI filtering (mains filter, shielding) to be usable for radio.

---
[< Back to Section Index](README.md)