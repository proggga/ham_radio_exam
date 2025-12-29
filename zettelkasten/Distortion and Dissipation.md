---
id: 202512292019
title: Distortion and Dissipation
tags: ["ham-radio", "circuits", "amplifiers", "performance"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Distortion and Dissipation

## Dissipation
Power lost as heat in the active device.
*   **Formula**: $P = U_{ce} \times I_c$
*   The device must operate within its **Safe Operating Area (SOA)** defined by the Dissipation Hyperbola on the datasheet. Exceeding this destroys the component.

## Harmonic Distortion
Non-linearity in an amplifier creates multiples of the fundamental frequency.
*   Example: A 14 MHz signal generates harmonics at 28 MHz ($2^{nd}$), 42 MHz ($3^{rd}$), etc.
*   Push-Pull amplifiers cancel even harmonics.
*   Low Pass Filters are used to suppress harmonics at the output.

## Intermodulation Distortion (IMD)
Occurs when two or more signals mix in a non-linear device.
*   Creates sum and difference products: $2f_1 - f_2$, $2f_2 - f_1$.
*   **Problem**: These "third-order" products often fall close to the desired frequency and cannot be filtered out easily.
*   Causes "splatter" in SSB transmissions.

## Related
*   [[Types of Interference]]
*   [[Amplifier Classes]]
