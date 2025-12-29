# Types of Interference

## 1. Receiver Overload
*   **Blocking (Blokkering):** A very strong signal (even if off-frequency) overloads the RF front-end of a receiver.
    *   **Effect:** The receiver goes deaf (desensitized) or gain fluctuates.
    *   **Mechanism:** The input transistor/FET is driven into saturation or cutoff by the strong signal voltage.

## 2. Mixing Products
*   **Intermodulation:** Two strong signals ($f_1$ and $f_2$) mix in a non-linear stage (receiver front-end or transmitter PA) to create "phantom" signals.
    *   **Formula:** $f_{IMD} = 2f_1 - f_2$ or $2f_2 - f_1$ (3rd Order). These often fall close to the original frequencies. See [Receiver Performance](../04_receivers/04_performance.md).
    *   **Example:** Signal A (145.0) and Signal B (145.1) produce intermod at 144.9 and 145.2.
*   **Cross-Modulation:** The modulation of a strong unwanted signal is transferred ("crosses over") to the weaker wanted signal.
    *   **Effect:** You hear the strong station in the background of the station you are trying to listen to.

## 3. Audio Interference
*   **LFD (Low Frequency Detection):** Also called "Audio Rectification".
    *   **Mechanism:** RF energy is picked up by cables (speaker, microphone, mains) and enters an audio amplifier. A PN junction ([Transistor/Diode](../02_components/05_semiconductors.md)) acts as a detector (rectifier).
    *   **Effect:**
        *   **AM:** You hear the voice clearly.
        *   **SSB:** You hear muffled, distorted "Donald Duck" sounds.
        *   **CW:** You hear clicks or thumping.
        *   **FM:** You might hear a change in volume or background hiss, but usually no voice.

## 4. Transmitter Defects
*   **Chirp:** The frequency of a CW transmitter shifts slightly during keying. (Oscillator instability due to load changes).
*   **Key Clicks:** Hard switching (too fast rise/fall time) in CW generates broadband sidebands (splatter).
*   **Splatter:** Overmodulation in SSB/AM causes the signal to widen, interfering with adjacent frequencies.

---
[Back to Index](../INDEX.md) | [Back to Dashboard](../../README.md)
