---
id: 202301011247
title: "RF Safety"
tags: ["ham-radio", "safety"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# RF Safety

## 1. Risks
*   **Thermal Effects:** RF energy heats body tissue (like a microwave oven).
    *   **Vulnerable Organs:** Eyes (Cataracts) and Testes (Sterility) - poor blood flow for cooling.
    *   **Resonance:** Body absorbs RF best when height $\approx \lambda/2$. See [[Antenna Types|Dipole]].
        *   Frequency range **30 - 300 MHz** is most hazardous (Whole body resonance).
*   **RF Burns:** Touching an antenna (especially high-voltage points like ends of a dipole) causes deep RF burns.

## 2. Exposure Limits (ICNIRP)
Limits are defined by **SAR** (Specific Absorption Rate) in W/kg.
*   **Occupational (Workers):** 0.4 W/kg.
*   **General Public:** 0.08 W/kg (Strict limit for neighbors/family).

### Field Strength Limits (V/m)
Maximum electric field strength for General Public (Reference levels):
*   **HF (10-30 MHz):** ~28 V/m.
*   **VHF (144 MHz):** ~28 V/m (specifically 27.7 V/m in some tables).
*   **UHF (430 MHz):** ~29 - 30 V/m.
*   *Note:* Limits are frequency dependent. Lower frequencies allow higher fields (e.g. 87 V/m at 1 MHz).

## 3. Safe Distance Calculation
To ensure field strength $E$ stays below the limit $E_{limit}$:
$$d_{safe} = \frac{\sqrt{30 \times EIRP}}{E_{limit}}$$

*   **EIRP:** Effective Isotropic Radiated Power (Transmitter Power - Cable Loss + Antenna Gain). See [[Antenna Characteristics|Characteristics]].
*   **Factors reducing risk:**
    *   **Duty Cycle:** We don't transmit 100% of the time. (CW/SSB < FM). See [[Power Amplifiers and Matching|Transmitters]].
    *   **Antenna Pattern:** Don't stand in front of the beam.
    *   **Height:** Place antennas high up, away from people.

## 4. Field Zones
*   **Near Field:** Complex fields close to antenna. Hazardous. Hard to measure.
    *   Avoid being within $\lambda$ distance.
*   **Far Field:** Plane wave radiation. $E$ and $H$ decrease linearly with distance.