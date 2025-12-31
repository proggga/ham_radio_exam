---
id: 202512292115
title: The Dipole Antenna
tags: ["ham-radio", "antennas"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# The Dipole Antenna

The dipole is the fundamental antenna against which others are often compared.

## Construction
*   **Length**: Approximately half a wavelength ($\lambda/2$).
    *   Formula (meters): $L = \frac{142.5}{f_{MHz}}$ (accounts for velocity factor/end effect, approx 0.95-0.96).
*   **Feedpoint**: Fed in the center.
    *   **Voltage**: **Low** at center (Feedpoint), **High** at ends. (High Z at ends).
    *   **Current**: **High** at center (Feedpoint), **Zero** at ends.

## Resonance on Harmonics
A dipole resonates not only at its fundamental frequency ($f$) but also at harmonics.
*   **Odd Harmonics (3rd, 5th...)**: The center remains a **Current Maximum** (Low [[Impedance (Impedantie)|Impedance]]). Can be fed directly.
*   **Even Harmonics (2nd, 4th...)**: The center becomes a **Voltage Maximum** (High Impedance). Hard to feed with low-Z coax.

## Characteristics
*   **Impedance**: $\approx 73 \Omega$ in free space. Lowers as it gets closer to the ground.
*   **Radiation Pattern**: Figure-8 (Broadside to the wire). Nulls off the ends.
*   **Polarization**: Horizontal (if hung horizontally).

## Variants
*   **Inverted V**: Center supported high, ends drooping.
    *   Omni-directional, lower impedance (~$50 \Omega$).
*   **Folded Dipole**: Folded back on itself.
    *   **Impedance**: $4 \times$ Dipole $\approx 300 \Omega$.
    *   **[[Bandwidth]]**: Wider than a standard dipole.
    *   Often used with a 4:1 Balun.
*   **Trap Dipole**: Uses LC parallel circuits (Traps) to electrically disconnect outer sections of the wire at higher frequencies, allowing multiband operation.

## Equivalent Circuit
*   **At [[Resonance]]**: Pure Resistance ($R_{rad} + R_{loss}$).
*   **Below Resonance (Too Short)**: Capacitive (needs series L to tune).
*   **Above Resonance (Too Long)**: Inductive (needs series C to tune).

## Related
*   [[Transmission Lines]]
*   [[Antenna Characteristics]]
