# Mixers

[Mixers](20_Detectors,_Oscillators_&_Mixers.md) are non-linear circuits that combine two frequencies ($f_1$ and $f_2$).

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
    *   *Use:* Generating DSB (Double Sideband) for [SSB](../01_electricity/34_Single_Sideband_SSB.md) transmitters.
*   **Double Balanced Mixer (DBM)**:
    *   Suppresses **both** inputs (Carrier and Audio/RF).
    *   Output: Sum and Difference frequencies only.
    *   *Use:* High-performance receivers, Up/Down converters.

## Applications
*   **[Superheterodyne Receiver](../04_receivers/02_Superheterodyne_Receiver.md)**: Converts RF to a fixed Intermediate Frequency (IF).
*   **Product Detector**: Demodulates [SSB](../01_electricity/34_Single_Sideband_SSB.md)/[CW](../01_electricity/33_CW_Abbreviations_&_Prosigns.md) (mixes IF with BFO).
*   **Modulators**: Creating [AM](../01_electricity/32_Analogue_Modulation_&_AM.md) (unbalanced) or DSB (balanced).

---
[< Back to Section Index](README.md)