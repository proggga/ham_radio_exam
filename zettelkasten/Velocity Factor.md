---
id: 202512292181
title: Velocity Factor
tags:
  - ham-radio
  - antennas
  - physics
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Velocity Factor (Verkortingsfactor)

Radio waves travel slower in a transmission line than in a vacuum due to the **dielectric constant** of the insulating material.

## Definition
The Velocity Factor ($VF$) is the ratio of the speed of the wave in the cable ($v_{cable}$) to the speed of light ($c$).
*   **Formula**: $$VF = \frac{v_{cable}}{c} = \frac{1}{\sqrt{\varepsilon_r}}$$

## Typical Values
*   **Open Wire (Air)**: $VF \approx 0.95 - 0.99$
*   **Foam Dielectric Coax**: $VF \approx 0.80 - 0.85$
*   **Solid PE Dielectric (RG-58)**: $VF \approx 0.66$

## Application
When cutting a cable to a specific electrical length (e.g., a $\lambda/4$ matching stub), the **physical length** must be shorter than the free-space wavelength.
*   **Formula**: $$L_{phys} = L_{elect} \times VF$$

## Related Notes
*   [[Transmission Lines]]
*   [[Capacitor Principles]] (Dielectric constant)
*   [[Impedance Transformation]]
