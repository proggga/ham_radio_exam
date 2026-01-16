id: 202501111620
title: Common Wire Antennas
tags: ["antennas", "practical", "transmission-lines"]
created: 2025-01-11
type: permanent-note
modified: 2025-01-11

aliases: ["Veelgebruikte Draadantennes", "G5RV", "Windom", "OCFD", "Off-Center Fed Dipole"]

# Common Wire Antennas

Beyond the standard [Dipole](02_The_Dipole_Antenna.md), several wire antenna designs are popular for their multiband capabilities or convenience.

## 1. G5RV
Designed by Louis Varney (G5RV).
*   **Design**: A $3\lambda/2$ center-fed dipole for 20m (14 MHz).
*   **Dimensions**:
    *   **Flat Top**: ~102 ft (31m).
    *   **Matching Section**: ~30 ft (9m) of **Ladder Line** (Open wire or Window line) acting as a 1:1 impedance transformer on 20m.
*   **Operation**:
    *   Works well on 80m, 40m, 20m, and 12m.
    *   **Requires an ATU (Tuner)** for most bands (except 20m).
    *   Often acts as a "Cloud Warmer" on 80m due to low height relative to wavelength.

## 2. Windom / OCFD (Off-Center Fed Dipole)
A dipole fed away from the center (typically at the 33%/67% point).
*   **Principle**: At this offset point, the impedance is roughly **200-300 $\Omega$** on the fundamental frequency *and* its even harmonics.
*   **Feed**: Uses a **4:1 or 6:1 Current Balun** to match to $50 \Omega$ coax.
*   **Bands**: A classic 80m Windom works on 80, 40, 20, and 10m without a tuner (or with a light touch).
*   **Risk**: prone to **Common Mode Current** on the coax shield. A good Choke Balun is essential to prevent RF in the shack.

## 3. Zepp Antenna
Originally used on Zeppelins.
*   **Design**: An **[End-Fed Antenna](03_End-Fed_Antenna.md)** fed with ladder line.
*   **Operation**: Essentially a dipole where one leg of the feeder is connected to the antenna and the other ends blindly.

## Comparison
| Antenna | Feed | Bands | Pros | Cons |
| :--- | :--- | :--- | :--- | :--- |
| **[Dipole](02_The_Dipole_Antenna.md)** | Center (Coax) | Single (odd harm) | Simple, predictable. | Single band. |
| **G5RV** | Center (Ladder) | Multiband (Tuner) | Robust, popular. | Needs Tuner, Feedline radiates if not careful. |
| **OCFD (Windom)** | Off-Center (Balun) | Multiband (No Tuner) | Easy match on harmonics. | RF in shack risk (CMC). |
| **[EFHW](03_End-Fed_Antenna.md)** | End (Transformer) | Multiband | Easy install. | High Voltage at feedpoint. |

---
[< Back to Section Index](README.md)