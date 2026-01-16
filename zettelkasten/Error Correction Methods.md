---
id: 202501101405
title: Error Correction Methods
tags: ["digital", "modes"]
created: 2025-01-10
type: permanent-note
modified: 2025-01-10
aliases: ["ARQ", "CRC", "FEC", "Foutdetectie en -correctie"]
---

# Error Correction Methods

In digital communications, errors occur due to noise, fading, or interference. We use specific methods to detect and fix them.

## 1. Error Detection: CRC (Cyclic Redundancy Check)
*   **Mechanism**: A mathematical calculation (checksum) performed on the data packet. The result is sent along with the data.
*   **Receiver**: Calculates the CRC of the received data.
    *   If `Calculated CRC == Received CRC`, data is good.
    *   If not, the packet is corrupted.
*   **Use**: Packet Radio ([[APRS (Automatic Packet Reporting System)|APRS]]), Ethernet.
*   *Note:* CRC detects errors but **cannot fix** them.

## 2. ARQ (Automatic Repeat Request)
*   **Mechanism**: If an error is detected (e.g., via CRC or Parity), the receiver requests the transmitter to send the packet again.
*   **Pros**: 100% error-free data (eventually).
*   **Cons**: Slows down throughput on noisy channels. Requires a two-way connection (Handshake).
*   **Use**: TCP/IP, AMTOR, Packet Radio.

## 3. FEC (Forward Error Correction)
*   **Mechanism**: Redundant bits are added to the data stream. The code is mathematically designed so that the receiver can **reconstruct** the original data even if some bits are wrong.
*   **Pros**: No return channel needed (works for Broadcast). Constant throughput.
*   **Cons**: Adds overhead (more bits to send).
*   **Use**: **FT8**, **D-STAR**, Satellite Telemetry, DAB/DVB.
*   *Analogy:* Phonetic Alphabet. If you hear "Bravo", even if the 'v' is static, you know it's 'B' because of the redundancy.

## Related
*   [[Packet Radio]]
*   [[Digital Transmission]]
*   [[Modern Digital Modes]]