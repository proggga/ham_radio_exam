---
id: 202512292058
title: Automatic Gain Control (AGC)
tags: ["ham-radio", "receivers", "circuits"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Automatic Gain Control (AGC)

AGC (also known as AVC - Automatic Volume Control) keeps the receiver's audio output volume constant despite large variations in incoming RF signal strength.

## Operation
1.  **Detection**: A sample of the IF signal is rectified (detected) to produce a DC voltage proportional to signal strength.
2.  **Filtering**: The DC is filtered (RC time constant) to remove audio modulation but track fading ([[Fading (QSB)|QSB]]).
    *   *Fast AGC:* For [[CW Abbreviations & Prosigns|CW]]/Data (reacts quickly).
    *   *Slow AGC:* For [[Single Sideband (SSB)|SSB]] (holds gain during pauses in speech).
3.  **Derivation from IF signal**: The IF signal is derived from the mixer stage, where the RF signal is mixed with the local oscillator signal to produce the IF signal.
4.  **Control Loop**: The DC voltage is applied to the grids/gates/bases of the RF and IF amplifiers, creating a control loop that adjusts the gain of the amplifiers based on the signal strength.
    *   Strong Signal $\rightarrow$ High negative DC $\rightarrow$ Reduced Gain.
    *   Weak Signal $\rightarrow$ Low/Zero DC $\rightarrow$ Maximum Gain.

## Functions
*   Prevents overloading of IF/Audio stages.
*   Compensates for fading (QSB).
*   Drives the **[[S-Meter]]** (Signal Strength Meter).

## Related
*   [[Superheterodyne Receiver]]
*   [[Measurements]] (S-Meter)
*   [[Amplifiers]]
