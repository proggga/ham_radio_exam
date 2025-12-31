# Receiver Types

## 1. Crystal Receiver (Kristalontvanger)
The simplest radio receiver.
*   **Components:** [Antenna](../06_antennas/01_Antenna_Types.md), Tuning Circuit ($L+C$), [Detector](07_Detectors_Demodulators.md) ([Diode](../02_components/17_Diodes.md)), [Headphones](09_Station_Accessories.md).
*   **Characteristics:** No amplification (passive), poor selectivity (bandwidth determines which stations are heard, usually too wide), powered solely by the RF signal.
*   **Detector:** Originally a Galena crystal, now a Germanium diode (low voltage drop).

## 2. Tuned Radio Frequency (TRF / Rechtuit)
*   **Structure:** [RF Amplifier](../03_circuits/14_Amplifiers.md) -> [Detector](07_Detectors_Demodulators.md) -> [Audio Amplifier](../03_circuits/14_Amplifiers.md).
*   **Pros:** Simple, more sensitive than crystal receiver.
*   **Cons:**
    *   **[Selectivity](03_Receiver_Performance.md):** Poor at high frequencies ([Q-factor](../03_circuits/06_Quality_Factor_Q.md) is constant, so bandwidth $B = f/Q$ increases with frequency).
    *   **Instability:** High gain on the same frequency leads to oscillation.
    *   **Tuning:** Difficult to tune multiple stages simultaneously (ganged capacitors).

## 3. Regenerative Receiver (Mexicaanse Hond)
A TRF receiver with **Positive Feedback** (Meekoppeling).
*   **Operation:** Part of the output is fed back to the input in phase. This compensates for losses in the [LC circuit](../03_circuits/01_Reactive_Combinations.md), effectively raising $Q$.
*   **Point of Oscillation:** Most sensitive just before oscillation.
*   **Pros:** Extremely high gain and selectivity with very few components (e.g., single tube/transistor). Can demodulate [CW](../01_electricity/33_CW_Abbreviations_&_Prosigns.md)/[SSB](../01_electricity/34_Single_Sideband_SSB.md) if allowed to oscillate (autodyne).
*   **Cons:** Unstable. Can radiate interference (act as a transmitter) if feedback is excessive ("Mexican Dog" howling).

## 4. Direct Conversion (DC / Homodyne)
Mixes the incoming RF directly to Audio frequencies.
*   **Structure:** RF [Filter](../03_circuits/03_Filters_&_Resonance.md) -> [Mixer](../03_circuits/23_Mixers.md) -> Audio Amp.
*   **Local Oscillator (LO):** Tuned to the same frequency as the RF (or very close).
*   **Mixing:** $f_{RF} - f_{LO} = f_{Audio}$.
*   **Pros:** Simple architecture for [SSB](../01_electricity/34_Single_Sideband_SSB.md)/[CW](../01_electricity/33_CW_Abbreviations_&_Prosigns.md). No [Image Frequency](05_Image_Frequency.md) problem (Images are at 0Hz or fold over into audio).
*   **Cons:**
    *   **Audio Image:** Both USB and LSB are folded into the audio passband (unless phasing methods are used).
    *   **LO Radiation:** LO signal can leak to the antenna.
    *   **Microphonics/Hum:** High gain at audio frequencies makes it sensitive to mechanical vibration and hum.

## 5. Superheterodyne Receiver
The standard for modern radios. Converts all incoming signals to a fixed **Intermediate Frequency (IF)**.
*   See [Superheterodyne Receiver](02_Superheterodyne_Receiver.md) for full details.

---
[< Back to Section Index](README.md)