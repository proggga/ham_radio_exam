# Fading (QSB)

Fading is the variation in signal strength at the receiver.

## Types of Fading
1.  **Multipath Fading**: The signal arrives via multiple paths (e.g., 1 hop vs 2 hops) with different phases.
    *   *Mechanism:* Phase cancellation.
    *   *Speed:* Slow to moderate.
2.  **Picket Fencing (Mobile Flutter)**: Rapid fluctuation in signal strength experienced by a **moving** vehicle on [VHF](07_VHFUHF_Bands_6m,_2m,_70cm.md)/UHF.
    *   *Cause:* Passing through alternating constructive and destructive interference zones (multipath) caused by reflections from buildings/terrain.
    *   *Analogy:* Like the strobing light seen when driving past a picket fence.
3.  **Polarization Fading**: The ionosphere twists the polarization of the wave (Faraday rotation).
    *   *Mechanism:* Cross-polarization loss.
4.  **Flutter Fading**: Rapid, cyclic variation in signal strength.
    *   *Cause:* [Propagation](14_Solar_Cycle_&_Propagation.md) through **Aurora** or highly disturbed ionosphere (Geomagnetic storm).
    *   *Sound:* Rapid "flutter" or "warble" on the signal.
5.  **Selective Fading**: Different frequencies within the same signal (bandwidth) fade differently.
    *   *Effect:* Audio distortion (makes voice sound robotic or hollow).

## Mitigation
*   **[AGC](../04_receivers/03_Automatic_Gain_Control_AGC.md)**: Automatic Gain Control in the receiver compensates for volume changes.
*   **Diversity Reception**: Using multiple antennas/receivers.

---
[< Back to Section Index](README.md)