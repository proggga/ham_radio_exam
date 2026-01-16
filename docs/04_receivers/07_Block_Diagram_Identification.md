# Block Diagram Identification (Exam Guide)

In the exam, you will often be asked to identify a device (Receiver, Transmitter, Transceiver) and its modulation type (AM, FM, SSB) based on a block diagram.

## 1. Receiver vs. Transmitter vs. Transceiver
Look at the **Signal Flow** (Arrows):
*   **Receiver (Ontvanger)**: Signal flows from **Antenna $\rightarrow$ Speaker**.
    *   *Input:* Antenna (Y symbol).
    *   *Output:* Speaker (Cone symbol) or Headphones.
*   **Transmitter (Zender)**: Signal flows from **Microphone $\rightarrow$ Antenna**.
    *   *Input:* Microphone (Circle/Line symbol).
    *   *Output:* Antenna.
*   **Transceiver (Zend/Ontvanger)**: Combined device.
    *   Look for **Switches** (T/R relays) changing the signal path.
    *   Often shares the Local Oscillator (VFO) and Filter between Tx and Rx.

## 2. Modulation Type Identification
Look for the **Detector** (in Rx) or **Modulator** (in Tx) stage.

### AM (Amplitude Modulation)
*   **Rx:** Envelope Detector (Diode symbol) usually after the IF amp.
*   **Tx:** Modulator acts on the Power Amplifier (PA) or Driver stage.

### FM (Frequency Modulation)
*   **Rx:**
    *   **Limiter (Begrenzer)**: Block before the detector to remove amplitude variations.
    *   **Discriminator / Ratio Detector**: Converts frequency changes to audio.
*   **Tx:**
    *   **Varicap/Reactance Modulator**: Connects directly to the Oscillator (VFO) to change frequency.
    *   *Key:* Modulation happens *at* the oscillator.

### SSB (Single Sideband / EZB)
*   **Rx:**
    *   **Product Detector**: A mixer stage at the end of the IF chain.
    *   **BFO (Beat Frequency Oscillator) / CIO (Carrier Insertion Oscillator)**: A crystal oscillator feeding the Product Detector.
    *   *Dead Giveaway:* Labels like "USB", "LSB", "BFO", or "Carrier".
*   **Tx:**
    *   **Balanced Modulator (Balansmodulator)**: Suppresses the carrier.
    *   **Sideband Filter**: Removes the unwanted sideband *immediately* after the modulator.

## 3. Architecture Types
*   **Direct Conversion (Zero-IF)**: RF $\rightarrow$ Mixer $\rightarrow$ Audio. No IF stages.
*   **Superheterodyne (Super)**: RF $\rightarrow$ Mixer $\rightarrow$ IF Amp $\rightarrow$ Detector.
*   **Double Superheterodyne (Dubbelsuper)**: Two Mixers, Two IF frequencies (e.g., 10.7 MHz and 455 kHz).

## Example Analysis (From User Image)
*   **Direction:** Antenna $\rightarrow$ Speaker. (It is a **Receiver**).
*   **Stages:** Two mixers (Double Super).
*   **Detector:** The final stage is a mixer fed by an oscillator labeled "USB" and "LSB".
*   **Conclusion:** The presence of USB/LSB oscillators identifies it as an **SSB (EZB) Receiver**.

---
[< Back to Section Index](README.md)