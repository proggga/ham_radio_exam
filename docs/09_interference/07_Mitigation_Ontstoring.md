# Mitigation (Ontstoring)

## 1. At the Transmitter (Source)
*   **Low Pass [Filter](../03_circuits/03_Filters_&_Resonance.md) (LPF):** Place between Transmitter and [Antenna](../10_safety/03_Antenna_&_Tower_Safety.md). Attenuates Harmonics (frequencies *above* the cutoff).
    *   *Circuit:* Pi-filter or T-filter ([Capacitor](../02_components/05_Capacitors.md) to ground).
*   **Power Level:** Use the minimum power necessary.
*   **[Shielding](../01_electricity/20_Shielding_Afscherming.md) (Afscherming)**: Enclose oscillator/RF stages in metal cans ("Inblikken").
    *   **Feedthrough Capacitors (Doorvoercondensatoren)**: Used to pass DC power/signals through the shield while shorting RF to the case (ground).

## 2. At the Victim (Immunity)
*   **High Pass Filter (HPF):** Place on TV/Radio antenna inputs to block [HF](../07_propagation/01_Propagation_Basics.md) amateur signals.
*   **Band Stop Filter (Notch/Sperkring):** Blocks a specific interfering frequency. Series LC to ground or Parallel LC in series.
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
*   **Capacitors:** Ceramic disc capacitors (low inductance). Values typically **1 nF - 10 nF**.
*   **Placement:** Across speaker terminals, audio inputs, or mains pins.
*   **Formula**: $X_C = \frac{1}{2\pi f C}$. Goal is $X_C \ll Z_{circuit}$.

## 5. Mains Filtering
*   **Mains Filter:** A combination of Series [Inductors](../02_components/09_Inductors_Spoelen.md) and Parallel Capacitors (L-C) built into a module.
*   **Ferrite Ring**: Wrapping the mains cord through a ferrite ring blocks common-mode RF from entering via the mains.

---
[< Back to Section Index](README.md)