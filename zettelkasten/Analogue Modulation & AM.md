---
id: 202512292105
title: Analogue Modulation & AM
tags: ["ham-radio", "modulation", "theory"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Analogue Modulation & AM

Modulation is the process of modifying a **Carrier Wave** to convey information.

## CW (Continuous Wave)
*   **Method**: On/Off keying of the carrier (Morse Code).
*   **Bandwidth**: Very narrow (~50-150 Hz).
*   **Efficiency**: High, simple to implement.

## AM (Amplitude Modulation)
*   **Method**: Varying the carrier amplitude in sync with the audio signal.
*   **Modulation Depth ($m$)**: $m = U_{audio} / U_{carrier}$.
    *   Max 100%. Overmodulation causes distortion and splatter.

### Sidebands
AM produces two sidebands:
*   **Upper Sideband (USB)**: $f_c + f_{audio}$
*   **Lower Sideband (LSB)**: $f_c - f_{audio}$
*   **Bandwidth**: $2 \times f_{max\_audio}$.

### Power Distribution
*   Carrier consumes most of the power (contains no information).
*   At 100% modulation, sidebands contain only 1/3 of total power.

## Related
*   [[Single Sideband (SSB)]]
*   [[Frequency Modulation (FM)]]
