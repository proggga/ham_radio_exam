---
id: 202512292016
title: Amplifier Classes
tags: ["ham-radio", "circuits", "amplifiers"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Amplifier Classes

Amplifier classes describe the conduction angle (bias point) of the amplifying device.

| Class | Conduction | Linearity | Efficiency ($\eta$) | Use |
| :--- | :--- | :--- | :--- | :--- |
| **Class A** | $360^\circ$ | Highest | Low (< 25-50%) | Audio, Pre-amps, [[Single Sideband (SSB)|SSB]] Linear |
| **Class B** | $180^\circ$ | Low | Medium (~50-78%) | Push-Pull Audio/RF |
| **Class AB**| $180^\circ - 360^\circ$| Good | Good | [[Single Sideband (SSB)|SSB]] Linear Amps |
| **Class C** | $< 180^\circ$ | Very Low | High (> 75%) | [[Frequency Modulation (FM)|FM]]/[[CW Abbreviations & Prosigns|CW]] RF PA, Freq Multipliers |

## Details

### Class A
*   **Bias:** Center of the linear part of the characteristic curve (Load Line).
*   **Current:** Flows at all times, even with no signal.
*   **Drawback:** Continuous power dissipation = Heat.

### Class B
*   **Bias:** At Cutoff ($U_{GS} = U_{pinch-off}$ or $U_{BE} = 0$).
*   **Current:** Flows only during the positive half-cycle (or negative for PNP).
*   **Push-Pull:** Two devices are required to reproduce the full wave. One handles positive, one negative. Eliminates even harmonics.

### Class C
*   **Bias:** Beyond Cutoff (Deep class C).
*   **Current:** Short pulses at the signal peaks.
*   **Harmonics:** Generates strong harmonics.
    *   **Frequency Multiplication:** Ideally suited for triplers ($3 \times f$) etc., because the output tank circuit can be tuned to a harmonic (e.g., $3^{rd}$ harmonic) while the input is driven at the fundamental.
*   **Requirements:** Requires a tuned circuit (LC tank) at the output to restore the sine wave (flywheel effect). Cannot be used for Audio.

## Related
*   [[Amplifier Operating Principles]]
*   [[Distortion and Dissipation]]
