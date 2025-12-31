# Emission Classes (ITU)

ITU codes describe the characteristics of a radio signal. Format: **[Modulation](../01_electricity/31_Modulation_&_Digital_Signals.md) [Signal Nature] [Information]**.

## 1. First Symbol: Modulation Type
*   **N**: Unmodulated carrier.
*   **A**: Amplitude Modulation (Double Sideband).
*   **H**: [Single Sideband](../01_electricity/34_Single_Sideband_SSB.md), **Full** Carrier (AME).
*   **J**: Single Sideband, **Suppressed** Carrier (SSB).
*   **R**: Single Sideband, **Reduced** Carrier.
*   **C**: Vestigial Sideband (TV).
*   **F**: [Frequency Modulation](../01_electricity/35_Frequency_Modulation_FM.md) (FM).
*   **G**: Phase Modulation (PM).

## 2. Second Symbol: Signal Nature
*   **0**: No modulating signal.
*   **1**: Digital, Single channel, **No subcarrier** (Direct keying/switching).
*   **2**: Digital, Single channel, **With subcarrier** (e.g., AFSK).
*   **3**: Analogue, Single channel (e.g., Voice).

## 3. Third Symbol: Information Type
*   **N**: None.
*   **A**: Telegraphy for **Aural** reception (Morse).
*   **B**: Telegraphy for **Automatic** reception (RTTY, PSK).
*   **C**: Facsimile (Fax).
*   **D**: Data transmission, Telemetry, Packet.
*   **E**: Telephony (Voice).
*   **F**: Television (Video).

## Common Examples (Exam Topic)
| Code | Description | Mode |
| :--- | :--- | :--- |
| **A1A** | [AM](../01_electricity/32_Analogue_Modulation_&_AM.md), On/Off keying, Aural Morse | **[CW](../01_electricity/33_CW_Abbreviations_&_Prosigns.md)** |
| **A3E** | AM, Analogue, Voice | **AM** |
| **J3E** | SSB, Suppressed Carrier, Analogue Voice | **SSB** |
| **F3E** | FM, Analogue, Voice | **FM** |
| **F1A** | FM, Direct Keying, Aural Morse | **FM CW** |
| **F2A** | FM, Subcarrier (Tone), Aural Morse | **FM CW (Tone)** |
| **F1B** | FM, Direct FSK, Automatic | **RTTY (FSK)** |
| **F2B** | FM, Subcarrier AFSK, Automatic | **RTTY (AFSK)** |
| **F1D** | FM, Direct Data | **Packet/Data** |
| **J2B** | SSB, Subcarrier AFSK, Automatic | **RTTY/PSK (SSB)** |
| **G3E** | PM, Analogue, Voice | **PM** |

---
[< Back to Section Index](README.md)