---
id: 202512292033
title: Crystals (Quartz)
tags: ["ham-radio", "components", "digital"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Crystals (Quartz)

Crystals are components made of quartz that vibrate at a precise frequency due to the **Piezoelectric effect**.

## Characteristics
*   **[[Resonance]]:** A crystal behaves like a resonant circuit with two closely spaced resonance frequencies:
    *   **Series [[Resonance]] ($f_s$):** Lower frequency. [[Impedance (Impedantie)|Impedance]] is very low (Dip).
    *   **Parallel [[Resonance]] ($f_p$):** Higher frequency. [[Impedance (Impedantie)|Impedance]] is very high (Peak).
    *   *Caveat:* When scanning frequency from low to high, you see a voltage **dip** (series) followed by a **peak** (parallel).
*   **Equivalent Circuit:** Series L, C, and R, all in parallel with a holder capacitance ($C_p$).
*   **Stability**: Provides very high frequency stability for oscillators and filters compared to LC circuits.
*   **Q-Factor**: Extremely high Q ([[Quality Factor (Q)|Quality Factor]]), resulting in sharp resonance.

## Types
*   **AT-cut**: The standard cut for good temperature stability over a wide range.
*   **TCXO (Temperature Compensated Crystal Oscillator)**: Contains a circuit that compensates for frequency drift due to temperature changes.
*   **OCXO (Oven Controlled Crystal Oscillator)**: The crystal is kept in a heated chamber (oven) at a constant temperature. Highest stability, but consumes more power.

## Related
*   [[Oscillators]]
*   [[High-Performance Filters]]
