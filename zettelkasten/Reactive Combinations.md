---
id: 202301011219
title: "Reactive Combinations"
tags: ["ham-radio", "circuits"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Reactive Combinations

## 1. Capacitors in Series and Parallel
[[Capacitors]] behave **opposite** to [[Resistors|Resistors]].

### Parallel Capacitors
Connecting [[Capacitors|Capacitors]] in parallel increases the total plate area.
*   **Formula:** Add the values.
    $$C_{tot} = C_1 + C_2 + C_3 + \dots$$
*   **Result:** $C_{tot}$ is larger than the largest capacitor.

### Series Capacitors
Connecting capacitors in series increases the effective distance between plates.
*   **Formula:** Inverse sum (like resistors in parallel).
    $$\frac{1}{C_{tot}} = \frac{1}{C_1} + \frac{1}{C_2} + \dots$$
*   **Result:** $C_{tot}$ is smaller than the smallest capacitor.

## 2. Inductors in Series and Parallel
[[Inductors (Spoelen)|Inductors]] behave **like** resistors (assuming no magnetic coupling between them).

### Series Inductors
*   **Formula:** Add the values.
    $$L_{tot} = L_1 + L_2 + L_3 + \dots$$

### Parallel Inductors
*   **Formula:** Inverse sum.
    $$\frac{1}{L_{tot}} = \frac{1}{L_1} + \frac{1}{L_2} + \dots$$

> **Note:** These formulas assume the inductors are magnetically shielded from each other. If their fields interact (mutual inductance), the formulas are more complex.

## Summary Table

| Connection | [[Resistors]] ($R$) | [[Inductors (Spoelen)|Inductors]] ($L$) | [[Capacitors]] ($C$) |
| :--- | :--- | :--- | :--- |
| **Series** | Add | Add | Inverse Sum |
| **Parallel** | Inverse Sum | Inverse Sum | Add |