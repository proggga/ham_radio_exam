---
id: 202501101409
title: End-Fed Antenna
tags:
  - ham-radio
  - antennas
created: 2025-01-10
type: permanent-note
modified: 2025-01-10

aliases: ["Eindgevoede antenne", "End-Fed Half Wave", "EFHW", "Zeppelin antenne"]
---

# End-Fed Antenna

The **End-Fed Half Wave (EFHW)** is a popular variant of the dipole, especially for portable operation and limited space.

## Principle
A standard [[The Dipole Antenna|Dipole]] is fed in the center, where the current is maximum and voltage is minimum ($Z \approx 73 \Omega$).
An **End-Fed** antenna is fed at the very end of the wire, where:
*   **Voltage is Maximum** (High Voltage point).
*   **Current is Minimum**.
*   **[[Impedance|Impedance]] is Very High**: Typically $2500 \Omega$ to $5000 \Omega$.

## Matching (The Unun)
To feed this high impedance with standard $50 \Omega$ [[Transmission Lines|Coax]], a broadband **Impedance Transformer** is required.
*   **Ratio**: Typically **49:1** or **64:1**.
    *   $50 \Omega \times 49 = 2450 \Omega$.
*   **Type**: **Unun** (Unbalanced to Unbalanced), as both the coax and the end-fed wire are unbalanced.

## Counterpoise
Although often advertised as "no ground required," an end-fed antenna **always** needs a counterpoise to complete the circuit.
*   **Coax Shield**: Usually, the shield of the coaxial cable acts as the counterpoise.
*   **Choke**: A **Common Mode Choke** is recommended about 0.05 $\lambda$ down the coax to stop RF from returning to the shack ([[Mitigation|RFI]]).

## Pros & Cons
*   **Pros**:
    *   Easy deployment (only one support needed).
    *   Multiband operation (resonates on harmonics like a dipole).
*   **Cons**:
    *   **High Voltage**: The feedpoint has very high RF voltage. Dangerous if touched while transmitting ([[Electrical Safety]]).
    *   **RF in Shack**: Higher risk of "RF bite" or interference if the counterpoise is insufficient.

## Variants
*   **Zeppelin (Zepp)**: An older version fed with balanced ladder line.
*   **Fuchs Antenna**: Using a parallel LC circuit tuner directly at the antenna base.

## Related
*   [[The Dipole Antenna]]
*   [[Impedance Transformation]]
*   [[Transmission Lines]]
*   [[Antenna & Tower Safety]]
