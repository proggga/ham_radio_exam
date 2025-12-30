# Receiver Types

## 1. Crystal Receiver (Kristalontvanger)
The simplest radio receiver.
*   **Components:** Antenna, Tuning Circuit ($L+C$), Detector (Diode), Headphones.
*   **Characteristics:** No amplification (passive), poor selectivity, powered solely by the RF signal.

## 2. Tuned Radio Frequency (TRF / Rechtuit)
*   **Structure:** RF Amplifier -> Detector -> Audio Amplifier.
*   **Pros:** Simple, sensitive.
*   **Cons:** Poor selectivity at high frequencies. Instability (oscillations) if gain is too high on one frequency.

## 3. Regenerative Receiver (Mexicaanse Hond)
A TRF receiver with **Positive Feedback** (Meekoppeling).
*   **Operation:** Part of the output is fed back to the input in phase. This increases the $Q$-factor and Gain.
*   **Pros:** Very high gain and selectivity with few components. Can demodulate CW/SSB if oscillating.
*   **Cons:** Unstable. Can radiate interference (act as a transmitter) if feedback is excessive.

## 4. Direct Conversion (DC / Homodyne)
Mixes the incoming RF directly to Audio frequencies.
*   **Local Oscillator (LO):** Tuned to the same frequency as the RF (or very close). See Oscillators.
*   **Mixing:** $f_{RF} - f_{LO} = f_{Audio}$.
*   **Pros:** Simple architecture for SSB/CW. No Image Frequency problem (Images are at 0Hz or fold over into audio).
*   **Cons:** Susceptible to hum, microphonics, and LO radiation.

---
[< Back to Section Index](README.md)