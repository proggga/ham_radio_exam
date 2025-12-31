# Transmission Line Types

Transmission lines carry RF energy from the transmitter to the antenna.

## Coaxial Cable (Asymmetric)
*   **Structure**: Central conductor, surrounded by a dielectric insulator, a conductive shield (braid/foil), and an outer jacket.
*   **[Impedance](../01_electricity/21_Impedance_Impedantie.md) ($Z_0$)**:
    *   **50 $\Omega$**: Standard for amateur radio (e.g., RG-58, RG-213, H-155).
    *   **75 $\Omega$**: Standard for TV/Satellite (low loss, but requires matching to 50 $\Omega$ systems).
*   **[Shielding](../01_electricity/20_Shielding_Afscherming.md)**: Keeps the RF field contained inside. Can be run near metal objects or buried.

## Open Wire / Twin Lead (Symmetric)
*   **Structure**: Two parallel wires separated by insulating spacers.
    *   *Examples*: "Ladder line", "Kippenladder", 300 $\Omega$ TV ribbon.
*   **Impedance ($Z_0$)**: Typically **300 $\Omega$, 450 $\Omega$, or 600 $\Omega$**.
*   **Characteristics**: Extremely low loss, even at high [SWR](16_Standing_Wave_Ratio_SWR.md). ideal for multiband doublets.
*   **Installation**: Must be kept away from metal and ground (affects impedance).

---
[< Back to Section Index](README.md)