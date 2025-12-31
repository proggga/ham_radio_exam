---
id: 202301011228
title: "Detectors (Demodulators)"
tags: ["ham-radio", "receivers"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Detectors (Demodulators)

## 1. AM Detection
*   **Envelope Detector (Omhullende-detector)**:
    *   **Circuit**: A diode (rectifier) followed by a low-pass RC filter.
    *   **Operation**: The diode chops off the negative half of the RF. The capacitor charges to the peak of the RF pulses, smoothing them into the audio envelope.
    *   **Load**: The resistor $R$ discharges the capacitor $C$ to follow the envelope. If $RC$ is too large, it clips high audio frequencies (diagonal clipping).

## 2. SSB and CW Detection
Requires a local carrier to replace the one suppressed at the transmitter.
*   **Product Detector**: A mixer circuit.
    *   Inputs: IF Signal + BFO (Beat Frequency Oscillator).
    *   Output: Audio ($f_{audio} = |f_{IF} - f_{BFO}|$).
*   **BFO Setting**:
    *   **[[CW Abbreviations & Prosigns|CW]]**: Set BFO $\approx 800$ Hz away from IF center to hear a tone.
    *   **USB**: Set BFO at the *lower* edge of the IF passband (carrier frequency).
    *   **LSB**: Set BFO at the *upper* edge of the IF passband.

## 3. FM Detection
Converts frequency changes into voltage changes.
*   **Limiter (Begrenzer)**: Essential before detection to remove Amplitude variations ([[AC Signals & Noise|Noise]]/Static). Usually a saturated amplifier.
*   **Slope Detector (Flankdetector)**: Uses the slope of a tuned circuit. Primitive, non-linear.
*   **Discriminator (Foster-Seeley)**: Good linearity, sensitive to amplitude (needs limiter).
*   **Ratio Detector**: [[Analogue Modulation & AM|AM]]-insensitive (built-in limiting action via capacitor).
*   **Quadrature Detector**: Uses a phase-shift network and product detector. Common in ICs.
*   **[[Phase Locked Loop (PLL)|PLL]] Detector**: A [[Phase Locked Loop (PLL)|Phase Locked Loop]] locks to the input signal. The **Error Voltage** that controls the VCO tracks the frequency deviation $\rightarrow$ This is the Audio output. High quality.

## Related