---
id: 202301011220
title: "Time Constants"
tags: ["ham-radio", "circuits"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29
---

# Time Constants ($\tau$)

When a resistor is combined with a capacitor or inductor, voltage and current do not change instantly. The speed of change is determined by the **Time Constant** (Tau, $\tau$).

## 1. RC Circuit (Resistor + Capacitor)
Charging or discharging a [[Capacitors|Capacitor]] through a [[Resistors|Resistor]].
*   **Formula:**
    $$\tau = R \times C$$
*   **Units:** Seconds ($s$) = Ohms ($\Omega$) $\times$ Farads ($F$).

### Process
*   **Charging:**
    *   At $t=0$, Capacitor acts as a short circuit (Current max, Voltage 0).
    *   After **$1 \tau$**: Voltage reaches **63%** of source voltage.
    *   After **$5 \tau$**: Capacitor is considered fully charged (~99%).
*   **Discharging:**
    *   After **$1 \tau$**: Voltage drops to **37%** of initial voltage (lost 63%).
    *   After **$5 \tau$**: Capacitor is considered empty.

## 2. RL Circuit (Resistor + Inductor)
Building up or collapsing current through an [[Inductors (Spoelen)|Inductor]].
*   **Formula:**
    $$\tau = \frac{L}{R}$$
*   **Units:** Seconds ($s$) = Henrys ($H$) / Ohms ($\Omega$).

### Process
*   **Current Buildup:**
    *   At $t=0$, Inductor opposes change (Current 0).
    *   After **$1 \tau$**: Current reaches **63%** of maximum ($U/R$).
    *   After **$5 \tau$**: Current is stable (maximum).
*   **Current Decay:**
    *   Opening a switch creates a high voltage spike (inductive kickback) as the field collapses to try and maintain current.
    *   Current decays to **37%** after $1 \tau$.