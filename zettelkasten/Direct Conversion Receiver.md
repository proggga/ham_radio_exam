id: 202512292200
title: Direct Conversion Receiver
tags: ["amplifiers", "circuits", "filters", "formulas", "modes", "oscillators", "receivers"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29

aliases: ["DC-ontvanger", "Directe Conversie Ontvanger", "Homodyne"]

# Direct Conversion Receiver (DC-ontvanger)

A **Direct Conversion Receiver** (also known as Homodyne or Synchrodyne) converts the incoming Radio Frequency (RF) signal directly to Audio Frequency (AF) in a single mixing stage.

## Principle of Operation
*   **Mixing**: The RF signal is mixed with a Local Oscillator (LO) signal.
*   **LO Frequency**: The LO is tuned to the **exact same frequency** as the incoming carrier (or suppressed carrier).
*   **Intermediate Frequency (MF)**: Since $f_{RF} \approx f_{LO}$, the resulting difference frequency is $0 \text{ Hz}$ (or audio frequencies). There is **no** IF amplifier stage like in a [[Superheterodyne Receiver]].

## Block Diagram Structure
1.  **HF Amplifier**: Amplifies weak antenna signals.
2.  **Mixer**: Combines RF and LO.
3.  **Low Pass Filter (LPF)**: Removes the sum frequencies ($f_{RF} + f_{LO}$) and passes the audio difference frequencies. **This filter determines the receiver's bandwidth.**
4.  **LF (Audio) Amplifier**: Amplifies the audio for the speaker/headphones.

## Characteristics
*   **Modes**:
    *   Excellent for **[[Single Sideband (SSB)|SSB]]** and **[[CW Abbreviations & Prosigns|CW]]**.
    *   Can receive **[[Analogue Modulation & AM|AM]]**, but requires very precise tuning to achieve "Zero Beat" (where $f_{LO} = f_{Carrier}$). If slightly off, a loud audible tone (heterodyne) is heard.
*   **Selectivity**: Determined entirely by the audio Low Pass Filter.
*   **Image Frequencies**: Does not suffer from image frequency problems in the traditional sense (like superhets), but "audio images" (the other sideband) can be an issue in simple designs.

## Pros & Cons
*   **Pros**: Simple design (few components), no expensive IF filters, clean audio.
*   **Cons**: Susceptible to "AC hum" and microphonics, LO leakage to antenna, requires stable LO.

## Related Notes
*   [[Receiver Types]]
*   [[Superheterodyne Receiver]]
*   [[Mixers]]
