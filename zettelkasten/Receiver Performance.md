---
id: 202301011229
title: "Receiver Performance"
tags: ["ham-radio", "receivers"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Receiver Performance

## 1. Sensitivity (Gevoeligheid)
The ability to receive weak signals.
*   **SINAD:** Signal-to-[[AC Signals & Noise|Noise]] and Distortion ratio. Typical spec: 12dB SINAD.
*   **[[AC Signals & Noise|Noise]] Figure (Ruisgetal, F):** Measure of how much noise the receiver adds.
    $$F = \frac{(S/N)_{in}}{(S/N)_{out}}$$
    *   Ideal receiver: $F = 1$ (0 [[Decibels & Logarithms|dB]]).
    *   **Independence:** [[AC Signals & Noise|Noise]] Figure is **independent** of bandwidth.
    *   **LNA (Low Noise Amplifier):** The first stage (RF Amp) is critical for system noise figure (Friis formula). See [[Amplifiers|Amplifiers]].

## 2. Selectivity (Selectiviteit)
The ability to separate the wanted signal from others.
*   **[[Bandwidth]]:** Determined by IF filters (Crystal, Mechanical, Ceramic). See [[Filters & Resonance|Filters]].
*   **Shape Factor:** Ratio of bandwidth at -60dB to -6dB. Ideal is 1:1.
    *   *Adjacent Channel Selectivity:* Ability to reject signals close to the receive frequency.
    *   *Image Rejection:* Ability to reject the image frequency (determined by RF front-end).

## 3. Dynamic Range & Distortion
The range between the noise floor and the signal level that causes distortion.
*   **Blocking (Desensitization):** A very strong nearby signal reduces the gain of the receiver, making weak signals inaudible.
*   **Cross-[[Modulation & Digital Signals|Modulation]] (Kruismodulatie):** The modulation of a strong unwanted signal is transferred ("crosses over") to the wanted weak signal. You hear the strong station's audio on the station you are tuned to.
*   **Intermodulation (IMD):** Two strong signals ($f_1, f_2$) mix in a non-linear stage to create phantom signals ($2f_1 - f_2$, etc.).
    *   *IP3 (Third Order Intercept Point):* A theoretical figure of merit. Higher is better.
*   **Reciprocal Mixing (Reciproke Menging):**
    *   Caused by **Phase Noise** in the Local Oscillator (LO).
    *   Noise sidebands of the LO mix with a strong adjacent signal, mapping it into the IF passband as noise.
    *   *Result:* Raised noise floor when strong signals are present nearby.

## 4. The S-Meter
Indicates received signal strength.
*   **Standard ([[Propagation Basics|HF]]):** **S9** corresponds to **50 $\mu V$** at the antenna input ($50 \Omega$).
*   **Steps:** One S-unit = **6 [[Decibels & Logarithms|dB]]** (Voltage ratio of 2). See [[Candidate Basic Skills|Decibels]].
    *   S8 = 25 $\mu V$.
    *   S9+20dB = 500 $\mu V$.

## 5. Signal-to-Noise Ratio (SNR)
*   **Audio Gain:** Increasing the audio gain (volume) increases both Signal and Noise equally. It does **NOT** improve the SNR.
*   **[[Bandwidth]]:** Increasing bandwidth increases noise power (Noise power $\propto$ [[Bandwidth]]). Doubling bandwidth doubles noise power (+3 [[Decibels & Logarithms|dB]]).