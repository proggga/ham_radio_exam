id: 202301011230
title: "Transmitter Architecture"
tags: ["amplifiers", "filters", "modes", "oscillators", "transmitters"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29

aliases: ["Zenderopbouw"]

# Transmitter Architecture

## 1. CW Transmitter
Simple On/Off keying of a carrier.
*   **Block Diagram:** [Oscillator](../03_circuits/07_Detectors,_Oscillators_&_Mixers.md) -> **Buffer/Isolator** -> Driver -> [Power Amplifier](02_Power_Amplifiers_and_Matching.md) (PA).
*   **Buffer (Scheidingstrap):** Prevents the PA/Driver load variations from pulling the oscillator frequency (Frequency Drift).
*   **Keying:** Usually keys the Driver stage to prevent oscillator instability ("Chirp"). Keying clicks are reduced by a **[Key](../04_receivers/07_Station_Accessories.md) Click [Filter](../03_circuits/03_Filters_&_Resonance.md)** (LC low pass).

## 2. FM Transmitter
Varying the frequency of the carrier.
*   **Direct FM:** Modulating the VCO directly (Reactance Modulator / [Varicap](../02_components/10_Varicap.md)).
*   **Indirect FM (Phase [Modulation](../01_electricity/19_Modulation_&_Digital_Signals.md)):** Modulating the phase of a crystal oscillator.
*   **Multipliers:** Frequency multipliers (Verdubbelaar/Verdrievoudiger) are often used to reach the final frequency.
    *   *Note:* Multiplication increases **Frequency** AND **Deviation**.
    *   *Example:* 12 MHz Osc x 12 -> 144 MHz. 1 kHz deviation -> 12 kHz deviation.

## 3. SSB Transmitter
Generates a Single Sideband suppressed carrier signal.
1.  **Audio Amp:** Processes microphone signal.
2.  **Balanced Modulator:** Mixes Audio and Carrier. Outputs **DSB** (Double Sideband, Carrier suppressed). See Mixers.
3.  **Sideband [Filter](../03_circuits/03_Filters_&_Resonance.md):** A sharp [Crystal Filter](../03_circuits/03_Filters_&_Resonance.md) selects *one* sideband (USB or LSB) and rejects the other.
4.  **Mixer:** Up-converts the IF signal to the final RF frequency.
5.  **Linear Amplifier:** Amplifies the signal without distortion ([Class A or AB](../03_circuits/06_Amplifiers.md)). **Class C cannot be used for SSB/AM.**

## 4. Control Circuits
*   **VOX (Voice Operated Transmit):** Automatically switches to TX when you speak.
*   **ALC (Automatic Level Control):** Feedback loop that prevents overdriving the PA (prevents splatter).
*   **Speech Processor:** Compresses audio dynamic range to increase average talk power.

---
[< Back to Section Index](README.md)