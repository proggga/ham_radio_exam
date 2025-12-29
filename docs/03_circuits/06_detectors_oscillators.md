# Detectors, Oscillators, and Mixers

## 1. Oscillators
Circuits that generate an AC signal from DC.
*   **Condition:** Barkhausen criterion.
    1.  **Loop Gain:** $\ge 1$.
    2.  **Phase Shift:** $0^\circ$ or $360^\circ$ (Positive Feedback).

### LC Oscillators (Variable Frequency)
*   **Hartley:** Uses an **inductive** voltage divider (tapped coil).
*   **Colpitts:** Uses a **capacitive** voltage divider.
*   **Clapp:** A Colpitts with an extra series capacitor for better stability.

### Crystal Oscillators (Fixed Frequency)
Uses a Quartz crystal (Piezoelectric effect) for high $Q$ and stability.
*   **Pierce:** Crystal connects between Base and Collector (or Grid/Anode). Acts as an inductor.
*   **Colpitts Crystal:** Crystal replaces the inductor in a standard Colpitts.
*   **Overtone:** The crystal vibrates at an odd harmonic (3rd, 5th, 7th) of its fundamental frequency. Used for VHF ($> 20 MHz$).
    *   Requires an LC tank to select the specific overtone.

### Stability
*   **TCXO:** Temperature Compensated Crystal Oscillator.
*   **OCXO:** Oven Controlled Crystal Oscillator (Heated to constant temp).
*   **VCO (Voltage Controlled Oscillator):** Uses a **Varicap** diode to tune frequency via a DC control voltage. Used in PLLs.

### Phase Noise
Short-term frequency instability (jitter) in the time domain appears as noise sidebands in the frequency domain.
*   **Effect:** Widens the signal, degrades receiver selectivity (reciprocal mixing).

## 2. Detectors (Demodulators)
Recovering information from the modulated carrier.
*   **AM:** **Envelope Detector** (Diode + Capacitor).
*   **SSB/CW:** **Product Detector**.
    *   Requires a **BFO** (Beat Frequency Oscillator) to re-insert the carrier.
    *   Audio = $|f_{RF} - f_{BFO}|$.
*   **FM:**
    *   **Discriminator / Ratio Detector:** Converts frequency changes to voltage.
    *   **PLL:** Phase Locked Loop.

## 3. Mixers (Mengtrappen)
Non-linear circuits that combine two frequencies ($f_1$ and $f_2$).
*   **Outputs:** Sum ($f_1 + f_2$) and Difference ($f_1 - f_2$), plus originals and harmonics.
*   **Use:** Superheterodyne receivers (RF + LO -> IF).

### Image Frequency (Spiegelfrequentie)
In a mixer, an unwanted signal can produce the same Intermediate Frequency (IF) as the desired signal.
$$f_{image} = f_{wanted} \pm 2 \cdot f_{IF}$$
*   Mitigation: Input filters (Preselector) or High 1st IF.

## 4. Phase Locked Loop (PLL)
A control system that locks an oscillator to a reference frequency.
*   **Components:**
    1.  **VCO:** Generates output.
    2.  **Reference:** Stable crystal.
    3.  **Phase Detector:** Compares VCO and Ref.
    4.  **Loop Filter:** Smooths error voltage.
    5.  **Divider:** Allows frequency synthesis (step size).
*   **Use:** Frequency synthesizers (VFOs), FM demodulation.
