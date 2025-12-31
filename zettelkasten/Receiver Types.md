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
*   **Components:** [[Antenna Types|Antenna]], Tuning Circuit ($L+C$), [[Detectors (Demodulators)|Detector]] ([[Diodes|Diode]]), [[Station Accessories|Headphones]].
*   **Characteristics:** No amplification (passive), poor selectivity (bandwidth determines which stations are heard, usually too wide), powered solely by the RF signal.
*   **Detector:** Originally a Galena crystal, now a Germanium diode (low voltage drop).

## 2. Tuned Radio Frequency (TRF / Rechtuit)
*   **Structure:** [[Amplifiers|RF Amplifier]] -> [[Detectors (Demodulators)|Detector]] -> [[Amplifiers|Audio Amplifier]].
*   **Pros:** Simple, more sensitive than crystal receiver.
*   **Cons:**
    *   **[[Receiver Performance|Selectivity]]:** Poor at high frequencies ([[Quality Factor (Q)|Q-factor]] is constant, so bandwidth $B = f/Q$ increases with frequency).
    *   **Instability:** High gain on the same frequency leads to oscillation.
    *   **Tuning:** Difficult to tune multiple stages simultaneously (ganged capacitors).

## 3. Regenerative Receiver (Mexicaanse Hond)
A TRF receiver with **Positive Feedback** (Meekoppeling).
*   **Operation:** Part of the output is fed back to the input in phase. This compensates for losses in the [[Reactive Combinations|LC circuit]], effectively raising $Q$.
*   **Point of Oscillation:** Most sensitive just before oscillation.
*   **Pros:** Extremely high gain and selectivity with very few components (e.g., single tube/transistor). Can demodulate [[CW Abbreviations & Prosigns|CW]]/[[Single Sideband (SSB)|SSB]] if allowed to oscillate (autodyne).
*   **Cons:** Unstable. Can radiate interference (act as a transmitter) if feedback is excessive ("Mexican Dog" howling).

## 4. Direct Conversion (DC / Homodyne)
Mixes the incoming RF directly to Audio frequencies.
*   **Structure:** RF [[Filters & Resonance|Filter]] -> [[Mixers|Mixer]] -> Audio Amp.
*   **Local Oscillator (LO):** Tuned to the same frequency as the RF (or very close).
*   **Mixing:** $f_{RF} - f_{LO} = f_{Audio}$.
*   **Pros:** Simple architecture for [[Single Sideband (SSB)|SSB]]/[[CW Abbreviations & Prosigns|CW]]. No [[Image Frequency]] problem (Images are at 0Hz or fold over into audio).
*   **Cons:**
    *   **Audio Image:** Both USB and LSB are folded into the audio passband (unless phasing methods are used).
    *   **LO Radiation:** LO signal can leak to the antenna.
    *   **Microphonics/Hum:** High gain at audio frequencies makes it sensitive to mechanical vibration and hum.

## 5. Superheterodyne Receiver
The standard for modern radios. Converts all incoming signals to a fixed **Intermediate Frequency (IF)**.
*   See [[Superheterodyne Receiver]] for full details.

## Related