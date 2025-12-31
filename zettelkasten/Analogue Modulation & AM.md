---
id: 202512292105
title: Analogue Modulation & AM
tags: ["ham-radio", "modulation", "theory"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Analogue Modulation & AM

[[Modulation & Digital Signals|Modulation]] is the process of modifying a **Carrier Wave** to convey information.

## AM (Amplitude Modulation)
*   **Method**: Varying the carrier amplitude in sync with the audio signal.
*   **[[Modulation & Digital Signals|Modulation]] Depth ($m$)**: $m = \frac{U_{audio}}{U_{carrier}} \times 100\%$.
    *   **$m=100\%$**: Carrier amplitude varies from $0$ to $2 \times U_{carrier}$.
    *   **Overmodulation ($m > 100\%$)**: Carrier cuts off at negative peaks. Causes severe **distortion** and **splatter** (harmonics/sidebands spreading out).

### Spectrum & Bandwidth
*   **Components**: Carrier ($f_c$) + Upper Sideband ($f_c + f_{audio}$) + Lower Sideband ($f_c - f_{audio}$).
*   **[[Bandwidth]]**: $B = 2 \times f_{max\_audio}$.
    *   *Example:* Audio up to 3 kHz $\rightarrow$ [[Bandwidth]] = 6 kHz. Broadcast AM uses 9 kHz spacing ($f_{max} = 4.5$ kHz).

### Power Distribution (Exam Topic)
*   **Carrier Power ($P_{c}$)**: Contains no information.
*   **Sideband Power ($P_{sb}$)**: Contains the information.
*   **Total Power ($P_{tot}$)**: $P_{tot} = P_c (1 + \frac{m^2}{2})$.
    *   At **100% [[Modulation & Digital Signals|Modulation]] ($m=1$)**:
        *   $P_{tot} = 1.5 \times P_c$.
        *   Sidebands contain only **1/3** of the total power (1/6 in USB, 1/6 in LSB).

### PEP Calculation (Peak Envelope Power)
**Definition**: The average power of one RF cycle at the crest (peak) of the modulation envelope.
*   **Visual**: On a scope, $U_{max}$ is the peak voltage (amplitude) of the highest wave.
*   **Calculation Steps**:
    1.  Determine Peak Voltage ($U_{peak}$) from scope (half of peak-to-peak).
    2.  Calculate [[RMS Voltage]]: $U_{eff} = U_{peak} / \sqrt{2}$.
    3.  Calculate Power: $P_{PEP} = \frac{U_{eff}^2}{R} = \frac{U_{peak}^2}{2R}$.
*   **Relation to Carrier**: At 100% modulation ($m=1$), $U_{peak} = 2 \times U_{carrier\_peak}$.
    *   Therefore, **$P_{PEP} = 4 \times P_{carrier}$**.

## CW (Continuous Wave)
*   **Method**: On/Off keying of the carrier (Morse Code).
*   **Designation**: A1A.
*   **[[Bandwidth]]**: Very narrow. Rule of thumb: $B \approx 3 \times \text{Speed (WPM)}$ or roughly 100-200 Hz (not 0 Hz!).
*   **Click [[Filters & Resonance|Filters]]**: Necessary to round off the keying edges to prevent "[[Station Accessories|Key]] Clicks" (wideband interference).
*   **Class C**: [[CW Abbreviations & Prosigns|CW]] can be amplified by Class C amplifiers (high efficiency) because amplitude is constant (when on).

## Related
*   [[Single Sideband (SSB)]]
*   [[Frequency Modulation (FM)]]
