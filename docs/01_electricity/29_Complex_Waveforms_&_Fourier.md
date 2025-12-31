# Complex Waveforms & Fourier

**Fourier Analysis** states that any complex periodic wave can be constructed from a sum of sine waves (Fundamental + Harmonics).

## Wave Types

### Square Wave (Blokgolf)
*   **Composition**: Fundamental + **Odd** harmonics ($3f, 5f, 7f...$).
    *   *Exam Tip:* If asked which harmonics a 1kHz symmetric square wave contains: 3kHz, 5kHz, 7kHz... (Even multiples like 2kHz, 4kHz are **absent**).
    *   *Visual Identification:* A wave with a strong 3rd harmonic often shows a characteristic "dip" or "dent" in the positive and negative peaks.
*   **Amplitude**: Harmonic $n$ drops as $1/n$.
*   **Sound**: Harsh, hollow.

### Triangle Wave (Driehoeksgolf)
*   **Composition**: Fundamental + **Odd** harmonics.
*   **Amplitude**: Harmonic $n$ drops as $1/n^2$ (faster decay than square).
*   **Sound**: Flute-like but buzzy.

### Sawtooth (Zaagtand)
*   **Composition**: Fundamental + **Even AND Odd** harmonics.
*   **Sound**: Very bright, buzzy (like a bowed string).

## Mixed Signals (AC + DC)
An AC signal can be superimposed on a DC voltage offset.
*   A **[Capacitor](../02_components/05_Capacitors.md)** blocks the DC component, passing only the AC.

---
[< Back to Section Index](README.md)