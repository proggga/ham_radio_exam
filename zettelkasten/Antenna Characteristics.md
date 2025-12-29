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
Antenna gain is a comparison of power in the strongest direction against a reference antenna.
*   **Isotropic Radiator:** A theoretical point source radiating equally in all directions (sphere).
    *   Unit: **dBi**.
*   **Dipole:** A real $\lambda/2$ antenna. See [[Antenna Types|Types]].
    *   Unit: **dBd**.
*   **Conversion:** $0 \text{ dBd} = 2.15 \text{ dBi}$.
    *   $Gain (dBi) = Gain (dBd) + 2.15$.

## 2. Radiated Power
*   **ERP (Effective Radiated Power):** Power relative to a dipole.
    *   $ERP = P_{transmitter} - Losses + Gain (dBd)$.
*   **EIRP (Effective Isotropic Radiated Power):** Power relative to an isotropic radiator.
    *   $EIRP = P_{transmitter} - Losses + Gain (dBi)$.

## 3. Radiation Resistance ($R_{rad}$)
A virtual resistance that accounts for the power radiated as EM waves.
*   Total Impedance $Z = R_{rad} + R_{loss} + jX$. See [[Reactance & Impedance|Impedance]].
*   **Efficiency ($\eta$):**
    $$\eta = \frac{R_{rad}}{R_{rad} + R_{loss}}$$
*   **Short Antennas:** Have very low $R_{rad}$. Efficiency is poor unless $R_{loss}$ is extremely low.

## 4. Patterns
*   **Horizontal Pattern:** Azimuth (compass direction).
*   **Vertical Pattern:** Elevation (angle above horizon).
*   **Beamwidth:** The angle between the -3dB (half-power) points on the main lobe.
*   **Front-to-Back Ratio:** The difference in signal strength (dB) between the front and back of a directional antenna.

## 5. Fields
See [[Electric, Magnetic, and Electromagnetic Fields|Fields]].
*   **Near Field:** Close to the antenna. E and H fields are not yet orthogonal. Reactive energy is stored here.
    *   *Limit:* $d \approx \lambda$ (or $2D^2/\lambda$ for large antennas).
*   **Far Field:** The radiating zone. E and H fields are perpendicular. Wave propagates as a plane wave.