---
id: 202512311240
title: Spread Spectrum & Frequency Hopping
tags: ["ham-radio", "modes", "military", "security"]
created: 2025-12-31
type: permanent-note
modified: 2025-12-31
---

# Spread Spectrum & Frequency Hopping

Spread Spectrum techniques spread a signal over a wide bandwidth, much larger than the minimum required to transmit the information. This provides immunity to interference and jamming.

## Techniques

### 1. Frequency Hopping (FHSS)
The carrier frequency rapidly changes (hops) according to a pseudorandom sequence known to both transmitter and receiver.
*   **Military Use**: Used in **SINCGARS** (Single Channel Ground and Airborne Radio System) and **HAVE QUICK** radios to prevent jamming and interception.
    *   *Hop Rate:* SINCGARS hops ~100 times per second.
    *   *Requirements:* Stations must be synchronized in **Time** (Time of Day) and **Hopset** (Frequency allocation/[[Station Accessories|Key]]).
*   **Amateur Use**: 219-220 MHz (1.25m band) and 902 MHz+ (33cm).

### 2. Direct Sequence (DSSS)
The signal is mixed with a high-speed pseudorandom code sequence (chipping code) before transmission.
*   **Effect**: The signal appears as wideband noise to a receiver without the correct code.
*   **Gain**: "Processing Gain" allows recovery of the signal even if it is below the noise floor.
*   **Example**: Wi-Fi (802.11b), GPS, and amateur Mesh Networks ([[Modern Digital Modes|AREDN]]).

## Advantages
1.  **[[Mixing Products (Interference)|Interference]] Rejection**: Narrowband interference (jammers) affects only a small fraction of the spread signal.
2.  **Low Probability of Intercept (LPI)**: Signals look like noise to unauthorized listeners.
3.  **Multiple Access (CDMA)**: Multiple users can share the same frequency band simultaneously using different codes.

## Related
*   [[Electronic Warfare (Jamming)]]
*   [[Modern Digital Modes]]
*   [[Bandwidth]]
