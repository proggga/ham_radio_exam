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

## Peak Inverse Voltage (PIV)
The maximum voltage across the non-conducting diode(s).
*   **Half-Wave (with Capacitor)**: The diode sees $2 \times U_{peak}$ (Input peak + Capacitor voltage).
*   **Full-Wave Center-Tap**: Each diode sees $2 \times U_{peak}$.
*   **Bridge Rectifier**: Each diode sees $1 \times U_{peak}$.
*   *Safety:* Always choose diodes with a PIV rating significantly higher than the theoretical maximum (e.g., $3 \times U_{eff}$).

## Related
*   [[Semiconductors]]
*   [[Power Supply Smoothing]]
