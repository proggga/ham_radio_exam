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
*   **SINAD:** Signal-to-Noise and Distortion ratio. Typical spec: 12dB SINAD.
*   **Noise Figure (Ruisgetal, F):** Measure of how much noise the receiver adds.
    $$F = \frac{(S/N)_{in}}{(S/N)_{out}}$$
    *   Ideal receiver: $F = 1$ (0 dB).
    *   **LNA (Low Noise Amplifier):** The first stage (RF Amp) is critical for system noise figure (Friis formula). See [[Amplifiers|Amplifiers]].

## 2. Selectivity (Selectiviteit)
The ability to separate the wanted signal from others.
*   **Bandwidth:** Determined by IF filters (Crystal, Mechanical, Ceramic). See [[Filters & Resonance|Filters]].
*   **Shape Factor:** Ratio of bandwidth at -60dB to -6dB. Ideal is 1:1.
    *   *Adjacent Channel Selectivity:* Ability to reject signals close to the receive frequency.
    *   *Image Rejection:* Ability to reject the image frequency (determined by RF front-end).

## 3. Dynamic Range
The range between the noise floor and the signal level that causes distortion.
*   **Blocking:** A very strong nearby signal desensitizes the receiver (gain compression).
*   **Intermodulation (IMD):** Two strong signals ($f_1, f_2$) mix to create phantom signals ($2f_1 - f_2$, etc.). See [[Types of Interference|Interference]].
    *   *IP3 (Third Order Intercept Point):* A theoretical figure of merit for IMD performance. Higher is better.

## 4. The S-Meter
Indicates received signal strength.
*   **Standard (HF):** **S9** corresponds to **50 $\mu V$** at the antenna input ($50 \Omega$).
*   **Steps:** One S-unit = **6 dB** (Voltage ratio of 2). See [[Candidate Basic Skills|Decibels]].
    *   S8 = 25 $\mu V$.
    *   S9+20dB = 500 $\mu V$.