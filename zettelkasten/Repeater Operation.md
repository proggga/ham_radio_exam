---
id: 202512311300
title: Repeater Operation
tags: ["ham-radio", "operating", "VHF", "UHF"]
created: 2025-12-31
type: permanent-note
modified: 2025-12-31
---

# Repeater Operation

Repeaters are automated stations that receive a signal on one frequency and simultaneously retransmit it on another frequency at higher power. They extend the range of portable and mobile stations, often allowing communications over 50 miles or more.

## Basic Operation
*   **Duplex**: Repeaters operate in duplex mode. They listen on an **Input** frequency and transmit on an **Output** frequency.
*   **Offset (Shift)**: The difference between the input and output frequencies.
    *   **2 meters ([[VHFUHF Bands (6m, 2m, 70cm)|VHF]])**: Usually **600 kHz** (0.6 MHz).
    *   **70 cm ([[VHFUHF Bands (6m, 2m, 70cm)|UHF]])**: Usually **5 MHz**.
    *   **Direction**: Can be Positive (+) or Negative (-).
    *   *Example:* Output 146.940 MHz minus 0.6 MHz offset = Input 146.340 MHz.

## Access Tones
To prevent interference, repeaters often require a specific low-frequency audio tone to be present on the signal to "open" the receiver squelch.
1.  **CTCSS (Continuous Tone-Coded [[Common Transceiver Controls|Squelch]] System)**: Also known as **PL Tone** (Private Line). Sub-audible tones (e.g., 100.0 Hz).
2.  **DCS (Digital Coded [[Common Transceiver Controls|Squelch]])**: A digital data stream used for the same purpose.
3.  **1750 Hz Tone (Burst)**: Common in Europe. A short audible tone burst sent to trigger the repeater.

## Protocol
*   **Listen First**: Ensure the repeater is not in use.
*   **Kerchunking**: Keying the mic briefly without speaking to check if you can hit the repeater. *Bad practice* unless you identify yourself.
*   **Identification**: You must transmit your call sign at the end of a contact and every 10 minutes (or as per local regulations).
*   **Time-Out Timer**: A safety feature that shuts off the repeater transmitter if a signal is too long (e.g., > 3 minutes). Prevents overheating if a transmitter gets stuck.
*   **Courtesy Tone**: A beep from the repeater indicating the other person has stopped transmitting and the repeater timer has reset.

## Related
*   [[VHFUHF Bands (6m, 2m, 70cm)]]
*   [[Modern Digital Modes]] ([[Modern Digital Modes|DMR]]/[[Modern Digital Modes|D-STAR]] repeaters)
*   [[Station Setup Guidelines]]
