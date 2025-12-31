# Rectification

Rectification is the process of converting Alternating Current (AC) into pulsating Direct Current (DC).

## Half-Wave Rectification
*   **Components**: 1 [Diode](../02_components/17_Diodes.md).
*   **Operation**: Passes only one half-cycle (positive or negative).
*   **Ripple Frequency**: Equal to input frequency ($50 Hz$).
*   **Efficiency**: Low (half power discarded).

## Full-Wave Rectification

### Center-Tap Transformer
*   **Components**: 2 [Diodes](../02_components/17_Diodes.md) + Center-tapped transformer.
*   **Operation**: [Diodes](../02_components/17_Diodes.md) conduct alternately on each half-cycle.

### Bridge Rectifier
*   **Components**: 4 Diodes (Bridge configuration).
*   **Benefit**: Does not require a center-tap transformer. Standard for most supplies.

### Characteristics (Full-Wave)
*   **Ripple Frequency**: Double the input frequency ($100 Hz$).
*   **Efficiency**: High. Both half-cycles are utilized.

## Peak Inverse Voltage (PIV)
The maximum voltage across the non-conducting diode(s).
*   **Half-Wave (with [Capacitor](../02_components/05_Capacitors.md))**: The diode sees $2 \times U_{peak}$ (Input peak + [Capacitor](../02_components/05_Capacitors.md) voltage).
*   **Full-Wave Center-Tap**: Each diode sees $2 \times U_{peak}$.
*   **Bridge Rectifier**: Each diode sees $1 \times U_{peak}$.
*   *[Safety](../10_safety/01_Electrical_Safety.md):* Always choose diodes with a PIV rating significantly higher than the theoretical maximum (e.g., $3 \times U_{eff}$).

---
[< Back to Section Index](README.md)