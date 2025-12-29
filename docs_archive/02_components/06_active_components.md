# Active Components: Tubes and Op-Amps

## 1. Operating Principle
Vacuum tubes operate on the principle of **Thermionic Emission** (Edison Effect).
*   **Heater (Gloeidraad):** Heats the cathode.
*   **Cathode:** Emits electrons when heated (forms a space charge or "electron cloud").
*   **Anode (Plate):** Attracts electrons if it has a high positive voltage relative to the cathode.
*   **Vacuum:** The glass envelope is evacuated so electrons don't collide with air molecules.

## 2. Tube Types

### The Diode (Two Electrodes)
*   **Parts:** Cathode + Anode.
*   **Function:** Rectification (like a semiconductor diode).
*   **Operation:** Current flows only when Anode is positive.

### The Triode (Three Electrodes)
*   **Added Part:** **Control Grid (Stuurrooster, $g_1$)**.
*   **Structure:** A mesh placed between Cathode and Anode.
*   **Operation:** A small negative voltage on the grid repels electrons, controlling the large current flowing to the anode.
*   **Characteristics:**
    *   **Amplification Factor ($\mu$):** Voltage gain.
    *   **Steepness / Transconductance ($S$):** $S = \Delta I_a / \Delta U_g$. (Unit: mA/V).
    *   **Internal Resistance ($R_i$):** $R_i = \Delta U_a / \Delta I_a$.
    *   **Formula:** $\mu = S \times R_i$.
*   **Drawback:** High capacitance between Anode and Grid ($C_{ag}$), causing oscillation at high frequencies (Miller effect).

### The Tetrode (Four Electrodes)
*   **Added Part:** **Screen Grid (Schermrooster, $g_2$)**.
*   **Placement:** Between Control Grid and Anode.
*   **Function:** Acts as an electrostatic shield between Anode and Control Grid.
    *   Reduces $C_{ag}$ drastically (better for HF).
*   **Voltage:** Maintained at a high positive DC potential (but usually lower than Anode).
*   **Drawback:** **Secondary Emission**. Electrons hitting the anode bounce back and are attracted to the screen grid (kink in characteristic curve).

### The Pentode (Five Electrodes)
*   **Added Part:** **Suppressor Grid (Remrooster / Vangrooster, $g_3$)**.
*   **Placement:** Between Screen Grid and Anode.
*   **Function:** Prevents secondary emission electrons from reaching the screen grid.
*   **Voltage:** Usually connected to the Cathode (0V).
*   **Characteristics:** High gain, high internal resistance.

## 3. Comparison with Semiconductors
*   **Heater:** Tubes need warmup time and consume heater power. [Transistors](05_semiconductors.md) don't.
*   **Voltage:** Tubes work at high voltages (100V - kV). Transistors work at low voltages.
*   **Impedance:** Tubes are high impedance devices.
*   **Hardness:** Tubes are more robust against temporary overloads and EMP compared to semiconductors.

## 4. Operational Amplifiers (Op-Amps)
(Integrated Circuits, typically semiconductor-based)
*   See [Amplifiers](../03_circuits/05_amplifiers.md).
*   **Characteristics:** Very high gain, differential input.
*   **Feedback (Tegenkoppeling):** Essential for linear operation.
*   **Configurations:** Inverting, Non-inverting, Buffer, Comparator.

### Feedback (Tegenkoppeling)
Op-amps are almost always used with negative feedback to control gain and stability.

### Configurations
1.  **Inverting Amplifier:** Output is inverted ($180^\circ$ phase shift).
    *   $Gain = -\frac{R_{feedback}}{R_{input}}$
2.  **Non-Inverting Amplifier:** Output is in phase.
    *   $Gain = 1 + \frac{R_{feedback}}{R_{ground}}$
3.  **Voltage Follower (Buffer):** Output connected directly to (-) input.
    *   $Gain = 1$. Used to match high Z source to low Z load.
4.  **Comparator:** No feedback. Compares inputs and outputs high/low.

---
[Back to Index](../INDEX.md) | [Back to Dashboard](../../README.md)
