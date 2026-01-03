---
id: 202512292100
title: Capacitor Types
tags: ["ham-radio", "components", "capacitors"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

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
*   **[[Propagation Basics|HF]]/[[VHFUHF Bands (6m, 2m, 70cm)|VHF]] Applications:**
    *   **Ceramic:** Preferred for [[VHFUHF Bands (6m, 2m, 70cm)|VHF]] (e.g., 145 MHz) due to low inductance.
    *   **Air/Vacuum:** Lowest losses (best dielectric) for [[Propagation Basics|HF]] applications.
    *   **Value:** Typical tuning capacitor for Shortwave ([[Propagation Basics|HF]]) is ~100 pF (compared to ~500 pF for Medium Wave).

## Variable Capacitors
*   **Air Variable**: Rotatable metal plates meshing together. Used for VFO tuning and [[Antenna & Tower Safety|Antenna]] Matching.
*   **Trimmer**: Small adjustable capacitor for screwdriver calibration.

## Breakdown Voltage
The maximum voltage the dielectric can withstand before arcing occurs. Exceeding this destroys the component.

## Typical Capacitance Ranges (Exam Reference)
Different dielectric materials are suitable for different capacitance ranges.

| Type | Typical Range | Key Application |
| :--- | :--- | :--- |
| **Air / Vacuum** | 1 pF - 500 pF | VFO Tuning, [[Antenna Tuning Unit (ATU)|ATU]] |
| **Mica** | 1 pF - 10 nF | High stability RF [[Filters & Resonance|Filters]] |
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

## Related
*   [[Capacitor Principles]]
*   [[Power Supply Smoothing]]
