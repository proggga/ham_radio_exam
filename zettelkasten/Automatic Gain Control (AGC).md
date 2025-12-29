---
id: 202512292058
title: Automatic Gain Control (AGC)
tags: ["ham-radio", "receivers", "circuits"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Automatic Gain Control (AGC)

AGC (Dutch: AVR - Automatische Volume Regeling) keeps the audio volume constant despite fading (QSB) or large differences in signal strength between stations.

## Operation
1.  A DC voltage is derived from the detector output.
2.  This voltage is proportional to the incoming signal strength.
3.  It is fed back to the **RF** and **IF** amplifiers.
4.  **Strong Signal** $\rightarrow$ High AGC voltage $\rightarrow$ Reduces Gain.
5.  **Weak Signal** $\rightarrow$ Low AGC voltage $\rightarrow$ Maximum Gain.

## Related
*   [[Superheterodyne Principle]]
*   [[Amplifiers]]
