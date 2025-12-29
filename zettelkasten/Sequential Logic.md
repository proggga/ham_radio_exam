---
id: 202512292037
title: Sequential Logic
tags: ["ham-radio", "digital", "logic"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Sequential Logic

In sequential logic, the output depends on the inputs **and** the previous state (Memory).

## Flip-Flops
The basic memory element storing 1 bit.
*   **RS Flip-Flop**: Set/Reset. Undefined if both are 1.
*   **D Flip-Flop (Data)**: Captures input D on clock edge. Used for registers.
*   **JK Flip-Flop**: Toggles output if both J and K are 1.

## Complex Circuits
*   **Register**: A group of flip-flops storing multiple bits (e.g., a Byte).
    *   *Shift Register*: Moves bits sideways (Serial-to-Parallel).
*   **Counter**: Counts clock pulses.
    *   Used for **Frequency Division** ($f_{out} = f_{in} / 2^n$).
    *   Essential for PLLs and Timers.

## Related
*   [[Phase Locked Loop (PLL)]]
*   [[Digital Signal Processing (DSP)]]
