# Causes of Interference

## 1. Emissions
*   **Fundamental:** The intended frequency. High field strength near the antenna can overload nearby electronics.
*   **Harmonics:** Multiples of the fundamental frequency ($2f, 3f, 4f...$).
    *   *Example:* A 7 MHz transmitter may cause interference on 14 MHz, 21 MHz, etc.
    *   *Cause:* Non-linear amplification ([Class C, AB](../03_circuits/14_Amplifiers.md)) produces harmonics.
*   **Spurious Emissions:** Parasitic oscillations or mixing products generated within the transmitter that are not harmonics.
    *   *Phase [Noise](../01_electricity/26_AC_Signals_&_Noise.md):* "skirts" of noise around the carrier due to [Oscillator](../03_circuits/20_Detectors,_Oscillators_&_Mixers.md) jitter.

## 2. Immunity (Susceptibility)
The inability of equipment to reject unwanted RF energy.
*   **Poor [Shielding](../01_electricity/20_Shielding_Afscherming.md):** Plastic cases allow RF to penetrate directly to the PCB.
*   **Lack of Filtering:** Missing mains filters or input filters on audio ports.
*   **Pin 1 Problem:** Grounding cable shields to the PCB signal ground instead of the metal chassis.

## 3. Propagation Paths
*   **Radiated:** Direct transmission through the air from antenna to victim device.
*   **Conducted:** RF traveling along wires (Mains cables, Speaker wires, Coax shields).
    *   **Common Mode Current:** RF flowing on the *outside* of a cable shield. Acts as a transmitting antenna inside the house.

---
[< Back to Section Index](README.md)