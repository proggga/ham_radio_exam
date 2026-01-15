---
id: 202501111645
title: Batteries
tags:
  - ham-radio
  - power-supply
  - portable
created: 2025-01-11
type: permanent-note
modified: 2025-01-11

aliases: ["Batterijen en Accu"s", "Batterijen", "Accu"s", "Batteries", "Accumulators"]
---

# Batteries

Batteries store electrical energy chemically. They are essential for portable operation and emergency power.

## 1. Capacity
*   Measured in **Ampere-hours (Ah)**.
*   **Formula**: $Capacity = Current \times Time$.
*   *Example:* A 7 Ah battery can theoretically deliver 1A for 7 hours, or 7A for 1 hour (though in practice, high currents reduce efficiency, see Peukert's Law).

## 2. Chemistries
### Primary (Non-Rechargeable)
*   **Zinc-Carbon / Alkaline**: 1.5V per cell. High internal resistance. Suitable for low-drain devices.

### Secondary (Rechargeable)
*   **Lead-Acid (Loodaccu)**:
    *   **Voltage**: Nominal 2.0V/cell (12V battery = 6 cells). Charged $\approx 13.8V$.
    *   **Types**: Flooded (Car), Sealed (SLA/AGM), Gel.
    *   **Pros**: Cheap, easy to charge.
    *   **Cons**: Heavy, sulphation if left discharged. **Ventilation required** (Hydrogen gas risk).
*   **NiCd (Nickel-Cadmium)**:
    *   **Voltage**: 1.2V/cell.
    *   **Pros**: High current delivery.
    *   **Cons**: Toxic (Cadmium), Memory Effect.
*   **NiMH (Nickel-Metal Hydride)**:
    *   **Voltage**: 1.2V/cell.
    *   **Pros**: Higher capacity than NiCd, less memory effect.
*   **Li-Ion / LiPo (Lithium-Ion)**:
    *   **Voltage**: 3.7V/cell (nominal).
    *   **Pros**: Very light, high energy density.
    *   **Cons**: **Fire hazard** if overcharged, punctured, or shorted. Requires Battery Management System (BMS).
*   **LiFePO4 (Lithium Iron Phosphate)**:
    *   **Voltage**: 3.2V/cell. (4 cells = 12.8V, perfect for 13.8V radios).
    *   **Pros**: Safest Lithium chemistry, constant discharge voltage, light.

## 3. Configuration
*   **Series**: Voltage adds up ($V_{tot} = V_1 + V_2$). Capacity stays the same.
*   **Parallel**: Capacity adds up ($Ah_{tot} = Ah_1 + Ah_2$). Voltage stays the same.
    *   *Warning:* Never connect batteries of different voltages in parallel!

## 4. Internal Resistance
All batteries have an internal resistance ($R_i$) that causes the terminal voltage to drop under load.
*   $V_{load} = V_{emf} - (I \times R_i)$.

## Related
*   [[Voltage and Current Sources]]
*   [[Power Supply]]
*   [[Electrical Safety]]
