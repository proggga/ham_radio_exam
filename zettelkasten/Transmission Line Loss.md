---
id: 202512292183
title: Transmission Line Loss
tags:
  - ham-radio
  - antennas
  - physics
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Transmission Line Loss (Attenuation)

As a signal travels through a transmission line, some energy is lost as heat. This is called attenuation (verzwakking).

## Factors
1.  **Frequency**: Loss increases with frequency (Skin effect and dielectric loss).
    *   Coax that is good for HF (30 MHz) may be useless for UHF (430 MHz).
2.  **Length**: Loss is proportional to length (dB per meter).
3.  **Dielectric**: Air has almost zero loss. Solid plastic has higher loss.
4.  **SWR**: High Standing Wave Ratio increases the effective loss.
    *   Current peaks cause higher $I^2R$ heating.
    *   Voltage peaks cause higher dielectric heating.

## Comparison
*   **Open Wire**: Extremely low loss. Ideal for tuned feeders with high SWR.
*   **Thin Coax (RG-58)**: High loss. Avoid for long runs or VHF/UHF.
*   **Thick Coax (RG-213/Ecoflex)**: Lower loss.

## Related Notes
*   [[Transmission Line Types]]
*   [[Standing Wave Ratio (SWR)]]
*   [[Decibels & Logarithms]]
