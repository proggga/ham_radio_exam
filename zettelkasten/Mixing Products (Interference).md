---
id: 202512292102
title: Mixing Products (Interference)
tags: ["ham-radio", "interference", "theory"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Mixing Products (Interference)

Non-linear stages in receivers or transmitters can mix signals to create unwanted "phantom" signals.

## Intermodulation Distortion (IMD)
Two strong signals ($f_1$ and $f_2$) mix to create sum and difference products.
*   **3rd Order Products**: $2f_1 - f_2$ and $2f_2 - f_1$.
    *   **Danger**: These often fall very close to the original frequencies and cannot be filtered easily.
    *   *Example*: Signals at 145.0 and 145.1 MHz produce interference at 144.9 and 145.2 MHz.

## Cross-Modulation
The modulation of a strong unwanted signal is transferred ("crosses over") to the weaker wanted signal.
*   **Effect**: You hear the audio of the strong station in the background of the station you are trying to listen to.

## Related
*   [[Mixers]]
*   [[Distortion and Dissipation]]
