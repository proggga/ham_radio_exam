---
id: 202501111600
title: Earthing Systems
tags: ["safety", "station-setup"]
created: 2025-01-11
type: permanent-note
modified: 2025-01-11

aliases: ["Aardingssystemen", "Aarding", "Grounding", "Earthing"]
---

# Earthing Systems

In a radio station, "Ground" refers to three distinct systems that must be handled correctly to ensure safety and performance. Confusing them is a common cause of interference and safety hazards.

## 1. Safety Earth (PE - Protective Earth)
*   **Purpose**: Electrical Safety. Protects people from electrocution if a mains fault occurs (e.g., live wire touches the chassis).
*   **Connection**: The Green/Yellow wire in the mains cord.
*   **Standard**: Must meet local electrical codes (NEN 1010 in Netherlands).
*   **Rule**: All metal chassis of mains-powered equipment (Class I) **MUST** be connected to Safety Earth.

## 2. RF Ground (Counterpoise)
*   **Purpose**: Radio Performance. Provides a return path for RF currents, especially for unbalanced antennas (Verticals, End-feds).
*   **Issue**: A long ground wire acts as an antenna. If the wire length is $\lambda/4$ (or odd multiples), it presents a high impedance, meaning the "ground" at the radio is NOT at zero potential.
    *   *Symptom:* "Hot chassis" (RF burns when touching the mic/key), RFI in the shack.
*   **Solution**:
    *   Keep RF ground leads **short** ($< \lambda/10$).
    *   Use wide copper straps (low inductance) instead of round wire.
    *   Use a **Tuned Counterpoise** (artificial ground) if a short ground is impossible.

## 3. Lightning Ground
*   **Purpose**: Fire Safety and Equipment Protection. Shunts the massive energy of a lightning strike directly to earth.
*   **Connection**: Heavy gauge copper wire or strap from the tower legs and cable entry point to ground rods driven into the soil outside.
*   **Bonding**: The Lightning Ground must be **bonded** (connected) to the Safety Earth system to prevent a difference in potential (flashover) during a strike.

## Common Problems
*   **Ground Loops**: Multiple paths to ground create loops that pick up magnetic hum (50Hz mains hum).
    *   *Fix:* Star Grounding (connect all equipment to a single central bus bar, then to earth).
*   **Daisy Chaining**: Connecting Radio -> Tuner -> Power Supply -> Ground. **Bad practice.** High impedance path. Use Star Grounding.

## Related
*   [[Electrical Safety]]
*   [[Antenna & Tower Safety]]
*   [[Station Setup Guidelines]]
*   [[Mitigation]]
