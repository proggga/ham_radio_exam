---
id: 202512292045
title: Bandwidth
tags: ["ham-radio", "circuits", "filters", "measurements"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Bandwidth

The bandwidth ($B$) of a filter or resonant circuit is the width of the frequency range where the power is at least half the maximum.

## Definition
*   **-3dB Points**: The upper and lower frequencies where signal drops by 3dB.
    *   Voltage is $\approx 0.707 \times Max$.
    *   Power is $0.5 \times Max$.

## Formula
$$B = \frac{f_{res}}{Q}$$
*   A higher $Q$ results in a narrower Bandwidth.

## Shape Factor
The ratio of bandwidth at -60dB (deep rejection) to bandwidth at -6dB.
*   Ideal Shape Factor is 1 (Rectangular filter).
*   Steep filters (Crystal/Mechanical) have better shape factors than simple LC filters.

## Related
*   [[Quality Factor (Q)]]
*   [[Decibels & Logarithms]]
