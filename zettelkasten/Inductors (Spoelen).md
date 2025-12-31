---
id: 202301011214
title: "Inductors (Spoelen)"
tags: ["ham-radio", "components"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Inductors (Spoelen)

## 1. Structure and Function
An inductor (coil) stores electrical energy in a **magnetic field** (See [[Electric, Magnetic, and Electromagnetic Fields|Fields]]).
*   **Construction:** A coil of conductive wire, often wound around a core.
    *   **Litz Wire:** Used for MF/[[Propagation Basics|HF]] coils to reduce **[[Skin Effect]]** (Copper losses). Consists of many thin insulated strands.
    *   **[[Shielding (Afscherming)|Shielding]]:** MF coils are often shielded with an aluminum can to prevent magnetic field interference with nearby components.
*   **Symbol:** A series of loops (like a spring).

## 2. Inductance (Zelfinductie)
The property of a coil to oppose changes in current flow.
*   **Symbol:** $L$.
*   **Unit:** Henry ($H$).
*   **Effect:** If voltage of 1 V is applied to 1 H, current increases by 1 A per second.

### Self-Induction & Lenz's Law
When current changes, the magnetic field changes. This inducing a voltage (**Back EMF**) that opposes the change (Lenz's Law).
*   *Inertia for electricity:* Hard to start current, hard to stop current.

## 3. Formula
For a single-layer coil, inductance depends on:
$$L = \frac{\mu_0 \cdot \mu_r \cdot n^2 \cdot A}{l}$$

[[Station Accessories|Key]] factors:
1.  **Turns ($n$):** Proportional to the **square** of turns ($n^2$). Double the turns = 4x Inductance.
2.  **Area ($A$):** Thicker coil = Higher inductance.
3.  **Length ($l$):** Longer coil (stretching it out) = **Lower** inductance.
    *   *[[Licensing in the Netherlands|Exam]] Tip:* If a coil is "stretched" (length increases, turns stay constant), $L$ decreases because the magnetic coupling between turns is reduced.
    *   *Formula Relationship:* $L \propto 1/l$.
4.  **Core Material ($\mu_r$):** Relative Permeability.
    *   Air: $\mu_r \approx 1$.
    *   Iron/Ferrite: $\mu_r \gg 1$ (Greatly increases inductance).
    *   *[[Shielding (Afscherming)|Shielding]]:* A conductive shield (aluminum can) around a coil *reduces* its inductance slightly due to eddy currents in the shield opposing the field.

### Mutual Inductance & Force
*   **Forces:**
    *   Currents in the **same** direction **attract**.
    *   Currents in **opposite** directions **repel**.
    *   *Exam Scenario:* Two coils with currents flowing towards the center (effectively opposite relative to each other's poles) will repel.

### Inductors in Circuits
*   **Series:** $L_{tot} = L_1 + L_2$ (Like [[Resistors]]).
*   **Parallel:** $\frac{1}{L_{tot}} = \frac{1}{L_1} + \frac{1}{L_2}$ (Like [[Resistors]]).

## 4. Applications
*   **Electromagnets:** Coil with iron core.
*   **[[Transformers]]:** Two magnetically coupled coils.
*   **[[Filters & Resonance|Filters]]:** Blocking high frequencies (choke). See [[Filters & Resonance|Filters]].