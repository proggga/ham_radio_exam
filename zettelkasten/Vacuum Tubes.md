---
id: 202512292020
title: Vacuum Tubes
tags: ["ham-radio", "components", "tubes"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Vacuum Tubes

Vacuum tubes (valves) operate on the principle of **Thermionic Emission** (Edison Effect).

## Structure & Operation
*   **Heater (Gloeidraad)**: Heats the cathode.
*   **Cathode**: Emits electrons when heated (forms a space charge).
*   **Anode (Plate)**: Attracts electrons if it has a high positive voltage relative to the cathode.
*   **Vacuum**: The glass envelope is evacuated to prevent collisions with air molecules.

## Tube Types

### The Diode (2 Electrodes)
*   **Parts**: Cathode + Anode.
*   **Function**: Rectification (current flows only one way).

### The Triode (3 Electrodes)
*   **Added Part**: **Control Grid (Stuurrooster, $g_1$)**.
*   **Operation**: A small negative voltage on the grid controls the large anode current.
*   **Parameters**:
    *   **Amplification Factor ($\mu$)**: Voltage gain.
    *   **Transconductance ($S$)**: $\Delta I_a / \Delta U_g$ (mA/V).
    *   **Internal Resistance ($R_i$)**: $\Delta U_a / \Delta I_a$.
*   **Drawback**: High Grid-Anode capacitance ($C_{ag}$) causes oscillation (Miller effect).

### The Tetrode (4 Electrodes)
*   **Added Part**: **Screen Grid (Schermrooster, $g_2$)**.
*   **Function**: Shields Anode from Control Grid, reducing $C_{ag}$ for better HF performance.
*   **Drawback**: **Secondary Emission** (electrons bouncing off anode attracted to screen grid).

### The Pentode (5 Electrodes)
*   **Added Part**: **Suppressor Grid (Remrooster, $g_3$)**.
*   **Function**: Prevents secondary emission electrons from reaching the screen grid.
*   **Characteristics**: High gain, high internal resistance.

## Comparison with Semiconductors
*   **Heater**: Tubes need warmup and consume more power.
*   **Voltage**: Tubes work at high voltages (100V - kV).
*   **Robustness**: More resistant to temporary overloads and EMP.

## Related
*   [[Semiconductors]]
*   [[Amplifiers]]
