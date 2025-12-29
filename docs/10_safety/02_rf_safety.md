# RF Safety

## 1. Risks
*   **Thermal Effects:** RF energy heats body tissue (like a microwave oven).
    *   **Vulnerable Organs:** Eyes (Cataracts) and Testes (Sterility) - poor blood flow for cooling.
    *   **Resonance:** Body absorbs RF best when height $\approx \lambda/2$. See [Dipole](../06_antennas/01_types.md).
        *   Frequency range **30 - 300 MHz** is most hazardous (Whole body resonance).
*   **RF Burns:** Touching an antenna (especially high-voltage points like ends of a dipole) causes deep RF burns.

## 2. Exposure Limits (ICNIRP)
Limits are defined by **SAR** (Specific Absorption Rate) in W/kg.
*   **Occupational (Workers):** 0.4 W/kg.
*   **General Public:** 0.08 W/kg (Strict limit for neighbors/family).

### Field Strength Limits
(Approximate values for Public exposure, exact table in HS17)
*   **HF (3-30 MHz):** ~28 V/m.
*   **VHF (144 MHz):** ~28 V/m.
*   **UHF (430 MHz):** ~29 V/m.

## 3. Safe Distance Calculation
To ensure field strength $E$ stays below the limit $E_{limit}$:
$$d_{safe} = \frac{\sqrt{30 \times EIRP}}{E_{limit}}$$

*   **EIRP:** Effective Isotropic Radiated Power (Transmitter Power - Cable Loss + Antenna Gain). See [Characteristics](../06_antennas/02_characteristics.md).
*   **Factors reducing risk:**
    *   **Duty Cycle:** We don't transmit 100% of the time. (CW/SSB < FM). See [Transmitters](../05_transmitters/02_power_amplifiers.md).
    *   **Antenna Pattern:** Don't stand in front of the beam.
    *   **Height:** Place antennas high up, away from people.

## 4. Field Zones
*   **Near Field:** Complex fields close to antenna. Hazardous. Hard to measure.
    *   Avoid being within $\lambda$ distance.
*   **Far Field:** Plane wave radiation. $E$ and $H$ decrease linearly with distance.

---
[Back to Index](../INDEX.md) | [Back to Dashboard](../../README.md)
