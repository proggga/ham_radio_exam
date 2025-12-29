---
id: 202512292040
title: Mixers
tags: ["ham-radio", "circuits", "receivers"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Mixers

Mixers are non-linear circuits that combine two frequencies ($f_1$ and $f_2$).

## Operation
Ideally, a mixer multiplies two signals. The output contains:
1.  **Sum**: $f_1 + f_2$
2.  **Difference**: $|f_1 - f_2|$
3.  Originals ($f_1, f_2$) and Harmonics (in practical mixers).

## Applications
*   **Superheterodyne Receiver**: Converts RF to a fixed Intermediate Frequency (IF).
*   **Product Detector**: Demodulates SSB/CW.
*   **Frequency Conversion**: Up-converters (Transmitters).

## Image Frequency (Spiegelfrequentie)
In a receiver mixer, an unwanted signal can produce the same IF as the desired signal.
*   **Formula**: $f_{image} = f_{wanted} \pm 2 \cdot f_{IF}$
*   **Mitigation**: Use input filters (Preselector) or a high 1st IF.

## Related
*   [[Superheterodyne Receiver]]
*   [[Distortion and Dissipation]] (Intermodulation)
