---
id: 202512311440
title: Doppler Shift
tags: ["ham-radio", "propagation", "physics", "satellite"]
created: 2025-12-31
type: permanent-note
modified: 2025-12-31
---

# Doppler Shift

Doppler [[Repeater Operation|Shift]] is the change in frequency of a wave in relation to an observer who is moving relative to the wave source.

## Mechanism
*   **Approaching Source**: Waves are compressed $\rightarrow$ Frequency **Increases** (Pitch goes up).
*   **Receding Source**: Waves are stretched $\rightarrow$ Frequency **Decreases** (Pitch goes down).

## Amateur Radio Applications
### 1. Satellites
As a Low Earth Orbit (LEO) satellite passes overhead:
*   **AOS (Acquisition of Signal)**: Satellite approaching. Frequency is **High**.
*   **TCA (Time of Closest Approach)**: Frequency is nominal.
*   **[[Line of Sight Propagation (LOS)|LOS]] (Loss of Signal)**: Satellite moving away. Frequency is **Low**.
*   **Correction**: The operator must tune the receiver *down* during the pass to follow the signal. [[VHFUHF Bands (6m, 2m, 70cm)|UHF]] shifts more than [[VHFUHF Bands (6m, 2m, 70cm)|VHF]].

### 2. EME (Moonbounce)
*   The Moon moves relative to the Earth.
*   [[Earth-Moon-Earth (EME)|EME]] signals shift by several kHz at 1296 MHz.

## Formula
$$\Delta f = \frac{v}{c} \times f$$
Where $v$ is relative velocity, $c$ is speed of light, $f$ is frequency.

## Related
*   [[Satellite Operation]]
*   [[Earth-Moon-Earth (EME)]]
