# Sampling Theory

Sampling is the process of taking snapshots of an analogue signal's voltage at regular intervals to create a digital representation.

## Nyquist-Shannon Theorem
To accurately reconstruct a continuous signal, the **Sample Rate ($f_s$)** must be at least **twice** the highest frequency component ($f_{max}$) of the signal.

*   **Formula**: $f_s > 2 \cdot f_{max}$
*   **Nyquist Frequency**: The highest frequency that can be sampled correctly ($f_s/2$).

## Aliasing
If the signal contains frequencies higher than the Nyquist limit ($> f_s/2$), these high frequencies are "folded back" and appear as false low frequencies (aliases).
*   **Analogy**: Wagon wheels appearing to spin backwards in movies.
*   **Solution**: An **Anti-Aliasing [Filter](../03_circuits/03_Filters_&_Resonance.md)** (Low Pass [Filter](../03_circuits/03_Filters_&_Resonance.md)) must be placed before the [ADC](39_Digital_Processing_Techniques.md) to remove frequencies above $f_s/2$.

---
[< Back to Section Index](README.md)