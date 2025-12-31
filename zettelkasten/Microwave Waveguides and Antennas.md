---
id: 202512311650
title: Microwave Waveguides and Antennas
tags: ["ham-radio", "antennas", "microwave", "propagation"]
created: 2025-12-31
type: permanent-note
modified: 2025-12-31
---

# Microwave Waveguides and Antennas

At microwave frequencies (above 1-3 GHz), standard cables (coax) become too lossy. **Waveguides**—hollow metal pipes—are used to guide electromagnetic energy.

## Waveguide Principles
*   **Analogy**: Acts like a "light pipe" or "RF pipe" for electromagnetic waves.
*   **Structure**: Hollow rectangular or circular metal pipe (Brass, Aluminum, Copper).
*   **Cutoff Frequency**: Waveguides act as High-Pass [[Filters & Resonance|Filters]]. They only propagate frequencies above a cutoff.
    *   For a rectangular waveguide (width $a$, height $b$), the cutoff frequency is determined by dimension $a$.
    *   **Condition**: Dimension $a$ must be at least $\lambda / 2$ (half-wavelength).
    *   *Formula*: $f_c = \frac{c}{2a}$.

## Propagation Modes
Waves do not travel as currents but as fields bouncing off the walls.
*   **TEM (Transverse Electromagnetic)**: Cannot exist in a waveguide (requires two separated conductors).
*   **TE (Transverse Electric)**: Electric field is perpendicular to the direction of travel.
*   **TM (Transverse Magnetic)**: Magnetic field is perpendicular to the direction of travel.
*   **Dominant Mode**: The mode with the lowest cutoff frequency (usually $TE_{10}$ for rectangular).

## Microwave Antennas
*   **Horn [[Antenna & Tower Safety|Antenna]]**: A flared open end of a waveguide. Provides moderate gain and matches the waveguide impedance to free space.
*   **Parabolic Dish**: A large reflector that focuses energy to a point (feed).
    *   **Gain**: Extremely high, proportional to diameter in wavelengths.
    *   **Beamwidth**: Very narrow pencil beam.
    *   **Feed**: Usually a small horn antenna or dipole placed at the focal point.

## Related
*   **[[Transmission Lines]]**
*   **[[Antenna Characteristics]]** (Gain, Beamwidth)
*   **[[VHFUHF Bands (6m, 2m, 70cm)]]**
