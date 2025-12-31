# Baluns

A **Balun** (**Bal**anced to **Un**balanced transformer) interfaces a balanced antenna (like a [Dipole](../06_antennas/02_The_Dipole_Antenna.md)) to an unbalanced transmission line (like Coaxial cable).

## Choke Balun (Current Balun)
*   **Function**: Forces the currents in the two output conductors to be equal and opposite.
*   **Purpose**: Prevents **Common Mode Current** from flowing on the *outside* of the coax shield.
*   **Construction**: Coils of coax ("Ugly Balun") or Ferrite beads/rings slipped over the cable.
*   **Importance**: Without a choke, the feedline radiates, causing [RFI](../09_interference/06_Causes_of_Interference.md) and distorting the antenna pattern.

## Voltage Balun
*   **Function**: Transforms impedance while converting balanced/unbalanced.
*   **Ratios**:
    *   **1:1**: No impedance change (e.g., [Dipole](../06_antennas/02_The_Dipole_Antenna.md) to Coax).
    *   **4:1**: Matches high impedance to low (e.g., Folded [Dipole](../06_antennas/02_The_Dipole_Antenna.md) $300\Omega$ to $75\Omega$ coax).
    *   **1:9** or **1:49**: Used for End-Fed antennas (High Z to $50\Omega$).

---
[< Back to Section Index](README.md)