# Power Supply (Voeding)

## 1. Rectification (Gelijkrichting)
The process of converting Alternating Current (AC) into pulsating Direct Current (DC).

### Half-Wave Rectification (Enkelzijdige gelijkrichting)
*   **Components:** 1 [Diode](../02_components/05_semiconductors.md).
*   **Operation:** Passes only the positive (or negative) half-cycles.
*   **Efficiency:** Low. Half the power is discarded.
*   **Ripple Frequency:** Equal to input frequency ($50 Hz$).
*   **Use:** Low power, non-critical applications.

### Full-Wave Rectification (Tweezijdige gelijkrichting)
*   **Center-Tap Transformer:** Uses 2 Diodes.
    *   Transformer secondary has a center tap (0V). Ends are anti-phase.
    *   Diodes conduct alternately.
*   **Bridge Rectifier (Bruggelijkrichter):** Uses 4 Diodes.
    *   Does not require a center-tap transformer.
    *   Standard method for most power supplies.
*   **Characteristics:**
    *   **Ripple Frequency:** Double the input frequency ($100 Hz$).
    *   **Efficiency:** High. Both half-cycles are used.

## 2. Smoothing (Afvlakking)
Converting pulsating DC into steady DC using filters.

### Reservoir Capacitor
A large electrolytic [Capacitor](../02_components/02_capacitors.md) connected in parallel with the output.
*   **Function:** Charges to the peak voltage ($U_{peak}$) during pulses and discharges into the load between pulses.
*   **Ripple (Rimpel):** The residual AC variation on the DC output.
    *   Larger Load Current -> **More** Ripple.
    *   Larger Capacitor -> **Less** Ripple.
    *   Higher Ripple Frequency (100Hz vs 50Hz) -> **Less** Ripple (easier to filter).
*   **Output Voltage:** $\approx U_{peak} = U_{eff} \times \sqrt{2}$.

### LC Filters
For better smoothing, an Inductor (Choke/Smoorspoel) and a second Capacitor are added.
*   **Configuration:** C-L-C (Pi-filter).
*   **Choke ($L$):** Opposes changes in current, smoothing the flow. See [Inductors](../02_components/03_inductors.md).
*   **Second Capacitor ($C$):** Further reduces voltage ripple.

## 3. Regulation (Stabilisatie)
Keeping the output voltage constant despite changes in Load Current or Mains Voltage.

### Zener Diode Regulator
*   **Configuration:** [Zener diode](../02_components/05_semiconductors.md) in reverse bias (parallel to load) + Series Resistor.
*   **Operation:** The Zener maintains a constant breakdown voltage.
*   **Resistor Calculation:**
    $$R_{series} = \frac{U_{in} - U_{zener}}{I_{zener} + I_{load}}$$
*   **Limitations:** Inefficient. Suitable only for low power / reference voltages.

### Linear Regulator
*   **Series Regulator:** A [Transistor](../02_components/05_semiconductors.md) (Emitter Follower) controls the output voltage, referenced to a Zener.
*   **Integrated Circuits (ICs):** e.g., 78xx (Positive), 79xx (Negative).
    *   *7812:* +12V output.
    *   *7805:* +5V output.
*   **Dissipation:** Excess power is converted to heat. ($P = (U_{in} - U_{out}) \times I$).

### Switch Mode Power Supply (SMPS)
*   **Operation:** Rectifies mains directly, then switches it at high frequency (kHz to MHz), transforms it, and rectifies again.
*   **Control:** **PWM** (Pulse Width Modulation) adjusts the duty cycle to regulate voltage.
*   **Pros:** High efficiency (> 80%), small, light (no heavy 50Hz transformer).
*   **Cons:** Generates **RF Noise (QRM)**. Requires good EMI filtering. See [Interference](../09_interference/01_types.md).

---
[Back to Index](../INDEX.md) | [Back to Dashboard](../../README.md)
