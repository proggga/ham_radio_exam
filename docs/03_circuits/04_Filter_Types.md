# Filter Types

[Filters](03_Filters_&_Resonance.md) allow specific frequencies to pass while rejecting others.

## Common Types
*   **Low Pass [Filter](03_Filters_&_Resonance.md) (LPF)**: Passes frequencies below a cut-off point. Attenuates higher frequencies.
    *   *Use*: Audio filtering, Harmonic suppression in transmitters.
*   **High Pass [Filter](03_Filters_&_Resonance.md) (HPF)**: Passes frequencies above a cut-off point.
    *   *Use*: Removing AC hum ($50Hz$), Pre-selectors.
*   **Band Pass Filter (BPF)**: Passes a specific range of frequencies.
    *   *Use*: Receiver tuning (passing only the desired station).
*   **Band Stop (Notch) Filter**: Blocks a specific frequency range.
    *   *Use*: Removing specific interference carriers.

## Cut-off Frequency ($f_c$)
The frequency where the signal power is reduced by half ($-3dB$).
*   RC Filter: $f_c = \frac{1}{2\pi RC}$
*   RL Filter: $f_c = \frac{R}{2\pi L}$

---
[< Back to Section Index](README.md)