---
id: 202512292162
title: Line of Sight Propagation (LOS)
tags:
  - ham-radio
  - propagation
  - vhf-uhf
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Line of Sight Propagation (LOS)

LOS is the direct path between transmitting and receiving antennas.

## Characteristics
*   **Frequency**: Dominant mode for [[VHFUHF Bands (6m, 2m, 70cm)|VHF]], UHF, and Microwave ($> 30 \text{ MHz}$).
*   **Limitation**: Blocked by terrain, buildings, and the curvature of the earth.

## Radio Horizon
Radio waves bend slightly over the horizon due to atmospheric refraction (density gradient of air).
*   **Optical Horizon**: Distance you can see with eyes.
*   **Radio Horizon**: $\approx 15\%$ further than Optical Horizon.
*   **Formula (HS14)**:
    $$d_{km} \approx 3.57 \times \sqrt{h_{m}}$$
    *   $d$ in kilometers, $h$ in meters.
    *   *Exam Tip:* Sometimes rounded to $d \approx 4 \sqrt{h}$ (gives slightly high result).
*   **Total Range**: The sum of the radio horizons of both antennas.
    $$D_{total} \approx 3.57 (\sqrt{h_{tx}} + \sqrt{h_{rx}})$$

## Extending the Range
*   **[[Antenna & Tower Safety|Antenna]] Height:** The most effective way to increase range.
*   **Diffraction (Knife-Edge):**
    *   Radio waves can bend slightly over sharp obstacles like mountain ridges or building edges.
    *   Allows communication into "shadow" areas that are technically non-line-of-sight.
    *   *Note:* Signal strength is usually reduced (attenuated).
*   **Reflection:** Bouncing signals off buildings or mountains to reach a receiver around a corner.

## Range Calculation
The theoretical maximum distance (Radio Horizon) $d$ in kilometers for an antenna at height $h$ (meters):
$$d \approx 3.57 \sqrt{h}$$
*   *Note:* This accounts for the **4/3 Earth Radius** effect (atmospheric refraction bends waves slightly down, extending the horizon).
*   **Total Range:** $d_{total} \approx 3.57 (\sqrt{h_{TX}} + \sqrt{h_{RX}})$

## Related Notes
*   [[VHFUHF Bands (6m, 2m, 70cm)]]
*   [[Tropospheric Propagation]] - Extensions beyond LOS.
