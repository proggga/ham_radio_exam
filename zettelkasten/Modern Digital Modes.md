---
id: 202512310007
title: Modern Digital Modes
tags: ["ham-radio", "digital", "operating"]
created: 2025-12-31
type: permanent-note
modified: 2025-12-31
---

# Modern Digital Modes

Modern amateur radio utilizes digital encoding for both voice and data, offering features like error correction, internet linking, and weak-signal performance.

## Digital Voice (DV)
Digital voice modes digitize speech before transmission.

### 1. DMR (Digital Mobile Radio)
*   **Technology**: Uses **TDMA** (Time Division Multiple Access) to fit **two simultaneous voice conversations** (Time Slots) into one 12.5 kHz channel.
*   **Networking**: Worldwide connectivity via internet-linked repeaters.
*   **Talkgroups**: Virtual channels (ID codes) that route communications to specific groups of users (e.g., "World Wide," "North America," "Local").
*   **Code Plug**: The configuration file programmed into the radio. Contains:
    *   Frequencies and [[Repeater Operation|Repeater]] offsets.
    *   **Talkgroup IDs**.
    *   **Color Code**: A digital access code (like [[Repeater Operation|CTCSS]]) for the repeater. Must match the repeater's color code to access it.
    *   User **Radio ID** (Call sign mapping).

### 2. D-STAR (Digital Smart Technologies for Amateur Radio)
*   **Technology**: Developed by JARL (Japan). Uses GMSK modulation.
*   **Features**: Simultaneously transmits Voice and Data (GPS position, Call sign).
*   **Requirement**: You must program your **Call Sign** into the radio before transmitting.
*   **Reflectors**: Internet servers that link D-STAR repeaters.

### 3. System Fusion (C4FM)
*   **Standard**: Yaesu proprietary implementation of C4FM (4-level FSK).
*   **WIRES-X**: Internet linking network for Fusion.

## Legacy & Data Modes
### Packet Radio
*   **Protocol**: AX.25.
*   **Speed**: Typically 1200 baud (AFSK on 2m/70cm) or 9600 baud (FSK).
*   **Application**: Sending error-corrected data packets.

### APRS (Automatic Packet Reporting System)
A specialized use of Packet Radio.
*   **Function**: Transmits real-time data:
    *   **GPS Location**: Position tracking of mobile stations.
    *   **Telemetry**: Weather station data (Wind, Temp).
    *   **Messages**: Short text messages.
*   **Frequency**: 144.800 MHz (Europe) / 144.390 MHz (USA).

## Weak Signal Data Modes (WSJT-X)
Designed for communication with extremely weak signals (often below the noise floor).

### FT8 (Franke-Taylor design, 8-FSK)
*   **Characteristics**: 15-second transmit intervals.
*   **Synchronization**: Requires precise computer clock time (< 1 second error).
*   **Automation**: QSOs are semi-automated (structured exchange of signal report and location).
*   **[[Bandwidth]]**: Very narrow (50 Hz), allowing many stations to operate in a small slice of the band.

## Infrastructure
*   **Hotspots**: Personal low-power access points (e.g., Raspberry Pi + RF hat) that connect a digital handheld radio to global networks via the user's home internet.
*   **Linking (RoIP)**: Connecting radios via the internet.
    *   **EchoLink**: Allows licensed amateurs to communicate via PC/Smartphone or DTMF-controlled repeaters.
    *   **IRLP (Internet Radio Linking Project)**: Connects repeaters globally via the internet.
*   **Mesh Networking (AREDN)**:
    *   Uses repurposed Wi-Fi hardware (2.4 GHz, 5.8 GHz) with custom amateur firmware.
    *   Creates a high-speed, self-healing data network independent of the commercial internet.
    *   Used for emergency data (video, VoIP, files).

## Related
*   [[Digital Transmission]]
*   [[Modulation & Digital Signals]]
*   [[Station Setup Guidelines]]
