---
id: 202512311410
title: Common Troubleshooting
tags: ["ham-radio", "operating", "maintenance", "troubleshooting"]
created: 2025-12-31
type: permanent-note
modified: 2025-12-31
---

# Common Troubleshooting

Diagnosing and fixing common station problems is a key skill for any radio operator.

## Audio Problems

### Distorted Audio (Transmit)
*   **Over-Deviation (FM)**: Audio is too loud and clipped.
    *   *Cause:* Talking too close to the microphone or Mic Gain too high.
    *   *Fix:* Speak farther away ("Eat the mic" is bad for FM) or turn down Mic Gain.
*   **RF Feedback**: Audio sounds garbled, buzzing, or has a "motorboat" sound.
    *   *Cause:* Stray RF energy is being picked up by the microphone cable shield and getting into the audio amplifier. Common with high SWR or poor grounding.
    *   *Fix:* Install a **Ferrite Choke** on the microphone cable. Improve station [[Station Setup Guidelines|RF Ground]].
*   **Low Voltage**: Audio sounds "warbly" or weak.
    *   *Cause:* Battery low or high resistance connection causing voltage drop during transmit peaks.
    *   *Fix:* Check power supply/battery and fuse holders.

### Hum (Receive/Transmit)
*   **Ground Loop**: A low-frequency hum (50/60 Hz) on the signal.
    *   *Cause:* Current flowing through the ground shield of audio cables between equipment (e.g., PC and Radio) powered from different AC outlets.
    *   *Fix:* Use **Audio Isolation Transformers** or optical isolators. Connect all equipment to a **Single Point Ground**.

## Antenna & Power Problems

### High SWR
*   **Intermittent SWR**: Readings jump around (erratic).
    *   *Cause:* Loose connection (PL-259), bad solder joint, or corroded connector.
    *   *Fix:* Wiggle cables to find the fault. Resolder or replace connectors.
*   **High SWR (Constant)**:
    *   *Cause:* Antenna detuned, water in coax, or short/open in feedline.
    *   *Fix:* Test with a **Dummy Load** at the end of the coax to rule out the cable. Check antenna dimensions.

### Mobile Noise
*   **Ignition Noise**: Popping sound varying with engine RPM.
    *   *Fix:* Use **Resistor Spark Plugs**. Turn on the radio's **Noise Blanker (NB)**.
*   **Alternator Whine**: Whine varying with engine RPM.
    *   *Fix:* Install power line filters (capacitors/chokes) on the radio's DC power lead. Connect radio power **directly to the battery**.

## Related
*   [[Station Setup Guidelines]]
*   [[RF Measurements]]
*   [[Mitigation (Ontstoring)]]
