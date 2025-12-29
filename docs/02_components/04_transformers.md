# Transformers (Transformatoren)

## 1. Function
A transformer transfers electrical energy between two or more circuits through electromagnetic induction. It is used to transform Voltage, Current, and Impedance.
*   **Ideal Transformer:** $P_{in} = P_{out}$ (No losses).
*   **Operating Principle:** A changing current in the primary winding creates a changing magnetic field, which induces a voltage in the secondary winding.
    *   *Note:* Transformers do **not** work with DC (Direct Current). A steady DC current creates a static magnetic field, which induces no voltage.

## 2. Construction
*   **Primary Coil (Winding):** Connected to the source.
*   **Secondary Coil (Winding):** Connected to the load.
*   **Core:** Directs the magnetic flux to ensure tight coupling between coils.
    *   **Laminated Iron (Weekijzer):** For Mains/Audio (Low freq). Laminations (lamellen) reduce Eddy Currents.
    *   **Ferrite / Powdered Iron:** For RF (High freq). These materials are magnetic but have high electrical resistance to prevent eddy currents.
    *   **Toroid (Ringkern):** Ring-shaped core. Highly efficient because the magnetic field is contained within the ring (self-shielding), resulting in low flux leakage.

## 3. Formulas
The transformation depends on the **Turns Ratio** ($\frac{N_{prim}}{N_{sec}}$).

### Voltage & Current
$$ \frac{U_{sec}}{U_{prim}} = \frac{N_{sec}}{N_{prim}} $$
$$ \frac{I_{sec}}{I_{prim}} = \frac{N_{prim}}{N_{sec}} $$

*   **Step-up:** More turns on secondary -> Higher Voltage, Lower Current.
*   **Step-down:** Fewer turns on secondary -> Lower Voltage, Higher Current.
*   **Ampere-Turns (Aw):** The magnetizing force is proportional to Current $\times$ Turns. In an ideal transformer, $I_p \cdot N_p = I_s \cdot N_s$.

### Impedance Transformation
Transformers can match impedances (e.g., matching a high-impedance tube amplifier to a low-impedance speaker).
$$ Z_{prim} = Z_{sec} \times (\frac{N_{prim}}{N_{sec}})^2 $$
*   The impedance ratio is the **square** of the turns ratio.
*   *Example:* To match $4 \Omega$ to $400 \Omega$ (ratio 1:100), you need a turns ratio of $\sqrt{100} = 10:1$.

## 4. Special Types
*   **Autotransformer:** Uses a single tapped winding. The secondary is part of the primary (or vice versa).
    *   *Pros:* Smaller, lighter, cheaper.
    *   *Cons:* **NO** galvanic isolation (Direct connection to mains). Dangerous for safety.
    *   *Variac:* An adjustable autotransformer.
*   **Balun (Balanced-Unbalanced):** Connects balanced lines (e.g., dipole antenna) to unbalanced lines (e.g., coax).
    *   *1:1 Balun:* Current balun (choke) to stop common-mode current.
    *   *4:1 Balun:* Impedance transformer (e.g., $200 \Omega$ antenna to $50 \Omega$ coax).

## 5. Losses
Real transformers are not 100% efficient.
1.  **Copper Loss ($I^2R$):** Heating in the wire windings due to resistance.
2.  **Iron Loss (Core Loss):**
    *   *Eddy Currents (Wervelstromen):* Circulating currents induced in the conductive core material. Reduced by using laminations or ferrite.
    *   *Hysteresis:* Energy lost flipping the magnetic domains in the core material 50 times (or more) per second. Reduced by using soft iron or ferrite.
3.  **Flux Leakage:** Magnetic field lines that escape the core and do not link the primary to the secondary.
4.  **No-load Current (Nullaststroom):** Current that flows in the primary even with no load, due to the finite inductance of the primary coil (it acts as a choke).
