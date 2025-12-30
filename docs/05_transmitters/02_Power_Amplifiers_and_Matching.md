# Power Amplifiers and Matching

## 1. Power Amplifiers (Eindtrap)
The final stage that drives the antenna.
*   **Linearity:**
    *   **SSB/AM:** Requires **Linear** amplification (Class A or AB) to preserve the envelope shape. Non-linearity causes **Splatter** (IMD).
    *   **CW/FM:** Can use **Non-linear** amplification (Class C) for higher efficiency, as amplitude contains no information.

## 2. Output Filters
Power amplifiers generate harmonics (multiples of the frequency).
*   **Low Pass Filter (LPF):** Essential at the output to suppress harmonics to legal levels. See Filters.
*   **Pi-Filter:** A common LC circuit ($\pi$-shape) used for both impedance matching and low-pass filtering.

## 3. Antenna Matching (ATU)
Matches the transmitter impedance (usually $50 \Omega$) to the antenna system. See Matching.
*   **Purpose:** Allows the PA to deliver full power (happy transmitter).
*   **Note:** An ATU at the transmitter does **NOT** fix the SWR on the feedline. It only matches the *input* of the feedline to the TX.

## 4. Cooling and Duty Cycle
*   **Dissipation:** Efficiency is never 100%. Heat must be removed (Heatsinks, Fans).
*   **Duty Cycle:** The percentage of time the transmitter is "key down".
    *   *CW/SSB:* Low duty cycle (~20-50%).
    *   *FM/Digital (FT8):* High duty cycle (100%). Requires better cooling.

---
[< Back to Section Index](README.md)