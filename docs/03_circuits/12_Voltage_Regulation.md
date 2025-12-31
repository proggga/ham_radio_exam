# Voltage Regulation

Regulation keeps the output voltage constant despite changes in Load Current or Mains Voltage.

## Zener Diode Regulator
*   **Component**: [Zener Diode](../02_components/19_Zener_Diode.md) (Zenerdioden).
*   **Setup**: Zener diode in reverse bias (parallel to load) + Series [Resistor](../02_components/01_Resistors.md).
*   **Operation**: Zener maintains constant breakdown voltage.
*   **Resistor**: $R_{series} = \frac{U_{in} - U_{zener}}{I_{zener} + I_{load}}$
*   **Use**: Low power reference voltages.

## Series Regulator (Emitter Follower)
Boosts the current capability of a Zener regulator.
*   **Circuit**: Zener reference connected to the Base of a pass transistor (Emitter Follower).
*   **Output Voltage**: $U_{out} = U_{zener} - U_{be}$
    *   For Silicon ($U_{be} \approx 0.6V$): $U_{out} = U_{zener} - 0.6V$.
    *   *Example:* A 5.6V Zener + Si transistor gives $\approx 5.0V$ output.

## Feedback Regulator
Uses an Op-Amp (Comparator) to compare output with a reference.
*   **Principle**: Negative feedback adjusts the pass transistor to keep $U_{out}$ constant.
*   **Stability**: Much better than simple series regulators.

## Linear Series Regulator (General)
Uses a transistor to control output voltage.
*   **Operation**: [Transistor](../02_components/18_Transistors_BJT_&_FET.md) acts as a variable resistor.
*   **Dissipation**: Excess power is lost as heat.
    *   $P = (U_{in} - U_{out}) \times I_{load}$

## IC Regulators
Integrated circuits simplifying regulation.
*   **78xx Series**: Positive voltage (e.g., 7812 for +12V).
*   **79xx Series**: Negative voltage (e.g., 7905 for -5V).

---
[< Back to Section Index](README.md)