---
id: 202512292151
title: Quantisation
tags:
  - ham-radio
  - dsp
  - theory
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Quantisation

Quantisation is the process of assigning a discrete digital value to each analogue sample.

## Bit Depth
The number of bits used to represent each sample determines the resolution (dynamic range).
*   **Resolution**: $2^n$ levels (where $n$ is the number of bits).
*   **Example**: 8-bit = 256 levels; 16-bit = 65,536 levels.
*   **Dynamic Range**: Approximately $6 [[Decibels & Logarithms|dB]]$ per bit. (16-bit $\approx$ 96 dB).

## Quantisation Noise
The error between the actual infinite-precision analogue voltage and the nearest digital step.
*   This error manifests as noise in the signal.
*   Higher bit depth = Smaller steps = Lower quantisation noise.

## Conversion
*   **ADC (Analogue-to-Digital Converter)**: Performs sampling and quantisation.
*   **DAC (Digital-to-Analogue Converter)**: Reconstructs the analogue voltage from digital numbers.

## Related Notes
*   [[Sampling Theory]]
*   [[Digital Signal Processing (DSP)]]
*   [[Digital Components & Crystals]]
