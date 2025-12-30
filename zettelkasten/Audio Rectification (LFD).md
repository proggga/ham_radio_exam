---
id: 202512292103
title: Audio Rectification (LFD)
tags: ["ham-radio", "interference", "emc"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

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
*   **CW**: Thumping or clicking sounds (Key Clicks/Plops) in time with the keying.
*   **FM**: Usually silent (FM has no amplitude variations). Strong FM signals may cause "Blocking" (reduction in volume) or hum.

## Mitigation (Ontstoring)
*   **Speaker Wires**:
    *   **Capacitors**: Connect a small ceramic capacitor (**1 nF - 10 nF**) across the speaker terminals *at the amplifier*.
        *   *Criterion:* $X_C$ should be low ($\approx 1 \Omega$) at RF, but high at Audio frequencies.
    *   **Ferrites**: Wrap the wire through a toroid core near the amplifier.
*   **Inputs**:
    *   **RC Filter**: Series resistor + Shunt capacitor (Low-pass) at the input pin.
    *   **Ferrite Bead**: Series bead on the input wire.
*   **Mains**: Mains filter (L-C) or ferrite ring on the power cord.

## Related
*   [[Detectors (Demodulators) 202512292039]]
*   [[Capacitor Principles]]
