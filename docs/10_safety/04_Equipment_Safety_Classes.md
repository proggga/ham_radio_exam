# Equipment Safety Classes

## Class I: Earthed
*   **Symbol:** Ground symbol ($\perp$ in circle).
*   **Protection:**
    1.  **Basic Insulation:** Covers live parts.
    2.  **Protective Earth (PE):** Metal chassis is connected to Earth.
*   **Failure Mode:** If insulation fails and live wire touches chassis -> Current flows to Earth -> Fuse blows or RCD trips.

## Class II: Double Insulated
*   **Symbol:** Square inside a square ($\square$).
*   **Protection:**
    1.  **Basic Insulation.**
    2.  **Supplementary Insulation:** A second independent layer (e.g., plastic casing).
*   **No Earth:** Does not require a safety earth connection. Mains cable has 2 wires (L, N).

## Class III: SELV
*   **Symbol:** Diamond with "III".
*   **Protection:** Supply voltage is too low to cause shock (< 60V DC / 30V AC).
*   **Source:** Batteries or a [Safety](01_Electrical_Safety.md) Transformer (SELV power supply).

---

# Other Hazards

## 1. Lightning
*   **Direct Strike:** Destroys equipment, fire risk.
*   **Induction:** Nearby strikes induce high voltages in antennas/cables.
*   **Protection:**
    *   **Disconnect:** Unplug antennas and mains during storms (Best protection).
    *   **Grounding:** Heavy gauge wire to earth electrode outside.
    *   **Spark Gaps:** Gas discharge tubes across [Coax](../06_antennas/13_Transmission_Lines.md).

## 2. Chemical
*   **Batteries:** Lithium types can burn/explode if shorted or punctured. Lead-acid releases Hydrogen (explosive) when charging.
*   **Beryllium Oxide (BeO):** White ceramic used in high-power RF transistors/tubes. **Toxic dust** if broken/filed. Do not machine!

## 3. Working at Heights
*   **Risk:** Falling, dropped tools.
*   **[Safety](01_Electrical_Safety.md):** Use a harness, hard hat, secure ladders, have a ground spotter.

---
[< Back to Section Index](README.md)