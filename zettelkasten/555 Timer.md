---
id: 202512311635
title: 555 Timer
tags: ["ham-radio", "components", "ic", "circuits"]
created: 2025-12-31
type: permanent-note
modified: 2025-12-31
---

# 555 Timer

The **555 Timer** is a versatile and widely used Integrated Circuit (IC) capable of producing accurate time delays or oscillations.

## Overview
*   **Package**: Typically 8-pin DIP (Dual In-line Package) or 14-pin DIP.
*   **Power**: Operates on 4.5V to 16V DC.
*   **Output**: Can source or sink up to 200mA (enough to drive an LED or small relay directly).

## Operating Modes

### 1. Monostable (One-Shot)
*   **Function**: Produces a single output pulse of a set duration when triggered.
*   **Trigger**: A low pulse on Pin 2 (Trigger).
*   **Timing**: Duration $t = 1.1 \times R \times C$.
*   **Use**: Timers, debounce switches, pulse stretching.

### 2. Astable (Free Running)
*   **Function**: Generates a continuous square wave (Oscillator).
*   **Timing**: Frequency depends on two resistors and one capacitor connected to the discharge and threshold pins.
*   **Use**: [[Oscillators]], tone generators, LED flashers, Morse code practice oscillators.

## Key Pins (8-pin version)
1.  **GND**: Ground.
2.  **TRIG**: Trigger input (active low).
3.  **OUT**: Output signal.
4.  **RESET**: Resets timing (active low).
5.  **CV**: Control Voltage (often bypassed with a capacitor).
6.  **THR**: Threshold (ends timing cycle).
7.  **DIS**: Discharge (discharges timing capacitor).
8.  **VCC**: Positive supply voltage.

## Related
*   [[Oscillators]]
*   [[Digital Components & Crystals|Digital Components]]
*   [[Time Constants]] (RC circuits determine timing)
