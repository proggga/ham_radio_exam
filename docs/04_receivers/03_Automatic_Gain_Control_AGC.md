# Automatic Gain Control (AGC)

AGC (also known as AVC - Automatic Volume Control) keeps the receiver's audio output volume constant despite large variations in incoming RF signal strength.

## Operation
1.  **Detection**: A sample of the IF signal is rectified (detected) to produce a DC voltage proportional to signal strength.
2.  **Filtering**: The DC is filtered (RC time constant) to remove audio modulation but track fading ([QSB](../07_propagation/16_Fading_QSB.md)).
    *   *Fast AGC:* For [CW](../01_electricity/33_CW_Abbreviations_&_Prosigns.md)/Data (reacts quickly).
    *   *Slow AGC:* For [SSB](../01_electricity/34_Single_Sideband_SSB.md) (holds gain during pauses in speech).
3.  **Derivation from IF signal**: The IF signal is derived from the mixer stage, where the RF signal is mixed with the local oscillator signal to produce the IF signal.
4.  **Control Loop**: The DC voltage is applied to the grids/gates/bases of the RF and IF amplifiers, creating a control loop that adjusts the gain of the amplifiers based on the signal strength.
    *   Strong Signal $\rightarrow$ High negative DC $\rightarrow$ Reduced Gain.
    *   Weak Signal $\rightarrow$ Low/Zero DC $\rightarrow$ Maximum Gain.

## Functions
*   Prevents overloading of IF/Audio stages.
*   Compensates for fading (QSB).
*   Drives the **[S-Meter](08_S-Meter.md)** (Signal Strength Meter).

---
[< Back to Section Index](README.md)