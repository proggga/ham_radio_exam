---
id: 202301011227
title: "Superheterodyne Receiver"
tags: ["ham-radio", "receivers", "index"]
created: 2025-12-29
type: index
modified: 2025-12-29
---

# Superheterodyne Receiver

The Superheterodyne ("Super") receiver converts any incoming RF signal to a fixed **Intermediate Frequency (IF)** for processing.

## Architecture (Block Diagram)
1.  **RF Amplifier / Preselector**: Selects the desired band, amplifies weak signals, and improves Signal-to-Noise ratio. Provides **Far-off Selectivity** (Image rejection).
2.  **Mixer**: Mixes RF ($f_{in}$) with Local Oscillator ($f_{LO}$). Output contains Sum and Difference.
3.  **Local Oscillator (VFO/LO)**: Tunable oscillator. $f_{LO}$ tracks $f_{in}$ to maintain a constant difference ($f_{IF}$).
4.  **IF Amplifier (Middenfrequent)**: Provides most of the receiver's gain and **Close-in Selectivity** (using sharp filters like Crystal or Ceramic filters).
    *   *Fixed Frequency:* Usually 455 kHz or 9 MHz (or 10.7 MHz).
5.  **Detector / Demodulator**: Recovers the audio information.
6.  **AF Amplifier**: Amplifies audio for speaker/headphones.
7.  **AGC (Automatic Gain Control)**: Derives a DC voltage from the signal strength to reduce gain of RF/IF stages, keeping volume constant.
8.  **BFO (Beat Frequency Oscillator)**: Needed for CW/SSB detection.

## Mixing (Frequency Conversion)
*   **Down-Conversion (Ondermenging):** $f_{LO}$ is lower than $f_{RF}$.
    *   $f_{IF} = f_{RF} - f_{LO}$.
*   **Up-Conversion (Bovenmenging):** $f_{LO}$ is higher than $f_{RF}$.
    *   $f_{IF} = f_{LO} - f_{RF}$.

## Double Superheterodyne (Dubbelsuper)
Uses two IF stages (e.g., 1st IF = 45 MHz, 2nd IF = 455 kHz).
*   **High 1st IF**: Improves **Image Rejection** (Image is far away).
*   **Low 2nd IF**: Improves **Selectivity** (easier to build sharp filters at low freq).

## Issues
*   **[[Image Frequency]] (Spiegelfrequentie)**: An unwanted signal at $f_{image} = f_{RF} \pm 2f_{IF}$ that also mixes to the IF.
*   **Spurious Responses**: Intermodulation products from strong nearby signals.

## Related
