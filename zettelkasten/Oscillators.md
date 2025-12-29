---
id: 202512292038
title: Oscillators
tags: ["ham-radio", "circuits", "oscillators"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Oscillators

Oscillators are circuits that generate an AC signal from DC.

## Barkhausen Criterion
For oscillation to occur and sustain:
1.  **Loop Gain**: $\ge 1$.
2.  **Phase Shift**: $0^\circ$ or $360^\circ$ (Positive Feedback).

## LC Oscillators (Variable Frequency)
Used in VFOs (Variable Frequency Oscillators).
*   **Hartley**: Uses an **inductive** voltage divider (tapped coil).
*   **Colpitts**: Uses a **capacitive** voltage divider.
*   **Clapp**: A Colpitts with an extra series capacitor for better stability.

## Crystal Oscillators (Fixed Frequency)
Uses a Quartz crystal for high stability.
*   **Pierce**: Crystal connects between Base and Collector.
*   **Overtone**: Crystal vibrates at an odd harmonic (3rd, 5th, etc.) for VHF use.

## Stability & Phase Noise
*   **Phase Noise**: Short-term frequency instability (jitter). Appears as noise sidebands. Widens the signal and degrades receiver selectivity.
*   **TCXO / OCXO**: Temperature compensated/controlled versions.

## Related
*   [[Crystals (Quartz)]]
*   [[Feedback Systems]]
