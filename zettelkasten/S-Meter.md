---
id: 202512302355
title: S-Meter (Signal Strength)
tags: ["ham-radio", "receivers", "measurements"]
created: 2025-12-30
type: permanent-note
modified: 2025-12-30
---

# S-Meter (Signal Strength)

The S-Meter indicates the relative strength of the received signal.

## Scale
*   **S1 to S9**: Each S-unit represents a **6 dB** difference (a factor of 4 in power, 2 in voltage).
*   **Above S9**: Calibrated in decibels (e.g., S9+10dB, S9+20dB).

## Standard Calibration (HF)
*   **S9** is defined as **50 $\mu$V** at the antenna input (assuming 50 $\Omega$ impedance).
*   **S8**: -6 dB relative to S9 = 25 $\mu$V.
*   **S7**: -12 dB relative to S9 = 12.5 $\mu$V.
*   ...
*   **S9+20dB**: 10x voltage of S9 = 500 $\mu$V.

*Note:* For VHF/UHF, S9 is sometimes defined as 5 $\mu$V, but HF standards (50 $\mu$V) are often used in exams.

## Operation
*   The S-meter is usually driven by the **AGC voltage** in the IF amplifier.
*   Because AGC is derived from the signal level, it provides a logarithmic measure suitable for the decibel scale.

## Related
*   [[Automatic Gain Control (AGC)]]
*   [[Decibels & Logarithms]]
