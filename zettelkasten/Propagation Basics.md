---
id: 202301011236
title: "Propagation Basics"
tags: ["ham-radio", "propagation"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Propagation Basics

## 1. Electromagnetic Waves
Radio waves consist of oscillating Electric ($E$) and Magnetic ($H$) fields. See [[Electric, Magnetic, and Electromagnetic Fields|Fields]].
*   **Orientation:** $E$ and $H$ are perpendicular to each other and to the direction of travel.
*   **Velocity:** $c \approx 300,000 \text{ km/s}$.
*   **Wavelength:** $\lambda = c / f$. See [[AC Signals & Noise|AC Signals]].

## 2. Polarization
Defined by the orientation of the **[[Electric Field]] ($E$)**.
*   **Horizontal:** [[The Dipole Antenna|Dipole]] parallel to the ground.
*   **Vertical:** Ground plane / vertical whip.
*   **Cross Polarization:** Loss of signal (~20-30 [[Decibels & Logarithms|dB]]) if TX is Vertical and RX is Horizontal (or vice versa). Important for [[VHFUHF Bands (6m, 2m, 70cm)|VHF]]/[[VHFUHF Bands (6m, 2m, 70cm)|UHF]]/Line of Sight. Less important for HF Skywave (ionosphere twists polarization).

## 3. Inverse Square Law
As the wave spreads out from a point source, power density decreases with the square of the distance.
*   Double the distance = 1/4 the power (-6 [[Decibels & Logarithms|dB]]).