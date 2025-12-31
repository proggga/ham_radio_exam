# Audio Rectification (LFD)

**Low Frequency Detection (LFD)** (Laagfrequentdetectie), also known as Audio Rectification or "Inpraten", is a common interference problem where radio signals are heard in non-radio audio equipment.

## Mechanism
1.  **Pickup**: Speaker wires, mains leads, or interconnects act as antennas, picking up RF energy.
2.  **Ingress**: RF enters the audio amplifier's feedback loop or input stage.
3.  **[Rectification](../03_circuits/10_Rectification.md)**: A PN junction (Base-Emitter of a transistor) in the input stage acts as a **diode detector**.
4.  **Amplification**: The detected audio (envelope) is amplified and heard through the speakers.

## Symptoms by Mode
*   **[AM](../01_electricity/32_Analogue_Modulation_&_AM.md)**: Clear, intelligible speech.
*   **[SSB](../01_electricity/34_Single_Sideband_SSB.md)**: Muffled, distorted, unintelligible rhythm (like "Donald Duck").
*   **[CW](../01_electricity/33_CW_Abbreviations_&_Prosigns.md)**: Thumping or clicking sounds (Key Clicks/Plops) in time with the keying.
*   **[FM](../01_electricity/35_Frequency_Modulation_FM.md)**: Usually silent (FM has no amplitude variations). Strong FM signals may cause "Blocking" (reduction in volume) or hum.

## Mitigation (Ontstoring)
*   **Speaker Wires**:
    *   **[Capacitors](../02_components/05_Capacitors.md)**: Connect a small ceramic capacitor (**1 nF - 10 nF**) across the speaker terminals *at the amplifier*.
        *   *Criterion:* $X_C$ should be low ($\approx 1 \Omega$) at RF, but high at Audio frequencies.
    *   **Ferrites**: Wrap the wire through a toroid core near the amplifier.
*   **Inputs**:
    *   **RC [Filter](../03_circuits/03_Filters_&_Resonance.md)**: Series resistor + Shunt capacitor (Low-pass) at the input pin.
    *   **Ferrite Bead**: Series bead on the input wire.
*   **Mains**: Mains filter (L-C) or ferrite ring on the power cord.

---
[< Back to Section Index](README.md)