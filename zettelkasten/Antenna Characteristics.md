---
id: 202301011233
title: "Antenna Characteristics"
tags: ["ham-radio", "antennas"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Antenna Characteristics

## 1. Gain
[[Antenna & Tower Safety|Antenna]] gain is a comparison of power in the strongest direction against a reference antenna.
*   **Polarization:** Determined by the direction of the **[[Electric Field]] (E-field)**. For a dipole, this is parallel to the element.
*   **Isotropic Radiator:** A theoretical point source radiating equally in all directions (sphere).
    *   Unit: **dBi**.
*   **[[The Dipole Antenna|Dipole]]:** A real $\lambda/2$ antenna. See [[Antenna Types|Types]].
    *   Unit: **dBd**.
*   **Conversion:** $0 \text{ dBd} = 2.15 \text{ dBi}$.
    *   $Gain (dBi) = Gain (dBd) + 2.15$.

## 2. Radiated Power
*   **ERP (Effective Radiated Power):** Power relative to a dipole.
    *   $ERP = P_{transmitter} - Losses + Gain (dBd)$.
*   **EIRP (Effective Isotropic Radiated Power):** Power relative to an isotropic radiator.
    *   $EIRP = P_{transmitter} - Losses + Gain (dBi)$.

### Calculation Example
**Scenario:** Transmitter power is 10 Watts. Coax cable loss is 3 [[Decibels & Logarithms|dB]]. [[Antenna & Tower Safety|Antenna]] is a [[Directional Antennas (Beams)|Yagi]] with 13 dBd gain. What is the ERP?
1.  **Convert Power to dBW:** $10 \text{ W} = 10 \text{ dBW}$.
2.  **Calculate Power at [[Antenna & Tower Safety|Antenna]]:** $10 \text{ dBW} - 3 \text{ [[Decibels & Logarithms|dB]]} = 7 \text{ dBW}$ (5 Watts).
3.  **Add Antenna Gain:** $7 \text{ dBW} + 13 \text{ dBd} = 20 \text{ dBW}$.
4.  **Convert back to Watts:** $20 \text{ dBW} = 100 \text{ W}$.
*   *Alternative (Factor method):* 3 [[Decibels & Logarithms|dB]] loss = 1/2 power. 13 dB gain $\approx$ 20x power.
    *   $10 \text{ W} \times 0.5 \times 20 = 100 \text{ W}$.

## 3. Radiation Resistance ($R_{rad}$)
A virtual resistance that accounts for the power radiated as EM waves.
*   Total [[Impedance (Impedantie)|Impedance]] $Z = R_{rad} + R_{loss} + jX$. See [[Reactance & Impedance|Impedance]].
*   **Efficiency ($\eta$):**
    $$\eta = \frac{R_{rad}}{R_{rad} + R_{loss}}$$
*   **Short Antennas:** Have very low $R_{rad}$. Efficiency is poor unless $R_{loss}$ is extremely low.

## 4. Patterns
*   **Horizontal Pattern:** Azimuth (compass direction).
*   **Vertical Pattern:** Elevation (angle above horizon).
*   **Beamwidth:** The angle between the -3dB (half-power) points on the main lobe.
*   **Front-to-Back Ratio:** The difference in signal strength (dB) between the front and back of a directional antenna.

## 6. Effective Aperture
*   **Concept**: The effective area of the wavefront that the antenna captures.
*   **Formula**: $A_{eff} = \frac{\lambda^2}{4\pi} \times G$
*   **Implication**: For the same gain, a lower frequency antenna (larger $\lambda$) captures more energy than a higher frequency antenna. This is why path loss increases with frequency (assuming constant antenna gain).

## 7. Mobile Considerations (Vehicle Shielding)
*   **Faraday Cage Effect**: Operating a handheld transceiver (HT) inside a vehicle significantly reduces signal strength because the metal body shields RF.
*   **Solution**: Use an external magnet-mount or fixed antenna on the roof.
    *   *Gain:* External antennas (e.g., 5/8 wave) often have gain over the standard "rubber duck".
    *   *[[Electrical Safety|Safety]]:* Moves the RF field away from the passengers.

## Related