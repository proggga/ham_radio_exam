# Receiver Performance

## 1. Sensitivity (Gevoeligheid)
The ability to receive weak signals.
*   **SINAD:** Signal-to-[Noise](../01_electricity/26_AC_Signals_&_Noise.md) and Distortion ratio. Typical spec: 12dB SINAD.
*   **Noise Figure (Ruisgetal, F):** Measure of how much noise the receiver adds.
    $$F = \frac{(S/N)_{in}}{(S/N)_{out}}$$
    *   Ideal receiver: $F = 1$ (0 [dB](../00_basic_skills.md)).
    *   **Independence:** Noise Figure is **independent** of bandwidth.
    *   **LNA (Low Noise Amplifier):** The first stage (RF Amp) is critical for system noise figure (Friis formula). See [Amplifiers](../03_circuits/14_Amplifiers.md).

## 2. Selectivity (Selectiviteit)
The ability to separate the wanted signal from others.
*   **[Bandwidth](../03_circuits/07_Bandwidth.md):** Determined by IF filters (Crystal, Mechanical, Ceramic). See [Filters](../03_circuits/03_Filters_&_Resonance.md).
*   **Shape Factor:** Ratio of bandwidth at -60dB to -6dB. Ideal is 1:1.
    *   *Adjacent Channel Selectivity:* Ability to reject signals close to the receive frequency.
    *   *Image Rejection:* Ability to reject the image frequency (determined by RF front-end).

## 3. Dynamic Range & Distortion
The range between the noise floor and the signal level that causes distortion.
*   **Blocking (Desensitization):** A very strong nearby signal reduces the gain of the receiver, making weak signals inaudible.
*   **Cross-[Modulation](../01_electricity/31_Modulation_&_Digital_Signals.md) (Kruismodulatie):** The modulation of a strong unwanted signal is transferred ("crosses over") to the wanted weak signal. You hear the strong station's audio on the station you are tuned to.
*   **Intermodulation (IMD):** Two strong signals ($f_1, f_2$) mix in a non-linear stage to create phantom signals ($2f_1 - f_2$, etc.).
    *   *IP3 (Third Order Intercept Point):* A theoretical figure of merit. Higher is better.
*   **Reciprocal Mixing (Reciproke Menging):**
    *   Caused by **Phase Noise** in the Local Oscillator (LO).
    *   Noise sidebands of the LO mix with a strong adjacent signal, mapping it into the IF passband as noise.
    *   *Result:* Raised noise floor when strong signals are present nearby.

## 4. The S-Meter
Indicates received signal strength.
*   **Standard ([HF](../07_propagation/01_Propagation_Basics.md)):** **S9** corresponds to **50 $\mu V$** at the antenna input ($50 \Omega$).
*   **Steps:** One S-unit = **6 dB** (Voltage ratio of 2). See [Decibels](../00_basic_skills.md).
    *   S8 = 25 $\mu V$.
    *   S9+20dB = 500 $\mu V$.

## 5. Signal-to-Noise Ratio (SNR)
*   **Audio Gain:** Increasing the audio gain (volume) increases both Signal and Noise equally. It does **NOT** improve the SNR.
*   **Bandwidth:** Increasing bandwidth increases noise power (Noise power $\propto$ Bandwidth). Doubling bandwidth doubles noise power (+3 dB).

---
[< Back to Section Index](README.md)