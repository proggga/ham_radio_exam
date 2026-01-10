# Link Budget

A **Link Budget** is a calculation of all power gains and losses in a communication system to ensure the received signal is strong enough to be decoded.

## The Equation
$$P_{RX} = P_{TX} + G_{TX} - L_{Path} + G_{RX} - L_{Misc}$$

*   $P_{RX}$: Received Power (dBm).
*   $P_{TX}$: Transmitter Output Power (dBm).
*   $G_{TX}$: Transmitter [Antenna Gain](../06_antennas/13_Antenna_Characteristics.md) (dBi).
*   $L_{Path}$: Path Loss (Free Space Path Loss) (dB).
*   $G_{RX}$: Receiver [Antenna Gain](../06_antennas/13_Antenna_Characteristics.md) (dBi).
*   $L_{Misc}$: Cable losses, connector losses, polarization mismatch (dB).

## Key Parameters
*   **[Sensitivity](../04_receivers/03_Receiver_Performance.md)**: The minimum signal level required for the receiver to work (e.g., -120 dBm).
*   **Fade Margin**: An extra "cushion" (e.g., 10-20 dB) added to the budget to account for [Fading](18_Fading_QSB.md) (QSB) or atmospheric changes.
*   **Free Space Path Loss (FSPL)**:
    *   Depends on **Frequency** and **Distance**.
    *   Doubling the distance = 6 dB loss.
    *   Doubling the frequency = 6 dB loss.

## Application
1.  Calculate total Gain ($TX Power + Antennas$).
2.  Calculate total Loss ($Path + Cables$).
3.  Resulting Signal > Receiver Sensitivity + Fade Margin?
    *   **Yes**: Link is feasible.
    *   **No**: Need more power, better antennas, or lower frequency.

---
[< Back to Section Index](README.md)