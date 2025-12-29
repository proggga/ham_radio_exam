---
id: 202301011226
title: "Receiver Types"
tags: ["ham-radio", "receivers"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Receiver Types

## 1. Crystal Receiver (Kristalontvanger)
The simplest radio receiver.
*   **Components:** [[Antenna Types|Antenna]], Tuning Circuit ($L+C$), [[Detectors (Demodulators)|Detector]] (Diode), Headphones.
*   **Characteristics:** No amplification (passive), poor selectivity, powered solely by the RF signal.

## 2. Tuned Radio Frequency (TRF / Rechtuit)
*   **Structure:** [[Amplifiers|RF Amplifier]] -> [[Detectors (Demodulators)|Detector]] -> [[Amplifiers|Audio Amplifier]].
*   **Pros:** Simple, sensitive.
*   **Cons:** Poor selectivity at high frequencies. Instability (oscillations) if gain is too high on one frequency.

## 3. Regenerative Receiver (Mexicaanse Hond)
A TRF receiver with **Positive Feedback** (Meekoppeling).
*   **Operation:** Part of the output is fed back to the input in phase. This increases the $Q$-factor and Gain.
*   **Pros:** Very high gain and selectivity with few components. Can demodulate CW/SSB if oscillating.
*   **Cons:** Unstable. Can radiate interference (act as a transmitter) if feedback is excessive.

## 4. Direct Conversion (DC / Homodyne)
Mixes the incoming RF directly to Audio frequencies.
*   **Local Oscillator (LO):** Tuned to the same frequency as the RF (or very close). See [[Detectors, Oscillators & Mixers|Oscillators]].
*   **Mixing:** $f_{RF} - f_{LO} = f_{Audio}$.
*   **Pros:** Simple architecture for SSB/CW. No Image Frequency problem (Images are at 0Hz or fold over into audio).
*   **Cons:** Susceptible to hum, microphonics, and LO radiation.