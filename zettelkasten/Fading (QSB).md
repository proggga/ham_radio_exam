---
id: 202512292122
title: Fading (QSB)
tags: ["ham-radio", "propagation", "interference"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Fading (QSB)

Fading is the variation in signal strength at the receiver.

## Causes
1.  **Multipath Propagation**: The signal arrives via two different paths (e.g., 1 hop vs 2 hops).
    *   If they arrive **in phase**, they add up (Strong).
    *   If they arrive **out of phase**, they cancel (Weak).
    *   The ionosphere is constantly moving, causing the phase relationship to drift.
2.  **Polarization Fading**: The ionosphere twists the polarization of the wave (Faraday rotation).
    *   If a horizontal wave twists to vertical, a horizontal antenna will receive it poorly.

## Mitigation
*   **AGC**: Automatic Gain Control in the receiver compensates for volume changes.
*   **Diversity Reception**: Using multiple antennas/receivers.

## Related
*   [[Automatic Gain Control (AGC)]]
*   [[Ionospheric Layers]]
