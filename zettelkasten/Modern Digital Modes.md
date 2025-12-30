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
*   **Standard**: Commercial standard (ETSI) adopted by amateurs.
*   **TDMA**: Uses Time Division Multiple Access to allow two simultaneous conversations on one 12.5 kHz channel (Time Slot 1 & 2).
*   **Key Concepts**:
    *   **Talkgroup (TG)**: A virtual channel identifier (e.g., TG 91 for World-Wide). Users subscribe to a TG to hear traffic.
    *   **Color Code (CC)**: Similar to CTCSS. Must match the repeater's setting to access it.
    *   **Code Plug**: The radio's configuration file containing frequencies, repeaters, contacts, and talkgroups.
    *   **ID**: Uses a numeric DMR ID (not call sign) for routing.

### 2. D-STAR (Digital Smart Technologies for Amateur Radio)
*   **Standard**: Developed by JARL (Japan).
*   **FDMA**: Frequency Division Multiple Access.
*   **Key Concepts**:
    *   **Call Sign Routing**: The user's call sign is embedded in the data stream.
    *   **Reflectors**: Internet servers that link multiple repeaters together.

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
*   **Bandwidth**: Very narrow (50 Hz), allowing many stations to operate in a small slice of the band.

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
