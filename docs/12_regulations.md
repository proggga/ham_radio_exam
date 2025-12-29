# Eindterm 12: Regulations (Regelgeving)

## Licensing in the Netherlands
Amateur radio operators enjoy a unique privilege: they are permitted to construct, modify, and operate transmitting equipment without requiring individual type approval for every device. This freedom comes with the responsibility to ensure that their transmissions do not cause interference to other radio services (such as aviation, emergency services, or broadcasting). To demonstrate the necessary technical and regulatory knowledge, aspiring amateurs must pass an exam.

### License Levels
In the Netherlands, there are two license classes, both administered by the **CBR** (Centraal Bureau Rijvaardigheidsbewijzen):
*   **N (Novice):** The entry-level license. It has lower exam requirements but fewer privileges regarding frequency bands and power output.
*   **F (Full):** The advanced license. It requires a deeper understanding of electronics and theory. Holders have access to all amateur bands and higher power limits.

### Registration and Supervision
After passing the exam, amateurs register with the **RDI** (Rijksinspectie Digitale Infrastructuur, formerly Agentschap Telecom), which is part of the Ministry of Economic Affairs. The RDI manages the frequency spectrum and issues call signs.

## Call Sign Structure
A call sign acts like a license plate for a radio station. In the Netherlands, call signs follow a specific format:
*   **PA to PI:** The standard prefix range for the Netherlands.
*   **PD:** Specifically reserved for **Novice (N)** license holders.
*   **PI:** Reserved for **organizations**, club stations, and repeaters (e.g., PI4VRZ).
*   **PA, PB, PC, PE, PF, PG, PH:** Assigned to **Full (F)** license holders.
*   **Suffix:** Typically 1 to 3 letters identifying the specific station.

- **Organisations:**
  - **ITU (International Telecommunication Union):** Allocates frequencies globally.
    - **Region 1:** Europe, Africa, Middle East, Northern Asia. (NL is here).
    - **Region 2:** Americas.
    - **Region 3:** Asia-Pacific.
  - **IARU:** International Amateur Radio Union (Lobby group).
  - **CEPT:** European Conference of Postal and Telecommunications Administrations.
  - **RDI (Rijksinspectie Digitale Infrastructuur):** Dutch regulator (formerly Agentschap Telecom).
- **Documents:**
  - **Radio Regulations (RR):** ITU treaty status.
    - **Article 25 (Amateur Service):**
      - **25.1:** International comms allowed.
      - **25.2:** Technical/Personal messages only.
      - **25.2A:** No encryption.
      - **25.3:** Emergency comms for 3rd parties (if permitted).
      - **25.5:** Morse requirement optional.
      - **25.6:** Competence verification required.
      - **25.9:** Call sign identification.
        - Requirement: Start, End, every 10 mins.
      - **25.9B:** Guest licensing.
  - **Guest Operation:** CEPT license (home call + /country).
  - **T/R 61-01:** CEPT License (Temporary operation abroad).
  - **T/R 61-02:** HAREC (Exam standard for Full license recognition).
- **Amateur Bands (NL Full License - Key Bands):**
  - **160m:** 1.810 - 1.880 MHz
  - **80m:** 3.500 - 3.800 MHz
  - **40m:** 7.000 - 7.200 MHz
  - **20m:** 14.000 - 14.350 MHz
  - **15m:** 21.000 - 21.450 MHz
  - **10m:** 28.000 - 29.700 MHz
  - **6m:** 50.000 - 52.000 MHz
  - **2m:** 144.000 - 146.000 MHz
  - **70cm:** 430.000 - 440.000 MHz
- **Service Status:**
  - **Primary:** Protected. Can claim protection from Secondary.
  - **Secondary:** No protection from Primary. Must not cause interference to Primary.
    - Example: Amateur secondary to Maritime Mobile on some 2m freqs.
- **Emission Classes (Uitzendklassen):** Format: `B B B` (Bandwidth, Signal, Info).
  - **1st Symbol (Modulation):**
    - A = AM (Double sideband).
    - J = SSB (Suppressed carrier).
    - F = FM.
    - G = PM.
  - **2nd Symbol (Signal Nature):**
    - 1 = Single channel, digital, no subcarrier (CW).
    - 2 = Single channel, digital, with subcarrier.
    - 3 = Analogue.
  - **3rd Symbol (Information):**
    - A = Aural telegraphy.
    - B = Electronic telegraphy.
    - E = Telephony (Voice).
    - F = Television (Video).
  - **Common Examples:**
    - **A1A:** CW (Morse).
    - **J3E:** SSB Voice.
    - **A3E:** AM Voice.
    - **F3E:** FM Voice.
  - **Bandwidth Designators:** H (Hz), K (kHz), M (MHz), G (GHz).
    - Example: 2K80J3E = 2.8 kHz SSB.
