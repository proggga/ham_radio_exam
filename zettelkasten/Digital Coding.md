---
id: 202512292109
title: Digital Coding
tags: ["ham-radio", "digital", "theory"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Digital Coding

Coding defines how characters are mapped to binary bits.

## Character Sets
*   **Baudot (CCITT-1)**:
    *   5-bit code ($2^5 = 32$ combinations).
    *   Uses "Letters Shift" and "Figures Shift" to support numbers/punctuation.
    *   Used in RTTY. No error correction.
*   **ASCII (CCITT-5)**:
    *   7-bit (128 chars) or 8-bit (256 chars) code.
    *   Standard for computers.

## Error Checking
*   **Parity**: Adding an extra bit to ensure the total number of 1s is Even (or Odd).
    *   Can detect single-bit errors but cannot correct them.
*   **FEC (Forward Error Correction)**: Advanced coding (like Convolutional or Reed-Solomon) that allows the receiver to repair errors without requesting retransmission.

## Related
*   [[Digital Transmission]]
