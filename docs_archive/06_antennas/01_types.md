# Antenna Types

## 1. The Dipole
The fundamental antenna.
*   **Length:** Approximately half a wavelength ($\lambda/2$).
*   **Feedpoint:** In the center (Voltage Low, Current High).
*   **Impedance:** $\approx 73 \Omega$ in free space. Lower if close to ground. See [Impedance](../03_circuits/07_reactance_impedance.md).
*   **Radiation Pattern:** Figure-8 (broadside to the wire). Nulls off the ends.
*   **Variants:**
    *   **Inverted V:** Center high, ends low. Omni-directional, lower impedance (~$50 \Omega$).
    *   **Folded Dipole:** High impedance (~$300 \Omega$). Wider bandwidth.
    *   **Trap Dipole:** Uses LC circuits (traps) to electrically shorten the antenna for multiple bands. See [Filters](../03_circuits/03_filters.md).

## 2. Vertical Antennas
*   **Ground Plane (GP):** Quarter-wave ($\lambda/4$) vertical element.
    *   Requires radials (ground plane).
    *   **Impedance:** ~$36 \Omega$ (horizontal radials) to ~$50 \Omega$ (drooping radials).
    *   **Radiation:** Omni-directional. Low angle of radiation (good for DX).
*   **Vertical Monopole:** Uses the earth as a mirror image to create a virtual dipole.

## 3. Directional Antennas (Beams)
*   **Yagi-Uda:** Parasitic array.
    *   **Driven Element:** Dipole.
    *   **Reflector:** ~5% longer, placed behind.
    *   **Director(s):** ~5% shorter, placed in front.
    *   **Gain:** High forward gain.
    *   **Front-to-Back Ratio:** Rejects signals from the rear.
*   **Quad:** Loops used as elements.

## 4. Other Types
*   **End-Fed:** Voltage fed (High Impedance, ~$2500-5000 \Omega$). Requires a transformer (Unun 1:49 or 1:64).
*   **Loop:**
    *   *Small Loop ($<\lambda/10$):* Magnetic loop. High Q, very narrow bandwidth. Good for noise rejection.
    *   *Large Loop ($\approx \lambda$):* Quad loop.
*   **Dummy Load (Kunstantenne):** A $50 \Omega$ non-inductive [Resistor](../02_components/01_resistors.md) used for testing transmitters without radiating. See [Measurements](../08_measurements/03_rf_measurements.md).

---
[Back to Index](../INDEX.md) | [Back to Dashboard](../../README.md)
