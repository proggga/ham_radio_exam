---
id: 202512292010
title: Decibels & Logarithms
tags: ["ham-radio", "basic-skills", "math", "measurements"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Decibels & Logarithms

Radio signals vary wildly in strength, often by factors of millions. The **Decibel (dB)** is a logarithmic unit used to express ratios (like gain or loss) in a manageable way.

## Logarithms
The logarithm is the power to which 10 must be raised to get a number.
*   $\log(100) = 2$ because $10^2 = 100$.
*   $\log(1000) = 3$.

## The Decibel Formula
*   **Power**: $dB = 10 \times \log_{10}(\frac{P_{out}}{P_{in}})$
*   **Voltage**: $dB = 20 \times \log_{10}(\frac{U_{out}}{U_{in}})$ (assuming equal impedance)

## Rules of Thumb
Calculating exact logs in your head is hard, but these rules cover most exam questions:
*   **+3 dB** $\approx$ 2x Power
*   **+6 dB** $\approx$ 4x Power (2x Voltage)
*   **+10 dB** = 10x Power
*   **-3 dB** $\approx$ Half Power (0.5x)
*   **-10 dB** = 1/10th Power (0.1x)

## Related
*   [[Antenna Types]] (Gain)
*   [[Amplifiers]] (Amplification)
