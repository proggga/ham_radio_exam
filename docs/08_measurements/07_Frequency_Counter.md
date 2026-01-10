# Frequency Counter

A Frequency Counter measures the precise frequency of a periodic signal.

## Operation
*   **Method**: Counts the number of cycles (pulses) that occur within a precise time window (Gate Time).
*   **Formula**: $Frequency = \frac{Count}{Gate Time}$.

## Characteristics
*   **Accuracy**: Depends entirely on the stability of its internal reference oscillator (usually a Crystal, TCXO, or OCXO).
*   **[Sensitivity](../04_receivers/03_Receiver_Performance.md)**: The input signal must be strong enough to trigger the counting logic.
*   **Resolution**: Longer gate times provide higher resolution (more digits).

---
[< Back to Section Index](README.md)