# Digital Transmission

## Speed Definitions
*   **Bit Rate (bps)**: The rate of information transfer (bits per second).
*   **Symbol Rate (Baud, Bd)**: The number of signal changes per second on the transmission line.
*   **Relationship**: $\text{Bit Rate} = \text{Baud Rate} \times \text{Bits per Symbol}$.
    *   *Binary (2 states):* 1 bit/symbol $\rightarrow$ bps = Baud.
    *   *4-Level (e.g. QPSK):* 2 bits/symbol $\rightarrow$ bps = 2 $\times$ Baud.
    *   *16-QAM:* 4 bits/symbol $\rightarrow$ bps = 4 $\times$ Baud.

## Codes (Exam Topic)
*   **Baudot (CCITT-1)**: 5-bit code. 32 combinations. Used in **RTTY**. No error correction.
*   **ASCII**: 7 or 8-bit code. Standard for computers.
*   **Parity**: Simple error detection (Even/Odd).

## Modulation Types

### FSK (Frequency Shift Keying)
*   Switching between two tones (Mark/Space). Used in **RTTY** (Shift usually 170 Hz).
*   **[Bandwidth](../03_circuits/07_Bandwidth.md) Formula**: $B \approx 2(1.6 \times f_{symbol} + \Delta f)$ or roughly **Shift + Baud rate** (plus some margin).
    *   *Exam Formula:* $B \approx 2(1.6 \cdot f_s + \Delta f)$ where $\Delta f$ is half the shift? No, typically $B \approx \text{Shift} + B_d$ is a good approximation, but rigorous formula is $B = 2(\Delta f + B_d)$. Note: $\Delta f$ is deviation (half the shift).
*   *Exam Tip:* FSK has constant amplitude (Class C amplifier allowed).

### PSK (Phase Shift Keying)
*   Changing the phase of the carrier.
*   **BPSK (2-PSK)**: 2 Phases ($0^\circ, 180^\circ$). 1 bit/symbol.
*   **QPSK (4-PSK)**: 4 Phases ($0^\circ, 90^\circ, 180^\circ, 270^\circ$). 2 bits/symbol.
*   **8-PSK**: 8 Phases. 3 bits/symbol.
*   **Efficiency**: Very spectrum efficient.

### QAM (Quadrature Amplitude Modulation)
*   Combines **Amplitude** and **Phase** modulation.
*   **Constellation Diagram**: Shows the possible states (dots) on an IQ plot.
*   **16-QAM**: 16 states $\rightarrow$ 4 bits per symbol.
*   Requires linear amplification (Class A/AB) due to amplitude component.

---
[< Back to Section Index](README.md)