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
*   **Formula**: $f_{IMD} = |n \cdot f_1 \pm m \cdot f_2|$.
*   **3rd Order Products**: $2f_1 - f_2$ and $2f_2 - f_1$.
    *   **Danger**: These often fall very close to the original frequencies and cannot be filtered easily.
    *   *Example:* Signals at 145.0 and 145.1 MHz produce interference at 144.9 and 145.2 MHz.
*   **Mitigation**: Use a receiver with a high IP3 (Intercept Point) or add an **Attenuator** (Verzwakker).

## Cross-Modulation (Kruismodulatie)
*   **Definition**: The transfer of modulation from a strong unwanted signal to the carrier of a weaker wanted signal.
*   **Effect**: You hear the audio of the strong station in the background of the station you are tuned to.
*   **Cause**: Non-linearity in the RF amplifier or Mixer.
*   **Context**: Common when a strong local transmitter is active nearby.

## Harmonics (Interference)
*   **Mechanism**: A transmitter radiates multiples of its fundamental frequency ($2f, 3f...$).
*   **Example**: A 144 MHz (2m) transmitter's 4th harmonic ($4 \times 144 = 576$ MHz) falls into UHF TV Band IV (Channel 34, ~575 MHz).
*   **Mitigation**: Low Pass Filter at the transmitter output.

## Related
*   [[Mixers]]
*   [[Distortion and Dissipation]]
