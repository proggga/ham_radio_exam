---
id: 202512292040
title: Mixers
tags: ["ham-radio", "circuits", "receivers"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Mixers

[[Detectors, Oscillators & Mixers|Mixers]] are non-linear circuits that combine two frequencies ($f_1$ and $f_2$).

## Operation
Ideally, a mixer multiplies two signals. The output contains:
1.  **Sum**: $f_1 + f_2$
2.  **Difference**: $|f_1 - f_2|$
3.  Originals ($f_1, f_2$) - depending on mixer type.

## Mixer Types (Exam Topic)
*   **Unbalanced Mixer**: Output contains Sum, Difference, Original $f_1$, and Original $f_2$.
*   **Single Balanced Mixer (Balanced Modulator)**:
    *   Suppresses **one** input (usually the Carrier).
    *   Output: Sidebands (Sum + Diff) only. No Carrier.
    *   *Use:* Generating DSB (Double Sideband) for [[Single Sideband (SSB)|SSB]] transmitters.
*   **Double Balanced Mixer (DBM)**:
    *   Suppresses **both** inputs (Carrier and Audio/RF).
    *   Output: Sum and Difference frequencies only.
    *   *Use:* High-performance receivers, Up/Down converters.

## Applications
*   **[[Superheterodyne Receiver]]**: Converts RF to a fixed Intermediate Frequency (IF).
*   **Product Detector**: Demodulates SSB/[[CW Abbreviations & Prosigns|CW]] (mixes IF with BFO).
*   **Modulators**: Creating [[Analogue Modulation & AM|AM]] (unbalanced) or DSB (balanced).

## Related
*   [[Superheterodyne Receiver]]
*   [[Distortion and Dissipation]] (Intermodulation)
