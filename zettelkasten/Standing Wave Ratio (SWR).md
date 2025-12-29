---
id: 202512292190
title: Standing Wave Ratio (SWR)
tags:
  - ham-radio
  - antennas
  - measurements
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Standing Wave Ratio (SWR)

The **Standing Wave Ratio (SWR)** (Dutch: *Staandegolfverhouding*) is a measure of the impedance match between the transmission line and the load (antenna).

## Definition
Ideally, all power sent by the transmitter is absorbed by the antenna and radiated. If the impedances do not match (e.g., $50 \Omega$ line vs $100 \Omega$ antenna), some power is **reflected** back to the source.

**Standing Waves** are formed by the interference pattern of the Forward wave ($V_{fwd}$) and the Reflected wave ($V_{ref}$) traveling in opposite directions on the line.

## Formulas
$$SWR = \frac{V_{max}}{V_{min}}$$

$$SWR = \frac{1 + \sqrt{P_{ref}/P_{fwd}}}{1 - \sqrt{P_{ref}/P_{fwd}}}$$

## Values
*   **1:1**: Perfect match. No reflection. $V_{max} = V_{min}$.
*   **1.5:1**: Excellent match.
*   **2:1**: Good match. $\approx 11\%$ reflected power.
*   **$\infty$:1**: Total reflection. Open or Short circuit.

## Impact
*   **Loss**: Higher SWR increases [[Transmission Line Loss]].
*   **Damage**: High voltage peaks can arc in cables; reflected power can overheat the transmitter PA.

## Related Notes
*   [[Impedance (Impedantie)]]
*   [[SWR Meter]]
*   [[Reflection Coefficient]]
