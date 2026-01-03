---
id: 202512292106
title: Single Sideband (SSB)
tags: ["ham-radio", "modulation", "theory"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Single Sideband (SSB)

SSB is a form of Amplitude [[Modulation & Digital Signals|Modulation]] where the Carrier and one Sideband are suppressed.

## Evolution (AM $\to$ DSB $\to$ SSB)
1.  **[[Analogue Modulation & AM|AM]]**: Carrier + 2 Sidebands. Least efficient.
2.  **DSB (Double Sideband)**: Carrier suppressed, 2 Sidebands remain.
    *   **Power**: At 100% [[Analogue Modulation & AM|AM]] mod equivalence, [[Analogue Modulation & AM|PEP]] is 1/4 of [[Analogue Modulation & AM|AM]] [[Analogue Modulation & AM|PEP]] (since amplitude is halved without carrier base).
    *   **[[Bandwidth]]**: Same as AM ($2 \times f_{audio}$).
3.  **SSB (Single Sideband)**: One sideband removed.
    *   **Efficiency**: All transmitted power is useful information.
    *   **[[Bandwidth]]**: Half that of AM/DSB (~2.4 - 2.7 kHz).
    *   **Signal-to-[[AC Signals & Noise|Noise]]**: 3 [[Decibels & Logarithms|dB]] improvement over DSB (half bandwidth = half noise) + 3 [[Decibels & Logarithms|dB]] power saving (no wasted sideband) $\rightarrow$ significant system gain over AM.

## Generation
1.  **Balanced Modulator**: Mixes Audio and Carrier. Output is **DSB** (Carrier suppressed).
2.  **[[Filters & Resonance|Filter]] Method**: A sharp Crystal [[Filters & Resonance|Filter]] or Mechanical [[Filters & Resonance|Filter]] removes the unwanted sideband.
    *   *USB:* Filter passes upper frequencies.
    *   *LSB:* Filter passes lower frequencies.

## Reception
Requires a receiver with a **Product Detector** ([[Mixers|Mixer]]) and a **BFO** (Beat Frequency Oscillator) to re-insert the missing carrier frequency locally.

## Power Measurement (PEP)
*   **Definition**: Peak Envelope Power. Average power of one RF cycle at the crest of the modulation envelope.
*   **Double Tone Test**: When testing with two equal tones (e.g., 1100 Hz and 1900 Hz):
    *   The Peak Voltage ($U_{peak}$) is the **sum** of the peak voltages of the two tones.
    *   If a meter shows peak voltage (e.g., 71V), calculate PEP as $P = U^2 / R$.
    *   *Example:* $U_{peak} = 71 \text{ V}$. $PEP = 71^2 / 50 \approx 100 \text{ W}$.

## Example Exam Question
**Question:** The most suitable bandwidth for an HF amateur receiver used for SSB (EZB) telephony reception is:
A. 7.5 kHz
B. 15 kHz
C. 2.4 kHz

**Answer:** **C (2.4 kHz)**.
*   **Why?**
    *   **SSB** only transmits one sideband containing the voice information.
    *   Intelligible human speech requires a frequency range of roughly 300 Hz to 2700 Hz.
    *   Therefore, a bandwidth of approximately **2.4 kHz** (2.7 kHz max) is standard for SSB filters.
    *   7.5 kHz is typical for AM; 15 kHz is typical for FM broadcast.

## Related
*   [[Analogue Modulation & AM]]
*   **[[Detectors (Demodulators)]]**
