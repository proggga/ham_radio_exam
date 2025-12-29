---
id: 202512292041
title: Phase Locked Loop (PLL)
tags: ["ham-radio", "circuits", "digital"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Phase Locked Loop (PLL)

A PLL is a control system that locks a variable oscillator to a stable reference frequency.

## Components
1.  **VCO (Voltage Controlled Oscillator)**: Generates the output frequency.
2.  **Reference Oscillator**: Very stable crystal source.
3.  **Phase Detector**: Compares the phase of the VCO (often divided down) to the Reference.
4.  **Loop Filter**: Smooths the error voltage from the detector.
5.  **Divider**: Divides the VCO frequency to match the reference steps.

## Applications
*   **Frequency Synthesizers**: Generating stable, tunable frequencies for VFOs.
*   **FM Demodulation**: Tracking frequency deviations.

## Related
*   [[Oscillators]]
*   [[Sequential Logic]] (Counters/Dividers)
