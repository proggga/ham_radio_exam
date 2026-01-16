id: 202301011245
title: "Mitigation"
tags: ["filters", "formulas", "interference", "oscillators", "safety"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29

aliases: ["Ontstoring", "EMC"]

# Mitigation (Ontstoring)

## 1. At the Transmitter (Source)
*   **Low Pass [Filter](../03_circuits/03_Filters_&_Resonance.md) (LPF):** Place between Transmitter and [Antenna](../10_safety/03_Antenna_&_Tower_Safety.md). Attenuates Harmonics (frequencies *above* the cutoff).
    *   *Circuit:* Pi-filter or T-filter ([Capacitor](../02_components/02_Capacitors.md) to ground).
*   **Power Level:** Use the minimum power necessary.
*   **Shielding (Afscherming)**: Enclose oscillator/RF stages in metal cans ("Inblikken").
    *   **Feedthrough [Capacitors](../02_components/02_Capacitors.md) (Doorvoercondensatoren)**: Used to pass DC power/signals through the shield while shorting RF to the case (ground).

## 2. At the Victim (Immunity)
*   **High Pass [Filter](../03_circuits/03_Filters_&_Resonance.md) (HPF):** Place on TV/Radio antenna inputs to block [HF](../07_propagation/01_Propagation_Basics.md) amateur signals.
*   **Band Stop [Filter](../03_circuits/03_Filters_&_Resonance.md) (Notch/Sperkring):** Blocks a specific interfering frequency. Series LC to ground or Parallel LC in series.
*   **Input Attenuator**: Reduces the signal level to prevent Intermodulation/Blocking.

## 3. Cable Filtering & Routing
*   **Ferrites (Ferrietkernen):**
    *   **Function:** Acts as a **Common Mode Choke**. Increases the inductance of the cable shield, blocking RF currents flowing on the outside.
    *   *Placement:* As close to the equipment (TX or Victim) as possible.
    *   *Effectiveness:* Multiple turns through a ring increase inductance ($L \propto n^2$).
*   **Routing (Siting):**
    *   **Separation**: Keep antenna cables, power lines, and telephone lines separated.
    *   **Crossing**: If cables must cross, they should cross at **90 degree angles** to minimize inductive coupling.
    *   **Length**: Keep ground leads and interconnects as short as possible to avoid resonance.

## 4. Decoupling (Ontkoppelen)
Using capacitors to short RF to ground.
*   **[Capacitors](../02_components/02_Capacitors.md):** Ceramic disc capacitors (low inductance). Values typically **1 nF - 10 nF**.
*   **Placement:** Across speaker terminals, audio inputs, or mains pins.
*   **Formula**: $X_C = \frac{1}{2\pi f C}$. Goal is $X_C \ll Z_{circuit}$.

## 5. Mains Filtering
*   **Mains Filter:** A combination of Series [Inductors](../02_components/03_Inductors.md) and Parallel Capacitors (L-C) built into a module.
*   **Ferrite Ring**: Wrapping the mains cord through a ferrite ring blocks common-mode RF from entering via the mains.

## 6. Social Aspects
Technique is only half the solution.
*   **Good Relations**: Maintain a friendly relationship with neighbors. They are more likely to cooperate if they like you.
*   **Cooperation**: Take complaints seriously. Work *with* the neighbor to solve the problem (e.g., offer to install a filter on their device).
*   **Responsibility**: Even if your equipment meets all standards, you have a moral obligation to help resolve interference caused by your transmissions.

---
[< Back to Section Index](README.md)