# Resistors: Types and Codes

## 1. Types of Resistors
*   **Fixed Resistors:** Value is constant.
    *   *Carbon Film:* Common, general purpose.
    *   *Metal Film:* Higher precision, lower noise.
    *   *Wirewound:* High power handling.
*   **Variable Resistors:** Value can be adjusted.
    *   *Potentiometer:* Three terminals (voltage divider). Used for volume control, etc.
    *   *Rheostat:* Two terminals (variable resistance). Limits current.
*   **Thermistors:** Temperature-dependent resistors.
    *   **NTC (Negative Temperature Coefficient):** Resistance **decreases** as temperature rises. (Used in sensing, inrush limiting).
    *   **PTC (Positive Temperature Coefficient):** Resistance **increases** as temperature rises. (Used in protection/fuses).

## 2. Color Code (Kleurcode)
Most axial resistors use a system of colored bands to indicate their resistance value and tolerance.

| Color | Digit (Ring 1 & 2) | Multiplier (Ring 3) | Tolerance (Ring 4) |
| :--- | :---: | :--- | :--- |
| **Black (Zwart)** | 0 | $1$ | |
| **Brown (Bruin)** | 1 | $10$ | 1% |
| **Red (Rood)** | 2 | $100$ | 2% |
| **Orange (Oranje)** | 3 | $1k$ | |
| **Yellow (Geel)** | 4 | $10k$ | |
| **Green (Groen)** | 5 | $100k$ | 0.5% |
| **Blue (Blauw)** | 6 | $1M$ | |
| **Violet** | 7 | $10M$ | |
| **Grey (Grijs)** | 8 | | |
| **White (Wit)** | 9 | | |
| **Gold (Goud)** | | $0.1$ | 5% |
| **Silver (Zilver)** | | $0.01$ | 10% |

### Reading the Code
1.  **Ring 1:** First digit.
2.  **Ring 2:** Second digit.
3.  **Ring 3:** Multiplier (Number of Zeros).
4.  **Ring 4:** Tolerance (Accuracy).

*Example:* Yellow, Violet, Orange, Gold.
*   Yellow = 4
*   Violet = 7
*   Orange = 3 (zeros) -> 000
*   Result: $47,000 \Omega = 47 k\Omega$.
*   Gold = $\pm 5\%$.

### Mnemonic (Ezelsbruggetje)
**Z**ij **B**rengt **R**ozen **O**p **G**errits **G**raf **B**ij **V**ies **G**rijs **W**eer.
(Zwart, Bruin, Rood, Oranje, Geel, Groen, Blauw, Violet, Grijs, Wit).

## 3. E-Series (Standard Values)
Resistors are not made in every possible value. They follow logarithmic series (Renard series).
*   **E12 Series (10%):** 10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82.
*   **E24 Series (5%):** Higher resolution steps.
