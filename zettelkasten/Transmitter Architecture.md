---
id: 202301011230
title: "Transmitter Architecture"
tags: ["ham-radio", "transmitters"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Transmitter Architecture

## 1. CW Transmitter
Simple On/Off keying of a carrier.
*   **Block Diagram:** [[Detectors, Oscillators & Mixers|Oscillator]] -> **Buffer/Isolator** -> Driver -> [[Power Amplifiers and Matching|Power Amplifier]] (PA).
*   **Buffer (Scheidingstrap):** Prevents the PA/Driver load variations from pulling the oscillator frequency (Frequency Drift).
*   **Keying:** Usually keys the Driver stage to prevent oscillator instability ("Chirp"). Keying clicks are reduced by a **[[Station Accessories|Key]] Click [[Filters & Resonance|Filter]]** (LC low pass).

## 2. FM Transmitter
Varying the frequency of the carrier.
*   **Direct [[Frequency Modulation (FM)|FM]]:** Modulating the VCO directly ([[Reactance (Reactantie)|Reactance]] Modulator / [[Varicap (Capaciteitsdiode)|Varicap]]).
*   **Indirect [[Frequency Modulation (FM)|FM]] (Phase [[Modulation & Digital Signals|Modulation]]):** Modulating the phase of a crystal oscillator.
*   **Multipliers:** Frequency multipliers (Verdubbelaar/Verdrievoudiger) are often used to reach the final frequency.
    *   *Note:* Multiplication increases **Frequency** AND **Deviation**.
    *   *Example:* 12 MHz Osc $\times$ 12 $\to$ 144 MHz. 1 kHz deviation $\to$ 12 kHz deviation.

## 3. SSB Transmitter
Generates a [[Single Sideband (SSB)|Single Sideband]] suppressed carrier signal.
1.  **Audio Amp:** Processes microphone signal.
2.  **Balanced Modulator:** Mixes Audio and Carrier. Outputs **DSB** (Double Sideband, Carrier suppressed). See [[Mixers]].
3.  **Sideband [[Filters & Resonance|Filter]]:** A sharp [[Filters & Resonance|Crystal Filter]] selects *one* sideband (USB or LSB) and rejects the other.
4.  **[[Mixers|Mixer]]:** Up-converts the IF signal to the final RF frequency.
5.  **Linear Amplifier:** Amplifies the signal without distortion ([[Amplifiers|Class A or AB]]). **Class C cannot be used for [[Single Sideband (SSB)|SSB]]/[[Analogue Modulation & AM|AM]].**

## 4. Control Circuits
*   **VOX (Voice Operated Transmit):** Automatically switches to TX when you speak.
*   **ALC (Automatic Level Control):** Feedback loop that prevents overdriving the PA (prevents splatter).
*   **Speech Processor:** Compresses audio dynamic range to increase average talk power.