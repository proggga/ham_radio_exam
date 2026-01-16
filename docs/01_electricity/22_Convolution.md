id: 202501101403
title: Convolution
tags: ["dsp", "filters"]
created: 2025-01-10
type: permanent-note
modified: 2025-01-10

aliases: ["Convolutie"]

# Convolution (Convolutie)

**Convolution** is the fundamental mathematical operation in [DSP](21_Digital_Signal_Processing_DSP.md) used to apply filters to signals.

## Concept
It combines two signals:
1.  **Input Signal ($x[n]$)**: The stream of digital samples coming from the ADC.
2.  **Impulse Response ($h[n]$)**: The filter's "fingerprint" (how it reacts to a single "bang").

## Operation
*   The impulse response "slides" over the input signal.
*   At each step, we multiply overlapping samples and sum the results.
*   **Result**: The filtered Output Signal ($y[n]$).
*   *Analogy:* Like calculating a moving average, but with weighted values.

## Domains
*   **Time Domain**: Convolution ($x * h$). Computationally expensive for long filters.
*   **Frequency Domain**: Multiplication ($X \cdot H$).
    *   Convolution in Time = Multiplication in Frequency.
    *   Fastest method: FFT $\rightarrow$ Multiply $\rightarrow$ Inverse FFT.

## Application
*   **FIR Filters**: An FIR filter *is* a hardware implementation of convolution. The "taps" (coefficients) are simply the values of the Impulse Response.

---
[< Back to Section Index](README.md)