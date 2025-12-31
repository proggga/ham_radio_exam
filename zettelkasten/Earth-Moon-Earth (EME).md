---
id: 202512311430
title: Earth-Moon-Earth (EME)
tags: ["ham-radio", "operating", "propagation", "weak-signal"]
created: 2025-12-31
type: permanent-note
modified: 2025-12-31
---

# Earth-Moon-Earth (EME)

Also known as **Moonbounce**, EME is a technique where radio signals are aimed at the Moon and reflected back to Earth to communicate with distant stations.

## Characteristics
*   **Path Loss**: Extremely high ($\approx 250 \text{ dB}$ round trip). Only a tiny fraction of the energy reflects off the Moon's surface.
*   **Requirements**:
    *   **High Power**: Usually legal limit (1500W).
    *   **High Gain Antennas**: Arrays of long Yagis or large Dishes.
    *   **Low Noise Preamplifiers**: Essential at the antenna to hear the weak echo.
*   **Frequencies**: Typically **50 MHz (6m)** to **10 GHz**, with **144 MHz (2m)** and **1296 MHz (23cm)** being most popular.

## Challenges
*   **Libration Fading**: Rapid fluttering of the signal caused by the Moon's "wobble" (Libration).
*   **[[Doppler Shift]]**: The frequency changes as the Moon moves relative to the Earth.
*   **Faraday Rotation**: The polarization of the signal rotates as it passes through the ionosphere.

## Modes
*   **CW**: Traditional mode, still used.
*   **Digital (JT65 / Q65)**: Part of the **WSJT-X** suite. Designed specifically for EME to decode signals far below the noise floor.

## Related
*   [[Propagation Modes]]
*   [[Antenna Characteristics]] (Gain)
*   [[Modern Digital Modes]] (WSJT-X)
