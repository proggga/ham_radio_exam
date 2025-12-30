# Transmitter Architecture

## 1. CW Transmitter
Simple On/Off keying of a carrier.
*   **Block Diagram:** Oscillator -> **Buffer/Isolator** -> Driver -> Power Amplifier (PA).
*   **Buffer (Scheidingstrap):** Prevents the PA/Driver load variations from pulling the oscillator frequency (Frequency Drift).
*   **Keying:** Usually keys the Driver stage to prevent oscillator instability ("Chirp"). Keying clicks are reduced by a **Key Click Filter** (LC low pass).

## 2. FM Transmitter
Varying the frequency of the carrier.
*   **Direct FM:** Modulating the VCO directly (Reactance Modulator / Varicap).
*   **Indirect FM (Phase Modulation):** Modulating the phase of a crystal oscillator.
*   **Multipliers:** Frequency multipliers (Verdubbelaar/Verdrievoudiger) are often used to reach the final frequency.
    *   *Note:* Multiplication increases **Frequency** AND **Deviation**.
    *   *Example:* 12 MHz Osc $\times$ 12 $\to$ 144 MHz. 1 kHz deviation $\to$ 12 kHz deviation.

## 3. SSB Transmitter
Generates a Single Sideband suppressed carrier signal.
1.  **Audio Amp:** Processes microphone signal.
2.  **Balanced Modulator:** Mixes Audio and Carrier. Outputs **DSB** (Double Sideband, Carrier suppressed). See Mixers.
3.  **Sideband Filter:** A sharp Crystal Filter selects *one* sideband (USB or LSB) and rejects the other.
4.  **Mixer:** Up-converts the IF signal to the final RF frequency.
5.  **Linear Amplifier:** Amplifies the signal without distortion (Class A or AB). **Class C cannot be used for SSB/AM.**

## 4. Control Circuits
*   **VOX (Voice Operated Transmit):** Automatically switches to TX when you speak.
*   **ALC (Automatic Level Control):** Feedback loop that prevents overdriving the PA (prevents splatter).
*   **Speech Processor:** Compresses audio dynamic range to increase average talk power.

---
[< Back to Section Index](README.md)