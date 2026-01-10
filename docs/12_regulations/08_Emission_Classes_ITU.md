# Emission Classes (ITU)

The ITU (International Telecommunication Union) uses a standardized system to classify radio frequency signals. A full designation includes the **Bandwidth** followed by a three-character **Emission Code**.

Format: **BBBB 123**
*   **BBBB**: Bandwidth
*   **1**: Modulation Type
*   **2**: Nature of Signal (Modulating Signal)
*   **3**: Type of Information

## Bandwidth Designation (First 4 characters)
The bandwidth is expressed with 3 digits and 1 letter. The letter acts as the decimal point and indicates the unit.
*   **H** = Hz
*   **K** = kHz
*   **M** = MHz
*   **G** = GHz

**Examples:**
*   `100H` = 100 Hz
*   `2K70` = 2.70 kHz
*   `11K2` = 11.2 kHz
*   `6M00` = 6.0 MHz

## 1. First Symbol: Modulation Type
Describes the modulation of the main carrier.

| Code | Description |
| :--- | :--- |
| **A** | Amplitude [Modulation](../01_electricity/31_Modulation_&_Digital_Signals.md) (Double Sideband) |
| **C** | Vestigial Sideband |
| **F** | [Frequency Modulation](../01_electricity/35_Frequency_Modulation_FM.md) |
| **G** | Phase [Modulation](../01_electricity/31_Modulation_&_Digital_Signals.md) |
| **H** | [Single Sideband](../01_electricity/34_Single_Sideband_SSB.md), **Full** Carrier (AME) |
| **J** | [Single Sideband](../01_electricity/34_Single_Sideband_SSB.md), **Suppressed** Carrier |
| **N** | Unmodulated carrier |
| **P** | Pulse (unmodulated) |
| **R** | [Single Sideband](../01_electricity/34_Single_Sideband_SSB.md), **Reduced** or Variable Carrier |

## 2. Second Symbol: Nature of Modulating Signal
Describes the type of signal modulating the carrier.

| Code | Description |
| :--- | :--- |
| **0** | No modulating signal |
| **1** | Digital, Single channel, **No subcarrier** (Direct keying/switching) |
| **2** | Digital, Single channel, **With subcarrier** (e.g., Tone modulated) |
| **3** | Analogue, Single channel (e.g., Voice) |
| **7** | Digital, Two or more channels |
| **8** | Analogue, Two or more channels |
| **9** | Composite (Digital + Analogue) |

## 3. Third Symbol: Type of Information
Describes what is being transmitted.

| Code | Description |
| :--- | :--- |
| **N** | None |
| **A** | Telegraphy for **Aural** reception (Morse by ear) |
| **B** | Telegraphy for **Automatic** reception (RTTY, PSK, Data) |
| **C** | Facsimile (Images) |
| **D** | Data transmission, Telemetry, Telecommand |
| **E** | Telephony (Voice) |
| **F** | Television (Video) |

## Common Examples
| Designation | Description | Mode |
| :--- | :--- | :--- |
| **A1A** | [AM](../01_electricity/32_Analogue_Modulation_&_AM.md), On/Off keying, Aural | **[CW](../01_electricity/33_CW_Abbreviations_&_Prosigns.md)** (Morse) |
| **A2A** | [AM](../01_electricity/32_Analogue_Modulation_&_AM.md), Tone modulated, Aural | **MCW** (Modulated CW) |
| **A3E** | [AM](../01_electricity/32_Analogue_Modulation_&_AM.md), Analogue, Voice | **[AM](../01_electricity/32_Analogue_Modulation_&_AM.md)** |
| **C3F** | Vestigial Sideband, Video | **Analogue TV** |
| **F1B** | [FM](../01_electricity/35_Frequency_Modulation_FM.md), Direct FSK, Automatic | **RTTY (FSK)** |
| **F2B** | [FM](../01_electricity/35_Frequency_Modulation_FM.md), AFSK Subcarrier, Automatic | **RTTY (AFSK)** |
| **F3E** | [FM](../01_electricity/35_Frequency_Modulation_FM.md), Analogue, Voice | **[FM](../01_electricity/35_Frequency_Modulation_FM.md)** |
| **H3E** | [SSB](../01_electricity/34_Single_Sideband_SSB.md), Full Carrier, Voice | **Compatible AM** |
| **J2B** | [SSB](../01_electricity/34_Single_Sideband_SSB.md), PSK/AFSK, Automatic | **PSK31, RTTY (SSB)** |
| **J3E** | [SSB](../01_electricity/34_Single_Sideband_SSB.md), Suppressed Carrier, Voice | **[SSB](../01_electricity/34_Single_Sideband_SSB.md)** |
| **N0N** | Continuous unmodulated carrier (Direction Finding) | **Carrier** |
| **R3E** | [SSB](../01_electricity/34_Single_Sideband_SSB.md), Reduced Carrier, Voice | **AME** (Military) |

### Typical Bandwidths
*   **[CW](../01_electricity/33_CW_Abbreviations_&_Prosigns.md)**: `100H` (100 Hz)
*   **[SSB](../01_electricity/34_Single_Sideband_SSB.md)**: `2K70` (2.7 kHz)
*   **[AM](../01_electricity/32_Analogue_Modulation_&_AM.md)**: `6K00` (6 kHz)
*   **[FM](../01_electricity/35_Frequency_Modulation_FM.md) (Narrow)**: `11K0` (11 kHz) - 2.5 kHz deviation
*   **[FM](../01_electricity/35_Frequency_Modulation_FM.md) (Wide)**: `16K0` (16 kHz) - 5 kHz deviation

## Sideband Terminology
*   **Single Sideband Suppressed Carrier (SSB-SC)**: Commonly just called **[SSB](../01_electricity/34_Single_Sideband_SSB.md)**. The carrier and one sideband are suppressed (removed) using filters or phasing. This concentrates all power into the single information-carrying sideband, making it efficient for long-distance communication (less bandwidth, less power wasted on carrier).
*   **Double Sideband Suppressed Carrier (DSB-SC)**: Only the carrier is suppressed, but both sidebands are transmitted. It has 100% modulation efficiency but uses double the bandwidth of SSB. Used in FM stereo generation.
*   **Vestigial Sideband (VSB)**: One sideband is fully transmitted, and the other is only **partially** suppressed (about 25-30% remains). This is a compromise used in **Analogue TV** to save bandwidth while simplifying receiver design.

## Example Exam Question
**Statement 1:** A double-sideband AM transmitter transmits a music signal. The emission class is **A3C**.
**Statement 2:** Hand-keyed Morse code signals are transmitted via an FM transmitter. The emission class is **F1E**.

**Which statement is correct?**
A. Only statement 2
B. Only statement 1
C. Neither statement

**Answer:** **C (Neither)**.
*   **Why?**
    *   Statement 1: AM Music/Voice is **A3E** (E = Telephony/Sound). **A3C** is AM Facsimile (Fax).
    *   Statement 2: FM Hand-keyed Morse (Aural) is **F1A** or **F2A**. **F1E** implies FM Digital Telephony (Voice).

---
[< Back to Section Index](README.md)