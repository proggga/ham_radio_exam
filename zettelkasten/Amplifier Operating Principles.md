---
id: 202512292015
title: Amplifier Operating Principles
tags: ["ham-radio", "circuits", "amplifiers"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Amplifier Operating Principles

An amplifier increases the amplitude of a signal (Voltage, Current, or Power) without changing its shape (ideally). It uses an active device to control a power source.

## Biasing (Instelling)
To work correctly, the active device (like a transistor) must be set to a specific **Operating Point** (Werkpunt or Instelpunt) using DC voltages and currents.
*   **Purpose**: To ensure the device operates in its linear region (for Class A) or appropriate cutoff point.
*   **Methods**:
    *   **Base/Gate Resistors**: Set the DC voltage.
    *   **Emitter/Source/Cathode Resistor**: Provides self-bias and thermal stability (negative feedback for DC).

## Load Line (Belastingslijn)
A graphical tool to visualize amplifier operation.
*   Plots **Collector Current ($I_c$)** vs **Collector-Emitter Voltage ($U_{ce}$)**.
*   **Line**: Connects the saturation point ($I_{max} = U_{supply}/R_{load}$) and cutoff point ($U_{max} = U_{supply}$).
*   **Operating Point ($P$)**: The DC bias point on this line.
    *   For **Class A**, $P$ is in the middle (allows max swing up and down).
    *   For **Class B**, $P$ is at cutoff ($I_c = 0$).

## Related
*   [[Semiconductors]]
*   [[Amplifier Classes]]
