# Aperture Antennas

Antennas that use a surface area (aperture) to capture or focus radio waves, typically used at [UHF](../07_propagation/07_VHFUHF_Bands_6m,_2m,_70cm.md) and Microwave frequencies ($\lambda < 10$ cm).

## 1. Parabolic Reflector (Dish)
Uses a parabolic surface to focus incoming parallel waves to a single point (Focus).
*   **Gain**: Depends on the diameter ($D$) relative to wavelength ($\lambda$).
    *   Formula: $G \approx 10 \log \eta (\frac{\pi D}{\lambda})^2$
    *   Rule of thumb: To get significant gain (> 10-15 [dB](../00_basic_skills.md)), diameter should be at least $3\lambda$.
*   **Beamwidth**: Very narrow.
    *   $\psi \approx 70 \frac{\lambda}{D}$ degrees.
*   **Feed**: [Dipole](02_The_Dipole_Antenna.md) or Horn antenna placed at the focus.

## 2. Horn Antenna
A flared waveguide.
*   Acts as an impedance transformer between the waveguide and free space.
*   Often used as a feed for dishes or as a gain standard.

## 3. Helical Antenna (Helix)
A conducting wire wound in the shape of a screw (helix) with a reflector plate.
*   **Mode**: Axial mode (radiates along the axis of the spiral).
*   **Polarization**: Circular (Right-Hand or Left-Hand depending on winding).
*   **Use**: Satellite communications (matches tumbling satellite polarization).

---
[< Back to Section Index](README.md)