# Power Amplifiers and Matching

## 1. Power Amplifiers (Eindtrap)
The final stage that drives the antenna.
*   **Linearity:**
    *   **[SSB](../01_electricity/34_Single_Sideband_SSB.md)/[AM](../01_electricity/32_Analogue_Modulation_&_AM.md):** Requires **Linear** amplification ([Class A or AB](../03_circuits/14_Amplifiers.md)) to preserve the envelope shape. Non-linearity causes **Splatter** (IMD).
    *   **[CW](../01_electricity/33_CW_Abbreviations_&_Prosigns.md)/[FM](../01_electricity/35_Frequency_Modulation_FM.md):** Can use **Non-linear** amplification ([Class C](../03_circuits/14_Amplifiers.md)) for higher efficiency, as amplitude contains no information.

## 2. Output Filters
Power amplifiers generate harmonics (multiples of the frequency).
*   **Low Pass [Filter](../03_circuits/03_Filters_&_Resonance.md) (LPF):** Essential at the output to suppress harmonics to legal levels. See [Filters](../03_circuits/03_Filters_&_Resonance.md).
*   **Pi-[Filter](../03_circuits/03_Filters_&_Resonance.md):** A common [LC circuit](../03_circuits/01_Reactive_Combinations.md) ($\pi$-shape) used for both impedance matching and low-pass filtering.

## 3. Antenna Matching (ATU)
Matches the transmitter impedance (usually $50 \Omega$) to the antenna system. See [Matching](../06_antennas/18_Matching_and_SWR.md).
*   **Purpose:** Allows the PA to deliver full power (happy transmitter).
*   **Note:** An [ATU](../06_antennas/21_Antenna_Tuning_Unit_ATU.md) at the transmitter does **NOT** fix the [SWR](../06_antennas/18_Matching_and_SWR.md) on the feedline. It only matches the *input* of the feedline to the TX.

## 4. Cooling and Duty Cycle
*   **Dissipation:** Efficiency is never 100%. Heat must be removed (Heatsinks, Fans).
*   **Duty Cycle:** The percentage of time the transmitter is "key down".
    *   *[CW](../01_electricity/33_CW_Abbreviations_&_Prosigns.md)/[SSB](../01_electricity/34_Single_Sideband_SSB.md):* Low duty cycle (~20-50%).
    *   *[FM](../01_electricity/35_Frequency_Modulation_FM.md)/Digital ([FT8](../11_procedures.md)):* High duty cycle (100%). Requires better cooling.

---
[< Back to Section Index](README.md)