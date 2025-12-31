# 11 Procedures

[< Back to Main Index](README.md)


# Rules & Procedures

This map covers the operational procedures, codes, and regulations for amateur radio contacts.

## The Contact (QSO)
*   **[Amateur Radio Activities](11_procedures.md)** - Types of operation (DX, Contesting, etc.).
*   **[Standard QSO Procedure](11_procedures.md)** - How to make a contact and exchange information.
*   **[Call Signs](11_procedures.md)** - Station identification structure.

## Reference Codes
*   **[Phonetic Alphabet](11_procedures.md)** - NATO alphabet for clear communication.
*   **[Q-Codes](11_procedures.md)** - 3-letter codes for efficient traffic (QTH, QSL, etc.).
*   **[CW Abbreviations & Prosigns](01_electricity/33_CW_Abbreviations_&_Prosigns.md)** - Shorthand for Morse code (73, 88, BK).

## Safety & Emergency
*   **[Emergency Signals](11_procedures.md)** - SOS and MAYDAY.
*   **[Electrical Safety](10_safety/01_Electrical_Safety.md)** - General safety guidelines.

## Regulatory
*   **[Rules & Regulations](12_regulations/03_Rules_&_Regulations.md)** - Legal regulations.

---


# Amateur Radio Activities

Amateur radio is a versatile hobby with many different aspects, allowing operators to specialize in areas that interest them most.

## Key Activities

*   **Homebrew & Experimentation**: The technical side of the hobby involving designing and building radios, antennas, and accessories.
*   **DXing**: The pursuit of contacts with distant or rare stations ("DX"). This often involves tracking solar conditions and using efficient antennas. See [The Ionosphere](07_propagation/12_The_Ionosphere.md).
*   **Contesting**: Competitive operating where the goal is to make as many contacts as possible within a set time.
    *   *Exchange:* Operators typically exchange specific information like **RST** + **Serial Number** or **Grid Locator**.
*   **Field Days**: Operating portable stations from temporary locations (e.g., open fields) to practice emergency readiness and enjoy low-noise reception away from urban QRM.
*   **Fox Hunting (Vossenjacht)**: A sport involving finding hidden transmitters using direction-finding equipment. See [Radio Direction Finding (RDF)](08_measurements/08_Radio_Direction_Finding_RDF.md).

## Grid Locators (Maidenhead)
A geographic coordinate system used by radio amateurs to succinctly describe their location.
*   **Format**: Pairs of letters and numbers (e.g., **JO22** or **JO22eb**).
    *   **Field**: 2 Letters (e.g., **JO**). Covers large area.
    *   **Square**: 2 Digits (e.g., **22**). $1^\circ$ Latitude by $2^\circ$ Longitude.
    *   **Subsquare**: 2 Letters (e.g., **eb**). More precise.
*   **Usage**: Essential for [VHF](07_propagation/07_VHFUHF_Bands_6m,_2m,_70cm.md)/UHF contesting and determining distance/bearing.

## Listening
You don't need a transmitter to participate. **WebSDR** sites (like the University of Twente's receiver) allow anyone to listen to amateur bands via a web browser. This is an excellent way to become familiar with [Standard QSO Procedure](11_procedures.md).

---


# Standard QSO Procedure

A standard contact (QSO) in amateur radio typically follows a structured format to ensure efficient communication.

## The Sequence

1.  **Calling CQ**: A general call inviting anyone to reply.
    *   Voice: "CQ CQ CQ this is PA0ABC..."
    *   [CW](01_electricity/33_CW_Abbreviations_&_Prosigns.md): "CQ CQ CQ DE PA0ABC K"
2.  **The Exchange**: Once contact is established, operators exchange essential information:
    *   **Signal Report (RST)**: Readability, Strength, and Tone.
    *   **Name & QTH**: The operator's name and location. The location is often given as a **Maidenhead Grid Locator** (e.g., JO22).
3.  **Closing**: The contact ends with "73" (Best Regards).

## Signal Reporting (RST)

The RST system is used to describe signal quality:

*   **R (Readability)**: 1 to 5 scale.
    *   1 = Unreadable
    *   5 = Perfectly readable
*   **S (Strength)**: 1 to 9 scale.
    *   1 = Faint signal
    *   9 = Very strong signal
    *   Signals stronger than S9 are reported as "S9 plus [dB](00_basic_skills.md)" (e.g., "59 + 20dB").
*   **T (Tone)**: 1 to 9 scale (CW only).
    *   1 = Very rough, broad AC note
    *   9 = Perfect sine wave

## Voice Prowords (Procedure Words)
Standard words used to clarify communication:
*   **"Over"**: I have finished speaking, expecting a reply.
*   **"Out"**: I have finished speaking, no reply expected. (Never say "Over and Out").
*   **"Roger"**: I have received and understood your last transmission.
*   **"Wilco"**: I will comply (Will Do).
*   **"Say Again"**: Please repeat.
*   **"Break"**: I am interrupting (often for emergency or urgent traffic).
*   **"Standby"**: Wait a moment.

## QSL Cards
A **QSL card** is a written confirmation of a radio contact.
*   **Physical Cards**: Often sent via a **QSL Bureau** or direct mail.
*   **Digital**: Services like **Logbook of the World (LoTW)** or **eQSL** provide electronic confirmation.

---


# Call Signs

A call sign is the unique identifier for an amateur radio station.

## Structure
A standard amateur call sign consists of:
1.  **Prefix**: Indicates the country (e.g., PA, K, G, JA).
2.  **Number**: Usually indicates a region or license class (e.g., 0-9).
3.  **Suffix**: Unique identifier for the station (1-3 letters).

## Dutch Call Signs (Netherlands)
*   **Assigned Series:** **PA** to **PI**.
*   **Full License (F-Registration):**
    *   **PA, PB, PC, PE, PF, PG, PH** followed by a number (0-5, 7-9).
    *   Suffix: 1 to 3 letters.
*   **Novice License (N-Registration):**
    *   **PD** followed by a number (0-5, 7-9).
*   **Special Use (Verenigingen/Contest):**
    *   **PI** followed by a number (usually 4 for societies).
    *   Number **6** is often used for special events/contests.
*   **Caribbean [Netherlands](12_regulations/07_Operating_Rules_Netherlands.md):** **PJ** (e.g., PJ2, PJ4).
*   **Suriname:** **PZ**.

## Forbidden Suffixes
Certain combinations are not issued to avoid confusion:
*   **SOS** (Distress signal).
*   **QOA** to **QUZ** (Q-codes).

## Operating Abroad / Special Conditions
*   **Visitor in NL:** Uses home call prefixed with **PA/** (Full) or **PD/** (Novice). Example: `PA/DL1ABC`.
*   **Portable:** `/P` (Portable) - Operating away from the home station.
*   **Mobile:** `/M` (Mobile) - Operating from a vehicle.
*   **Maritime Mobile:** `/MM` - Operating from a vessel at sea.
*   **Aeronautical Mobile:** `/AM` - Operating from an aircraft.

See [Rules & Procedures](11_procedures.md) for broader rules.

---


# Phonetic Alphabet

The NATO phonetic alphabet is used internationally to spell out call signs and names clearly, especially when signals are weak or interference is present.

| Letter | Word     | Letter | Word     |
| :---   | :---     | :---   | :---     |
| **A**  | Alfa     | **N**  | November |
| **B**  | Bravo    | **O**  | Oscar    |
| **C**  | Charlie  | **P**  | Papa     |
| **D**  | Delta    | **Q**  | Quebec   |
| **E**  | Echo     | **R**  | Romeo    |
| **F**  | Foxtrot  | **S**  | Sierra   |
| **G**  | Golf     | **T**  | Tango    |
| **H**  | Hotel    | **U**  | Uniform  |
| **I**  | India    | **V**  | Victor   |
| **J**  | Juliett  | **W**  | Whiskey  |
| **K**  | Kilo     | **X**  | X-ray    |
| **L**  | Lima     | **Y**  | Yankee   |
| **M**  | Mike     | **Z**  | Zulu     |

## Usage
When identifying, spell your call sign phonetically:
*   *PA0ABC* becomes **Papa Alfa Zero Alfa Bravo Charlie**.

---


# Q-Codes

Q-codes are three-letter codes starting with Q. They were originally developed for telegraphy to save time but are widely used in voice communications as well.

A question mark after the code turns it into a question.

## Common Q-Codes (Exam Topic)

| Code | Question (?) | Answer / Advice | Mnemonic |
| :--- | :--- | :--- | :--- |
| **QRA** | What is the name of your station? | The name of my station is... | |
| **QRG** | Will you tell me my exact frequency? | Your exact frequency is... | |
| **QRK** | What is the readability of my signals? | The readability of your signals is (1-5). | **K**waliteit |
| **QRL** | Are you busy? | I am busy. | |
| **QRM** | Is my transmission being interfered with? | You are being interfered with (**Man-made**). | **M**an-made |
| **QRN** | Are you troubled by static? | I am troubled by static (**Natural/Atmospheric**). | **N**atural |
| **QRO** | Shall I increase transmitter power? | Increase transmitter power. | **O**phogen |
| **QRP** | Shall I decrease transmitter power? | Decrease transmitter power (Low power). | **P**etty (Small) |
| **QRT** | Shall I stop sending? | Stop sending (Closing down). | s**T**op |
| **QRV** | Are you ready? | I am ready. | a**V**ailable |
| **QRX** | When will you call me again? | Call me again at ... (Wait). | **X** (Time/Cross) |
| **QRZ** | Who is calling me? | You are being called by... | **Z**ijt gij? |
| **[QSB](07_propagation/16_Fading_QSB.md)** | Are my signals fading? | Your signals are fading. | **S**lenk en **B**ult |
| **QSL** | Can you acknowledge receipt? | I acknowledge receipt (Confirm contact). | **L**ezen |
| **QSO** | Can you communicate with ...? | I can communicate with ... (Contact). | **O**ver |
| **QSY** | Shall I change frequency? | Change frequency to ... | Zwaa**Y** |
| **QTH** | What is your position/location? | My position/location is... | **H**ome |

## Usage Note
In voice operation, these are often used as nouns or verbs: "I have a lot of QRM here" or "Let's QSY to 14.250".

---


# Emergency Signals

Emergency signals have absolute priority over all other communications.

## Telegraphy (CW)
*   **SOS**: `... --- ...` (Save Our Souls).
*   Sent as a single continuous sequence without spaces between letters.

## Telephony (Voice)
*   **MAYDAY**: From French "m'aidez" (help me).
*   Used only when there is grave and imminent danger to life or vessel.

## Amateur Radio Emergency Communication
In times of disaster, amateur radio operators may form emergency networks (e.g., ARES, RAYNET) to provide communications when standard infrastructure fails.

See [Electrical Safety](10_safety/01_Electrical_Safety.md) for personal safety guidelines.

---


# Repeater Operation

Repeaters are automated stations that receive a signal on one frequency and simultaneously retransmit it on another frequency at higher power. They extend the range of portable and mobile stations, often allowing communications over 50 miles or more.

## Basic Operation
*   **Duplex**: Repeaters operate in duplex mode. They listen on an **Input** frequency and transmit on an **Output** frequency.
*   **Offset (Shift)**: The difference between the input and output frequencies.
    *   **2 meters (VHF)**: Usually **600 kHz** (0.6 MHz).
    *   **70 cm (UHF)**: Usually **5 MHz**.
    *   **Direction**: Can be Positive (+) or Negative (-).
    *   *Example:* Output 146.940 MHz minus 0.6 MHz offset = Input 146.340 MHz.

## Access Tones
To prevent interference, repeaters often require a specific low-frequency audio tone to be present on the signal to "open" the receiver squelch.
1.  **CTCSS (Continuous Tone-Coded Squelch System)**: Also known as **PL Tone** (Private Line). Sub-audible tones (e.g., 100.0 Hz).
2.  **DCS (Digital Coded Squelch)**: A digital data stream used for the same purpose.
3.  **1750 Hz Tone (Burst)**: Common in Europe. A short audible tone burst sent to trigger the repeater.

## Protocol
*   **Listen First**: Ensure the repeater is not in use.
*   **Kerchunking**: Keying the mic briefly without speaking to check if you can hit the repeater. *Bad practice* unless you identify yourself.
*   **Identification**: You must transmit your call sign at the end of a contact and every 10 minutes (or as per local regulations).
*   **Time-Out Timer**: A safety feature that shuts off the repeater transmitter if a signal is too long (e.g., > 3 minutes). Prevents overheating if a transmitter gets stuck.
*   **Courtesy Tone**: A beep from the repeater indicating the other person has stopped transmitting and the repeater timer has reset.

---


# Common Transceiver Controls

Understanding transceiver controls is essential for proper operation and signal quality.

## Transmitter Controls
*   **Microphone Gain (Mic Gain)**: Controls the audio level sent to the transmitter.
    *   *Excessive Gain:* Causes **distortion** and splattering (over-deviation in [FM](01_electricity/35_Frequency_Modulation_FM.md), flat-topping/splatter in [SSB](01_electricity/34_Single_Sideband_SSB.md)).
*   **Power Output**: Adjustable power level. Use the minimum power necessary to maintain contact.
*   **VOX (Voice Operated Exchange)**: Automatically switches to transmit when you speak.
    *   *Anti-VOX:* Prevents speaker audio from tripping the VOX.
*   **PTT (Push-to-Talk)**: Manual switch to transmit.

## Receiver Controls
*   **VFO (Variable Frequency Oscillator)**: The main tuning dial used to select frequency.
*   **Volume (AF Gain)**: Controls audio loudness.
*   **Squelch**: Mutes the audio when no signal is present.
    *   *Adjustment:* Set just above the noise threshold.
    *   *Too High:* Weak signals are blocked.
    *   *Too Low:* Constant static noise.
*   **RIT / Clarifier (Receiver Incremental Tuning)**: Changes the *receive* frequency without changing the *transmit* frequency.
    *   *Use:* To tune in a station that is slightly off-frequency (e.g., voice sounds like Donald Duck in SSB) without shifting your own transmit frequency.
*   **RF Gain**: Adjusts the sensitivity of the receiver's RF amplifier stage. Reducing it can help with strong local signals.
*   **[AGC](04_receivers/03_Automatic_Gain_Control_AGC.md) (Automatic Gain Control)**: Automatically adjusts gain to keep audio volume constant despite fading.
    *   *Settings:* Fast ([CW](01_electricity/33_CW_Abbreviations_&_Prosigns.md)), Slow (SSB), Off.

## Function Controls
*   **Memory**: Stores frequencies for quick recall.
*   **Scan**: Automatically searches a range of frequencies or memory channels for activity.
*   **Split**: Operates with different Transmit and Receive frequencies (essential for working DX pileups or Repeaters).
*   **Repeater Offset**: The frequency difference between input and output (e.g., 600 kHz on 2m).
*   **Tone / CTCSS**: Selects the sub-audible tone required to access repeaters.

---


# Common Troubleshooting

Diagnosing and fixing common station problems is a key skill for any radio operator.

## Audio Problems

### Distorted Audio (Transmit)
*   **Over-Deviation (FM)**: Audio is too loud and clipped.
    *   *Cause:* Talking too close to the microphone or Mic Gain too high.
    *   *Fix:* Speak farther away ("Eat the mic" is bad for FM) or turn down Mic Gain.
*   **RF Feedback**: Audio sounds garbled, buzzing, or has a "motorboat" sound.
    *   *Cause:* Stray RF energy is being picked up by the microphone cable shield and getting into the audio amplifier. Common with high SWR or poor grounding.
    *   *Fix:* Install a **Ferrite Choke** on the microphone cable. Improve station [RF Ground](11_procedures.md).
*   **Low Voltage**: Audio sounds "warbly" or weak.
    *   *Cause:* Battery low or high resistance connection causing voltage drop during transmit peaks.
    *   *Fix:* Check power supply/battery and fuse holders.

### Hum (Receive/Transmit)
*   **Ground Loop**: A low-frequency hum (50/60 Hz) on the signal.
    *   *Cause:* Current flowing through the ground shield of audio cables between equipment (e.g., PC and Radio) powered from different AC outlets.
    *   *Fix:* Use **Audio Isolation Transformers** or optical isolators. Connect all equipment to a **Single Point Ground**.

## Antenna & Power Problems

### High SWR
*   **Intermittent SWR**: Readings jump around (erratic).
    *   *Cause:* Loose connection (PL-259), bad solder joint, or corroded connector.
    *   *Fix:* Wiggle cables to find the fault. Resolder or replace connectors.
*   **High SWR (Constant)**:
    *   *Cause:* Antenna detuned, water in coax, or short/open in feedline.
    *   *Fix:* Test with a **Dummy Load** at the end of the coax to rule out the cable. Check antenna dimensions.

### Mobile Noise
*   **Ignition Noise**: Popping sound varying with engine RPM.
    *   *Fix:* Use **Resistor Spark Plugs**. Turn on the radio's **Noise Blanker (NB)**.
*   **Alternator Whine**: Whine varying with engine RPM.
    *   *Fix:* Install power line filters (capacitors/chokes) on the radio's DC power lead. Connect radio power **directly to the battery**.

---


# Station Setup Guidelines

Proper setup of an amateur radio station ensures safety, performance, and equipment longevity.

## 1. Power Supply Wiring
*   **Voltage Drop**: Transceivers draw high current (e.g., 20A for 100W [HF](07_propagation/01_Propagation_Basics.md)). Thin wires cause voltage drop ($V = I \times R$), leading to radio malfunction or shutdown.
    *   *Rule:* Use **short, heavy-gauge** wires (e.g., AWG 12 or 10 / 4mm²).
*   **Fusing**: Fuses must be placed in **BOTH** positive and negative leads close to the power source (battery/supply).
    *   *Reason:* Prevents the equipment ground coax shield from becoming the return path if the negative lead disconnects (fire hazard).

## 2. Grounding & Bonding
Proper grounding serves two distinct purposes: **Electrical Safety** and **RF Performance**.

### Safety Ground (Protective Earth - PE)
*   **Purpose**: Protects the operator from electrical shock if a high-voltage wire touches the chassis.
*   **Connection**: The Green/Yellow wire in the mains cord connects the metal chassis to the building's Earthing system.
*   **Never disconnect** the safety ground to solve noise problems.

### RF Ground
*   **Purpose**: Provides a low-impedance return path for RF currents, prevents "hot chassis" (RF burns), and improves antenna efficiency (especially for [HF](07_propagation/01_Propagation_Basics.md) verticals/long wires).
*   **Conductor**: RF flows on the surface of a conductor (**[Skin Effect](01_electricity/41_Skin_Effect.md)**). Use wide **Copper Strap** or flat braid. Round wire has high impedance (inductance) at RF.
*   **Configuration**:
    *   **Single Point Ground**: Connect all equipment to a common bus bar behind the station. Connect the bus bar to an external ground rod with a short, wide strap.
    *   **Avoid Loops**: Do not daisy-chain equipment (A -> B -> C -> Ground).
*   **Ground Rods**:
    *   Use 8-ft (2.4m) copper-clad steel rods.
    *   **Multiple Rods**: Spacing rods apart (e.g., 2x length) reduces resistance better than a single deep rod. Connect them with heavy strap.
    *   **Soil Treatment**: In poor soil, chemically treating the ground (Rock Salt, Copper Sulfate) or using a "Salt Pipe" can significantly lower resistance.

### Field Expedient Grounding (Military Tips)
*   **Soil Conductivity**: Moisture and Salinity improve grounding.
    *   *Tip:* If soil is dry, pour water and **salt** around the ground stake.
*   **Counterpoise**: In poor soil (Desert, Rock, Permafrost/Snow), a ground stake works poorly. Use a **Counterpoise** (a network of wires laid on or above the ground) to create an artificial ground plane.
*   **EMP Protection**: Disconnect antennas and ground equipment when not in use to protect against EMP (Electromagnetic Pulse) and Lightning.

## 3. Computer Interface
Digital modes ([FT8](11_procedures.md), RTTY, Packet) require interfacing the radio to a computer.
*   **Audio**:
    *   Radio `Speaker/Line Out` -> PC `Line In`.
    *   PC `Line Out` -> Radio `Mic/Line In`.
*   **Control (CAT/PTT)**:
    *   **CAT (Computer Aided Transceiver)**: Allows the PC to control frequency/mode.
    *   **PTT**: Via VOX (Voice Operated), CAT command, or Serial Port (RTS/DTR) keying.
*   **Isolation**: Use **Isolation [Transformers](02_components/10_Transformers.md)** for audio and **Optocouplers** for PTT/Keying to prevent ground loops and hum.

## 4. Antenna Positioning
*   **Clearance**: Keep antennas away from power lines (fall distance + margin).
*   **EMC**: Place antennas as far as possible from household electronics to reduce interference pickup and RFI causing issues.
*   **Feedline**: Use high-quality coax (RG-213, LMR-400) for long runs, especially at [VHF](07_propagation/07_VHFUHF_Bands_6m,_2m,_70cm.md)/UHF.

## 5. Siting (Military/Field)
*   **High Ground**: Maximizes Line-of-Sight range.
*   **Obstacles**: Avoid placing antennas near large metal structures or dense foliage (absorbs signals).
*   **Silencing**: In urban areas, hide antennas to avoid attracting attention (Stealth).

---


# Satellite Operation

Amateur radio satellites act as "repeaters in space," receiving signals on one band (Uplink) and retransmitting them on another (Downlink).

## Basic Concepts
*   **LEO (Low Earth Orbit)**: Most amateur satellites are LEO (altitude 99-1200 miles).
    *   *Pass Duration:* Short, typically 10-20 minutes.
*   **Uplink/Downlink**: The frequencies used.
    *   **Mode U/V**: Uplink on [UHF](07_propagation/07_VHFUHF_Bands_6m,_2m,_70cm.md) (70cm), Downlink on VHF (2m).
    *   **Mode V/U**: Uplink on VHF (2m), Downlink on UHF (70cm).
*   **Transponder Modes**:
    *   **[FM](01_electricity/35_Frequency_Modulation_FM.md)**: Single channel, similar to a terrestrial repeater.
    *   **Linear ([SSB](01_electricity/34_Single_Sideband_SSB.md)/[CW](01_electricity/33_CW_Abbreviations_&_Prosigns.md))**: A "passband" transponder that retransmits a range of frequencies (e.g., 20-100 kHz wide). Multiple QSOs can happen simultaneously.

## Operating Procedures
1.  **Power**: Use the **minimum power** necessary. Excessive power triggers the satellite's [AGC](04_receivers/03_Automatic_Gain_Control_AGC.md) (Automatic Gain Control), reducing sensitivity for everyone else ("Alligator" - all mouth, no ears).
2.  **Tracking**: You must track the satellite's position (Azimuth and Elevation) as it moves across the sky.
3.  **Doppler Shift**: The frequency changes as the satellite moves toward (higher freq) or away (lower freq) from you.
    *   *Correction:* You must adjust your transmit/receive frequency continuously during the pass. UHF requires more correction than VHF.
    *   *Spin [Fading](07_propagation/16_Fading_QSB.md):* Periodic signal fading caused by the rotation of the satellite and its antennas.

## International Space Station (ISS)
*   **Privileges**: Any amateur with a Technician class license (or equivalent) can contact the ISS.
*   **Modes**: FM Voice, Packet (APRS), and SSTV.

## Telemetry
*   **Beacons**: Satellites often transmit a beacon signal with health and status information.
*   **Access**: Anyone (licensed or not) is allowed to receive telemetry.

---


# Earth-Moon-Earth (EME)

Also known as **Moonbounce**, EME is a technique where radio signals are aimed at the Moon and reflected back to Earth to communicate with distant stations.

## Characteristics
*   **Path Loss**: Extremely high ($\approx 250 \text{ dB}$ round trip). Only a tiny fraction of the energy reflects off the Moon's surface.
*   **Requirements**:
    *   **High Power**: Usually legal limit (1500W).
    *   **High Gain Antennas**: Arrays of long Yagis or large Dishes.
    *   **Low Noise Preamplifiers**: Essential at the antenna to hear the weak echo.
*   **Frequencies**: Typically **50 MHz (6m)** to **10 GHz**, with **144 MHz (2m)** and **1296 MHz (23cm)** being most popular.

## Challenges
*   **Libration Fading**: Rapid fluttering of the signal caused by the Moon's "wobble" (Libration).
*   **[Doppler Shift](07_propagation/02_Doppler_Shift.md)**: The frequency changes as the Moon moves relative to the Earth.
*   **Faraday Rotation**: The polarization of the signal rotates as it passes through the ionosphere.

## Modes
*   **CW**: Traditional mode, still used.
*   **Digital (JT65 / Q65)**: Part of the **WSJT-X** suite. Designed specifically for EME to decode signals far below the noise floor.

---


# Image Modes (SSTV & ATV)

Amateur radio operators can transmit still pictures and real-time video using specialized modes.

## 1. SSTV (Slow Scan Television)
SSTV is used to transmit **still images** (like a fax) over voice-bandwidth channels.
*   **Bandwidth**: Fits within a standard 3 kHz [SSB](01_electricity/34_Single_Sideband_SSB.md) or [FM](01_electricity/35_Frequency_Modulation_FM.md) voice channel.
*   **Transmission Time**: Takes 8 to 120 seconds to send one image (depending on the mode/resolution).
*   **Technology**: Audio tones vary in frequency to represent brightness and color (FM subcarrier).
*   **Frequencies**: Popular on [20m Band](07_propagation/21_20m_Band.md) (14.230 MHz) and [2m](07_propagation/07_VHFUHF_Bands_6m,_2m,_70cm.md) FM (145.800 MHz from the **ISS**).
*   **Software**: MMSSTV, QSSTV.

## 2. ATV (Amateur Television)
ATV involves transmitting **real-time video** and audio (like broadcast TV).
*   **Fast-Scan TV (FSTV)**:
    *   **Bandwidth**: Very wide (6 MHz), similar to old analog broadcast TV (NTSC/PAL).
    *   **Bands**: Restricted to **70cm (420 MHz)** and higher frequencies because of the bandwidth requirement.
*   **Digital ATV (DATV)**: Uses digital encoding (DVB-S/DVB-T) for better quality and efficiency.

## Regulations
*   **Indecency**: Transmitting obscene or indecent images is strictly prohibited.
*   **Identification**: You must identify your station (voice or CW) periodically, even if the image contains your callsign.

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
    *   Frequencies and Repeater offsets.
    *   **Talkgroup IDs**.
    *   **Color Code**: A digital access code (like CTCSS) for the repeater. Must match the repeater's color code to access it.
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
*   **[Bandwidth](03_circuits/07_Bandwidth.md)**: Very narrow (50 Hz), allowing many stations to operate in a small slice of the band.

## Infrastructure
*   **Hotspots**: Personal low-power access points (e.g., Raspberry Pi + RF hat) that connect a digital handheld radio to global networks via the user's home internet.
*   **Linking (RoIP)**: Connecting radios via the internet.
    *   **EchoLink**: Allows licensed amateurs to communicate via PC/Smartphone or DTMF-controlled repeaters.
    *   **IRLP (Internet Radio Linking Project)**: Connects repeaters globally via the internet.
*   **Mesh Networking (AREDN)**:
    *   Uses repurposed Wi-Fi hardware (2.4 GHz, 5.8 GHz) with custom amateur firmware.
    *   Creates a high-speed, self-healing data network independent of the commercial internet.
    *   Used for emergency data (video, VoIP, files).

---


# APRS (Automatic Packet Reporting System)

APRS is a digital communications protocol for exchanging information among a large number of stations covering a large (local) area. It is a specialized application of [Packet Radio](11_procedures.md).

## Functions
*   **Position Tracking**: Mobile stations with GPS transmit their location (Latitude/Longitude), speed, and heading. displayed on maps.
*   **Telemetry**: Transmission of weather data (WX stations), battery voltage, or other sensor data.
*   **Messaging**: Short text messages between stations (similar to SMS).
*   **Objects**: Marking locations of interest (e.g., marathon checkpoints, repeater locations) on the map.

## Technical Details
*   **Protocol**: AX.25 (same as standard Packet Radio).
*   **Modulation**: AFSK (Audio Frequency Shift Keying).
*   **Baud Rate**: Typically **1200 baud** on VHF.
*   **Frequencies**:
    *   **North America**: 144.390 MHz
    *   **Europe**: 144.800 MHz
    *   **ISS**: 145.825 MHz

## Infrastructure
*   **Digipeaters**: "Digital Repeaters" that listen for packets and retransmit them to extend range.
*   **IGates (Internet Gateways)**: Stations that receive RF packets and feed them into the **APRS-IS** (Internet Service), allowing global viewing on websites like [aprs.fi](https://aprs.fi).
*   **Path**: A setting in the packet that determines how many hops (digipeaters) the packet should take (e.g., `WIDE1-1, WIDE2-1`).

---


# Spread Spectrum & Frequency Hopping

Spread Spectrum techniques spread a signal over a wide bandwidth, much larger than the minimum required to transmit the information. This provides immunity to interference and jamming.

## Techniques

### 1. Frequency Hopping (FHSS)
The carrier frequency rapidly changes (hops) according to a pseudorandom sequence known to both transmitter and receiver.
*   **Military Use**: Used in **SINCGARS** (Single Channel Ground and Airborne Radio System) and **HAVE QUICK** radios to prevent jamming and interception.
    *   *Hop Rate:* SINCGARS hops ~100 times per second.
    *   *Requirements:* Stations must be synchronized in **Time** (Time of Day) and **Hopset** (Frequency allocation/Key).
*   **Amateur Use**: 219-220 MHz (1.25m band) and 902 MHz+ (33cm).

### 2. Direct Sequence (DSSS)
The signal is mixed with a high-speed pseudorandom code sequence (chipping code) before transmission.
*   **Effect**: The signal appears as wideband noise to a receiver without the correct code.
*   **Gain**: "Processing Gain" allows recovery of the signal even if it is below the noise floor.
*   **Example**: Wi-Fi (802.11b), GPS, and amateur Mesh Networks ([AREDN](11_procedures.md)).

## Advantages
1.  **Interference Rejection**: Narrowband interference (jammers) affects only a small fraction of the spread signal.
2.  **Low Probability of Intercept (LPI)**: Signals look like noise to unauthorized listeners.
3.  **Multiple Access (CDMA)**: Multiple users can share the same frequency band simultaneously using different codes.

---


# Emergency Operations

Amateur radio often serves as a backup communication system during disasters when standard infrastructure (phones, internet) fails.

## Net Operations
A "Net" (Network) is a gathering of stations on a specific frequency at a specific time.

### Net Control Station (NCS)
The station in charge of the net.
*   **Duties**: Calls the net to order, directs traffic, and manages the frequency.
*   **Procedure**: Stations must ask permission from the NCS before transmitting ("Directing traffic").

### Types of Nets
1.  **Directed Net**: Strict control. Stations only speak when spoken to by NCS. Used during emergencies or high-volume traffic.
2.  **Open/Free Net**: Casual. Stations can talk to each other directly.

## Traffic Handling
The passing of formal messages (radiograms) between stations.
*   **Preamble**: Header information (Message number, precedence, station of origin, check).
    *   *Check:* The count of words in the text body. Used to verify accuracy.
*   **Phonetics**: Use the [Phonetic Alphabet](11_procedures.md) for difficult words.
*   **[Prosigns](01_electricity/33_CW_Abbreviations_&_Prosigns.md)**: Use [CW Abbreviations & Prosigns](01_electricity/33_CW_Abbreviations_&_Prosigns.md) to manage flow (e.g., "BREAK" to interrupt for urgent traffic).

## Emergency Declarations
*   **Priority**: Emergency traffic *always* has priority over routine traffic.
*   **Tactical [Call Signs](11_procedures.md)**: Using functional names (e.g., "Shelter 1", "Command Post") instead of personal call signs to simplify coordination (though legal ID is still required).

## Organizations
*   **ARES (US)**: Amateur Radio Emergency Service.
*   **RACES (US)**: Radio Amateur Civil Emergency Service (Civil Defense).
*   **DARES (NL)**: Dutch Amateur Radio Emergency Service.

---


# Radio Operations in Harsh Environments

Environmental conditions significantly impact radio performance and equipment reliability.

## 1. Desert Operations
*   **Grounding**: Dry sand is a poor electrical conductor. Normal ground rods are ineffective.
    *   *Solution:* Use **Counterpoises** (wire networks on/above ground) instead of earth grounds.
*   **[Propagation](07_propagation/14_Solar_Cycle_&_Propagation.md)**: Lack of obstacles is good for Line-of-Sight, but lack of ground reflection hurts surface wave range.
*   **Equipment**:
    *   **Heat**: Electrolyte in wet batteries evaporates. Transmitters overheat.
    *   **Dust**: Clogs vents and damages moving parts. Use dust covers.
    *   **Static**: Wind-blown sand generates high static charges. Tape antenna tips to reduce corona discharge noise.

## 2. Jungle Operations
*   **Propagation**: Dense vegetation absorbs RF energy (especially vertically polarized signals).
    *   *Range:* Significantly reduced.
    *   *Solution:* Use **Horizontal Polarization** (Dipoles) high in trees or clearings.
*   **Equipment**:
    *   **Humidity**: Causes corrosion and fungus growth.
    *   *Solution:* Keep equipment dry, lighted (sunlight kills fungus), and use moisture/fungus-proofing paint.

## 3. Cold Weather Operations
*   **Batteries**: Capacity drops drastically in cold.
    *   *Solution:* Keep batteries warm (inside coat) until use.
*   **Cables**: Insulation becomes brittle and cracks. Handle with care.
*   **Grounding**: Frozen ground (Permafrost) has very poor conductivity.
    *   *Solution:* Use **Counterpoises** raised above the snow.
*   **Static**: Charged snow particles cause high static noise (precipitation static).

## 4. Urban Operations
*   **Obstacles**: Buildings block Line-of-Sight ([VHF](07_propagation/07_VHFUHF_Bands_6m,_2m,_70cm.md)/UHF).
    *   *Solution:* Use retransmission (relays) or [NVIS](07_propagation/10_Near_Vertical_Incidence_Skywave_NVIS.md) (Near Vertical Incidence Skywave) on [HF](07_propagation/01_Propagation_Basics.md).
*   **[Interference](09_interference/03_Mixing_Products_Interference.md)**: High levels of man-made electrical noise (QRM).
*   **Concealment**: Antennas can be disguised as utility lines or clotheslines.

---