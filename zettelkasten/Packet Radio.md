---
id: 202501111605
title: Packet Radio
tags:
  - ham-radio
  - digital
  - protocols
created: 2025-01-11
type: permanent-note
modified: 2025-01-11

aliases: ["Packet Radio", "AX.25", "AX25"]
---

# Packet Radio (AX.25)

Packet Radio is a mode of digital communication that sends data in structured bursts ("packets"). It is the foundation for modern systems like [[APRS (Automatic Packet Reporting System)|APRS]].

## 1. The Protocol: AX.25
Derived from the X.25 commercial standard, adapted for Amateur (A) Radio.
*   **Layer 2 Protocol**: Corresponds to the Data Link Layer in the OSI model.
*   **Function**: Handles addressing, error detection, and packet framing.

## 2. Frame Structure
An AX.25 frame consists of several fields:
1.  **Flag**: Start delimiter (01111110).
2.  **Destination Call**: Callsign of the receiving station.
3.  **Source Call**: Callsign of the sender.
4.  **Digipeaters**: List of repeaters to route through (optional).
5.  **Control**: Type of packet (Unnumbered Information, Connect Request, Ack, etc.).
6.  **PID**: Protocol ID (identifies Layer 3 protocol, e.g., TCP/IP or No Layer 3).
7.  **Data (Info)**: The actual message (max 256 bytes typically).
8.  **FCS (Frame Check Sequence)**: A **CRC-16** checksum for error detection.
9.  **Flag**: End delimiter.

## 3. Operation Modes
*   **Connected Mode**: A virtual circuit is established.
    *   Handshake: `CONNECT Request` -> `CONNECT Ack`.
    *   **ARQ (Automatic Repeat Request)**: Receiver sends an ACK (Acknowledgement) for every good packet. If sender gets no ACK, it retries. Guarantees error-free delivery.
*   **Unconnected (UI) Mode**: "Fire and Forget".
    *   No handshake, no ACKs.
    *   Used for **Beacons** and **[[APRS (Automatic Packet Reporting System)|APRS]]**.
    *   *Benefit:* Efficient for broadcast info. *Drawback:* No guarantee of receipt.

## 4. Hardware/Modulation
*   **TNC (Terminal Node Controller)**: The "modem" that handles the AX.25 protocol.
*   **AFSK (Audio Frequency Shift Keying)**: Common on VHF.
    *   1200 Baud (Bell 202 standard).
    *   Tones: 1200 Hz / 2200 Hz.
*   **FSK / GMSK**: Used for higher speeds (9600 baud).

## Related
*   **[[APRS (Automatic Packet Reporting System)]]**
*   **[[Digital Transmission]]**
*   **[[Error Correction Methods]]** (CRC, ARQ)
*   **[[Modern Digital Modes]]**
