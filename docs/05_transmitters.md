# Eindterm 5: Transmitters (Zenders)

- **Architecture:**
  - **CW:** Keying the carrier buffer.
  - **SSB:** Audio -> Balanced Modulator (creates DSB) -> Sideband Filter (selects USB/LSB) -> Mixer (to RF) -> PA.
  - **FM:** Audio -> Reactance Modulator (VCO) -> Multipliers -> PA.
  - **VOX:** Voice Operated Switch. Automatic TX/RX switching.
  - **Speech Processor:** Increases average power without increasing PEP.
  - **ALC:** Automatic Level Control. Prevents overdriving PA.
- **Power Amplifier (PA):**
  - **Linearity:** Crucial for SSB/AM to avoid splattering (Intermodulation Distortion).
  - **Low Pass Filter:** At output to suppress Harmonics.
- **Interference:**
  - **Chirp:** Unstable oscillator during keying.
  - **Key Clicks:** Rise/fall time too fast.
  - **Overmodulation:** Causes splatter (bandwidth spread).
