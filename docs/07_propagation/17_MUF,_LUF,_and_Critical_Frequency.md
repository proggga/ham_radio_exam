# MUF, LUF, and Critical Frequency

These parameters define the "Operating Window" for [HF](01_Propagation_Basics.md) communication.

## Critical Frequency ($f_c$)
The highest frequency sent **straight up** (Vertical Incidence) that returns to earth. Frequencies higher than $f_c$ escape into space if sent vertically.

## MUF (Maximum Usable Frequency)
The highest frequency that will support communication between two specific points (oblique angle).
*   **Relation**: $MUF \approx \frac{f_c}{\cos(\theta)}$ (where $\theta$ is the angle of incidence).
*   Low angle signals (DX) have a higher MUF than vertical signals.

## LUF (Lowest Usable Frequency)
The lowest frequency that is not completely **absorbed** (mostly by the D-layer).
*   Below the LUF, the signal is too weak to be heard.

## Operating Window
The range between LUF and MUF.
*   **Day**: Window is wide (High MUF, High LUF).
*   **Night**: Window shifts lower (Low MUF, Low LUF).

---
[< Back to Section Index](README.md)