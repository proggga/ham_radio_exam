id: 202301011231
title: "Power Amplifiers and Matching"
tags: ["amplifiers", "filters", "modes", "semiconductors", "transmission-lines", "transmitters"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29

aliases: ["Eindversterkers en aanpassing"]

# Power Amplifiers and Matching

## 1. Power Amplifiers (Eindtrap)
The final stage that drives the antenna.
*   **Linearity:**
    *   **SSB/AM:** Requires **Linear** amplification ([Class A or AB](../03_circuits/06_Amplifiers.md)) to preserve the envelope shape. Non-linearity causes **Splatter** (IMD).
    *   **CW/FM:** Can use **Non-linear** amplification ([Class C](../03_circuits/06_Amplifiers.md)) for higher efficiency, as amplitude contains no information.

## 2. Output Filters
Power amplifiers generate harmonics (multiples of the frequency).
*   **Low Pass [Filter](../03_circuits/03_Filters_&_Resonance.md) (LPF):** Essential at the output to suppress harmonics to legal levels. See [Filters](../03_circuits/03_Filters_&_Resonance.md).
*   **Pi-[Filter](../03_circuits/03_Filters_&_Resonance.md):** A common [LC circuit](../03_circuits/01_Reactive_Combinations.md) ($\pi$-shape) used for both impedance matching and low-pass filtering.

## 3. Antenna Matching (ATU)
Matches the transmitter impedance (usually $50 \Omega$) to the antenna system. See [Matching](../06_antennas/18_Matching_and_SWR.md).
*   **Purpose:** Allows the PA to deliver full power (happy transmitter).
*   **Note:** An ATU at the transmitter does **NOT** fix the [SWR](../06_antennas/18_Matching_and_SWR.md) on the feedline. It only matches the *input* of the feedline to the TX.

## 4. Cooling and Duty Cycle
*   **Dissipation:** Efficiency is never 100%. Heat must be removed (Heatsinks, Fans).
*   **Duty Cycle:** The percentage of time the transmitter is "key down".
    *   *CW/SSB:* Low duty cycle (~20-50%).
    *   *FM/Digital ([FT8](../11_procedures.md)):* High duty cycle (100%). Requires better cooling.

---
[< Back to Section Index](README.md)