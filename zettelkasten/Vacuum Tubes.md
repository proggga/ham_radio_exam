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
*   **Function**: [[Rectification]] (current flows only one way).

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
*   **Function**:
    *   Shields Anode from Control Grid, reducing Grid-Anode capacitance ($C_{ag}$). This improves [[Propagation Basics|HF]] stability and gain.
    *   Makes Anode current ($I_a$) less dependent on Anode Voltage ($U_a$), increasing internal resistance ($R_i$) and Gain factor ($\mu$).
*   **Drawback**: **Secondary Emission**. High speed electrons hitting the Anode knock other electrons loose. If $U_a < U_{g2}$, these electrons are attracted to the screen grid, causing a "dip" in the characteristic curve (negative resistance region). This causes instability.

### The Pentode (5 Electrodes)
*   **Added Part**: **Suppressor Grid (Remrooster, $g_3$)**.
*   **Position**: Between Screen Grid and Anode.
*   **Connection**: Usually connected to the **Cathode** (0V relative to Anode), making it negative relative to the Anode.
*   **Function**: Repels secondary emission electrons back to the Anode, eliminating the Tetrode's dip.
*   **Characteristics**: High gain, very high internal resistance. Standard for RF power amplifiers.

### Beam Power Tube
A specialized variant of the Tetrode/Pentode designed for high power handling and efficiency.
*   **Structure**: Uses **Beam-Forming Plates** instead of a suppressor grid (or in addition to special grid alignment).
*   **Operation**: The beam plates focus the electron stream into concentrated beams towards the anode. The alignment of control and screen grid wires reduces screen grid current.
*   **Advantage**: Higher efficiency and power output than standard pentodes.
*   **Examples**: 6L6, 6146, 807 (common in older ham transmitters).

## Tube Configurations (Basisschakelingen)
Analogous to [[Transistors (BJT & FET)|Transistor]]/FET circuits.
*   **Common Cathode (GKS)**:
    *   Input: Grid | Output: Anode.
    *   *Equivalent:* Common Emitter (GES) / Common Source (GSS).
    *   *Characteristics:* High Gain, Phase Inversion ($180^\circ$).
*   **Cathode Follower (GAS - Common Anode)**:
    *   Input: Grid | Output: Cathode.
    *   *Equivalent:* Emitter Follower (GCS) / Source Follower (GDS).
    *   *Characteristics:* Gain < 1, High Input Z, Low Output Z. Used as Buffer.
*   **Grounded Grid (GRS)**:
    *   Input: Cathode | Output: Anode.
    *   *Equivalent:* Common Base (GBS) / Common Gate (GGS).
    *   *Characteristics:* Non-inverting, Low Input Z. Used in [[VHFUHF Bands (6m, 2m, 70cm)|VHF]]/[[VHFUHF Bands (6m, 2m, 70cm)|UHF]] amplifiers.

## Comparison with Semiconductors
*   **Heater**: [[Tubes & Op-Amps|Tubes]] need warmup and consume more power.
*   **Voltage**: [[Tubes & Op-Amps|Tubes]] work at high voltages (100V - kV).
*   **Robustness**: More resistant to temporary overloads and EMP.

## Related
*   [[Semiconductors]]
*   [[Amplifiers]]
