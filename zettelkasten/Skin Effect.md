---
id: 202512302200
title: Skin Effect
tags: ["ham-radio", "physics", "components"]
created: 2025-12-30
type: permanent-note
modified: 2025-12-30
---

# Skin Effect

The tendency of an alternating current (AC) to distribute itself within a conductor such that the current density is largest near the surface of the conductor, and decreases with greater depths.

## Mechanism
*   **Eddy Currents**: The changing magnetic field inside the conductor induces eddy currents that cancel the current flow in the center and reinforce it at the surface.
*   **Result**: The effective cross-sectional area of the conductor is reduced.

## Consequences
*   **Increased Resistance**: The AC resistance of the wire is higher than its DC resistance.
*   **Frequency Dependent**: The effect becomes more pronounced as frequency increases.
    *   Depth of penetration ($\delta$) decreases as frequency increases.

## Mitigation
To reduce losses due to skin effect in RF coils and antennas:
1.  **Litz Wire**: Wire made of many thin, individually insulated strands (used at MF/[[Propagation Basics|HF]]). Increases total surface area.
2.  **Silver Plating**: Plating copper wire with silver (highly conductive) reduces resistance at the surface (used at [[VHFUHF Bands (6m, 2m, 70cm)|VHF]]/[[VHFUHF Bands (6m, 2m, 70cm)|UHF]]).
3.  **Tubing**: Using hollow tubes instead of solid wire for antennas (since the center carries no current anyway).
4.  **Spacing**: Spacing turns of a coil reduces proximity effect (related to skin effect).

## Exam Scenarios
*   Resistance of a coil increases with frequency.
*   Use silver-plated wire or Litz wire to minimize losses.

## Related
*   [[Inductors (Spoelen)]]
*   [[Transformer Losses]]
