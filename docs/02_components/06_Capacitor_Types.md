# Capacitor Types

## Fixed Capacitors
*   **Ceramic**: General purpose, RF coupling/decoupling.
*   **Plastic Film**: Stable, audio/power applications.
*   **Mica**: High stability, high Q, used in filters.

## Electrolytic Capacitors (Elco)
*   **Characteristics**: High capacitance per volume.
*   **Polarized**: Has Positive (+) and Negative (-) terminals.
    *   **Warning**: Connecting in reverse causes explosion/failure.
    *   **Use**: Power supply smoothing, audio coupling.

## Frequency Characteristics
*   **[HF](../07_propagation/01_Propagation_Basics.md)/[VHF](../07_propagation/07_VHFUHF_Bands_6m,_2m,_70cm.md) Applications:**
    *   **Ceramic:** Preferred for [VHF](../07_propagation/07_VHFUHF_Bands_6m,_2m,_70cm.md) (e.g., 145 MHz) due to low inductance.
    *   **Air/Vacuum:** Lowest losses (best dielectric) for [HF](../07_propagation/01_Propagation_Basics.md) applications.
    *   **Value:** Typical tuning capacitor for Shortwave ([HF](../07_propagation/01_Propagation_Basics.md)) is ~100 pF (compared to ~500 pF for Medium Wave).

## Variable Capacitors
*   **Air Variable**: Rotatable metal plates meshing together. Used for VFO tuning and [Antenna](../10_safety/03_Antenna_&_Tower_Safety.md) Matching.
*   **Trimmer**: Small adjustable capacitor for screwdriver calibration.

## Breakdown Voltage
The maximum voltage the dielectric can withstand before arcing occurs. Exceeding this destroys the component.

## Typical Capacitance Ranges (Exam Reference)
Different dielectric materials are suitable for different capacitance ranges.

| Type | Typical Range | Key Application |
| :--- | :--- | :--- |
| **Air / Vacuum** | 1 pF - 500 pF | VFO Tuning, [ATU](../06_antennas/21_Antenna_Tuning_Unit_ATU.md) |
| **Mica** | 1 pF - 10 nF | High stability RF [Filters](../03_circuits/03_Filters_&_Resonance.md) |
| **Ceramic** | 1 pF - 100 nF | RF coupling/decoupling, general purpose |
| **Plastic Film** | 1 nF - 10 µF | Audio, timing circuits |
| **Electrolytic (Elco)** | 1 µF - > 10,000 µF | **Power Supply Smoothing**, low frequency coupling |

## Example Exam Question
**Question:** A capacitor with a capacitance of **200 µF** is a:
A. Mica capacitor
B. Electrolytic capacitor
C. Air capacitor

**Answer:** **B (Electrolytic capacitor)**.
*   **Why?**
    *   **Air** and **Mica** capacitors are used for high frequencies and typically have very small values (picofarads to nanofarads).
    *   **200 µF** is a relatively large value, requiring a thin dielectric and large surface area, which is characteristic of **Electrolytic** capacitors (used for power supplies/audio).

---
[< Back to Section Index](README.md)