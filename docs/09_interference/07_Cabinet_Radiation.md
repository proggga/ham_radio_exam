id: 202501101406
title: Cabinet Radiation
tags: ["emc", "interference", "safety"]
created: 2025-01-10
type: permanent-note
modified: 2025-01-10

aliases: ["Kaststraling"]

# Cabinet Radiation (Kaststraling)

**Cabinet Radiation** is RF energy radiated directly from the chassis or case of a transmitter, rather than through the antenna connector.

## Mechanism
*   **Poor Shielding**: If the transmitter's internal circuitry is not properly enclosed in a metal case (Faraday cage), RF fields can escape.
*   **Leakage Points**: RF can leak through:
    *   Ventilation holes.
    *   Meter openings.
    *   Seams between metal plates (if not electrically bonded).
    *   Power and control cables acting as antennas (Common Mode current).

## Consequences
*   **Interference (RFI)**: Can cause interference to nearby electronics (TV, Audio, Computers) even if the antenna is perfect.
*   **RF Burns**: Touching the case might cause RF burns if the chassis is "hot" with RF.

## Mitigation
1.  **Shielding**: Use a complete metal enclosure. Ensure good electrical contact between all panels (remove paint at screw points).
2.  **Decoupling**: Use bypass capacitors and ferrites on all wires *leaving* the case (Power, Mic, Key, Data) to prevent them from carrying RF out.
3.  **Grounding**: Ensure the chassis is connected to a good RF ground.

---
[< Back to Section Index](README.md)