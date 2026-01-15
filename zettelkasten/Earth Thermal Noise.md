---
id: 202501101410
title: Earth Thermal Noise
tags:
  - ham-radio
  - propagation
  - noise
created: 2025-01-10
type: permanent-note
modified: 2025-01-10

aliases: ["Thermische ruis van het aardoppervlak", "Earth Noise"]
---

# Earth Thermal Noise

**Earth Thermal Noise** (Thermische ruis van het aardoppervlak) is a significant noise source in space communications ([[Satellite Operation]], [[Earth-Moon-Earth (EME)|EME]]).

## Mechanism
*   **Warm Body**: The Earth is a physical body with a temperature of approx. 290 Kelvin.
*   **Black Body Radiation**: Any object above absolute zero radiates electromagnetic energy (noise) across a wide spectrum.
*   **[[Noise Types|Thermal Noise]]**: The Earth acts like a giant resistor generating thermal noise ($P = kTB$).

## Impact on Operations
*   **Satellite Downlink**: When a satellite antenna points towards Earth (which it usually does), it "sees" this 290K background noise.
*   **Ground Station**:
    *   Pointing antennas at the **Cold Sky** (away from the sun/galactic center) yields a very low noise temperature (~3K - 10K).
    *   Pointing antennas near the **Horizon** or slightly down towards the **Earth** dramatically increases the noise floor.
*   **G/T Ratio**: System performance is measured by Gain over Temperature. Picking up Earth noise increases $T$, degrading performance.

## Practical Tip
For weak signal work (EME), moonrise and moonset are noisy times because the antenna main lobe or sidelobes pick up the thermal noise from the Earth's surface.

## Related
*   [[Noise Types]]
*   [[Satellite Operation]]
*   [[Earth-Moon-Earth (EME)]]
*   [[Directional Antennas (Beams)]]
