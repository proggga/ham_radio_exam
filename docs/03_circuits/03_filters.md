# Filters and Resonance

## 1. Filter Types
Filters allow specific frequencies to pass while rejecting others.
*   **Low Pass (LPF):** Passes low frequencies (e.g., Audio, Harmonics suppression).
    *   *Cut-off frequency ($f_k$):* Where $R = X$.
    *   $f_k = \frac{1}{2\pi RC}$ or $f_k = \frac{R}{2\pi L}$.
*   **High Pass (HPF):** Passes high frequencies.
*   **Band Pass (BPF):** Passes a range of frequencies (Resonant circuit).
*   **Band Stop (Notch):** Blocks a specific frequency.

## 2. Resonance (Resonantie)
Occurs in an LC circuit when Inductive Reactance equals Capacitive Reactance ($X_L = X_C$).

### Resonant Frequency ($f_{res}$)
Calculated using the **Thomson Formula**:
$$f_{res} = \frac{1}{2\pi \sqrt{L \cdot C}}$$

### Series Resonance
*   **Impedance:** Minimal ($Z = R_{loss} \approx 0$).
*   **Behavior:** Acts as a short circuit at resonance.
*   **Application:** Suction circuit (Zuigkring) to remove interference.

### Parallel Resonance
*   **Impedance:** Maximal ($Z$ is very high).
*   **Behavior:** Acts as an open circuit at resonance.
*   **Application:** Tuning circuit, Trap (Sperkring).

## 3. Quality Factor (Q)
$Q$ is a measure of the "quality" or efficiency of a resonant circuit (Ratio of stored energy to energy lost per cycle).
*   **High Q:** Sharp resonance peak, narrow bandwidth.
*   **Low Q:** Broad resonance peak, wide bandwidth.

### Formulas for Q
*   **Series Circuit:** $Q = \frac{X_L}{R_s} = \frac{1}{\omega C R_s}$
    *   $R_s$ is the series loss resistance. Lower $R$ = Higher $Q$.
*   **Parallel Circuit:** $Q = \frac{R_p}{X_L} = \omega C R_p$
    *   $R_p$ is the parallel loss resistance. Higher $R$ = Higher $Q$.

## 4. Bandwidth (Bandbreedte)
The width of the frequency range where the power is at least half the maximum ($-3dB$ points).
$$B = \frac{f_{res}}{Q}$$
*   **-3dB Point:** Voltage is $\approx 0.707 \times Max$. Power is $0.5 \times Max$.
*   **Shape Factor:** Ratio of bandwidth at -60dB to -6dB. Ideal is 1 (rectangular filter).

## 5. High-Performance Filters
Used in the Intermediate Frequency (IF) stages of receivers for selectivity.
*   **Crystal Filter:** Very high $Q$, sharp edges.
*   **Mechanical Filter:** Resonates mechanically. High $Q$, flat top.
*   **Ceramic Filter:** Cheap, medium performance.
