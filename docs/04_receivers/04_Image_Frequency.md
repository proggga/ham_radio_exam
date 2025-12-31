# Image Frequency (Spiegelfrequentie)

A major disadvantage of the superheterodyne architecture. The mixer produces the IF from *two* possible RF frequencies: the desired signal and the image.

## The Problem
If the receiver is tuned to $f_{RF}$ and uses high-side injection ($f_{LO} > f_{RF}$):
*   $f_{LO} = f_{RF} + f_{IF}$

An unwanted signal at $f_{Image} = f_{LO} + f_{IF}$ will also produce the IF difference:
*   $f_{Image} - f_{LO} = f_{IF}$

**Formula**: $f_{Image} = f_{RF} + 2 \cdot f_{IF}$

## Mitigation
1.  **Preselector**: A sharp RF filter before the mixer to reject the image frequency.
2.  **High IF**: Using a high IF (e.g., 45 MHz) moves the image frequency far away ($+90 MHz$), making it easy for the preselector to block.
3.  **Double Conversion**: Using two IF stages.
    *   **1st IF (High)**: Ensures good **Image Rejection**.
    *   **2nd IF (Low)**: Ensures good **Selectivity** (Adjacent channel rejection).

---
[< Back to Section Index](README.md)