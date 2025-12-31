# Phase Locked Loop (PLL)

A PLL is a control system that locks a variable oscillator (VCO) to a stable reference frequency.

## Components
1.  **VCO (Voltage Controlled Oscillator)**: Generates the output frequency.
2.  **Reference Oscillator**: Very stable crystal source.
3.  **Phase Detector (Phase Comparator)**: Compares the phase of the VCO (or divided VCO) to the Reference.
4.  **Loop [Filter](03_Filters_&_Resonance.md)**: A Low-Pass Filter that smooths the output of the Phase Detector into a DC Control Voltage ($U_{reg}$).
5.  **Programmable Divider ($\div N$)**: Divides the VCO frequency down to the reference frequency for comparison.

## Operation
*   If the VCO is too fast, the phase detector sees a phase difference.
*   It adjusts the Control Voltage to slow the VCO down.
*   Result: VCO is "locked" to the reference. $f_{VCO} = N \times f_{ref}$.

## Applications
*   **Frequency Synthesis**: By changing the divider ratio $N$, the output frequency changes in steps equal to the reference frequency ($f_{ref}$).
    *   Stable as a crystal, tunable like a VFO.
*   **[FM](../01_electricity/35_Frequency_Modulation_FM.md) Demodulation**:
    *   The PLL tries to track the incoming FM signal (VCO follows input frequency).
    *   The **Control Voltage** (Error Voltage) must vary exactly like the modulation to keep the VCO locked.
    *   Therefore, the **Control Voltage IS the Demodulated Audio**.

---
[< Back to Section Index](README.md)