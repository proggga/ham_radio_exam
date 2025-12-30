---
id: 202301011207
title: "Voltage and Current Sources"
tags: ["ham-radio", "electricity"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Voltage and Current Sources

## 1. Ideal vs Real Sources
*   **Ideal Voltage Source:** Maintains constant voltage regardless of the current drawn. Internal resistance $R_i = 0$.
*   **Real Voltage Source:** Voltage drops as current increases due to internal resistance.

## 2. Internal Resistance ($R_i$)
Every real battery or power supply has an internal resistance $R_i$ in series with the ideal Electromotive Force (EMF).

### Terminology
*   **EMF (Bronspanning, $E$):** The voltage of the source with **no load** (open circuit).
*   **Terminal Voltage ($U_{klem}$):** The voltage measured at the terminals under load.
    *   $U_{klem} = E - (I_{load} \times R_i)$
    *   Ideally $R_i = 0$, so $U_{klem} = E$.
*   **Short Circuit Current ($I_{short}$):** Maximum current if terminals are shorted ($R_{load} = 0$).
    *   $I_{short} = \frac{E}{R_i}$ (from [[Voltage, Current, and Ohm's Law|Ohm's Law]])

### Calculation Example
**Scenario:** A battery has an EMF of 12V. When a $5 \Omega$ load resistor is connected, the terminal voltage drops to 11V. What is the Internal Resistance ($R_i$)?

1.  **Calculate Current:**
    $$I = \frac{U_{load}}{R_{load}} = \frac{11V}{5\Omega} = 2.2A$$
2.  **Calculate Voltage Drop across Internal Resistance:**
    $$U_{drop} = E - U_{load} = 12V - 11V = 1V$$
3.  **Calculate Internal Resistance:**
    $$R_i = \frac{U_{drop}}{I} = \frac{1V}{2.2A} \approx 0.45 \Omega$$

**Comparison:** If another battery drops to 10V with the same load:
*   $I = 10V / 5\Omega = 2A$
*   $U_{drop} = 12V - 10V = 2V$
*   $R_i = 2V / 2A = 1 \Omega$
*   *Conclusion:* The battery with the larger voltage drop has the **higher** internal resistance.

## 3. Battery Capacity
*   Measured in **Ampere-hours (Ah)**.
*   Example: A 50 Ah battery can theoretically deliver:
    *   1 A for 50 hours.
    *   50 A for 1 hour.

## 4. Battery Chemistries
*   **Primary Cells (Non-Rechargeable):**
    *   **Zinc-Carbon / Alkaline**: Standard disposable batteries (1.5V).
*   **Secondary Cells (Rechargeable):**
    *   **Lead-Acid**: 12V (nominal 13.8V). Heavy. Used in cars and base stations. *Risk:* Hydrogen gas (explosive) when charging.
    *   **NiCd (Nickel-Cadmium)**: 1.2V. Robust but suffers from "memory effect".
    *   **NiMH (Nickel-Metal Hydride)**: 1.2V. Higher capacity than NiCd, less memory effect.
    *   **Li-Ion / LiPo (Lithium-Ion)**: 3.7V per cell. High energy density. *Risk:* Fire/Explosion if overcharged or punctured. Requires specialized chargers.

## 5. Combining Sources
*   **Series:**
    *   Voltage adds up ($U_{tot} = U_1 + U_2$).
    *   Internal resistance adds up.
    *   Capacity (Ah) stays the same (limited by weakest cell).
    *   **Opposing Polarity:** If one battery is connected in reverse, subtract its voltage from the total.
*   **Parallel:**
    *   Voltage stays the same (Must connect identical voltage cells!).
    *   Capacity (Ah) adds up.
    *   Internal resistance decreases ($R_{tot} = R_i / n$).
    *   **Unequal Voltages:** Connecting batteries with different EMFs in parallel is dangerous. The higher voltage source will discharge into the lower one (charging it), causing high circulating currents limited only by the internal resistances. The resulting terminal voltage is indeterminate without knowing the exact internal resistances.

## 5. Active Components as Sources
*   **Transistor Current Source:** A bipolar transistor with a fixed base voltage and emitter resistor acts as a **Constant Current Source**.
    *   The collector current $I_c$ is determined by the base voltage and emitter resistor, independent of the collector load (as long as not saturated).
    *   *Caveat:* If the collector load resistance ($R_c$) changes, the current stays the same. If $R_c$ is reduced by 3x, the power dissipated in it ($P = I^2 R$) also drops by 3x.