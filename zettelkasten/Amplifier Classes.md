---
id: 202512292016
title: Amplifier Classes
tags: ["ham-radio", "circuits", "amplifiers"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Amplifier Classes

Amplifier classes describe the conduction angle (bias point) of the amplifying device.

| Class | Conduction | Linearity | Efficiency | Use |
| :--- | :--- | :--- | :--- | :--- |
| **Class A** | $360^\circ$ (100%) | Highest | Low (25-50%) | Audio, Pre-amps |
| **Class B** | $180^\circ$ (50%) | Low | Medium (~78%) | Push-Pull Audio/RF |
| **Class AB**| $180^\circ - 360^\circ$| Good | Good | SSB Linear Amps |
| **Class C** | $< 180^\circ$ (Pulses)| Very Low | High (>80%) | FM/CW RF PA |

## Push-Pull
A configuration using two devices working alternately (usually Class B or AB).
*   One amplifies the positive half, the other the negative half.
*   **Benefit**: Eliminates **even** harmonics (2nd, 4th, etc.).
*   **Requires**: Phase-splitting (e.g., center-tapped transformer) to drive the inputs.

## Related
*   [[Amplifier Operating Principles]]
*   [[Distortion and Dissipation]]
