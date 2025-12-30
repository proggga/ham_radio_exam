---
id: 202512292026
title: Power Supply Smoothing
tags: ["ham-radio", "circuits", "power-supply"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Power Supply Smoothing

Smoothing converts the pulsating DC from a rectifier into steady DC using filters.

## Reservoir Capacitor
A large electrolytic capacitor connected in parallel with the output.
*   **Action**: Charges to peak voltage ($U_{peak}$) during pulses and discharges into the load between pulses.
*   **Output Voltage**: $\approx U_{peak} = U_{eff} \times \sqrt{2}$.

### Ripple (Rimpel)
The residual AC variation on the DC output.
*   **Factors**:
    *   **Higher Load Current** $\rightarrow$ **More** Ripple.
    *   **Larger Capacitor** $\rightarrow$ **Less** Ripple.
    *   **Higher Frequency** (100Hz vs 50Hz) $\rightarrow$ **Less** Ripple (easier to filter).

## LC Filters
For better smoothing, an Inductor (Choke) and a second Capacitor are added.
*   **Pi-Filter (C-L-C)**: Common configuration.
*   **Choke ($L$)**: Opposes changes in current, smoothing the flow.
*   **Capacitor ($C$)**: Further reduces voltage ripple.
*   **Comparison (C-filter vs LC-filter)**:
    *   **C-filter (Elco only)**: High ripple, very high peak currents through diodes (charging happens in short bursts).
    *   **LC-filter (Choke input or Pi)**: Lower ripple, lower peak currents (choke spreads out the charging time), slightly lower output voltage (due to DC resistance of choke).

## Related
*   [[Capacitors]]
*   [[Inductors (Spoelen)]]
