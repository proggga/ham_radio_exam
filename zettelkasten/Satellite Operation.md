---
id: 202512310006
title: Satellite Operation
tags: ["ham-radio", "operating", "space"]
created: 2025-12-31
type: permanent-note
modified: 2025-12-31
---

# Satellite Operation

Amateur radio satellites act as "repeaters in space," receiving signals on one band (Uplink) and retransmitting them on another (Downlink).

## Basic Concepts
*   **LEO (Low Earth Orbit)**: Most amateur satellites are LEO (altitude 99-1200 miles).
    *   *Pass Duration:* Short, typically 10-20 minutes.
*   **Uplink/Downlink**: The frequencies used.
    *   **Mode U/V**: Uplink on [[VHFUHF Bands (6m, 2m, 70cm)|UHF]] (70cm), Downlink on VHF (2m).
    *   **Mode V/U**: Uplink on VHF (2m), Downlink on UHF (70cm).
*   **Transponder Modes**:
    *   **[[Frequency Modulation (FM)|FM]]**: Single channel, similar to a terrestrial repeater.
    *   **Linear ([[Single Sideband (SSB)|SSB]]/[[CW Abbreviations & Prosigns|CW]])**: A "passband" transponder that retransmits a range of frequencies (e.g., 20-100 kHz wide). Multiple QSOs can happen simultaneously.

## Operating Procedures
1.  **Power**: Use the **minimum power** necessary. Excessive power triggers the satellite's [[Automatic Gain Control (AGC)|AGC]] (Automatic Gain Control), reducing sensitivity for everyone else ("Alligator" - all mouth, no ears).
2.  **Tracking**: You must track the satellite's position (Azimuth and Elevation) as it moves across the sky.
3.  **Doppler Shift**: The frequency changes as the satellite moves toward (higher freq) or away (lower freq) from you.
    *   *Correction:* You must adjust your transmit/receive frequency continuously during the pass. UHF requires more correction than VHF.
    *   *Spin [[Fading (QSB)|Fading]]:* Periodic signal fading caused by the rotation of the satellite and its antennas.

## International Space Station (ISS)
*   **Privileges**: Any amateur with a Technician class license (or equivalent) can contact the ISS.
*   **Modes**: FM Voice, Packet (APRS), and SSTV.

## Telemetry
*   **Beacons**: Satellites often transmit a beacon signal with health and status information.
*   **Access**: Anyone (licensed or not) is allowed to receive telemetry.

## Related
*   [[VHFUHF Bands (6m, 2m, 70cm)]]
*   [[Propagation Modes]]
*   [[Doppler Shift]]
