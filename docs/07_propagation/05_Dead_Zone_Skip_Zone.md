id: 202501101200
title: Dead Zone (Skip Zone)
tags: ["ionosphere", "propagation"]
created: 2025-01-10
type: permanent-note
modified: 2025-01-10

aliases: ["Dode Zone (Stille Zone)", "Dode Zone", "Stille Zone", "Skip Zone", "Dead Zone"]

# Dead Zone (Skip Zone)

The **Dead Zone** (Dutch: *Dode Zone* or *Stille Zone*) is a region where a radio transmission cannot be received. It is located between the outer limit of the Ground Wave and the point where the first reflected Sky Wave returns to Earth.

## Concept
When transmitting on [HF](01_Propagation_Basics.md), the signal travels via two primary modes:
1.  **Ground Wave**: Follows the curvature of the Earth but attenuates relatively quickly (e.g., after 50-100 km).
2.  **Sky Wave**: Radiates upward towards the Ionosphere and is refracted back to Earth at a distance (the **Skip Distance**).

If the Ground Wave dies out *before* the Sky Wave returns to Earth, there is a gap in coverage. A receiver located in this gap will hear nothing (or very weak scatter).

## Geometry
*   **A**: Transmitter location.
*   **D**: End of Ground Wave range.
*   **B**: Point where the first Sky Wave lands (determined by the **Skip Distance**).
*   **Dead Zone**: The distance from **D** to **B**.

## Factors Influencing the Dead Zone
1.  **Frequency**:
    *   Higher frequencies generally have a larger **Skip Distance** (they require a shallower angle to be refracted).
    *   This results in a **larger** Dead Zone.
    *   **Exam Rule**: If a Dead Zone is present, the transmission frequency is **higher** than the Critical Frequency. (If it were lower, the signal would be reflected straight back down, covering the area immediately around the transmitter via NVIS).
2.  **Ionospheric Conditions**:
    *   Higher ionization (e.g., during solar max or daytime) allows steeper angles to be reflected.
    *   Steeper angles mean a shorter Skip Distance $\rightarrow$ **smaller** Dead Zone.
3.  **Antenna Take-off Angle**:
    *   Vertical antennas often have low take-off angles, good for DX but creating a large Dead Zone.
    *   Horizontal dipoles low to the ground shoot straight up (high angle).

## Solutions
To communicate with a station inside the Dead Zone, you must eliminate the gap between Ground Wave and Sky Wave.
*   **[Near Vertical Incidence Skywave (NVIS)](06_Near_Vertical_Incidence_Skywave_NVIS.md)**: Using high-angle radiation (shooting straight up) to reflect signals back down very close to the transmitter. Ideally used on lower frequencies (40m, 80m).
*   **Lower Frequency**: Switching to a lower frequency (if below the Critical Frequency) allows for steeper reflection angles.

## Exam Terminology
*   **Skip Distance (Sprongafstand)**: Distance from transmitter to first sky wave reflection.
*   **Dead Zone (Dode/Stille Zone)**: Area with no signal (Skip Distance minus Ground Wave range).

---
[< Back to Section Index](README.md)