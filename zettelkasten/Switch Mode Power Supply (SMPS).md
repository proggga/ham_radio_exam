---
id: 202512292028
title: Switch Mode Power Supply (SMPS)
tags: ["ham-radio", "circuits", "power-supply"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Switch Mode Power Supply (SMPS)

## Operation
1.  Rectifies mains to high voltage DC.
2.  Switches this DC at high frequency (kHz to MHz).
3.  Transforms/Regulates using an Inductor/Transformer.
4.  Rectifies and filters output.
*   **Regulation**: Uses **PWM** (Pulse Width Modulation) to adjust duty cycle ($D$).

## Topologies
Identify these by the arrangement of the Inductor (L), Switch (T), and Diode (D).
*   **Step-Down (Buck)**: Output < Input.
    *   Formula: $U_{out} \approx D \times U_{in}$
    *   *Circuit:* Switch in series, then Diode to ground, Inductor to output.
*   **Step-Up (Boost)**: Output > Input.
    *   *Circuit:* Inductor in series, Switch to ground, Diode to output.
*   **Inverting**: Output polarity opposite to input.
    *   *Circuit:* Switch in series, Inductor to ground, Diode reverse biased to output.

## Characteristics
*   **Pros**: High efficiency (> 80%), small, lightweight.
*   **Cons**: Generates **RF Noise (QRM)** due to fast switching transients.
    *   Requires extensive EMI filtering (mains filter, shielding) to be usable for radio.

## Related
*   [[Types of Interference]]
*   [[Physics Principles]] (Efficiency)
