---
id: 202512292021
title: Operational Amplifiers (Op-Amps)
tags: ["ham-radio", "components", "circuits", "amplifiers"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Operational Amplifiers (Op-Amps)

An Op-Amp is a high-gain integrated circuit amplifier with differential inputs.

## Characteristics
*   **Gain**: Very high open-loop gain.
*   **Inputs**: Inverting (-) and Non-Inverting (+).
*   **Impedance**: Very high input impedance, low output impedance.

## Feedback (Tegenkoppeling)
Op-amps are almost always used with **negative feedback** to control gain and stability.

## Configurations

### 1. Inverting Amplifier
Output is inverted ($180^\circ$ phase shift).
*   **Gain**: $A = -\frac{R_{feedback}}{R_{input}}$

### 2. Non-Inverting Amplifier
Output is in phase with input.
*   **Gain**: $A = 1 + \frac{R_{feedback}}{R_{ground}}$

### 3. Voltage Follower (Buffer)
Output connected directly to (-) input.
*   **Gain**: 1
*   **Use**: Impedance matching (High Z source to Low Z load).

### 4. Comparator
No feedback used. Compares inputs and swings output to positive or negative rail.

## Related
*   [[Amplifiers]]
*   [[Feedback Systems]]
