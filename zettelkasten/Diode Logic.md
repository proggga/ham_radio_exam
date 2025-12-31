---
id: 202512302230
title: Diode Logic
tags: ["ham-radio", "components", "digital"]
created: 2025-12-30
type: permanent-note
modified: 2025-12-30
---

# Diode Logic

[[Diodes]] can be used to construct simple logic gates (AND, OR) by utilizing their property of conducting current in only one direction.

## Principles
*   **Highest Potential Wins**: In a circuit where multiple diode cathodes meet a common point (with a resistor to ground), the diode with the **highest** anode potential will conduct, raising the common point to that potential (minus 0.7V). The other diodes will be reverse-biased (blocked).
*   **Lowest Potential Wins**: In a circuit where multiple diode anodes meet a common point (with a resistor to V+), the diode with the **lowest** cathode potential will conduct, pulling the common point down.

## Basic Gates

### OR Gate (Positive Logic)
*   **Structure**: Anodes are inputs, cathodes connected together to a resistor to Ground.
*   **Behavior**: If **Input A** OR **Input B** is High, the Output is High.
*   *Analogy*: Several one-way valves feeding a single pipe. Pressure in any input opens its valve and pressurizes the output.

### AND Gate (Positive Logic)
*   **Structure**: Cathodes are inputs, anodes connected together to a resistor to V+.
*   **Behavior**: Only if **Input A** AND **Input B** are High (blocking current flow to ground), the Output remains High (pulled up by resistor). If any input is Low, that diode conducts and pulls the output Low.

## Exam Scenarios
*   **Battery Backup**: Two batteries connected via diodes to a single load. The battery with the higher voltage powers the load; the other diode blocks.
*   **Signal Selection**: "Which diode conducts?" -> Look for the diode with the most positive Anode relative to Cathode.

## Related
*   [[Diodes]]
*   [[Digital Techniques]]
