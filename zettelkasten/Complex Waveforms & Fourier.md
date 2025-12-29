---
id: 202512292031
title: Complex Waveforms & Fourier
tags: ["ham-radio", "theory", "ac-signals"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Complex Waveforms & Fourier

**Fourier Analysis** states that any complex periodic wave can be constructed from a sum of sine waves (Fundamental + Harmonics).

## Wave Types

### Square Wave (Blokgolf)
*   **Composition**: Fundamental + **Odd** harmonics ($3f, 5f, 7f...$).
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
*   A **Capacitor** blocks the DC component, passing only the AC.

## Related
*   [[AC Signal Parameters]]
*   [[Distortion and Dissipation]] (Harmonics)
