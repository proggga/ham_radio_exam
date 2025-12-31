# Digital Logic Gates

Digital circuits process binary data (0s and 1s).
*   **Logic High (1)**: Near supply voltage.
*   **Logic Low (0)**: Near ground (0V, typically < 0.8V).

## Standard Gates (IEC Symbols)
The exam uses IEC symbols (rectangular boxes).

| Gate | IEC Symbol | Function | Output | Formula |
| :--- | :--- | :--- | :--- | :--- |
| **NOT** | `1` with output `o` | Inverter | 1 if Input is 0 | $Q = \bar{A}$ |
| **BUFFER** | `1` | Driver | 1 if Input is 1 | $Q = A$ |
| **AND** | `&` | Series Logic | 1 only if **ALL** inputs are 1 | $Q = A \cdot B$ |
| **OR** | `≥1` | Parallel Logic | 1 if **ANY** input is 1 | $Q = A + B$ |
| **NAND** | `&` with output `o` | Not AND | 0 only if **ALL** inputs are 1 | $Q = \overline{A \cdot B}$ |
| **NOR** | `≥1` with output `o` | Not OR | 1 only if **ALL** inputs are 0 | $Q = \overline{A + B}$ |
| **XOR** | `=1` | Exclusive OR | 1 if inputs are **different** | $Q = A \oplus B$ |
| **XNOR** | `=1` with output `o` | Equivalence | 1 if inputs are **same** | $Q = \overline{A \oplus B}$ |

*   *Note:* The small circle (`o`) or triangle at an output (or input) indicates **Inversion** (NOT).

## Internal Structure (Exam Insight)
*   **NOT Gate**: Can be built with a single transistor in Common Emitter configuration (no emitter resistor).
    *   Input High $\to$ [Transistor](18_Transistors_BJT_&_FET.md) Saturates (Conducts) $\to$ Output Low (connected to ground via transistor).
    *   Input Low $\to$ [Transistor](18_Transistors_BJT_&_FET.md) Cutoff $\to$ Output High (pulled up to Vcc).

---
[< Back to Section Index](README.md)