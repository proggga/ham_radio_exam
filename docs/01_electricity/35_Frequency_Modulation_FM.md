# Frequency Modulation (FM)

FM conveys information by varying the frequency of the carrier. Amplitude remains constant.

## Parameters
*   **Deviation ($\Delta f$)**: The maximum frequency shift from the center frequency.
    *   Determined by the **Amplitude** of the audio signal.
*   **[Modulation](31_Modulation_&_Digital_Signals.md) Index ($m$)**:
    *   Formula: $m = \frac{\Delta f}{f_{mod}}$
    *   *Note:* Different from [AM](32_Analogue_Modulation_&_AM.md) modulation depth. Can be > 1.
*   **[Bandwidth](../03_circuits/07_Bandwidth.md) (Carson's Rule)**:
    *   Formula: $B \approx 2(\Delta f + f_{max\_audio})$
    *   *Example:* $\Delta f = 3$ kHz, Audio = 3 kHz $\rightarrow B = 2(3+3) = 12$ kHz. (NBFM).

## Phase Modulation (PM)
Closely related to FM. Often used in mobile radios.
*   **Principle**: Varies the **Phase** of the carrier.
*   **Difference from FM**:
    *   **FM**: Deviation depends *only* on Audio Amplitude.
    *   **PM**: Deviation depends on Audio Amplitude **AND** Audio Frequency (higher tones cause faster phase change $\rightarrow$ higher deviation).
*   **Equivalence**: PM with a 6dB/octave audio low-pass filter (integrator) behaves exactly like FM.

## Frequency Multiplication
*   If an FM signal is passed through a **Frequency Multiplier** (e.g., Doubler, Tripler):
    *   **Carrier Frequency** is multiplied ($f_{out} = n \times f_{in}$).
    *   **Deviation ($\Delta f$)** is **ALSO** multiplied ($ \Delta f_{out} = n \times \Delta f_{in}$).
    *   **[Modulation](31_Modulation_&_Digital_Signals.md) Index ($m$)** is multiplied.
    *   **Audio Frequency ($f_{mod}$)** remains **UNCHANGED**.

## Generation
*   **Direct FM**: Modulating a VCO ([Varicap](../02_components/22_Varicap_Capaciteitsdiode.md)) directly.
*   **Indirect FM**: Using a Phase Modulator after a crystal oscillator.

## Characteristics
*   **[Noise](26_AC_Signals_&_Noise.md) Immunity**: FM receivers limit amplitude variations (static), resulting in quiet backgrounds.
*   **Capture Effect**: The receiver locks onto the strongest signal, completely suppressing weaker signals on the same frequency.

---
[< Back to Section Index](README.md)