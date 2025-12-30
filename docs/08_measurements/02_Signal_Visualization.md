# Signal Visualization

## 1. Oscilloscope
Visualizes signals in the **Time Domain** (Voltage vs Time).
*   **Components (Analogue):** Cathode Ray Tube (CRT), Vertical/Horizontal Amplifiers, Timebase.
*   **Operation:** Electron beam sweeps across the screen (X-axis = Time) while signal deflects it up/down (Y-axis = Voltage).
*   **Measurements:**
    *   **Amplitude:** Peak-to-Peak voltage ($U_{pp}$).
    *   **Period ($T$):** Time for one cycle.
    *   **Frequency:** Calculated as $f = 1/T$.
    *   **Waveform:** Sine, Square, Distortion, Modulation depth.
    *   **Lissajous Figures:** XY-mode (Channel A = X, Channel B = Y).
        *   Used to compare **Frequency** and **Phase** of two signals.
        *   *Circle:* Same frequency, $90^\circ$ phase shift.
        *   *Diagonal Line:* Same frequency, $0^\circ$ or $180^\circ$ phase shift.
        *   *Loops:* Frequency ratio (e.g., 2:1 is a figure-8).
*   **Probes:** 1:1 or 10:1 (Attenuator). 10:1 reduces capacitive loading on the circuit.

## 2. Spectrum Analyzer
Visualizes signals in the **Frequency Domain** (Amplitude vs Frequency).
*   **Display:** X-axis = Frequency, Y-axis = Amplitude (dBm).
*   **Measurements:**
    *   **Harmonics:** Check for suppression of $2f, 3f$, etc.
    *   **Spurious Emissions:** Detect unwanted parasitic oscillations.
    *   **Bandwidth:** Measure occupied bandwidth of a modulated signal. See Modulation.
    *   **Intermodulation:** Visualise IP3 products. See Interference.

---
[< Back to Section Index](README.md)