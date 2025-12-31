# Transmitter Architecture

## 1. CW Transmitter
Simple On/Off keying of a carrier.
*   **Block Diagram:** [Oscillator](../03_circuits/20_Detectors,_Oscillators_&_Mixers.md) -> **Buffer/Isolator** -> Driver -> [Power Amplifier](02_Power_Amplifiers_and_Matching.md) (PA).
*   **Buffer (Scheidingstrap):** Prevents the PA/Driver load variations from pulling the oscillator frequency (Frequency Drift).
*   **Keying:** Usually keys the Driver stage to prevent oscillator instability ("Chirp"). Keying clicks are reduced by a **[Key](../04_receivers/09_Station_Accessories.md) Click [Filter](../03_circuits/03_Filters_&_Resonance.md)** (LC low pass).

## 2. FM Transmitter
Varying the frequency of the carrier.
*   **Direct [FM](../01_electricity/35_Frequency_Modulation_FM.md):** Modulating the VCO directly ([Reactance](../02_components/07_Reactance_Reactantie.md) Modulator / [Varicap](../02_components/22_Varicap_Capaciteitsdiode.md)).
*   **Indirect [FM](../01_electricity/35_Frequency_Modulation_FM.md) (Phase [Modulation](../01_electricity/31_Modulation_&_Digital_Signals.md)):** Modulating the phase of a crystal oscillator.
*   **Multipliers:** Frequency multipliers (Verdubbelaar/Verdrievoudiger) are often used to reach the final frequency.
    *   *Note:* Multiplication increases **Frequency** AND **Deviation**.
    *   *Example:* 12 MHz Osc $\times$ 12 $\to$ 144 MHz. 1 kHz deviation $\to$ 12 kHz deviation.

## 3. SSB Transmitter
Generates a [Single Sideband](../01_electricity/34_Single_Sideband_SSB.md) suppressed carrier signal.
1.  **Audio Amp:** Processes microphone signal.
2.  **Balanced Modulator:** Mixes Audio and Carrier. Outputs **DSB** (Double Sideband, Carrier suppressed). See [Mixers](../03_circuits/23_Mixers.md).
3.  **Sideband [Filter](../03_circuits/03_Filters_&_Resonance.md):** A sharp [Crystal Filter](../03_circuits/03_Filters_&_Resonance.md) selects *one* sideband (USB or LSB) and rejects the other.
4.  **[Mixer](../03_circuits/23_Mixers.md):** Up-converts the IF signal to the final RF frequency.
5.  **Linear Amplifier:** Amplifies the signal without distortion ([Class A or AB](../03_circuits/14_Amplifiers.md)). **Class C cannot be used for [SSB](../01_electricity/34_Single_Sideband_SSB.md)/[AM](../01_electricity/32_Analogue_Modulation_&_AM.md).**

## 4. Control Circuits
*   **VOX (Voice Operated Transmit):** Automatically switches to TX when you speak.
*   **ALC (Automatic Level Control):** Feedback loop that prevents overdriving the PA (prevents splatter).
*   **Speech Processor:** Compresses audio dynamic range to increase average talk power.

---
[< Back to Section Index](README.md)