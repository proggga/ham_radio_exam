---
id: 202512292101
title: Receiver Overload
tags: ["ham-radio", "interference", "receivers"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Receiver Overload

Receiver overload occurs when a very strong signal (even if off-frequency) enters the RF front-end of a receiver.

## Blocking (Blokkering)
*   **Effect**: The receiver goes "deaf" (desensitized) or the gain fluctuates wildly.
*   **Mechanism**:
    *   A strong RF signal drives the input transistor/FET/Tube into non-linearity.
    *   The input junction acts as a **rectifier** (diode), creating a DC voltage from the RF signal.
    *   This DC voltage shifts the **Operating Point** (Instelpunt/Bias) of the amplifier.
    *   *Result:* The amplifier gain drops or cuts off completely (Class C operation).
*   **Mitigation**:
    *   **Attenuator (Verzwakker)**: Reducing the input signal moves the stage back into its linear range.
    *   **Preselector**: Better filtering before the first amplifier.
    *   **Antenna Orientation**: Rotating a directional antenna (Yagi) to null the interference.

## Related
*   [[Superheterodyne Principle]]
*   [[Amplifier Operating Principles]]
