---
id: 202301011244
title: "Causes of Interference"
tags: ["ham-radio", "interference"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Causes of Interference

## 1. Emissions
*   **Fundamental:** The intended frequency. High field strength near the antenna can overload nearby electronics.
*   **Harmonics:** Multiples of the fundamental frequency ($2f, 3f, 4f...$).
    *   *Example:* A 7 MHz transmitter may cause interference on 14 MHz, 21 MHz, etc.
    *   *Cause:* Non-linear amplification ([[Amplifiers|Class C, AB]]) produces harmonics.
*   **Spurious Emissions:** Parasitic oscillations or mixing products generated within the transmitter that are not harmonics.
    *   *Phase Noise:* "skirts" of noise around the carrier due to [[Detectors, Oscillators & Mixers|Oscillator]] jitter.

## 2. Immunity (Susceptibility)
The inability of equipment to reject unwanted RF energy.
*   **Poor Shielding:** Plastic cases allow RF to penetrate directly to the PCB.
*   **Lack of Filtering:** Missing mains filters or input filters on audio ports.
*   **Pin 1 Problem:** Grounding cable shields to the PCB signal ground instead of the metal chassis.

## 3. Propagation Paths
*   **Radiated:** Direct transmission through the air from antenna to victim device.
*   **Conducted:** RF traveling along wires (Mains cables, Speaker wires, Coax shields).
    *   **Common Mode Current:** RF flowing on the *outside* of a cable shield. Acts as a transmitting antenna inside the house.