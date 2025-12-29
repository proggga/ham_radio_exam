# Matching and SWR

## 1. Standing Wave Ratio (SWR)
A measure of how well the load (antenna) is matched to the transmission line.
*   **Mismatch:** Causes reflection of power back to the transmitter.
*   **Standing Waves:** Interference between Forward and Reflected waves creates static peaks ($V_{max}$) and troughs ($V_{min}$) of voltage on the line.
*   **Formula:**
    $$SWR = \frac{V_{max}}{V_{min}}$$
    $$SWR = \frac{1 + \sqrt{P_{ref}/P_{fwd}}}{1 - \sqrt{P_{ref}/P_{fwd}}}$$
*   **Values:**
    *   1:1 = Perfect match (No reflection).
    *   $\infty$ = Total reflection (Open or Short circuit).

## 2. Baluns
**Bal**anced to **Un**balanced transformer.
*   **Purpose:** To connect a symmetric antenna ([Dipole](01_types.md)) to an asymmetric line ([Coax](03_transmission_lines.md)).
*   **Choke Balun (Mantelstroomfilter):**
    *   Coils of coax or Ferrite beads.
    *   **Function:** Stops current flowing on the *outside* of the coax shield (Common Mode Current).
    *   *Why?* Currents on the shield cause the feedline to radiate, leading to interference (RFI) and distorted antenna patterns.
*   **Voltage Balun:** Transforms impedance (e.g., 4:1 for a folded dipole).

## 3. Antenna Tuning Unit (ATU)
Also called a Transmatch or Matchbox.
*   **Function:** Transforms the impedance at the "Shack end" of the feedline to $50 \Omega$ for the transmitter.
*   **Important:** It does **NOT** tune the antenna or change the SWR on the feedline. It only satisfies the transmitter's protection circuits.
    *   High SWR on the coax still causes loss, even if the ATU shows 1:1 to the radio.

## 4. Smith Chart
A graphical tool used to plot impedance, SWR, and design matching networks.
*   Center = $Z_0$ (Perfect match).
*   Circles = Constant Resistance.
*   Arcs = Constant Reactance. See [Reactance](../03_circuits/07_reactance_impedance.md).

---
[Back to Index](../INDEX.md) | [Back to Dashboard](../../README.md)
