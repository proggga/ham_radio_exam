# Semiconductors: Diodes and Transistors

## 1. Semiconductor Theory
*   **Material:**
    *   **Silicon (Si):** Most common. Isolator in pure form. Crystalline structure (tetrahedral).
    *   **Germanium (Ge):** Older material. Higher leakage current, lower melting point.
*   **Atomic Structure:** Semiconductor atoms have **4** valence electrons. They share electrons with neighbors to form a stable crystal lattice (8 shared electrons).
*   **Doping (Dotering):** Adding impurities to modify conductivity (~1 atom per 100 million).
    *   **N-type:** Doped with an element having **5** valence electrons (e.g., Phosphorus/Fosfor, Arsenic). Creates free **Electrons**.
    *   **P-type:** Doped with an element having **3** valence electrons (e.g., Boron/Borium, Indium). Creates **Holes** (Gaten) - vacancies where an electron is missing.

### The PN Junction (PN-Overgang)
When P-type and N-type materials are joined:
1.  Electrons from N diffuse into P; Holes from P diffuse into N.
2.  They recombine near the junction.
3.  This creates a **Depletion Zone** (Uitputtingszone) devoid of free charge carriers.
4.  The N-side becomes slightly positive, the P-side slightly negative, creating a "barrier potential" that stops further diffusion.

## 2. Diodes
A two-terminal device containing one PN junction.
*   **Anode:** P-type region.
*   **Cathode:** N-type region.

### Operation
*   **Forward Bias (Doorlaat):** Anode (+), Cathode (-).
    *   The external field pushes carriers *towards* the junction, overcoming the depletion zone.
    *   **Threshold Voltage (Drempelspanning):** ~0.6V - 0.7V for Silicon, ~0.2V for Germanium. Current flows freely once exceeded.
*   **Reverse Bias (Sper):** Anode (-), Cathode (+).
    *   The external field pulls carriers *away* from the junction, widening the depletion zone.
    *   Current is blocked (except for a tiny, temperature-dependent leakage current).

### Types & Characteristics
*   **Rectifier Diode:** Converts AC to DC.
*   **Zener Diode:**
    *   Designed to conduct in reverse breakdown (Avalanche/Zener effect) without damage.
    *   Used for voltage stabilization (acts as a constant voltage source).
*   **Varicap (Capaciteitsdiode):**
    *   Operates in **Reverse Bias**.
    *   The depletion zone acts as the dielectric of a capacitor.
    *   Higher Reverse Voltage -> Wider Depletion Zone -> **Lower Capacitance**.
    *   Used for electronic tuning (VCOs).
*   **LED (Light Emitting Diode):**
    *   Recombination of electrons and holes releases energy as photons.
    *   Material: Gallium-Arsenide (GaAs) etc.
    *   Forward Voltage: ~1.7V (Red) to ~4.6V (Blue/UV).
*   **Schottky:** Metal-semiconductor junction. Low forward drop (~0.2V), fast switching.
*   **PIN Diode:** P-Intrinsic-N layers. Used as RF switch or variable resistor.

### Dissipation
Power dissipated as heat: $P = I_{forward} \times U_{diode}$.

## 3. Transistors
Active devices used for amplification or switching.

### Bipolar Junction Transistor (BJT)
Current-controlled device. Two PN junctions (NPN or PNP).
*   **Terminals:** Base (B), Collector (C), Emitter (E).
*   **Operation:** A small Base current ($I_b$) allows a large Collector current ($I_c$) to flow.
*   **Gain ($\beta$ or $h_{FE}$):** $I_c = \beta \times I_b$.

### Field Effect Transistor (FET)
Voltage-controlled device.
*   **Terminals:** Gate (G), Drain (D), Source (S).
*   **Operation:** Voltage on the Gate creates an electric field that controls the width of the conducting channel (and thus the current) between Source and Drain.
*   **Transconductance (Steilheid, S):** Change in $I_d$ per Volt change in $U_{gs}$. Unit: mA/V (or Siemens). $S = 1/R$.
*   **JFET:** Junction FET. Gate is a reverse-biased PN junction (High Input Z).
*   **MOSFET:** Metal-Oxide-Semiconductor. Gate is insulated by oxide (Infinite Input Z).

## 4. Transistor Configurations
| Config | Input | Output | Characteristics |
| :--- | :--- | :--- | :--- |
| **Common Emitter/Source** | Base/Gate | Collector/Drain | Voltage & Current Gain. Phase Inverted ($180^\circ$). Most common. |
| **Common Collector/Drain** (Follower) | Base/Gate | Emitter/Source | Voltage Gain $\approx 1$, High $Z_{in}$, Low $Z_{out}$. Buffer. |
| **Common Base/Gate** | Emitter/Source | Collector/Drain | Voltage Gain, No Current Gain. Low $Z_{in}$. HF Amplifiers. |
