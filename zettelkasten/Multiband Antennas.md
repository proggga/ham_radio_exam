---
id: 202512301545
title: Multiband Antennas
tags: ["ham-radio", "antennas"]
created: 2025-12-30
type: permanent-note
modified: 2025-12-30
---

# Multiband Antennas

Antennas designed to operate efficiently on multiple frequency bands.

## 1. Trap Dipole (Sperkring Dipool)
Uses parallel LC circuits (**Traps**) inserted into the antenna wire.
*   **Operation**:
    *   **At Resonant Frequency of Trap**: High impedance (acts as an insulator). The outer part of the antenna is cut off. The antenna acts as a shorter dipole for the higher frequency.
    *   **Below Resonant Frequency**: Inductive. Acts as a loading coil, electrically lengthening the antenna.
*   **Advantage**: Single feedline for multiple bands (e.g., W3DZZ for 80/40m).
*   **Disadvantage**: Traps have losses (Q-factor), heavier wind load, narrower bandwidth.

## 2. Fan Dipole (Parallel Dipole)
Multiple dipoles for different bands connected to the same center feedpoint.
*   **Operation**: The signal "sees" the dipole with the lowest impedance (resonant one) and uses it.
*   **Advantage**: Simple, no lossy traps.
*   **Disadvantage**: Wires can interact (detuning), mechanical complexity.

## 3. Log Periodic Antenna (LogPer)
A directional array where elements are scaled logarithmically.
*   **Operation**: Broad bandwidth (can cover 10-30 MHz continuously).
*   **Gain**: Moderate (less than a Yagi for the same boom length).

## Related
*   [[The Dipole Antenna]]
*   [[Filters & Resonance]]
