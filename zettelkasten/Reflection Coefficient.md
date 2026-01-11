---
id: 202501111210
title: Reflection Coefficient
tags:
  - ham-radio
  - antennas
  - math
created: 2025-01-11
type: permanent-note
modified: 2025-01-11

dutch_title: "Reflectiecoëfficiënt"
aliases: ["Reflectiecoëfficiënt", "Rho", "Gamma"]
---

# Reflection Coefficient ($\Gamma$ or $\rho$)

The **Reflection Coefficient** measures the ratio of the reflected wave amplitude to the incident (forward) wave amplitude at a mismatch.

## Formula
$$\Gamma = \frac{V_{ref}}{V_{fwd}}$$

In terms of Impedance ($Z_{load}$) and Characteristic Impedance ($Z_0$):
$$\Gamma = \frac{Z_{load} - Z_0}{Z_{load} + Z_0}$$

## Values
*   **$\Gamma = 0$**: Perfect match ($Z_{load} = Z_0$). No reflection. [[Standing Wave Ratio (SWR)|SWR]] = 1:1.
*   **$\Gamma = 1$**: Open Circuit ($Z_{load} = \infty$). 100% reflection (in phase).
*   **$\Gamma = -1$**: Short Circuit ($Z_{load} = 0$). 100% reflection (180° phase reversal).

## Relationship to SWR
$$SWR = \frac{1 + |\Gamma|}{1 - |\Gamma|}$$

## Return Loss (RL)
**Return Loss** expresses the ratio of Reflected Power to Forward Power in decibels. It describes how well the load matches the line.
*   **Formula**: $$RL_{dB} = -20 \log_{10} |\Gamma|$$
*   **Interpretation**:
    *   **High RL (e.g., > 20 dB)**: Very little reflection (Good Match).
    *   **Low RL (e.g., < 10 dB)**: Significant reflection (Poor Match).
    *   *Note:* In professional RF, Return Loss is often preferred over SWR.

## Related
*   [[Standing Wave Ratio (SWR)]]
*   [[Transmission Lines]]
*   [[Smith Chart]]
