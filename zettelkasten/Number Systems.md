---
id: 202512292011
title: Number Systems
tags: ["ham-radio", "basic-skills", "digital"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Number Systems

Computers and digital modes rely on non-decimal systems.

## Systems
1.  **Decimal (Base 10)**: Our daily system (digits 0-9).
2.  **Binary (Base 2)**: Uses only 0 and 1. Fundamental for digital logic and computing.
    *   **Bit**: Binary Digit (0 or 1).
    *   **Byte**: 8 bits ($2^8 = 256$ values).
    *   **MSB**: Most Significant Bit (leftmost).
    *   **LSB**: Least Significant Bit (rightmost).
3.  **Hexadecimal (Base 16)**: Uses 0-9 and A-F. Used to represent binary data compactly (one hex digit = 4 binary bits).
    *   A=10, B=11, C=12, D=13, E=14, F=15.

## Conversions (Exam Topic)

### Decimal to Binary
Method: Repeated division by 2.
1.  Is the number odd? If yes, LSB = 1. If no, LSB = 0.
2.  Subtract the bit value (0 or 1), divide by 2.
3.  Repeat for the result until 0 is reached.
*   *Example:* 5. Odd $\to$ 1. (5-1)/2 = 2. Even $\to$ 0. (2-0)/2 = 1. Odd $\to$ 1. (1-1)/2 = 0. Result: **101**.

### Binary to Decimal
Sum the weights of the positions where the bit is 1.
*   Positions: $... 2^3 (8) \mid 2^2 (4) \mid 2^1 (2) \mid 2^0 (1)$
*   *Example:* $101_2 = 1\times4 + 0\times2 + 1\times1 = 5_{10}$.

## Binary Arithmetic
*   **Addition**:
    *   $0+0=0$
    *   $0+1=1$
    *   $1+0=1$
    *   $1+1=10$ (0 carry 1)
*   **Subtraction**:
    *   $1-0=1$
    *   $1-1=0$
    *   $10-1=1$
*   **Multiplication**: Equivalent to left shift.
*   **Division**: Equivalent to right shift.

## Related
*   [[Modulation & Digital Signals]]
*   [[Digital Components & Crystals]]
