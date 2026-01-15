---
id: 202512292042
title: Filter Types
tags: ["ham-radio", "circuits", "filters"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29

aliases: ["Soorten filters", "Bandfilters", "Laagdoorlaat", "Hoogdoorlaat"]
---

# Filter Types

[[Filters & Resonance|Filters]] allow specific frequencies to pass while rejecting others.

## Common Types
*   **Low Pass [[Filters & Resonance|Filter]] (LPF)**: Passes frequencies below a cut-off point. Attenuates higher frequencies.
    *   *Use*: Audio filtering, Harmonic suppression in transmitters.
*   **High Pass [[Filters & Resonance|Filter]] (HPF)**: Passes frequencies above a cut-off point.
    *   *Use*: Removing AC hum ($50Hz$), Pre-selectors.
*   **Band Pass Filter (BPF)**: Passes a specific range of frequencies.
    *   *Use*: Receiver tuning (passing only the desired station).
*   **Band Stop (Notch) Filter**: Blocks a specific frequency range.
    *   *Use*: Removing specific interference carriers.

## Filter Topologies (Exam Topic 3.2)
*   **Pi-Filter ($\pi$-filter)**: Looks like the Greek letter $\pi$.
    *   **Structure**: Shunt C - Series L - Shunt C. (Capacitor to ground, Series Inductor, Capacitor to ground).
    *   *Characteristics*: Low Pass. Steep roll-off. Used in transmitter output stages (matches impedance and filters harmonics).
*   **T-Filter**: Looks like the letter T.
    *   **Structure**: Series L - Shunt C - Series L. (Inductor, Capacitor to ground, Inductor).
    *   *Characteristics*: Low Pass (typically). Used in antenna tuners and matching networks.

## Cut-off Frequency ($f_c$)
The frequency where the signal power is reduced by half ($-3dB$).
*   RC Filter: $f_c = \frac{1}{2\pi RC}$
*   RL Filter: $f_c = \frac{R}{2\pi L}$

## Related
*   [[Resonance]]
*   [[High-Performance Filters]]
