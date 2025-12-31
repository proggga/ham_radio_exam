# Shielding (Afscherming)

Shielding prevents the coupling of electric, magnetic, or electromagnetic fields between circuits.

## Types of Shielding

### 1. Electrostatic Shielding (Electric Fields)
*   **Material**: Highly conductive material (Copper, Aluminium).
*   **Mechanism**: Faraday Cage. Charges redistribute on the surface to cancel the field inside.
*   **Application**: Faraday shield between transformer windings to stop capacitive coupling.

### 2. Magnetic Shielding (Low Frequency)
*   **Frequency**: Audio / Mains (50/60 Hz).
*   **Material**: High permeability ferromagnetic material (Soft Iron, Mu-Metal).
*   **Mechanism**: The material provides a low-reluctance path for magnetic flux, diverting it around the protected region.
    *   *[Exam](../12_regulations/02_Licensing_in_the_Netherlands.md) Phrase*: "Geleider voor het magnetisch veld" (Conductor for the magnetic field).

### 3. RF Shielding (High Frequency)
*   **Frequency**: RF (> 100 kHz).
*   **Material**: Highly conductive material (Aluminium, Copper).
*   **Mechanism**: The changing magnetic field induces **Eddy Currents** in the shield. These currents generate an opposing magnetic field (Lenz's Law) that cancels the original field outside the shield.
*   **Effect on Coils**: Placing a conductive shield around a coil:
    *   **Decreases Inductance ($L$)**: The opposing field weakens the coil's field.
    *   **Decreases [Quality Factor](../03_circuits/06_Quality_Factor_Q.md) ($Q$)**: [Energy](08_Power_and_Energy.md) is lost as heat due to the resistance of the shield to eddy currents.

## Summary Table

| Frequency | Field Type | Shield Material | Mechanism |
| :--- | :--- | :--- | :--- |
| **LF (Audio)** | Magnetic | Soft Iron / Mu-Metal | Flux Diversion (Conduction) |
| **[HF](../07_propagation/01_Propagation_Basics.md) (RF)** | Electromagnetic | Aluminium / Copper | Eddy Current Cancellation |
| **Any** | Electric | Copper / Al Foil | Faraday Cage |

---
[< Back to Section Index](README.md)