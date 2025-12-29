---
id: 202301011228
title: "Detectors (Demodulators)"
tags: ["ham-radio", "receivers"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Detectors (Demodulators)

## 1. AM Detection
*   **Envelope Detector:** A simple [[Semiconductors|Diode]] followed by an RC [[Filters & Resonance|low-pass filter]].
*   **Operation:** The diode rectifies the RF; the capacitor smooths the RF ripples, leaving the Audio envelope.

## 2. SSB and CW Detection
Requires re-inserting the missing carrier.
*   **Product Detector:** A [[Detectors, Oscillators & Mixers|mixer]] circuit.
*   **BFO (Beat Frequency Oscillator):** Generates a local carrier at the IF frequency.
*   **Mixing:** $f_{IF} \pm f_{BFO} = f_{Audio}$.
    *   *CW:* BFO is offset by ~800Hz to produce an audible tone.
    *   *SSB:* BFO is placed on the suppressed carrier frequency to restore voice pitch.

## 3. FM Detection
Converts frequency variations into voltage variations.
*   **Discriminator (Foster-Seeley):** Sensitive to amplitude variations (needs a Limiter).
*   **Ratio Detector:** Less sensitive to amplitude noise.
*   **PLL Detector:** A [[Detectors, Oscillators & Mixers|Phase Locked Loop]] tracks the input frequency. The error voltage driving the VCO is the demodulated audio.
*   **Limiter (Begrenzer):** An amplifier driven into saturation (clipping) placed before the FM detector. Removes AM noise (static/impulse noise).