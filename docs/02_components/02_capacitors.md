# Capacitors (Condensatoren)

## 1. Structure and Function
A capacitor stores electrical energy in an **electric field** (See [Fields](../01_electricity/09_fields.md)).
*   **Construction:** Two conductive plates (electrodes) separated by an insulating material called the **dielectric** (diëlektricum).
*   **Symbol:** Two parallel lines. (Curved line for the negative plate in some electrolytic symbols).

## 2. Capacitance (Capaciteit)
The ability to store charge.
*   **Symbol:** $C$.
*   **Unit:** Farad ($F$).
    *   $1 \text{ F} = 1 \text{ Coulomb per Volt} (C/V)$.
    *   Practical units: $\mu F$ (micro), $nF$ (nano), $pF$ (pico).

### Formula
The capacitance depends on the geometry and material:
$$C \approx 0.0885 \cdot \varepsilon_r \cdot \frac{A}{d}$$
*(Note: In this specific exam formula format, C is in pF, A in $cm^2$, d in cm).*

Key factors:
1.  **Plate Area ($A$):** Larger area = Higher capacitance.
2.  **Distance ($d$):** Smaller distance = Higher capacitance.
3.  **Dielectric Constant ($\varepsilon_r$):** also called Permittivity.
    *   $\varepsilon_r$ indicates how much better the material insulates/stores field compared to vacuum.
    *   Vacuum/Air: $\varepsilon_r \approx 1$.
    *   Solid materials: $\varepsilon_r > 1$ (increases capacitance).

## 3. Relationships
*   **Charge:** $Q = I \times t$ (Current $\times$ Time).
*   **Charge on Capacitor:** $Q = C \times U$.
    *   $U$ is the voltage across the capacitor.
    *   See [Time Constants](../03_circuits/02_time_constants.md) for charging behavior.

## 4. Types
*   **Fixed Capacitors:** Ceramic, Plastic film, Mica.
*   **Electrolytic (Elco):** High capacitance, **Polarized** (+ and -). Must not be connected in reverse.
*   **Variable Capacitors:**
    *   **Air Variable:** Rotatable plates (used in tuning).
    *   **Trimmer:** Small adjustable capacitor for calibration.

## 5. Breakdown Voltage (Doorslagspanning)
The maximum voltage the dielectric can withstand before arcing occurs. Exceeding this destroys the component.

---
[Back to Index](../INDEX.md) | [Back to Dashboard](../../README.md)
