---
id: 202301011202
title: "Voltage, Current, and Ohm's Law"
tags: ["ham-radio", "electricity"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Voltage, Current, and Ohm's Law

## 1. Electric Current (Stroom)
Current is the flow of electric charge.
*   **Symbol:** $I$
*   **Unit:** Ampere ($A$)
*   **Definition:** $1 \text{ A} = 1 \text{ Coulomb per second} (C/s)$. See [[Atomic Theory & Conductivity|Atomic Theory]] for Charge.
*   **Formula:** $I = \frac{Q}{t}$ (Current = Charge / Time).

### Direction of Current
*   **Electron Flow:** Electrons move from **Minus (-)** to **Plus (+)**.
*   **Technical Current Direction:** Defined historically as flowing from **Plus (+)** to **Minus (-)**.
    *   *Convention:* In electronics, we always calculate using the Technical Direction (Plus to Minus).

## 2. Voltage (Spanning)
Voltage is the potential difference between two points. It is the "pressure" that pushes charge through a circuit.
*   **Symbol:** $U$ (sometimes $V$ or $E$)
*   **Unit:** Volt ($V$)
*   **Analogy:** Voltage is like water pressure; Current is like water flow.

## 3. Resistance (Weerstand)
Resistance is the opposition to current flow.
*   **Symbol:** $R$
*   **Unit:** Ohm ($\Omega$)
*   **Analogy:** Resistance is like a narrow pipe restricting water flow.

## 4. Ohm's Law (Wet van Ohm)
The fundamental relationship between Voltage, Current, and Resistance.
$$U = I \times R$$

Derived forms:
*   $I = \frac{U}{R}$
*   $R = \frac{U}{I}$

### IV-Characteristic (Stroom-spanningskarakteristiek)
If you plot Current ($I$) on the Y-axis against Voltage ($U$) on the X-axis:
*   For a fixed resistor, the result is a straight line through the origin.
*   **Steep line:** Low resistance (Large current increase for small voltage increase).
*   **Flat line:** High resistance (Small current increase for large voltage increase).
*   **Parallel:**
    *   Voltage stays the same (Must connect identical voltage cells!).
    *   *Caveat:* Connecting sources with **unequal** voltages in parallel is dangerous. The higher voltage source will discharge into the lower one with high current (limited only by internal resistances), potentially causing overheating or explosion. Ideally, the terminal voltage settles somewhere between the two EMFs.
    *   Capacity (Ah) adds up.
    *   Internal resistance decreases ($R_{tot} = R_i / n$).