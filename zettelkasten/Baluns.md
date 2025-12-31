---
id: 202512292191
title: Baluns
tags:
  - ham-radio
  - antennas
  - components
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Baluns

A **Balun** (**Bal**anced to **Un**balanced transformer) interfaces a balanced antenna (like a [[The Dipole Antenna|Dipole]]) to an unbalanced transmission line (like Coaxial cable).

## Choke Balun (Current Balun)
*   **Function**: Forces the currents in the two output conductors to be equal and opposite.
*   **Purpose**: Prevents **Common Mode Current** from flowing on the *outside* of the coax shield.
*   **Construction**: Coils of coax ("Ugly Balun") or Ferrite beads/rings slipped over the cable.
*   **Importance**: Without a choke, the feedline radiates, causing [[Causes of Interference|RFI]] and distorting the antenna pattern.

## Voltage Balun
*   **Function**: Transforms impedance while converting balanced/unbalanced.
*   **Ratios**:
    *   **1:1**: No impedance change (e.g., Dipole to Coax).
    *   **4:1**: Matches high impedance to low (e.g., Folded Dipole $300\Omega$ to $75\Omega$ coax).
    *   **1:9** or **1:49**: Used for End-Fed antennas (High Z to $50\Omega$).

## Related Notes
*   [[Transmission Line Types]] - Coax (Unbalanced) vs Twin Lead (Balanced).
*   [[The Dipole Antenna]] - A balanced load.
*   [[Transformers]]
