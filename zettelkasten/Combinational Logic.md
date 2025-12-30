---
id: 202512292036
title: Combinational Logic
tags: ["ham-radio", "digital", "logic"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Combinational Logic

In combinational logic, the output depends **only** on the current state of the inputs (no memory).

## Adders
Circuits that perform binary addition.

### Half Adder
Adds 2 bits ($A, B$). Cannot handle a carry input.
*   **Outputs**: Sum ($S$), Carry ($C$).
*   **Logic**:
    *   $S = A \oplus B$ (XOR)
    *   $C = A \cdot B$ (AND)
*   **Truth Table**:
    *   0+0=0 (C=0)
    *   0+1=1 (C=0)
    *   1+0=1 (C=0)
    *   1+1=0 (C=1)

### Full Adder
Adds 3 bits ($A, B, C_{in}$).
*   **Inputs**: Bit A, Bit B, Carry In ($C_{in}$).
*   **Outputs**: Sum ($S$), Carry Out ($C_{out}$).
*   **Construction**: Can be built from two Half Adders and an OR gate.

## Related
*   [[Digital Logic Gates]]
*   [[Number Systems]]
