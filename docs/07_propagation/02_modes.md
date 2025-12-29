# Propagation Modes

## 1. Ground Wave (Grondgolf)
The wave follows the curvature of the earth.
*   **Frequency:** Dominant at Low Frequencies (LF/MF) and lower HF (160m/80m during day).
*   **Polarization:** Vertical works best (less absorption by ground).
*   **Range:** Depends on conductivity of the ground (Saltwater is best).

## 2. Sky Wave (Ruimtegolf)
The wave refracts off the ionosphere and returns to earth.
*   **Frequency:** HF (3-30 MHz).
*   **Mechanism:** Ionized layers in the upper atmosphere bend the wave.
*   **Skip Distance:** The distance from the transmitter to where the first hop lands.
*   **Dead Zone (Dode zone):** The area between the end of the ground wave coverage and the first sky wave landing. No signal is received here.

## 3. Line of Sight (LOS)
Direct wave between antennas.
*   **Frequency:** VHF, UHF, and above.
*   **Radio Horizon:** Radio waves bend slightly over the horizon due to atmospheric refraction.
    *   Radio Horizon $\approx 4/3 \times$ Optical Horizon.
    *   Formula: $d (km) \approx 4.1 \times (\sqrt{h_{tx}} + \sqrt{h_{rx}})$ (heights in meters).

## 4. Tropospheric Modes
*   **Ducting:** Temperature inversion (warm air over cold air) creates a "duct" that traps VHF/UHF signals, carrying them hundreds of km.
*   **Troposcatter:** Scattering off turbulence/irregularities in the troposphere.
*   **Rain Scatter:** Microwave signals reflecting off rain storms.

## 5. Exotic Modes
*   **Aurora:** Reflection off ionized sheets at the magnetic poles. Signals sound fluttery or "hisss-like". CW is best.
*   **Meteor Scatter:** Reflection off ionized trails from meteors. Short bursts (pings).
*   **EME:** Earth-Moon-Earth. Bouncing signals off the moon. High path loss (~250 dB).
