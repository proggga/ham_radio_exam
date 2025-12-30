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

## 4. Combining Sources
*   **Series:**
    *   Voltage adds up ($U_{tot} = U_1 + U_2$).
    *   Internal resistance adds up.
    *   Capacity (Ah) stays the same (limited by weakest cell).
*   **Parallel:**
    *   Voltage stays the same (Must connect identical voltage cells!).
    *   Capacity (Ah) adds up.
    *   Internal resistance decreases ($R_{tot} = R_i / n$).