---
id: 202512292192
title: Antenna Tuning Unit (ATU)
tags:
  - ham-radio
  - antennas
  - equipment
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Antenna Tuning Unit (ATU)

An **ATU**, also known as an [[Antenna & Tower Safety|Antenna]] Tuner, Transmatch, or Matchbox, is a device placed between the transmitter and the feedline.

## Function
It acts as an adjustable impedance transformer.
*   **Input**: Matches the $50 \Omega$ output of the transmitter.
*   **Output**: Matches the complex impedance ($R \pm jX$) of the antenna system.

## Critical Limitation
An ATU does **NOT** "tune the antenna".
*   It creates a conjugate match at the **transmitter end** of the line.
*   The **[[Standing Wave Ratio (SWR)|SWR]] on the transmission line** between the ATU and the antenna remains unchanged.
*   If the SWR on the line is high, cable losses will still occur, even if the transmitter sees 1:1.

## Placement
*   **In the Shack**: Protects the radio, but doesn't reduce feedline loss.
*   **Remote (at Antenna)**: The best location. Matches the antenna to the line, ensuring low SWR on the entire coax run.

## Related Notes
*   [[Standing Wave Ratio (SWR)]]
*   [[Transmission Line Loss]]
*   [[Reactance & Impedance]]
