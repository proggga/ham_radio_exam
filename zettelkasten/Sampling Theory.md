---
id: 202512292150
title: Sampling Theory
tags:
  - ham-radio
  - dsp
  - theory
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Sampling Theory

Sampling is the process of taking snapshots of an analogue signal's voltage at regular intervals to create a digital representation.

## Nyquist-Shannon Theorem
To accurately reconstruct a continuous signal, the **Sample Rate ($f_s$)** must be at least **twice** the highest frequency component ($f_{max}$) of the signal.

*   **Formula**: $f_s > 2 \cdot f_{max}$
*   **Nyquist Frequency**: The highest frequency that can be sampled correctly ($f_s/2$).

## Aliasing
If the signal contains frequencies higher than the Nyquist limit ($> f_s/2$), these high frequencies are "folded back" and appear as false low frequencies (aliases).
*   **Analogy**: Wagon wheels appearing to spin backwards in movies.
*   **Solution**: An **Anti-Aliasing [[Filters & Resonance|Filter]]** (Low Pass [[Filters & Resonance|Filter]]) must be placed before the [[Digital Processing Techniques|ADC]] to remove frequencies above $f_s/2$.

## Related Notes
*   [[Digital Signal Processing (DSP)]]
*   [[Quantisation]]
*   [[Filters & Resonance]]
