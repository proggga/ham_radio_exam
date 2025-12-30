---
id: 202512292034
title: Digital Logic Gates
tags: ["ham-radio", "digital", "logic"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Digital Logic Gates

Digital circuits process binary data (0s and 1s).
*   **Logic High (1)**: Near supply voltage (e.g., 5V, 3.3V).
*   **Logic Low (0)**: Near ground (0V).

## Standard Gates

| Gate | Symbol (IEC) | Function | Output = 1 when... | Formula |
| :--- | :--- | :--- | :--- | :--- |
| **NOT** | `1` | Inverter | Input is 0 | $Q = \bar{A}$ |
| **BUFFER** | `1` | Driver | Input is 1 | $Q = A$ |
| **AND** | `&` | Series | All inputs are 1 | $Q = A \cdot B$ |
| **OR** | `>=1` | Parallel | At least one input is 1 | $Q = A + B$ |
| **NAND** | `&` + `o` | Not AND | Not all inputs are 1 | $Q = \overline{A \cdot B}$ |
| **NOR** | `>=1` + `o`| Not OR | No inputs are 1 | $Q = \overline{A + B}$ |
| **XOR** | `=1` | Exclusive OR | Inputs are different | $Q = A \oplus B$ |
| **XNOR** | `=1` + `o` | Equivalence | Inputs are the same | $Q = \overline{A \oplus B}$ |

## Related
*   [[Boolean Algebra]]
*   [[Number Systems]]
