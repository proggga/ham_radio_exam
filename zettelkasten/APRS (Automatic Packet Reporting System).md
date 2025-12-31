---
id: 202512311230
title: APRS (Automatic Packet Reporting System)
tags: ["ham-radio", "digital", "operating", "packet"]
created: 2025-12-31
type: permanent-note
modified: 2025-12-31
---

# APRS (Automatic Packet Reporting System)

APRS is a digital communications protocol for exchanging information among a large number of stations covering a large (local) area. It is a specialized application of [[Modern Digital Modes|Packet Radio]].

## Functions
*   **Position Tracking**: Mobile stations with GPS transmit their location (Latitude/Longitude), speed, and heading. displayed on maps.
*   **Telemetry**: Transmission of weather data (WX stations), battery voltage, or other sensor data.
*   **Messaging**: Short text messages between stations (similar to SMS).
*   **Objects**: Marking locations of interest (e.g., marathon checkpoints, repeater locations) on the map.

## Technical Details
*   **Protocol**: AX.25 (same as standard Packet Radio).
*   **[[Modulation & Digital Signals|Modulation]]**: AFSK (Audio Frequency [[Repeater Operation|Shift]] Keying).
*   **Baud Rate**: Typically **1200 baud** on [[VHFUHF Bands (6m, 2m, 70cm)|VHF]].
*   **Frequencies**:
    *   **North America**: 144.390 MHz
    *   **Europe**: 144.800 MHz
    *   **ISS**: 145.825 MHz

## Infrastructure
*   **Digipeaters**: "Digital Repeaters" that listen for packets and retransmit them to extend range.
*   **IGates (Internet Gateways)**: Stations that receive RF packets and feed them into the **APRS-IS** (Internet Service), allowing global viewing on websites like [aprs.fi](https://aprs.fi).
*   **Path**: A setting in the packet that determines how many hops (digipeaters) the packet should take (e.g., `WIDE1-1, WIDE2-1`).

## Related
*   [[Modern Digital Modes]]
*   [[Satellite Operation]] (ISS uses APRS)
*   [[Emergency Operations]]
