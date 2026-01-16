id: 202512292103
title: "Audio Rectification"
tags: ["amplifiers", "emc", "filters", "interference", "modes", "semiconductors"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29

aliases: ["Laagfrequentdetectie", "LFD"]

# Audio Rectification (LFD)

**Low Frequency Detection (LFD)** (Laagfrequentdetectie), also known as Audio Rectification or "Inpraten", is a common interference problem where radio signals are heard in non-radio audio equipment.

## Mechanism
1.  **Pickup**: Speaker wires, mains leads, or interconnects act as antennas, picking up RF energy.
2.  **Ingress**: RF enters the audio amplifier's feedback loop or input stage.
3.  **Rectification**: A PN junction (Base-Emitter of a transistor) in the input stage acts as a **diode detector**.
4.  **Amplification**: The detected audio (envelope) is amplified and heard through the speakers.

## Symptoms by Mode
*   **AM**: Clear, intelligible speech.
*   **SSB**: Muffled, distorted, unintelligible rhythm (like "Donald Duck").
*   **CW**: Thumping or clicking sounds ([Key](../04_receivers/07_Station_Accessories.md) Clicks/Plops) in time with the keying.
*   **FM**: Usually silent (FM has no amplitude variations). Strong FM signals may cause "Blocking" (reduction in volume) or hum.

## Mitigation (Ontstoring)
*   **Speaker Wires**:
    *   **[Capacitors](../02_components/02_Capacitors.md)**: Connect a small ceramic capacitor (**1 nF - 10 nF**) across the speaker terminals *at the amplifier*.
        *   *Criterion:* $X_C$ should be low ($\approx 1 \Omega$) at RF, but high at Audio frequencies.
    *   **Ferrites**: Wrap the wire through a toroid core near the amplifier.
*   **Inputs**:
    *   **RC [Filter](../03_circuits/03_Filters_&_Resonance.md)**: Series resistor + Shunt capacitor (Low-pass) at the input pin.
    *   **Ferrite Bead**: Series bead on the input wire.
*   **Mains**: Mains filter (L-C) or ferrite ring on the power cord.

---
[< Back to Section Index](README.md)