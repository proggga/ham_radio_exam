# Voltage and Current Sources

## 1. Ideal vs Real Sources
*   **Ideal Voltage Source:** Maintains constant voltage regardless of the current drawn. Internal resistance $R_i = 0$.
*   **Real Voltage Source:** Voltage drops as current increases due to internal resistance.

## 2. Internal Resistance ($R_i$)
Every real battery or power supply has an internal resistance $R_i$ in series with the ideal Electromotive Force (EMF).

### Terminology
*   **EMF (Bronspanning, $E$):** The voltage of the source with **no load** (open circuit).
*   **Terminal Voltage (Klemspanning, $U_k$):** The voltage available at the terminals when current $I$ flows.
    $$U_k = E - (I \times R_i)$$
*   **Short Circuit Current ($I_{short}$):** Maximum current when terminals are shorted ($R_{load} = 0$).
    $$I_{short} = \frac{E}{R_i}$$

### Power Transfer
Maximum power is transferred to the load when the Load Resistance equals the Internal Resistance ($R_{load} = R_i$).
*   Efficiency at this point is only 50% (half power lost in source).

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
