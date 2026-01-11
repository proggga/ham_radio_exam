# Oscillators

Oscillators are circuits that generate an AC signal from DC.

## Barkhausen Criterion
For oscillation to occur and sustain:
1.  **Loop Gain**: $\ge 1$ (starts > 1, stabilizes at 1).
2.  **Phase [Shift](../11_procedures.md)**: $0^\circ$ or $360^\circ$ (Positive Feedback).
    *   In a common-emitter/source circuit (180° shift), the feedback network must provide an additional 180°.

## LC Oscillators (Variable Frequency)
Used in VFOs (Variable Frequency Oscillators). Frequency determined by $f = \frac{1}{2\pi\sqrt{LC}}$.
*   **Hartley**: Uses an **inductive** voltage divider (tapped coil).
    *   *Mnemonic:* **H**artley = **H**enry ([Inductor](../02_components/09_Inductors_Spoelen.md)).
*   **Colpitts**: Uses a **capacitive** voltage divider (two capacitors in series).
    *   *Mnemonic:* **C**olpitts = **C**apacity.
*   **Clapp**: A Colpitts with an extra series capacitor to tune the inductance. Improves stability.
*   **Seiler**: A variation of Colpitts with a capacitive divider coupled loosely to the active device.

## Crystal Oscillators (Fixed Frequency)
Uses a [Quartz](../02_components/27_Crystals_Quartz.md) crystal for high stability.
*   **Pierce**: Crystal connects between input and output (e.g., Gate-Drain). Crystal acts as an inductor. No tuned circuit needed for fundamental mode.
*   **Miller**: Uses internal capacitance of the active device (FET) for feedback. Crystal is parallel to the input.
*   **Overtone**: Crystal vibrates at an odd harmonic (3rd, 5th, etc.).
    *   **Requirement:** An LC tank circuit tuned to the harmonic is required in the output to force oscillation at the overtone frequency.

## Voltage Controlled Oscillator (VCO)
*   Frequency is controlled by a DC voltage.
*   **Component**: Uses a **[Varicap](../02_components/22_Varicap_Capaciteitsdiode.md)** (capacitance diode) in the tuned circuit. Reverse voltage changes capacitance $\to$ changes frequency.

## Stability & Phase Noise
*   **Phase [Noise](../01_electricity/26_AC_Signals_&_Noise.md)**: Short-term frequency instability (jitter). Appears as noise sidebands. Widens the signal and degrades receiver selectivity.
*   **Stability**: Improved by mechanical rigidity, temperature control (TCXO/OCXO), and loose coupling between oscillator and load (buffer).

## Parasitic Oscillations
Unwanted oscillations caused by stray capacitance/inductance (often in PA stages).
*   **Symptoms**: Overheating, distortion, interference.
*   **Cure**: Ferrite beads on leads, neutralizing capacitors.

---
[< Back to Section Index](README.md)