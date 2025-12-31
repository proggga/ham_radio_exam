# Sequential Logic

In sequential logic, the output depends on the inputs **and** the previous state (Memory).

## Flip-Flops
The basic memory element storing 1 bit.

### RS Flip-Flop (Set-Reset)
*   **Inputs**: Set (S), Reset (R).
*   **Outputs**: $Q$, $\bar{Q}$.
*   **Behavior**:
    *   $S=1, R=0 \rightarrow Q=1$ (Set)
    *   $S=0, R=1 \rightarrow Q=0$ (Reset)
    *   $S=0, R=0 \rightarrow$ No Change (Memory)
    *   $S=1, R=1 \rightarrow$ **Forbidden** (Undefined state).
*   **Construction**: Two cross-coupled NAND or NOR gates.

### D Flip-Flop (Data / Delay)
*   **Inputs**: Data (D), Clock (CLK).
*   **Behavior**: Copies input D to output Q on the clock edge (e.g., rising edge).
*   **Use**: Shift Registers, Memory.

### JK Flip-Flop
*   **Inputs**: J, K, Clock.
*   **Behavior**: Like RS, but handles the "11" state.
    *   $J=1, K=0 \rightarrow$ Set
    *   $J=0, K=1 \rightarrow$ Reset
    *   $J=1, K=1 \rightarrow$ **Toggle** (Q flips).
*   **Master-Slave**: A configuration used to prevent race conditions (instability) during the clock pulse. Input is read on one edge, output changes on the other.

## Applications

### Registers
*   **Storage**: A group of flip-flops (e.g., 8 D-types) storing a binary word (Byte).
*   **Shift Register**: Bits are passed from one flip-flop to the next on each clock pulse. Used for Serial $\leftrightarrow$ Parallel conversion.

### Counters / Frequency Dividers
*   **Ripple Counter**: Chain of Flip-Flops where the output of one clocks the next.
*   **Frequency Division**: Each flip-flop divides the frequency by 2.
    *   $f_{out} = \frac{f_{in}}{2^n}$ where $n$ is the number of flip-flops.
    *   *Example:* 3 flip-flops divide by $2^3 = 8$.

---
[< Back to Section Index](README.md)