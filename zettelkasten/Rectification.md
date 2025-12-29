---
id: 202512292025
title: Rectification
tags: ["ham-radio", "circuits", "power-supply"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Rectification

Rectification is the process of converting Alternating Current (AC) into pulsating Direct Current (DC).

## Half-Wave Rectification
*   **Components**: 1 Diode.
*   **Operation**: Passes only one half-cycle (positive or negative).
*   **Ripple Frequency**: Equal to input frequency ($50 Hz$).
*   **Efficiency**: Low (half power discarded).

## Full-Wave Rectification

### Center-Tap Transformer
*   **Components**: 2 Diodes + Center-tapped transformer.
*   **Operation**: Diodes conduct alternately on each half-cycle.

### Bridge Rectifier
*   **Components**: 4 Diodes (Bridge configuration).
*   **Benefit**: Does not require a center-tap transformer. Standard for most supplies.

### Characteristics (Full-Wave)
*   **Ripple Frequency**: Double the input frequency ($100 Hz$).
*   **Efficiency**: High. Both half-cycles are utilized.

## Related
*   [[Semiconductors]]
*   [[Power Supply Smoothing]]
