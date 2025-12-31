---
id: 202512292056
title: Superheterodyne Principle
tags: ["ham-radio", "receivers", "theory"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Superheterodyne Principle

The **Superheterodyne** receiver converts any incoming RF signal to a fixed **Intermediate Frequency (IF)** before amplification and detection. This allows for superior selectivity and sensitivity compared to direct conversion or TRF receivers.

## Block Diagram
1.  **RF Amplifier / Preselector**: [[Filters & Resonance|Filters]] and amplifies the antenna signal.
    *   *Purpose*: Improves Signal-to-[[AC Signals & Noise|Noise]] ratio and rejects Image Frequencies.
2.  **[[Mixers|Mixer]] (Mengtrap)**: Combines RF with Local Oscillator signal.
    *   *Output*: Sum and Difference frequencies ($f_{RF} \pm f_{LO}$).
    *   *Caveat:* **Frequency Deviation** ($\Delta f$) of an [[Frequency Modulation (FM)|FM]] signal is **preserved** during mixing. It remains the same at the IF.
3.  **Local Oscillator (LO)**: Generates a tunable frequency ($f_{LO}$).
    *   Tuning maintains: $|f_{RF} - f_{LO}| = f_{IF}$.
4.  **IF Filter**: Determines the main selectivity ([[Bandwidth]]) of the receiver.
5.  **IF Amplifier**: Provides the bulk of the receiver's gain at a fixed frequency.
6.  **Detector**: Demodulates the signal to Audio.
7.  **Audio Amplifier**: Drives the speaker.

## Related
*   [[Mixers]]
*   [[Image Frequency]]
