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
1.  Rectifies mains directly to high voltage DC.
2.  Switches this DC at high frequency (kHz to MHz).
3.  Transforms it (small transformer due to high freq).
4.  Rectifies and filters output.
*   **Regulation**: Uses **PWM** (Pulse Width Modulation) to adjust duty cycle.

## Characteristics
*   **Pros**: High efficiency (> 80%), small, lightweight.
*   **Cons**: Generates **RF Noise (QRM)** due to fast switching transients.
    *   Requires extensive EMI filtering to be usable for radio.

## Related
*   [[Types of Interference]]
*   [[Physics Principles]] (Efficiency)
