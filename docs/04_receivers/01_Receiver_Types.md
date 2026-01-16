id: 202301011226
title: "Receiver Types"
tags: ["amplifiers", "filters", "formulas", "modes", "oscillators", "receivers", "semiconductors"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29

aliases: ["Ontvangertypes"]

# Receiver Types

## 1. Crystal Receiver (Kristalontvanger)
The simplest radio receiver.
*   **Components:** [Antenna](../06_antennas/01_Antenna_Types.md), Tuning Circuit ($L+C$), [Detector](04_Detectors_Demodulators.md) ([Diode](../02_components/07_Diodes.md)), [Headphones](07_Station_Accessories.md).
*   **Characteristics:** No amplification (passive), poor selectivity (bandwidth determines which stations are heard, usually too wide), powered solely by the RF signal.
*   **Detector:** Originally a Galena crystal, now a Germanium diode (low voltage drop).

## 2. Tuned Radio Frequency (TRF / Rechtuit)
*   **Structure:** [RF Amplifier](../03_circuits/06_Amplifiers.md) -> [Detector](04_Detectors_Demodulators.md) -> [Audio Amplifier](../03_circuits/06_Amplifiers.md).
*   **Pros:** Simple, more sensitive than crystal receiver.
*   **Cons:**
    *   **[Selectivity](05_Receiver_Performance.md):** Poor at high frequencies (Q-factor is constant, so bandwidth $B = f/Q$ increases with frequency).
    *   **Instability:** High gain on the same frequency leads to oscillation.
    *   **Tuning:** Difficult to tune multiple stages simultaneously (ganged capacitors).

## 3. Regenerative Receiver (Mexicaanse Hond)
A TRF receiver with **Positive Feedback** (Meekoppeling).
*   **Operation:** Part of the output is fed back to the input in phase. This compensates for losses in the [LC circuit](../03_circuits/01_Reactive_Combinations.md), effectively raising $Q$.
*   **Point of Oscillation:** Most sensitive just before oscillation.
*   **Pros:** Extremely high gain and selectivity with very few components (e.g., single tube/transistor). Can demodulate CW/SSB if allowed to oscillate (autodyne).
*   **Cons:** Unstable. Can radiate interference (act as a transmitter) if feedback is excessive ("Mexican Dog" howling).

## 4. Direct Conversion (DC / Homodyne)
Mixes the incoming RF directly to Audio frequencies.
*   **Structure:** RF [Filter](../03_circuits/03_Filters_&_Resonance.md) -> Mixer -> Audio Amp.
*   **Local Oscillator (LO):** Tuned to the same frequency as the RF (or very close).
*   **Mixing:** $f_{RF} - f_{LO} = f_{Audio}$.
*   **Pros:** Simple architecture for SSB/CW. No [Image Frequency](../09_interference/04_Image_Frequency.md) problem (Images are at 0Hz or fold over into audio).
*   **Cons:**
    *   **Audio Image:** Both USB and LSB are folded into the audio passband (unless phasing methods are used).
    *   **LO Radiation:** LO signal can leak to the antenna.
    *   **Microphonics/Hum:** High gain at audio frequencies makes it sensitive to mechanical vibration and hum.
*   See Direct Conversion Receiver for full details.

## 5. Superheterodyne Receiver
The standard for modern radios. Converts all incoming signals to a fixed **Intermediate Frequency (IF)**.
*   See [Superheterodyne Receiver](02_Superheterodyne_Receiver.md) for full details.

---
[< Back to Section Index](README.md)