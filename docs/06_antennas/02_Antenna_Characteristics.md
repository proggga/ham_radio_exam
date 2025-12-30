# Antenna Characteristics

## 1. Gain
Antenna gain is a comparison of power in the strongest direction against a reference antenna.
*   **Isotropic Radiator:** A theoretical point source radiating equally in all directions (sphere).
    *   Unit: **dBi**.
*   **Dipole:** A real $\lambda/2$ antenna. See Types.
    *   Unit: **dBd**.
*   **Conversion:** $0 \text{ dBd} = 2.15 \text{ dBi}$.
    *   $Gain (dBi) = Gain (dBd) + 2.15$.

## 2. Radiated Power
*   **ERP (Effective Radiated Power):** Power relative to a dipole.
    *   $ERP = P_{transmitter} - Losses + Gain (dBd)$.
*   **EIRP (Effective Isotropic Radiated Power):** Power relative to an isotropic radiator.
    *   $EIRP = P_{transmitter} - Losses + Gain (dBi)$.

### Calculation Example
**Scenario:** Transmitter power is 10 Watts. Coax cable loss is 3 dB. Antenna is a Yagi with 13 dBd gain. What is the ERP?
1.  **Convert Power to dBW:** $10 \text{ W} = 10 \text{ dBW}$.
2.  **Calculate Power at Antenna:** $10 \text{ dBW} - 3 \text{ dB} = 7 \text{ dBW}$ (5 Watts).
3.  **Add Antenna Gain:** $7 \text{ dBW} + 13 \text{ dBd} = 20 \text{ dBW}$.
4.  **Convert back to Watts:** $20 \text{ dBW} = 100 \text{ W}$.
*   *Alternative (Factor method):* 3 dB loss = 1/2 power. 13 dB gain $\approx$ 20x power.
    *   $10 \text{ W} \times 0.5 \times 20 = 100 \text{ W}$.

## 3. Radiation Resistance ($R_{rad}$)
A virtual resistance that accounts for the power radiated as EM waves.
*   Total Impedance $Z = R_{rad} + R_{loss} + jX$. See Impedance.
*   **Efficiency ($\eta$):**
    $$\eta = \frac{R_{rad}}{R_{rad} + R_{loss}}$$
*   **Short Antennas:** Have very low $R_{rad}$. Efficiency is poor unless $R_{loss}$ is extremely low.

## 4. Patterns
*   **Horizontal Pattern:** Azimuth (compass direction).
*   **Vertical Pattern:** Elevation (angle above horizon).
*   **Beamwidth:** The angle between the -3dB (half-power) points on the main lobe.
*   **Front-to-Back Ratio:** The difference in signal strength (dB) between the front and back of a directional antenna.

## 5. Fields
See Fields.
*   **Near Field:** Close to the antenna. E and H fields are not yet orthogonal. Reactive energy is stored here.
    *   *Limit:* $d \approx \lambda$ (or $2D^2/\lambda$ for large antennas).
*   **Far Field:** The radiating zone. E and H fields are perpendicular. Wave propagates as a plane wave.

---
[< Back to Section Index](README.md)