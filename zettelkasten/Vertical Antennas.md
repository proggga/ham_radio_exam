---
id: 202512292116
title: Vertical Antennas
tags: ["ham-radio", "antennas"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29

aliases: ["Verticale antennes", "Groundplane"]
---

# Vertical Antennas

Vertical antennas are popular for DX (long distance) due to their low angle of radiation.

## Ground Plane (GP)
A Quarter-wave ($\lambda/4$) vertical element.
*   **Radials**: Requires a ground plane (artificial ground) made of wires (radials).
*   **[[Impedance|Impedance]]**:
    *   Horizontal radials: $\approx 36 \Omega$.
    *   Drooping radials ($45^\circ$): $\approx 50 \Omega$ (Good match for coax).

## 5/8 Wave Vertical
*   **Length**: $\approx 5/8 \lambda$ (physically longer than 1/4 wave).
*   **Gain**: **Higher gain** ($\approx 3 \text{ [[Decibels & Logarithms|dB]]}$) than a 1/4 wave vertical because it compresses the radiation pattern closer to the horizon.
*   **Matching**: Not naturally resonant at $50 \Omega$ (has capacitive reactance). Requires a **loading coil** at the base to match impedance.
*   **Use**: Very popular for mobile [[VHFUHF Bands (6m, 2m, 70cm)|VHF]]/[[VHFUHF Bands (6m, 2m, 70cm)|UHF]] work.

## Characteristics
*   **Radiation Pattern**: Omni-directional (radiates equally in all horizontal directions).
*   **Take-off Angle**: Low angle, good for reaching the ionosphere for long hops.
*   **[[AC Signals & Noise|Noise]]**: Susceptible to man-made noise (QRM) which is often vertically polarized.

## Variants
*   **Ground Plane (GP)**: Using radials (horizontal or drooping).
*   **5/8 Wave**: Higher gain ($~3 dBd$), lower angle of radiation. Needs a matching coil at the base.
*   **[[J-Pole Antenna]]**: A popular end-fed vertical variant that does not require radials.
*   **[[Discone Antenna]]**: Extremely wideband vertical (unity gain) used for scanning.

## Related
*   [[The Dipole Antenna]]
*   [[Propagation Modes]]
*   [[Ground Wave Propagation]]
