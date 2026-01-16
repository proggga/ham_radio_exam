id: 202512292116
title: Vertical Antennas
tags: ["antennas", "ionosphere", "math", "transmission-lines"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29

aliases: ["Verticale antennes", "Groundplane"]

# Vertical Antennas

Vertical antennas are popular for DX (long distance) due to their low angle of radiation.

## Ground Plane (GP)
A Quarter-wave ($\lambda/4$) vertical element.
*   **Radials**: Requires a ground plane (artificial ground) made of wires (radials).
*   **Impedance**:
    *   Horizontal radials: $\approx 36 \Omega$.
    *   Drooping radials ($45^\circ$): $\approx 50 \Omega$ (Good match for coax).

## 5/8 Wave Vertical
*   **Length**: $\approx 5/8 \lambda$ (physically longer than 1/4 wave).
*   **Gain**: **Higher gain** ($\approx 3 \text{ dB}$) than a 1/4 wave vertical because it compresses the radiation pattern closer to the horizon.
*   **Matching**: Not naturally resonant at $50 \Omega$ (has capacitive reactance). Requires a **loading coil** at the base to match impedance.
*   **Use**: Very popular for mobile [VHF](../07_propagation/15_VHFUHF_Bands_6m,_2m,_70cm.md)/[UHF](../07_propagation/15_VHFUHF_Bands_6m,_2m,_70cm.md) work.

## Characteristics
*   **Radiation Pattern**: Omni-directional (radiates equally in all horizontal directions).
*   **Take-off Angle**: Low angle, good for reaching the ionosphere for long hops.
*   **[Noise](../01_electricity/14_AC_Signals_&_Noise.md)**: Susceptible to man-made noise (QRM) which is often vertically polarized.

## Variants
*   **Ground Plane (GP)**: Using radials (horizontal or drooping).
*   **5/8 Wave**: Higher gain ($~3 dBd$), lower angle of radiation. Needs a matching coil at the base.
*   **[J-Pole Antenna](08_J-Pole_Antenna.md)**: A popular end-fed vertical variant that does not require radials.
*   **[Discone Antenna](09_Discone_Antenna.md)**: Extremely wideband vertical (unity gain) used for scanning.

---
[< Back to Section Index](README.md)