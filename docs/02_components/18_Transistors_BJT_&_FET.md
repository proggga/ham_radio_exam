# Transistors

Active components used for amplification and switching.

## Bipolar Junction Transistor (BJT)
*   **Type:** Current-controlled current source.
*   **Structure:** NPN (current flows Collector $\to$ Emitter) or PNP (Emitter $\to$ Collector).
*   **Terminals:** Base (B), Collector (C), Emitter (E).
*   **Principle:** A small Base current ($I_b$) controls a large Collector current ($I_c$).
*   **Current Gain ($\beta$ or $h_{FE}$):**
    *   Formula: $\beta = \frac{I_c}{I_b}$
    *   Typical value: 20 - 500 (often $\approx 100$).
    *   $I_e \approx I_c$ (precisely $I_e = I_c + I_b$).

### Biasing (Instellen)
To function as an amplifier, the transistor must be "biased" (DC operating point set) so it stays in the active region (between cutoff and saturation).
*   **Base-Emitter Voltage ($U_{be}$):** Must be $\approx 0.6V$ (Si) or $0.2V$ (Ge) for conduction.
*   **Voltage Divider Method (Stable):**
    1.  Voltage divider ($R_1, R_2$) sets Base Voltage ($U_b$).
    2.  Emitter Voltage ($U_e$) follows Base: $U_e = U_b - 0.6V$.
    3.  Emitter Current ($I_e$) set by Emitter [Resistor](01_Resistors.md) ($R_e$): $I_e = \frac{U_e}{R_e}$.
    4.  Collector Current $I_c \approx I_e$.
    5.  Collector Voltage ($U_c$) set by Collector Resistor ($R_c$) and supply ($U_{supply}$): $U_c = U_{supply} - I_c \cdot R_c$.
*   **Gain Formula (Approx):**
    *   Voltage Gain ($A_u$) $\approx \frac{R_c}{R_e}$ (if $R_e$ is present and unbypassed).
    *   *Note:* If $R_e$ is bypassed with a capacitor, gain is much higher, limited by internal $r_e$.

### Configurations
1.  **Common Emitter (GES):** High Gain (Current & Voltage). Phase reversal ($180^\circ$).
2.  **Common Base (GBS):** Low Input Z, High Output Z. Current gain $\approx 1$. **Good for [HF](../07_propagation/01_Propagation_Basics.md)/[VHF](../07_propagation/07_VHFUHF_Bands_6m,_2m,_70cm.md)** amplification (low feedback capacitance).
    *   *Mnemonic:* "Basic Income" (Basisinkomen) = Low Income (Low Input Z), High Expenses (High Output Z).
3.  **Common Collector (GCS / Emitter Follower):** High Input Z ($\approx \beta \times R_E$), Low Output Z. Voltage gain $\approx 1$. Used as **Buffer**.

## Field Effect Transistor (FET)
*   **Type:** Voltage-controlled current source.
*   **Terminals:** Gate (G), Drain (D), Source (S).
*   **Input [Impedance](../01_electricity/21_Impedance_Impedantie.md):** Extremely high (Gate draws almost 0 current).
*   **J-FET (Junction FET):**
    *   **N-Channel:** Normal operation when Gate is **negative** relative to Source.
    *   **P-Channel:** Normal operation when Gate is **positive** relative to Source.
    *   **Depletion Zone:** Voltage on Gate expands depletion zone, narrowing the channel and reducing current ($I_D$).
*   **Transconductance (Steilheid, $S$):**
    *   Measure of how much $I_D$ changes for a change in $U_{GS}$.
    *   Formula: $S = \frac{\Delta I_D}{\Delta U_{GS}}$ (Unit: mA/V or mS).
    *   Relationship to Resistance: $S \approx \frac{1}{R_{internal}}$.
*   **MOSFET (Metal-Oxide-[Semiconductor](15_Semiconductors.md) FET):**
    *   Gate insulated by oxide layer (very high $R_{in}$).
    *   **Modes of Operation**:
        *   **Depletion Mode**: Normally ON. Conducting channel exists with $U_{GS} = 0$. Apply voltage to close (deplete) it. Similar to JFET.
        *   **Enhancement Mode**: Normally OFF. No channel at $U_{GS} = 0$. Apply voltage to create (enhance) a channel. Used in logic gates and power switching.
    *   **Dual-Gate MOSFET:** Two gates. Gate 2 often used for Gain Control ([AGC](../04_receivers/03_Automatic_Gain_Control_AGC.md)) or isolating input from output (reduced Miller effect).
    *   **Handling (ESD Safety)**: The thin oxide layer is easily punctured by Static Electricity (ESD). Always handle with grounded tools/wrist straps and keep leads shorted until soldering.

### FET Amplification
*   **Voltage Gain ($A_u$):**
    *   With Source Resistor ($R_S$) unbypassed: $A_u \approx \frac{R_D}{R_S}$.
    *   Without $R_S$ (or bypassed): $A_u = S \cdot R_D$.

## Frequency Characteristics
*   **Gain-[Bandwidth](../03_circuits/07_Bandwidth.md) Product ($f_T$):** The frequency where current gain ($\beta$) drops to 1.
*   **Effect:** Current gain decreases as frequency increases.

## Comparison Table

| Feature | BJT | FET |
| :--- | :--- | :--- |
| **Control** | Current ($I_b$) | Voltage ($U_{GS}$) |
| **Input Impedance** | Low/Medium | Very High |
| **Charge Carriers** | Electrons & Holes (Bipolar) | Electrons (N) or Holes (P) (Unipolar) |
| **[Noise](../01_electricity/26_AC_Signals_&_Noise.md)** | Higher | Lower (generally) |
| **Sensitivity** | Robust | Sensitive to static (MOSFET) |

---
[< Back to Section Index](README.md)