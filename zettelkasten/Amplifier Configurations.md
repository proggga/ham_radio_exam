---
id: 202512302345
title: Amplifier Configurations
tags: ["ham-radio", "circuits", "amplifiers"]
created: 2025-12-30
type: permanent-note
modified: 2025-12-30
---

# Amplifier Configurations

There are three basic circuit configurations for amplifying components (BJT, FET, Tube), defined by which terminal is common to both input and output (AC ground).

## 1. Common Emitter / Source / Cathode
*   **The Standard Amplifier**. Most widely used.
*   **Input**: Base / Gate / Grid.
*   **Output**: Collector / Drain / Anode.
*   **Common**: Emitter / Source / Cathode.
*   **Characteristics**:
    *   **Voltage Gain**: High ($\approx R_L / R_E$).
    *   **Current Gain**: High ($\beta$).
    *   **Power Gain**: Very High (Highest of all).
    *   **Phase**: **Inverted ($180^\circ$)**.
    *   **Input Z**: Medium (BJT) / High (FET/Tube).
    *   **Output Z**: Medium/High.

## 2. Common Collector / Drain / Anode (Follower)
*   **The Buffer**. Used for impedance matching.
*   **Input**: Base / Gate / Grid.
*   **Output**: Emitter / Source / Cathode.
*   **Common**: Collector / Drain / Anode (connected to supply rail, which is AC ground).
*   **Characteristics**:
    *   **Voltage Gain**: $\approx 1$ (Unity).
    *   **Current Gain**: High.
    *   **Power Gain**: Moderate.
    *   **Phase**: **Non-Inverted ($0^\circ$)**.
    *   **Input Z**: **High** (Voltage Follower).
    *   **Output Z**: **Low**.
    *   **Names**: Emitter Follower, Source Follower, Cathode Follower.

## 3. Common Base / Gate / Grid
*   **The [[Propagation Basics|HF]] Specialist**. Used in RF amplifiers.
*   **Input**: Emitter / Source / Cathode.
*   **Output**: Collector / Drain / Anode.
*   **Common**: Base / Gate / Grid.
*   **Characteristics**:
    *   **Voltage Gain**: High.
    *   **Current Gain**: $\approx 1$ (Unity).
    *   **Power Gain**: High.
    *   **Phase**: **Non-Inverted ($0^\circ$)**.
    *   **Input Z**: **Low**.
    *   **Output Z**: High.
*   **Advantage**: Low feedback capacitance (Miller effect avoided), making it stable at high frequencies ([[VHFUHF Bands (6m, 2m, 70cm)|VHF]]/[[VHFUHF Bands (6m, 2m, 70cm)|UHF]]).

## Summary Table

| Parameter | Common Emitter (GES/GSS/GKS) | Common Collector (GCS/GDS/GAS) | Common Base (GBS/GGS/GRS) |
| :--- | :--- | :--- | :--- |
| **Input Signal** | Base/Gate | Base/Gate | Emitter/Source |
| **Output Signal** | Collector/Drain | Emitter/Source | Collector/Drain |
| **Voltage Gain** | High ($>>1$) | $\approx 1$ | High ($>>1$) |
| **Current Gain** | High ($>>1$) | High ($>>1$) | $\approx 1$ |
| **Power Gain** | **Very High** | Moderate | High |
| **Input Z** | Medium | **High** | **Low** |
| **Output Z** | Medium | **Low** | High |
| **Phase** | **Inverted ($180^\circ$)** | In Phase ($0^\circ$) | In Phase ($0^\circ$) |
| **Application** | General Purpose, Audio | Buffer, [[Impedance (Impedantie)|Impedance]] Matching | RF/[[VHFUHF Bands (6m, 2m, 70cm)|VHF]] Amplifier |

## Mnemonics
*   **"Common" terminal** is the one *not* used for Input or Output.
*   **Follower** = Voltage follows input = Gain of 1.
*   **Basic Income** (Basisinkomen): **Common Base** has **Low** Input impedance (Low Income) and **High** Output impedance.
