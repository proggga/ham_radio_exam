---
id: 202301011241
title: "Signal Visualization"
tags: ["ham-radio", "measurements"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29

dutch_title: "Signaalweergave"
aliases: ["Signaalweergave"]
---

# Signal Visualization

## 1. Oscilloscope
Visualizes signals in the **Time Domain** (Voltage vs Time).
*   **Components (Analogue):** Cathode Ray Tube (CRT), Vertical/Horizontal [[Amplifiers]], Timebase.
*   **Operation:** Electron beam sweeps across the screen (X-axis = Time) while signal deflects it up/down (Y-axis = Voltage).
*   **[[Measurements]]:**
    *   **Amplitude:** Peak-to-Peak voltage ($U_{pp}$).
    *   **Period ($T$):** Time for one cycle.
    *   **Frequency:** Calculated as $f = 1/T$.
    *   **Waveform:** Sine, Square, Distortion, [[Modulation & Digital Signals|Modulation]] depth.
    *   **Envelope (Omhullende):** Visualizing the amplitude variation of an AM/SSB signal over time.
        *   Used to measure **[[Analogue Modulation & AM|Modulation Depth]]** (AM) or **[[Analogue Modulation & AM|PEP]]** (SSB).
        *   *Exam:* Identifying the shape of an AM signal (carrier + audio) vs. FM (constant amplitude).
    *   **Lissajous Figures:** XY-mode (Channel A = X, Channel B = Y).
        *   Used to compare **Frequency** and **Phase** of two signals.
        *   *Circle:* Same frequency, $90^\circ$ phase shift.
        *   *Diagonal Line:* Same frequency, $0^\circ$ or $180^\circ$ phase shift.
        *   *Loops:* Frequency ratio (e.g., 2:1 is a figure-8).
*   **Probes:** 1:1 or 10:1 (Attenuator). 10:1 reduces capacitive loading on the circuit.

## 2. Spectrum Analyzer
Visualizes signals in the **Frequency Domain** (Amplitude vs Frequency).
*   **Display:** X-axis = Frequency, Y-axis = Amplitude (dBm).
*   **[[Measurements]]:**
    *   **Harmonics:** Check for suppression of $2f, 3f$, etc.
    *   **Spurious Emissions:** Detect unwanted parasitic oscillations.
    *   **[[Bandwidth]]:** Measure occupied bandwidth of a modulated signal. See [[Modulation & Digital Signals|Modulation]].
    *   **Intermodulation:** Visualise IP3 products. See [[Types of Interference|Interference]].