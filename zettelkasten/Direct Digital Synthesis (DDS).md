---
id: 202501111205
title: Direct Digital Synthesis (DDS)
tags: ["circuits", "dsp", "filters", "formulas", "math", "oscillators"]
created: 2025-01-11
type: permanent-note
modified: 2025-01-11
aliases: ["DDS", "Directe digitale frequentiesynthese"]
---

# Direct Digital Synthesis (DDS)

**Direct Digital Synthesis (DDS)** is a method of generating arbitrary periodic waveforms (like sine waves) from a single, fixed-frequency reference clock using digital techniques.

## Block Diagram Components
1.  **Reference Clock**: A stable crystal oscillator ($f_{clk}$).
2.  **Phase Accumulator**: A counter that increments by a specific value ("Tuning Word" or step size) on each clock cycle. The output represents the *phase* of the signal.
3.  **Lookup Table (Phase-to-Amplitude Converter)**: A ROM memory storing the values of a Sine wave. The Phase Accumulator output addresses this memory to retrieve the corresponding digital amplitude.
4.  **[[Digital Processing Techniques|DAC]] (Digital-to-Analog Converter)**: Converts the digital amplitude sequence into an analog voltage (stepped sine wave).
5.  **Reconstruction [[Filters & Resonance|Filter]] (Low Pass)**: Removes the clock frequency and aliasing artifacts (steps) to produce a smooth sine wave.

## Operation
*   **Frequency Control**: Changing the "Tuning Word" changes how fast the accumulator overflows (completes a cycle). Larger step size = Higher frequency.
*   **Formula**: $f_{out} = \frac{M \times f_{clk}}{2^n}$
    *   $M$: Tuning Word (Step size)
    *   $n$: Bit depth of the accumulator (e.g., 32 bits).

## Pros & Cons
*   **Pros**:
    *   Extremely fast frequency switching (microseconds).
    *   Very high frequency resolution (can tune in sub-Hz steps).
    *   Phase continuous switching.
*   **Cons**:
    *   **Spurious Emissions (Spurs)**: Quantization errors and DAC non-linearities create unwanted signals.
    *   Frequency limit: $f_{out}$ is limited by the Nyquist limit ($\approx 40\%$ of $f_{clk}$ in practice).

## Related
*   [[Digital Signal Processing (DSP)]]
*   [[Oscillators]]
*   [[Phase Locked Loop (PLL)]] (Alternative synthesis method)