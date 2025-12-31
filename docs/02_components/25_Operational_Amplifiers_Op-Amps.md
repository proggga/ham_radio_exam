# Operational Amplifiers (Op-Amps)

An Op-Amp is a high-gain integrated circuit amplifier with differential inputs.

## Characteristics
*   **Gain**: Very high open-loop gain ($A_0$), typically $10^5$ to $10^6$.
*   **Gain-[Bandwidth](../03_circuits/07_Bandwidth.md) Product (GBW)**: The open-loop gain decreases linearly with frequency. The product of Gain $\times$ Frequency is constant.
    *   *Example:* A 741 Op-amp has a GBW of $\approx 1$ MHz. At 1 MHz, gain is 1. At 1 kHz, gain is 1000.
*   **Inputs**: Inverting (-) and Non-Inverting (+).
    *   **Rule**: In a negative feedback configuration, the voltage difference between inputs is zero ($U_+ = U_-$).
*   **[Impedance](../01_electricity/21_Impedance_Impedantie.md)**: Very high input impedance ($Z_{in}$), low output impedance ($Z_{out}$).
*   **[Offset](../11_procedures.md) Nulling**: Terminals provided to zero the output voltage when inputs are zero.

## Feedback (Tegenkoppeling)
Op-amps are almost always used with **negative feedback** to control gain and stability.

## Configurations

### 1. Inverting Amplifier
Output is inverted ($180^\circ$ phase shift).
*   **Gain**: $A_u = -\frac{R_2}{R_1}$ (where $R_2$ is feedback, $R_1$ is input resistor).
*   **Input [Impedance](../01_electricity/21_Impedance_Impedantie.md)**: Equal to $R_1$ (Virtual ground at input).
*   **Virtual Ground**: The (-) input is at 0V potential but not connected to ground.

### 2. Non-Inverting Amplifier
Output is in phase with input.
*   **Gain**: $A_u = 1 + \frac{R_2}{R_1}$ (where $R_2$ is feedback, $R_1$ is to ground).
*   **Input [Impedance](../01_electricity/21_Impedance_Impedantie.md)**: Extremely High (Input connects directly to Op-Amp gate/base).

### 3. Voltage Follower (Buffer)
Output connected directly to (-) input.
*   **Gain**: 1 ($A_u = 1$).
*   **Characteristics**: Extremely High $Z_{in}$, Low $Z_{out}$.
*   **Use**: Impedance matching (High Z source to Low Z load).

### 4. Summing Amplifier (Optelversterker)
Adds multiple input voltages together (inverted).
*   **Formula**: $U_{out} = -R_f (\frac{U_1}{R_1} + \frac{U_2}{R_2} + ...)$
*   *Special Case*: If all resistors are equal, $U_{out} = -(U_1 + U_2 + ...)$.

### 5. Difference Amplifier (Verschilversterker)
Amplifies the difference between two inputs.
*   **Formula**: $U_{out} = \frac{R_2}{R_1} (U_2 - U_1)$ (assuming matched resistor pairs).
*   **Condition**: [Resistors](01_Resistors.md) must be precisely matched for good Common Mode Rejection.

### 6. Comparator
No feedback used. Compares inputs ($U_{in}$ vs $U_{ref}$).
*   If $U_{in} > U_{ref} \rightarrow U_{out} = +U_{supply}$
*   If $U_{in} < U_{ref} \rightarrow U_{out} = -U_{supply}$

---
[< Back to Section Index](README.md)