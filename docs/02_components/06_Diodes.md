# Diodes

A diode is a two-terminal component formed by a single PN junction that allows current to flow in only one direction.

## Operation
*   **Forward Bias (Doorlaat):** Current flows if voltage > **Threshold Voltage** (~0.7V Si, ~0.2V Ge).
*   **Reverse Bias (Sper):** Current is blocked (except for tiny leakage).

## Characteristics
*   **Power Dissipation ($P$):** Heat generated in the diode.
    *   $P \approx I_F \times U_F$
    *   For Silicon: $P \approx I_F \times 0.6V$ (or $0.7V$)
    *   For Germanium: $P \approx I_F \times 0.2V$
*   **Peak Inverse Voltage (PIV):** The maximum voltage the diode can withstand in reverse bias before breaking down.
    *   *Exam Rule of Thumb:* Select a diode with PIV $> 2 \times U_{peak}$ (or $\approx 3 \times U_{eff}$) for safety in rectifier circuits.

## Types
*   **Rectifier Diode:** Converts AC to DC.
*   **Zener Diode:** Conducts in reverse at a specific "Zener Voltage". Used for Voltage Regulation.
*   **LED (Light Emitting Diode):** Emits light when forward biased.
*   **Varicap (Capaciteitsdiode):** Acts as a variable capacitor in reverse bias.

## Connection Issues
*   **Series Connection:** To increase voltage handling.
    *   *Problem:* Unequal leakage currents can cause unequal voltage distribution.
    *   *Solution:* High-value **Balancing Resistors** in parallel with each diode.
*   **Parallel Connection:** To increase current handling.
    *   *Problem:* Unequal forward voltages can cause one diode to hog all the current (thermal runaway).
    *   *Solution:* Low-value **Series Resistors** (e.g., $0.1 \Omega$) with each diode to balance current.

---
[< Back to Section Index](README.md)