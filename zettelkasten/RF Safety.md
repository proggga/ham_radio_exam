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
    *   **Vulnerable Organs:** Eyes (poor cooling, risk of Cataracts) and Testes/Reproductive organs.
    *   **Frequency [[Receiver Performance|Sensitivity]]:**
        *   **Eyes:** Most sensitive > **1000 MHz** (1 GHz).
        *   **Brain/Head:** Sensitive > **400 MHz**.
        *   **Whole Body [[Resonance]]:** **30 - 300 MHz**. The body absorbs RF most efficiently in this range (height $\approx \lambda/2$).
*   **RF Burns:** Direct contact with antennas (high voltage ends) causes deep, slow-healing burns.

## 2. Exposure Limits (ICNIRP/FCC)
Limits are often defined by **SAR** (Specific Absorption Rate) in W/kg or **MPE** (Maximum Permissible Exposure) in mW/cm².

### Environments
*   **Controlled Environment (Occupational)**: Areas where people are aware of the potential for exposure and can control it (e.g., the operator). Limits are higher (0.4 W/kg).
*   **Uncontrolled Environment (General Public)**: Areas where people have no knowledge or control of exposure (e.g., neighbors). Limits are stricter (0.08 W/kg).

### Duty Cycle
The percentage of time the transmitter is actually transmitting.
*   **Averaging**: Exposure limits are based on time-averaging (e.g., over 6 or 30 minutes).
*   **Effect**: A lower duty cycle allows for higher peak power while staying within average limits.
    *   *[[Frequency Modulation (FM)|FM]]:* 100% ([[Station Accessories|Key]] down continuously).
    *   *[[CW Abbreviations & Prosigns|CW]]:* $\approx 40\%$.
    *   *[[Single Sideband (SSB)|SSB]]:* $\approx 20\%$ (Voice peaks).
    *   *Calculation:* $\text{Average Power} = \text{Peak Power} \times \text{Duty Cycle}$.

### Field Strength (V/m)
Typical Reference Levels for the public:
*   **[[Propagation Basics|HF]] (10-30 MHz):** $\approx 28 \text{ V/m}$.
*   **[[VHFUHF Bands (6m, 2m, 70cm)|VHF]] (144 MHz):** $\approx 28 \text{ V/m}$.
*   **[[VHFUHF Bands (6m, 2m, 70cm)|UHF]] (430 MHz):** $\approx 29 \text{ V/m}$ (Limits rise with frequency above resonance).

## 3. Safe Distance Calculation
To ensure the field strength $E$ stays below the limit $E_{limit}$:
$$d_{safe} = \frac{\sqrt{30 \times EIRP}}{E_{limit}}$$

*   **EIRP**: Effective Isotropic Radiated Power.
    *   $EIRP = P_{transmitter} \times Gain_{antenna} \times 1.64$ (if gain is relative to dipole).
    *   *Note:* $1 \text{ dipole gain (0 dBd)} = 1.64 \times \text{isotropic (2.15 dBi)}$.
*   **[[Licensing in the Netherlands|Exam]] Example**:
    *   $P = 400 \text{ W}$, Gain = 10 dBd (factor 10), Limit = 28 V/m.
    *   $EIRP = 400 \times 10 \times 1.64 = 6560 \text{ W}$.
    *   $d = \sqrt{30 \times 6560} / 28 \approx \sqrt{196800} / 28 \approx 443 / 28 \approx 16 \text{ m}$.

## 4. Field Zones
*   **Near Field (Nabije veld):** Complex region close to antenna ($d < \lambda$). E and H fields are not related by $377 \Omega$. Hazardous.
*   **Far Field (Verre veld):** Plane wave radiation ($d > 2\lambda$). $E$ and $H$ decrease linearly with distance ($1/d$).

## Related