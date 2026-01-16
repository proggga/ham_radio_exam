# Amplifier Operating Principles

An amplifier increases the amplitude of a signal (Voltage, Current, or Power) without changing its shape (ideally). It uses an active device to control a power source.

## Biasing (Instelling)
To work correctly, the active device (like a transistor) must be set to a specific **Operating Point** (Werkpunt or Instelpunt) using DC voltages and currents.
*   **Purpose**: To ensure the device operates in its linear region (for Class A) or appropriate cutoff point.
*   **Methods**:
    *   **Base/Gate [Resistors](../02_components/01_Resistors.md)**: Set the DC voltage.
    *   **Emitter/Source/Cathode [Resistor](../02_components/01_Resistors.md)**: Provides self-bias and thermal stability (negative feedback for DC).

## Load Line (Belastingslijn)
A graphical tool to visualize amplifier operation and select the Operating Point.
*   **Graph:** Plots Output Current ($I_D$ or $I_C$) vs Output Voltage ($U_{DS}$ or $U_{CE}$).
*   **Construction:** Drawn as a straight line connecting two extreme points:
    1.  **Cutoff Point (Sper):** Current = 0. Voltage = Supply Voltage ($U_b$).
    2.  **Saturation Point (Verzadiging):** Voltage = 0. Current = $U_b / (R_{load} + R_{source/emitter})$.
*   **Operating Point (Werkpunt, P):** The intersection of the Load Line and the device's characteristic curve for the chosen bias voltage ($U_{GS}$ or $I_B$).
    *   **Class A:** P is in the middle of the line (maximum swing).
    *   **Class B:** P is at Cutoff ($I=0$).

### Calculations
*   **Source/Emitter [Resistor](../02_components/01_Resistors.md) ($R_S$ or $R_E$):** Used to set the bias point.
    *   $R_S = \frac{U_{GS}}{I_D}$ (Note: $U_{GS}$ is the required bias voltage).
*   **Bypass [Capacitor](../02_components/05_Capacitors.md):**
    *   A capacitor parallel to $R_S$ or $R_E$ increases AC gain by bypassing the resistor for signals (AC Load Line is steeper than DC Load Line).
    *   Without bypass: Gain $\approx R_L / R_E$.
    *   With bypass: Gain is much higher (limited by internal resistance).

## Dissipation
*   **Formula:** $P_{diss} = U_{DS} \times I_D$ (or $U_{CE} \times I_C$).
*   **Hyperbola:** The limit of safe operation plotted on the graph ($P_{max} = constant$). The Load Line must lie below this curve to prevent overheating.

---
[< Back to Section Index](README.md)