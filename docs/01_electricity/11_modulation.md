# Modulation and Digital Signals

## 1. Analogue Modulation
Modifying a [Carrier wave](10_ac_signals.md) to convey information.

### CW (Continuous Wave)
*   On/Off keying of the carrier (Morse Code). See [Procedures](../11_procedures.md).
*   Narrowest bandwidth (~50-150 Hz).

### AM (Amplitude Modulation)
*   Varying carrier amplitude with audio.
*   **Modulation Depth ($m$):** $m = U_{audio} / U_{carrier}$. Max 100%.
*   **Sidebands:** Sum ($f_c + f_a$) and Difference ($f_c - f_a$) frequencies.
*   **Bandwidth:** $2 \times f_{max\_audio}$.
*   **Power:** Carrier power + Sideband power. At 100% mod, sidebands are 1/3 of total power.

### SSB (Single Sideband / EZB)
*   AM with Carrier and one Sideband suppressed.
*   **Efficiency:** All power is useful information.
*   **Bandwidth:** ~2.4 - 2.7 kHz (for voice).
*   **USB/LSB:** Upper or Lower Sideband.

### FM (Frequency Modulation)
*   Varying carrier frequency with audio.
*   **Deviation ($\Delta f$):** Max frequency shift from center. See [Bandwidth](10_ac_signals.md).
*   **Modulation Index:** $m = \Delta f / f_{mod}$.
*   **Bandwidth (Carson's Rule):** $B \approx 2(\Delta f + f_{max\_audio})$.
*   **Capture Effect:** Receiver locks onto the strongest signal, suppressing weaker ones. Good noise immunity.

## 2. Digital Signals

### Transmission
*   **Baud Rate (Bd):** Symbol rate (changes per second).
*   **Bit Rate (bps):** Information rate. $\text{Bit Rate} = \text{Baud} \times \text{Bits per Symbol}$.

### Modulation Types
*   **ASK:** Amplitude Shift Keying.
*   **FSK:** Frequency Shift Keying (Used in RTTY).
*   **PSK:** Phase Shift Keying (BPSK, QPSK).
*   **QAM:** Quadrature Amplitude Modulation (Amplitude + Phase).
See [Digital Components](../02_components/07_digital_components.md) for binary basics.

### Coding
*   **Baudot (CCITT-1):** 5-bit code (32 chars). No error correction.
*   **ASCII (CCITT-5):** 7 or 8-bit code.
*   **Parity:** Simple error check bit.

---
[Back to Index](../INDEX.md) | [Back to Dashboard](../../README.md)
