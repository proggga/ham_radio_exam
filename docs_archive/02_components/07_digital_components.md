# Digital Components and Crystals

## 1. Crystals (Kristallen)
Components made of quartz that vibrate at a precise frequency (Piezoelectric effect).
*   **Function:** Frequency stability for oscillators and filters.
*   **Types:**
    *   **AT-cut:** Standard cut for temperature stability.
    *   **TCXO:** Temperature Compensated Crystal Oscillator.
    *   **OCXO:** Oven Controlled (Heated) Crystal Oscillator. Highest stability. See [Oscillators](../03_circuits/06_detectors_oscillators.md).

## 2. Digital Logic
Circuits that process binary data (0s and 1s).
*   **Logic Levels:**
    *   **1 (High):** Near supply voltage (e.g., 5V or 3.3V).
    *   **0 (Low):** Near ground (0V).

### Logic Gates (Poorten)
Fundamental building blocks of digital circuits.

| Gate | Symbol (IEC) | Function | Output = 1 when... | Formula |
| :--- | :--- | :--- | :--- | :--- |
| **NOT (NIET)** | `1` | Inverter | Input is 0 | $Q = \bar{A}$ |
| **AND (EN)** | `&` | Series | All inputs are 1 | $Q = A \cdot B$ |
| **OR (OF)** | `>=1` | Parallel | At least one input is 1 | $Q = A + B$ |
| **NAND** | `&` + `o` | Not AND | Not all inputs are 1 (0 only if all 1) | $Q = \overline{A \cdot B}$ |
| **NOR** | `>=1` + `o`| Not OR | No inputs are 1 (1 only if all 0) | $Q = \overline{A + B}$ |
| **XOR** | `=1` | Exclusive OR | Inputs are different | $Q = A \oplus B$ |
| **XNOR** | `=1` + `o` | Equivalence | Inputs are the same | $Q = \overline{A \oplus B}$ |

### Boolean Algebra (Schakelalgebra)
Rules for simplifying logic circuits.
*   **De Morgan's Laws:**
    1.  $\overline{A \cdot B} = \bar{A} + \bar{B}$ (NAND is equivalent to OR with inverted inputs).
    2.  $\overline{A + B} = \bar{A} \cdot \bar{B}$ (NOR is equivalent to AND with inverted inputs).

### Combinational Logic
Circuits where output depends only on current inputs.
*   **Adder:** Adds binary numbers.
    *   *Half Adder:* Adds 2 bits (Sum + Carry).
    *   *Full Adder:* Adds 3 bits (A + B + Carry_in).

### Sequential Logic
Circuits with memory (state); output depends on inputs and previous state.
*   **Flip-Flop:** Stores 1 bit.
    *   **RS Flip-Flop:** Set/Reset. Undefined state if both R=1 and S=1.
    *   **Clocked RS:** Inputs are only read when Clock signal is active.
    *   **D Flip-Flop (Data):** Captures the input (D) on the clock edge. Used for registers.
    *   **JK Flip-Flop:** Like RS, but J=1 K=1 toggles the output (divides frequency by 2).
*   **Register:** A group of flip-flops used to store multiple bits (e.g., a Byte).
    *   *Shift Register:* Bits move sideways on each clock pulse (Serial-to-Parallel conversion).
*   **Counter:** A chain of flip-flops that counts clock pulses.
    *   Used for frequency division ($f_{out} = f_{in} / 2^n$) and timers.
    *   Essential for [PLL](../03_circuits/06_detectors_oscillators.md#37-pll-phase-locked-loop) and [DSP](../01_electricity/12_dsp.md).

## 3. Number Systems
*   **Binary (Tweetallig):** Base 2. Digits 0, 1.
    *   $1011_2 = 1\times8 + 0\times4 + 1\times2 + 1\times1 = 11_{10}$.
*   **Hexadecimal (Zestientallig):** Base 16. Digits 0-9, A-F.
    *   Used to represent 4 bits (Nibble) per digit.
    *   $A = 10, F = 15$.
    *   $1F_{16} = 1\times16 + 15\times1 = 31_{10}$.


---
[Back to Index](../INDEX.md) | [Back to Dashboard](../../README.md)
