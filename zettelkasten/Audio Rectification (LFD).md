---
id: 202512292103
title: Audio Rectification (LFD)
tags: ["ham-radio", "interference", "emc"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Audio Rectification (LFD)

**Low Frequency Detection (LFD)**, or Audio Rectification, is a common interference problem in consumer electronics.

## Mechanism
1.  RF energy is picked up by cables (speaker wires, microphone leads) acting as antennas.
2.  The RF enters an audio amplifier.
3.  A PN junction (Transistor or Diode) in the input stage acts as a **detector** (rectifier), extracting the audio modulation from the RF carrier.

## Symptoms
*   **AM**: Voice is heard clearly.
*   **SSB**: Muffled, distorted, unintelligible "Donald Duck" sounds.
*   **CW**: Clicking or thumping sounds.
*   **FM**: Often just a change in background hum or volume; FM is not easily detected by simple rectification.

## Mitigation
*   **Ferrite cores**: Clamped on cables to block common-mode RF.
*   **Bypass Capacitors**: Short RF to ground at the input.

## Related
*   [[Detectors (Demodulators) 202512292039]]
*   [[Capacitor Principles]]
