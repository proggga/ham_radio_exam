# Varicap (Capaciteitsdiode)

A diode designed to act as a voltage-controlled capacitor. Also known as a **Varactor**.

## Operation
*   **Reverse Bias**: Used exclusively in **Reverse Bias** (Sperrichting).
*   **Depletion Zone**: Acting as the dielectric of a capacitor.
    *   **Higher Reverse Voltage** $\rightarrow$ Wider Depletion Zone $\rightarrow$ **Lower Capacitance**.
    *   **Lower Reverse Voltage** $\rightarrow$ Narrower Depletion Zone $\rightarrow$ **Higher Capacitance**.

## Application
*   **Tuning**: Used in LC circuits (VFOs, filters) to change frequency electronically.
*   **Circuit**: Often connected in series with a fixed capacitor to block DC control voltage from the inductor.
    *   Control voltage is applied via a high-value resistor (e.g., $100k\Omega$) to prevent loading the RF circuit (preserving $Q$).

## Characteristics
*   **Capacitance Range**: Typically small (e.g., 5-50 pF).
*   **Symbol**: [Diode](17_Diodes.md) with a capacitor plate on the cathode.

## Exam Calculations
*   **[Resonance](../03_circuits/05_Resonance.md) Formula**: $f = \frac{1}{2\pi\sqrt{LC}}$
*   **Relationship**: Frequency is inversely proportional to the square root of capacitance ($f \propto \frac{1}{\sqrt{C}}$).
*   **Scenario**: To **double** the frequency ($2 \times f$), the capacitance must be reduced to **one quarter** ($1/4 \times C$).
    *   Because $\sqrt{1/4} = 1/2$, and $1 / (1/2) = 2$.
    *   *Action:* Increase the reverse voltage to decrease capacitance.

---
[< Back to Section Index](README.md)