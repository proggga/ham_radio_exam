# 11 Procedures

[< Back to Main Index](README.md)


# Rules & Procedures

This map covers the operational procedures, codes, and regulations for amateur radio contacts.

## The Contact (QSO)
*   **Amateur Radio Activities** - Types of operation (DX, Contesting, etc.).
*   **Standard QSO Procedure** - How to make a contact and exchange information.
*   **Call Signs** - Station identification structure.

## Reference Codes
*   **Phonetic Alphabet** - NATO alphabet for clear communication.
*   **Q-Codes** - 3-letter codes for efficient traffic (QTH, QSL, etc.).
*   **CW Abbreviations & Prosigns** - Shorthand for Morse code (73, 88, BK).

## Safety & Emergency
*   **Emergency Signals** - SOS and MAYDAY.
*   **Electrical Safety** - General safety guidelines.

## Regulatory
*   **202301011248-eindterm-10-regulations-voorschriften** - Legal regulations.

---


# Common Transceiver Controls

Understanding transceiver controls is essential for proper operation and signal quality.

## Transmitter Controls
*   **Microphone Gain (Mic Gain)**: Controls the audio level sent to the transmitter.
    *   *Excessive Gain:* Causes **distortion** and splattering (over-deviation in FM, flat-topping/splatter in SSB).
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
*   **AGC (Automatic Gain Control)**: Automatically adjusts gain to keep audio volume constant despite fading.
    *   *Settings:* Fast (CW), Slow (SSB), Off.

## Function Controls
*   **Memory**: Stores frequencies for quick recall.
*   **Scan**: Automatically searches a range of frequencies or memory channels for activity.
*   **Split**: Operates with different Transmit and Receive frequencies (essential for working DX pileups or Repeaters).
*   **Repeater Offset**: The frequency difference between input and output (e.g., 600 kHz on 2m).
*   **Tone / CTCSS**: Selects the sub-audible tone required to access repeaters.

---


# Station Setup Guidelines

Proper setup of an amateur radio station ensures safety, performance, and equipment longevity.

## 1. Power Supply Wiring
*   **Voltage Drop**: Transceivers draw high current (e.g., 20A for 100W HF). Thin wires cause voltage drop ($V = I \times R$), leading to radio malfunction or shutdown.
    *   *Rule:* Use **short, heavy-gauge** wires (e.g., AWG 12 or 10 / 4mm²).
*   **Fusing**: Fuses must be placed in **BOTH** positive and negative leads close to the power source (battery/supply).
    *   *Reason:* Prevents the equipment ground coax shield from becoming the return path if the negative lead disconnects (fire hazard).

## 2. Grounding & Bonding
*   **Safety Ground (PE)**: All metal chassis must connect to the mains Earth for electrical safety (shock protection).
*   **RF Ground**: A low-impedance path to earth for RF currents.
    *   *Method:* Connect all equipment to a common bus (copper strap) and then to a ground rod.
    *   *Avoid:* Daisy-chaining grounds (Equipment A -> Equipment B -> Ground). This creates ground loops.
    *   *Conductor:* Use **Flat Copper Strap** or braid (RF travels on the surface/skin effect). Round wire has high inductance.

## 3. Computer Interface
Digital modes (FT8, RTTY, Packet) require interfacing the radio to a computer.
*   **Audio**:
    *   Radio `Speaker/Line Out` -> PC `Line In`.
    *   PC `Line Out` -> Radio `Mic/Line In`.
*   **Control (CAT/PTT)**:
    *   **CAT (Computer Aided Transceiver)**: Allows the PC to control frequency/mode.
    *   **PTT**: Via VOX (Voice Operated), CAT command, or Serial Port (RTS/DTR) keying.
*   **Isolation**: Use **Isolation Transformers** for audio and **Optocouplers** for PTT/Keying to prevent ground loops and hum.

## 4. Antenna Positioning
*   **Clearance**: Keep antennas away from power lines (fall distance + margin).
*   **EMC**: Place antennas as far as possible from household electronics to reduce interference pickup and RFI causing issues.
*   **Feedline**: Use high-quality coax (RG-213, LMR-400) for long runs, especially at VHF/UHF.

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
    *   **Mode U/V**: Uplink on UHF (70cm), Downlink on VHF (2m).
    *   **Mode V/U**: Uplink on VHF (2m), Downlink on UHF (70cm).
*   **Transponder Modes**:
    *   **FM**: Single channel, similar to a terrestrial repeater.
    *   **Linear (SSB/CW)**: A "passband" transponder that retransmits a range of frequencies (e.g., 20-100 kHz wide). Multiple QSOs can happen simultaneously.

## Operating Procedures
1.  **Power**: Use the **minimum power** necessary. Excessive power triggers the satellite's AGC (Automatic Gain Control), reducing sensitivity for everyone else ("Alligator" - all mouth, no ears).
2.  **Tracking**: You must track the satellite's position (Azimuth and Elevation) as it moves across the sky.
3.  **Doppler Shift**: The frequency changes as the satellite moves toward (higher freq) or away (lower freq) from you.
    *   *Correction:* You must adjust your transmit/receive frequency continuously during the pass. UHF requires more correction than VHF.
    *   *Spin Fading:* Periodic signal fading caused by the rotation of the satellite and its antennas.

## International Space Station (ISS)
*   **Privileges**: Any amateur with a Technician class license (or equivalent) can contact the ISS.
*   **Modes**: FM Voice, Packet (APRS), and SSTV.

## Telemetry
*   **Beacons**: Satellites often transmit a beacon signal with health and status information.
*   **Access**: Anyone (licensed or not) is allowed to receive telemetry.

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
*   **Phonetics**: Use the Phonetic Alphabet for difficult words.
*   **Prosigns**: Use CW Abbreviations & Prosigns to manage flow (e.g., "BREAK" to interrupt for urgent traffic).

## Emergency Declarations
*   **Priority**: Emergency traffic *always* has priority over routine traffic.
*   **Tactical Call Signs**: Using functional names (e.g., "Shelter 1", "Command Post") instead of personal call signs to simplify coordination (though legal ID is still required).

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
*   **Propagation**: Lack of obstacles is good for Line-of-Sight, but lack of ground reflection hurts surface wave range.
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
*   **Obstacles**: Buildings block Line-of-Sight (VHF/UHF).
    *   *Solution:* Use retransmission (relays) or NVIS (Near Vertical Incidence Skywave) on HF.
*   **Interference**: High levels of man-made electrical noise (QRM).
*   **Concealment**: Antennas can be disguised as utility lines or clotheslines.

---