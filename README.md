# HAM Radio Exam Preparation (Netherlands Full Licence / F-examen)

**🚀 SYSTEM MIGRATED TO ZETTELKASTEN**

This repository has been converted into a **Zettelkasten Knowledge System** to allow for better cross-referencing and modular study.

### 📚 Study Modes
1.  **[📖 Read the Study Guide](docs/README.md)**: A linear, book-like version generated from the notes. Best for sequential studying.
2.  **[📂 Enter Zettelkasten](zettelkasten/README.md)**: Browse the raw atomic notes, explore connections, and see the knowledge graph.

### 🧠 What is Zettelkasten?
The **Zettelkasten** (German for "Slip Box") method organizes knowledge into small, atomic notes that are linked together. It is best viewed using **[Obsidian](https://obsidian.md/)**, a powerful knowledge base tool that works on top of a local folder of Markdown files.

*   **Atomic Notes**: Each file covers one specific concept (e.g., *Ohm's Law*, *Dipole Antenna*).
*   **Connections**: Notes link to related concepts (e.g., *Dipole* links to *Impedance* and *Resonance*), mimicking how the brain works.
*   **Maps of Content (MOC)**: Index files (like the Master Index below) that organize notes into topics.

---

### Archived Content
The old hierarchical documentation has been moved to `docs_archive/` for reference but is no longer the primary source.

---

## Original Objective
This repository serves as a preparation checklist for the Dutch HAM radio exam (RZAM-F).
**Structure:** Follows the official Dutch CBR exam requirements (*Eindtermen*).
**Language:** English, with key Dutch terms in parentheses `(...)`.
**Content:** Enriched with detailed explanations, formulas, and concepts from the UK Full Licence syllabus to provide a deep study guide.

**[📂 Open Master Index](zettelkasten/Master%20Index.md)** - A comprehensive list of all topics.


## [Eindterm 0: Candidate Basic Skills (Basisvaardigheden van de kandidaat)](docs/00_basic_skills.md)

- [ ] **0.1 Mathematical Skills**
  - [ ] **Standard Form / Scientific Notation:** Manipulating powers of 10.
  - [ ] **Prefixes:**
  - [ ] **Formulas:** Rearranging equations.
  - [ ] **Logarithms & Decibels:**
    - [ ] **Logarithms:** Inverse of exponentiation (10^2 = 100 -> log(100) = 2).
    - [ ] **Decibel (dB):** Logarithmic unit for ratios.
      - [ ] **Power Ratio:** dB = 10 * log(P_out / P_in).
      - [ ] **Voltage/Current Ratio:** dB = 20 * log(U_out / U_in).
  - [ ] **Trigonometry (Goniometrie):**
    - [ ] **Sine & Cosine:** Fundamental for AC analysis.
    - [ ] **Phase:** Shift between waveforms.
    - [ ] **Radians:** Natural unit of angle. 360 degrees = 2 * pi radians.
    - [ ] **Pythagoras Theorem:** a^2 + b^2 = c^2. (Used for Impedance Z = sqrt(R^2 + X^2)).
  - [ ] **Graphs:** Interpreting linear and logarithmic scales.


## [Eindterm 1: Electricity, Electromagnetism, and Radio Theory (Elektriciteitsleer, elektromagnetisme en radiotheorie)](docs/01_electricity/)

### [1.1 Conductivity (Stroomgeleiding)](docs/01_electricity/02_Atomic_Structure.md)
- [ ] **Atomic Structure:**
  - [ ] **Nucleus (Kern):** Protons (+) and Neutrons (neutral).
  - [ ] **Shell (Schil):** Electrons (-).
  - [ ] **Ion:** Atom with net charge (gained or lost electrons).
- [ ] **Materials:**
  - [ ] **Conductors (Geleiders):** Low resistance, free electrons (e.g., Copper, Silver, Gold).
  - [ ] **Semiconductors (Halfgeleiders):** Conductivity between conductor and insulator (e.g., Silicon, Germanium).
  - [ ] **Insulators (Isolatoren):** High resistance (e.g., Glass, Ceramic, Plastic).
- [ ] **Basic Quantities:**
  - [ ] **Charge (Q, Coulomb):** 1 C ≈ 6.24 x 10^18 electrons.
  - [ ] **[Current (I, Ampere)](docs/01_electricity/07_Voltage,_Current,_and_Ohm's_Law.md):** Flow of charge (Q) per time (t). Formula: I = Q / t
  - [ ] **Direction:** Technical direction (Plus to Minus) vs Electron flow (Minus to Plus).
  - [ ] **[Voltage (U, Volt)](docs/01_electricity/07_Voltage,_Current,_and_Ohm's_Law.md):** Potential difference. Energy per charge.
  - [ ] **[Resistance (R, Ohm)](docs/01_electricity/07_Voltage,_Current,_and_Ohm's_Law.md):** Opposition to current flow.
  - [ ] **[Specific Resistance (Soortelijke weerstand, rho)](docs/01_electricity/06_Resistivity_Soortelijke_Weerstand.md):**
    - [ ] rho = Specific resistance of material (Ohm-meter).
    - [ ] l = Length (m).
    - [ ] A = Cross-sectional area (m^2).
- [ ] **[Ohm's Law (Wet van Ohm)](docs/01_electricity/07_Voltage,_Current,_and_Ohm's_Law.md):**
- [ ] **[Kirchhoff's Laws (Wetten van Kirchhoff)](docs/01_electricity/13_Circuits_and_Kirchhoff's_Laws.md):**
  - [ ] **First Law (Current/Stroom):** Sum of currents entering a junction = Sum of currents leaving.
  - [ ] **Second Law (Voltage/Spanning):** Sum of EMFs = Sum of potential drops in a closed loop.
- [ ] **[Power (Vermogen) & Energy](docs/01_electricity/08_Power_and_Energy.md):**
  - [ ] Power Formula: P = U * I  (or P = I^2 * R, or P = U^2 / R). Unit: Watt.
  - [ ] Energy Formula: W = P * t. Unit: Joule or Watt-hour.
  - [ ] Battery Capacity: measured in Ampere-hours (Ah).
- [ ] **[Measurements](docs/01_electricity/12_Measurements.md):** Voltage (Parallel), Current (Series), Resistance.

### [1.2 Sources (Bronnen)](docs/01_electricity/18_Voltage_and_Current_Sources.md)
- [ ] **Voltage Source Properties:**
  - [ ] **EMF (Bronspanning/EMK):** Voltage generated by the source.
  - [ ] **Internal Resistance (Ri):** Resistance inside the battery/source.
  - [ ] **Terminal Voltage (U_klem):** U_klem = E - (I * Ri). Voltage drops under load.
  - [ ] **Short Circuit Current:** I_short = E / Ri.
- [ ] **Combinations:**
  - [ ] **Series:** Voltages add up, Internal resistance adds up.
  - [ ] **Parallel:** Capacity adds up, Voltage remains the same (identical cells only).

### [1.3 Electric Field (Elektrisch veld)](docs/01_electricity/19_Electric,_Magnetic,_and_Electromagnetic_Fields.md)
- [ ] **Concept:** Force field between charged plates.
- [ ] **Field Strength (E):** E = U / d (Voltage / distance). Unit: V/m.
- [ ] **Formulas:**
  - [ ] **Capacitor:** C = epsilon_0 * epsilon_r * A / d.
  - [ ] **Force on Charge:** F = Q * E.
- [ ] **Shielding (Afscherming):** Faraday Cage (conductive enclosure blocks static electric fields).

### [1.4 Magnetic Field (Magnetisch veld)](docs/01_electricity/19_Electric,_Magnetic,_and_Electromagnetic_Fields.md)
- [ ] **Concept:** Field around current-carrying wires and coils.
  - [ ] Right-hand grip rule.
- [ ] **Shielding:** Using high-permeability materials (e.g., Mu-metal) to divert magnetic flux. Low resistance (Copper) does NOT shield magnetic fields well.

### [1.5 Electromagnetic Field (Elektromagnetisch veld)](docs/01_electricity/19_Electric,_Magnetic,_and_Electromagnetic_Fields.md)
- [ ] **Radio Waves:** Combination of Electric (E) and Magnetic (H) fields at right angles.
- [ ] **Velocity:** c is approx 300,000,000 m/s (in vacuum).
- [ ] **Relationship:** v = f * lambda (Velocity = Frequency * Wavelength).
- [ ] **Polarisation (Polarisatie):** Defined by the orientation of the **E-field** (Horizontal, Vertical, Circular).

### [1.6 Sinusoidal Signals (Sinusvormige signalen)](docs/01_electricity/26_AC_Signals_&_Noise.md)
- [ ] **Parameters:**
  - [ ] **Amplitude (U_max):** Peak voltage.
  - [ ] **Effective/RMS Value (U_eff):** DC equivalent heating effect.
  - [ ] **Period (T):** Time for one cycle (seconds).
  - [ ] **Frequency (f):** f = 1 / T (Hertz).
  - [ ] **Phase:** Relative timing between two waves (measured in degrees or radians).
  - [ ] **Wavelength (lambda):** lambda = c / f. (Distance a wave travels in one period).
  - [ ] **Angular Frequency (omega):** omega = 2 * pi * f (radians/second).
  - [ ] **Instantaneous Voltage:** u(t) = U_max * sin(omega * t + phi).

### [1.7 Non-sinusoidal Signals (Niet-sinusvormige signalen)](docs/01_electricity/26_AC_Signals_&_Noise.md)
- [ ] **Square Wave (Blokgolf):** Fundamental frequency + odd harmonics (3f, 5f, 7f...). Amplitudes decrease as 1/n.
- [ ] **Triangle Wave (Driehoeksgolf):** Fundamental + odd harmonics. Amplitudes decrease as 1/n^2.
- [ ] **Sawtooth (Zaagtand):** Contains both even and odd harmonics.
- [ ] **Fourier Analysis:** Any complex periodic wave is a sum of sine waves (Fundamental + Harmonics).
- [ ] **DC Component:** Average voltage level.
- [ ] **Noise (Ruis):**
  - [ ] **Thermal Noise:** Pn = k * T * B (k=Boltzmann, T=Kelvin, B=Bandwidth).
  - [ ] **Shot Noise:** Generated in PN junctions.
  - [ ] **Atmospheric (QRN):** Static, Lightning.
  - [ ] **Man-made (QRM):** Machinery, Electronics.
  - [ ] Noise floor increases with bandwidth and temperature.

### [1.8 Modulated Signals (Gemoduleerde signalen)](docs/01_electricity/31_Modulation_&_Digital_Signals.md)
- [ ] **Analogue:**
  - [ ] **CW (Morse):** Keying the carrier on/off. Narrow bandwidth (~50-150 Hz).
  - [ ] **AM (Amplitude Modulation):**
    - [ ] **Modulation Depth (Modulatiediepte, m):** Ratio of audio amplitude to carrier amplitude (m = U_audio / U_carrier). m=1 (100%) is max.
    - [ ] **Sidebands (Zijbanden):** Lower Sideband (LSB) and Upper Sideband (USB).
    - [ ] **Bandwidth:** B = 2 * f_max_audio.
    - [ ] **Power:** P_total = P_carrier * (1 + m^2 / 2).
      - [ ] At 100% mod: Sidebands contain 1/3 of total power (1/6 each).
      - [ ] PEP (Peak Envelope Power) = 4 * P_carrier (at 100% mod).
  - [ ] **SSB (Enkelzijband, EZB):** Carrier and one sideband suppressed.
    - [ ] **Sideband Selection:** USB vs LSB depends on IF design / Frequency convention.
    - [ ] **Efficiency:** All power useful. Bandwidth ~2.4 - 2.7 kHz.
  - [ ] **FM (Frequency Modulation) / PM (Phase Modulation):**
    - [ ] **Deviation (Frequentiezwaai, Delta f):** Max frequency change from center.
    - [ ] **Modulation Index (m):** m = Delta f / f_mod.
    - [ ] **Bandwidth (Carson's Rule):** B = 2 * (Delta f + f_max_audio).
      - [ ] Valid for beta >= 1 (Wideband FM).
      - [ ] For NBFM (beta < 1), spectrum is narrower.
      - [ ] NBFM (Narrow Band): B ~ 12.5 kHz.
    - [ ] **Pre-emphasis / De-emphasis:** Boosting high audio frequencies before transmission and reducing them after reception to improve S/N.
    - [ ] **Capture Effect:** Stronger signal suppresses weaker co-channel signal.
      - [ ] Improves noise immunity.
      - [ ] Makes FM unsuitable for weak-signal work.
- [ ] **Digital:**
  - [ ] **Baud vs Bit rate:**
    - [ ] **Baud (Bd):** Symbol rate (changes per second).
    - [ ] **Bit rate (bps):** Information rate. Bit rate = Baud * bits_per_symbol.
  - [ ] **Types:**
    - [ ] **ASK:** Amplitude Shift Keying.
    - [ ] **FSK:** Frequency Shift Keying (RTTY).
    - [ ] **PSK:** Phase Shift Keying (BPSK, QPSK).
    - [ ] **QAM:** Quadrature Amplitude Modulation (Amplitude + Phase).
  - [ ] **Coding:**
    - [ ] **Baudot (CCITT-1):** 5-bit code (32 characters). Used in RTTY.
    - [ ] **ASCII (CCITT-5):** 7 or 8-bit code.
    - [ ] **Parity:** Error check bit.

### [1.9 Power and Energy (Vermogen en energie)](docs/01_electricity/08_Power_and_Energy.md)
- [ ] **Decibels (dB):** Logarithmic ratio.
  - [ ] Power Ratio: 10 * log(P2 / P1)
  - [ ] Voltage Ratio: 20 * log(U2 / U1)
- [ ] **Impedance Matching (Aanpassing):** Max power transfer occurs when Source Impedance = Load Impedance.
- [ ] **PEP (Peak Envelope Power):** Average power of one RF cycle at the crest of the modulation envelope.

### [1.10 Digitization (Digitalisering)](docs/01_electricity/38_Digital_Signal_Processing_DSP.md)
- [ ] **ADC / DAC:** Analogue to Digital / Digital to Analogue.
- [ ] **Sampling:** Taking snapshots of voltage.
- [ ] **Nyquist Theorem:** Sample rate must be at least **2x** the highest frequency component (fs > 2 * f_max) to avoid aliasing.
- [ ] **Aliasing:** False signals created if sampling is too slow.
- [ ] **Quantisation:** Assigning a digital value to the sample. Leads to Quantisation Noise (resolution error).
- [ ] **Filters:** Anti-alias filter (before ADC) and Reconstruction filter (after DAC).


## [Eindterm 2: Components (Componenten)](docs/02_components/)

### [2.1 Resistor (Weerstand)](docs/02_components/01_Resistors.md)
- [ ] **Function:** Limits current, dissipates heat.
- [ ] **Unit:** Ohm.
- [ ] **Types:** Fixed, Variable, Thermistors (NTC/PTC).
- [ ] **Color Code:** 4-band code for value and tolerance.
- [ ] **E-Series:** Standard values (E12, E24).

### [2.2 Capacitor (Condensator)](docs/02_components/05_Capacitors.md)
- [ ] **Function:** Stores charge in electric field.
- [ ] **Formula:** C depends on Area, Distance, Dielectric.
- [ ] **Reactance (Xc):** 1 / (2pi f C).
- [ ] **Types:** Ceramic, Electrolytic (Polarized), Variable.

### [2.3 Inductor / Coil (Spoel)](docs/02_components/09_Inductors_Spoelen.md)
- [ ] **Function:** Stores energy in magnetic field.
- [ ] **Self-Induction:** Back EMF opposes current change (Lenz).
- [ ] **Reactance (Xl):** 2pi f L.
- [ ] **Factors:** Turns squared (N^2), Core material (mu).

### [2.4 Transformers (Transformatoren)](docs/02_components/10_Transformers.md)
- [ ] **Ratio:** Voltage proportional to turns; Impedance proportional to turns squared.
- [ ] **Cores:** Laminated iron (LF), Ferrite/Toroid (HF).
- [ ] **Losses:** Eddy currents, Hysteresis, Copper loss.

### [2.5 Semiconductors (Halfgeleiders)](docs/02_components/15_Semiconductors.md)
- [ ] **Diodes:** Rectifier, Zener, Varicap, LED.
- [ ] **Transistors:**
  - [ ] **BJT:** NPN/PNP. Current controlled.
  - [ ] **FET:** JFET/MOSFET. Voltage controlled. High Input Z.
- [ ] **Configurations:** Common Emitter/Source (Gain), Follower (Buffer).

### [2.6 Active Components (Actieve Componenten)](docs/02_components/22_Tubes_&_Op-Amps.md)
- [ ] **Vacuum Tubes:** Triode, Tetrode, Pentode.
- [ ] **Op-Amps:** High gain, differential input. Inverting/Non-inverting modes.

### [2.7 Digital & Crystals](docs/02_components/25_Digital_Components_&_Crystals.md)
- [ ] **Logic Gates:** AND, OR, NOT, NAND, NOR, XOR.
- [ ] **Flip-flops:** Memory elements.
- [ ] **Crystals:** Piezoelectric effect. High stability (TCXO, OCXO).

### 3.2 Analogue Filters (Analoge filters)
- [ ] **Resonant Circuits (LC):**
  - [ ] **Series LC:**
    - [ ] Impedance **Minimal** at resonance (Z = R_loss).
    - [ ] Acts as **Acceptor/Suction** circuit (Zuigkring).
    - [ ] Below f0: Capacitive. Above f0: Inductive.
  - [ ] **Parallel LC:**
    - [ ] Impedance **Maximal** at resonance (High Z).
    - [ ] Formula (High-Q approx): Z_dyn = L / (C * R_series).
    - [ ] Acts as **Rejector/Blocking** circuit (Sperkring).
    - [ ] Below f0: Inductive. Above f0: Capacitive.
  - [ ] **Resonant Frequency:** f0 = 1 / (2 * pi * sqrt(L * C)).
- [ ] **Filter Types:**
  - [ ] Low Pass (LPF), High Pass (HPF), Band Pass (BPF), Band Stop (Notch).
  - [ ] **Q-Factor (Kwaliteitsfactor):**
    - [ ] High Q -> Sharp peak -> Narrow Bandwidth.
    - [ ] Bandwidth B = f0 / Q.
  - [ ] **Crystal Filter:** Very High Q (thousands), very narrow bandwidth.
  - [ ] **Mechanical Filter:** Used in IF stages, very high Q (hundreds), narrow bandwidth, physically vibrates.
  - [ ] **Ceramic Filter:** Piezoelectric, medium Q, IF stages.
- [ ] **Decibels in Filters:**
  - [ ] **-3dB Point:** Cut-off frequency (Half Power point, Voltage x 0.707).
  - [ ] **-60dB Point:** Used to define Shape Factor (-60dB BW / -6dB BW).

### 3.3 Power Supply (Voeding)
- [ ] **Rectification:**
  - [ ] Half-wave (1 diode), Full-wave centre-tap (2 diodes), Bridge (4 diodes).
- [ ] **Smoothing:** Large capacitor to reduce Ripple (Rimpel). 
  - [ ] Capacitor charges to U_peak, discharges during gaps.
- [ ] **Stabilisation:**
  - [ ] **Zener:** Simple parallel regulator. Series resistor R = (U_in - U_zener) / (I_zener + I_load).
  - [ ] **Series Regulator:** Zener ref + Transistor (Emitter follower) for higher current.
  - [ ] **Integrated Circuits:** 78xx (Positive), 79xx (Negative).
- [ ] **Switch Mode (SMPS):** High efficiency, small, but creates RF noise (EMC).
  - [ ] **PWM:** Pulse Width Modulation controls output voltage.

### 3.4 Amplifiers (Versterker)
- [ ] **Coupling Methods:**
  - [ ] **RC Coupling:** Resistor + Capacitor. Audio/Wideband. Cheap.
  - [ ] **LC/Choke Coupling:** Higher efficiency for RF. DC voltage on collector = V_supply.
  - [ ] **Transformer:** Impedance matching, isolation. Used in RF and Push-Pull.
- [ ] **Operating Characteristics:**
  - [ ] **Load Line (Belastingslijn):** Graphical line on characteristic curves representing the load. Intersection with device curve is the Operating Point (Werkpunt).
  - [ ] **Dissipation:** Heat loss (P = U_ce * I_c). Must stay within the **Dissipation Hyperbola** (Safe Operating Area).
- [ ] **Feedback (Terugkoppeling):**
  - [ ] **Negative Feedback (Tegenkoppeling):** Reduces gain, reduces distortion, increases bandwidth. (e.g., unbypassed emitter resistor).
  - [ ] **Positive Feedback (Meekoppeling):** Increases gain, reduces bandwidth. Used in oscillators and regenerative receivers.
- [ ] **Classes:**
  - [ ] **Class A:** Conducts 100% (360 deg). Bias in middle of linear range. High linearity, low efficiency (max 25% with resistor, 50% with transformer).
  - [ ] **Class B:** Conducts 50% (180 deg). Bias at cut-off. Push-pull needed to avoid Crossover Distortion. Efficiency max 78.5%.
  - [ ] **Class AB:** Conducts >50% but <100%. Compromise between A and B. Reduced crossover distortion.
  - [ ] **Class C:** Conducts < 50%. Pulses. High efficiency (>80%). RF PA only (requires output tank circuit to restore sine wave).
- [ ] **Distortion:** Harmonic (multiples of freq), Intermodulation (mixing of two freqs).

### 3.5 Detectors (Detector)
- [ ] **AM Detector:** Simple Diode (Envelope detector).
- [ ] **Product Detector:** For SSB/CW. Mixes incoming signal with BFO (Beat Frequency Oscillator) to recover audio.
- [ ] **FM Detector:** Discriminator, Ratio Detector.

### 3.6 Oscillators (Oscillator)
- [ ] **Condition:** Barkhausen criterion (Loop gain = 1, Phase shift = 0 or 360 degrees). Positive Feedback.
- [ ] **LC Oscillators:**
  - [ ] **Meissner:** Inductive coupling (transformer feedback).
  - [ ] **Hartley:** Inductive voltage divider (Tapped coil).
  - [ ] **Colpitts:** Capacitive voltage divider.
  - [ ] **Butler:** Crystal oscillator variant with improved stability.
  - [ ] **Clapp:** Variation of Colpitts with series capacitor for better frequency stability.
- [ ] **Crystal Oscillators:** Piezoelectric effect. High Q, high stability.
  - [ ] **Pierce:** Crystal between Base and Collector (or Gate/Drain). Acts as inductor.
  - [ ] **Overtone:** Crystal vibrates at odd harmonic (3rd, 5th). Requires LC tank to select overtone.
  - [ ] **Temperature Compensation:** TCXO (Compensated), OCXO (Oven Controlled).
- [ ] **VCO:** Voltage Controlled Oscillator. Uses Varicap (Capaciteitsdiode) to tune frequency.
- [ ] **Phase Noise:** Jitter in time domain = noise sidebands in freq domain. Critical for digital modes and receiver selectivity.

### 3.7 PLL (Phase Locked Loop)
- [ ] **Components:**
  - [ ] **Reference Oscillator:** Stable crystal oscillator.
  - [ ] **Phase Detector (Fasevergelijker):** Compares reference phase with VCO phase. Output is Error Voltage.
  - [ ] **Loop Filter (LDF):** Low pass filter to smooth error voltage. Determines lock speed and stability.
  - [ ] **VCO:** Voltage Controlled Oscillator. Frequency adjusted by error voltage.
  - [ ] **Divider:** Divides VCO frequency for comparison (in synthesizers).
- [ ] **Use:** Frequency synthesis (stable variable frequency), FM demodulation, FM generation.

### 3.8 Mixers (Mengtrap)
- [ ] **Operation:** Non-linear device combining f1 and f2.
- [ ] **Output:** Sum (f1+f2) and Difference (f1-f2), plus originals and harmonics.
- [ ] **Image Frequency (Spiegelfrequentie):** Unwanted signal that mixes to the same IF.
  - [ ] Mitigation: High IF or Double Conversion (Dubbelsuper), Preselection filters.

### 3.9 DSP (Digitale signaalverwerking)
- [ ] **Sampling:**
  - [ ] **Nyquist-Shannon Theorem:** Sample rate must be > 2 * f_max_signal to avoid aliasing.
  - [ ] **Aliasing:** High frequencies masquerading as low frequencies. Blocked by Anti-Alias Filter (Low Pass) before ADC.
- [ ] **ADC / DAC:** Analogue-to-Digital / Digital-to-Analogue Converters.
  - [ ] **Quantisation Noise:** Noise due to finite bit resolution (rounding errors).
- [ ] **DDS (Direct Digital Synthesis):** Generating sine waves from a lookup table + DAC. Fast switching, high resolution.
- [ ] **FFT (Fast Fourier Transform):** Convert Time domain signals to Frequency domain (Spectrum display).
- [ ] **Digital Filters:**
  - [ ] **FIR (Finite Impulse Response):** Stable, linear phase.
  - [ ] **IIR (Infinite Impulse Response):** Feedback used, potential instability, acts like analog filter.


## [Eindterm 3: Circuits (Schakelingen)](docs/03_circuits/)

- [ ] **Series/Parallel:** Formulas for R, C, and L.
- [ ] **Voltage Divider:** Potentiometer principles.

### [3.2 Time Constants (Tijdconstanten)](zettelkasten/Time%20Constants%20($	au$).md)
- [ ] **RC and RL:** Tau = RC or L/R.
- [ ] **Charge/Discharge:** 63% at 1 Tau.

### [3.3 Filters](docs/03_circuits/03_Filters_&_Resonance.md)
- [ ] **Types:** LPF, HPF, BPF, Notch.
- [ ] **LC Circuits:** Series (Acceptor) vs Parallel (Rejector).
- [ ] **Selectivity:** Q-factor, Crystal/Mechanical filters.

### [3.4 Power Supply (Voeding)](docs/03_circuits/09_Power_Supply.md)
- [ ] **Rectification:** Half-wave, Full-wave, Bridge.
- [ ] **Smoothing:** Reservoir capacitor.
- [ ] **Stabilisation:** Zener, Linear regulator, SMPS (Switch mode).

### [3.5 Amplifiers (Versterkers)](docs/03_circuits/14_Amplifiers.md)
- [ ] **Classes:** A, B, AB, C. Efficiency vs Linearity.
- [ ] **Feedback:** Negative (Stability) vs Positive (Oscillation).
- [ ] **Distortion:** Harmonic, Intermodulation.

### [3.6 Detectors & Oscillators](docs/03_circuits/20_Detectors,_Oscillators_&_Mixers.md)
- [ ] **Oscillators:** Hartley, Colpitts, Crystal, VCO.
- [ ] **Detectors:** Envelope (AM), Product (SSB/CW), Discriminator (FM).
- [ ] **Mixers:** Sum and Difference frequencies. Image frequency.
- [ ] **PLL:** Phase Locked Loop for synthesis.


## [Eindterm 4: Receivers (Ontvangers)](docs/04_receivers/)

### [4.1 Receiver Types (Ontvangertypen)](docs/04_receivers/01_Receiver_Types.md)
- [ ] **TRF (Rechtuit):** Simple, poor selectivity.
- [ ] **Regenerative:** High gain/selectivity, unstable.
- [ ] **Direct Conversion:** Simple for SSB/CW, audio issues.

### [4.2 Superheterodyne](docs/04_receivers/02_Superheterodyne_Receiver.md)
- [ ] **Mixing:** RF + LO = IF.
- [ ] **Image Frequency:** Major disadvantage.
- [ ] **Double Conversion:** High 1st IF (Image), Low 2nd IF (Selectivity).
- [ ] **AGC:** Automatic Gain Control.

### [4.3 Detectors (Detectoren)](docs/04_receivers/06_Detectors_Demodulators.md)
- [ ] **AM:** Envelope detector.
- [ ] **SSB/CW:** Product detector (needs BFO).
- [ ] **FM:** Discriminator, Ratio Detector, PLL.

### [4.4 Performance (Prestaties)](docs/04_receivers/07_Receiver_Performance.md)
- [ ] **Sensitivity:** SINAD, Noise Figure.
- [ ] **Selectivity:** Bandwidth, Shape Factor.
- [ ] **Dynamic Range:** Blocking, Intermodulation (IP3).
- [ ] **S-Meter:** S9 = 50 uV.


## [Eindterm 5: Transmitters (Zenders)](docs/05_transmitters/)

### [5.1 Architecture (Opbouw)](docs/05_transmitters/01_Transmitter_Architecture.md)
- [ ] **CW:** Oscillator -> Buffer -> PA.
- [ ] **FM:** VCO (Direct) or Phase Mod (Indirect). Multipliers.
- [ ] **SSB:** Audio -> Bal Mod -> Filter -> Mixer -> PA.
- [ ] **Controls:** VOX, ALC, Speech Processing.

### [5.2 Power Amplifiers (Eindtrappen)](docs/05_transmitters/02_Power_Amplifiers_and_Matching.md)
- [ ] **Linearity:** Required for SSB/AM (Class A/AB).
- [ ] **Efficiency:** Class C for FM/CW.
- [ ] **Filtering:** LPF to suppress harmonics.
- [ ] **Matching:** ATU.


## [Eindterm 6: Antennas and Transmission Lines (Antennes en transmissielijnen)](docs/06_antennas/)

### [6.1 Antenna Types (Antennetypen)](docs/06_antennas/01_Antenna_Types.md)
- [ ] **Dipole:** Half-wave, center-fed.
- [ ] **Vertical:** Ground plane, radials.
- [ ] **Directional:** Yagi-Uda (Beam), Quad.
- [ ] **Other:** End-fed, Loop, Dummy Load.

### [6.2 Characteristics (Eigenschappen)](docs/06_antennas/09_Antenna_Characteristics.md)
- [ ] **Gain:** dBi vs dBd.
- [ ] **Power:** ERP vs EIRP.
- [ ] **Radiation Resistance:** Efficiency factor.
- [ ] **Pattern:** Front-to-Back ratio, Beamwidth.

### [6.3 Transmission Lines (Transmissielijnen)](docs/06_antennas/10_Transmission_Lines.md)
- [ ] **Types:** Coax (Asymmetric) vs Open Wire (Symmetric).
- [ ] **Velocity Factor:** Signal speed in cable.
- [ ] **Transformation:** Quarter-wave lines invert impedance.

### [6.4 Matching (Aanpassing)](docs/06_antennas/15_Matching_and_SWR.md)
- [ ] **SWR:** Standing Wave Ratio.
- [ ] **Balun:** Balanced to Unbalanced (Choke vs Transformer).
- [ ] **ATU:** Antenna Tuning Unit (matches TX to line).


## [Eindterm 7: Propagation (Propagatie)](docs/07_propagation/)

### [7.1 Basics](docs/07_propagation/01_Propagation_Basics.md)
- [ ] **EM Waves:** E and H fields.
- [ ] **Polarization:** Horizontal/Vertical.
- [ ] **Inverse Square Law:** Power loss with distance.

### [7.2 Modes](docs/07_propagation/02_Propagation_Modes.md)
- [ ] **Ground Wave:** LF/MF, follows earth.
- [ ] **Sky Wave:** HF, ionospheric refraction.
- [ ] **Line of Sight:** VHF/UHF. Radio Horizon.
- [ ] **Tropospheric:** Ducting, Scatter.

### [7.3 Ionosphere](docs/07_propagation/11_The_Ionosphere.md)
- [ ] **Layers:** D (Absorbs), E, F1/F2 (Reflect).
- [ ] **Solar Cycle:** Sunspots, SFI.
- [ ] **Frequencies:** MUF, LUF, Critical Frequency.
- [ ] **Fading:** QSB causes.

### [7.4 Band Characteristics](zettelkasten/Amateur%20Radio%20Bands.md)
- [ ] **HF Bands:** 160m to 10m properties.
- [ ] **VHF/UHF:** 6m, 2m, 70cm usage.
- [ ] **Propagation:** Day vs Night, Solar Max vs Min.


## [Eindterm 8: Measurements (Metingen)](docs/08_measurements/)

### [8.1 Multimeters](docs/08_measurements/01_Multimeters_Universeelmeters.md)
- [ ] **Analogue:** Moving coil, Sensitivity (kOhm/V), Loading effect.
- [ ] **Digital:** High input impedance, ADC.
- [ ] **Technique:** Voltage (Parallel), Current (Series), Resistance (Isolated).

### [8.2 Visualization](docs/08_measurements/02_Signal_Visualization.md)
- [ ] **Oscilloscope:** Time domain (Voltage vs Time). Amplitude, Period.
- [ ] **Spectrum Analyzer:** Frequency domain (Amplitude vs Frequency). Harmonics, Bandwidth.

### [8.3 RF Measurements](docs/08_measurements/03_RF_Measurements.md)
- [ ] **SWR Meter:** Forward/Reflected power. Calibration.
- [ ] **Frequency Counter:** Gate time, Accuracy.
- [ ] **Dip Meter:** Measuring resonant frequency of unpowered circuits.
- [ ] **Dummy Load:** Non-inductive 50 Ohm load for testing.


## [Eindterm 9: Interference and Immunity (Storing en immuniteit)](docs/09_interference/)

### [9.1 Types of Interference](docs/09_interference/01_Types_of_Interference.md)
- [ ] **Receiver Overload:** Blocking (Desensitization).
- [ ] **Mixing Products:** Intermodulation ($2f_1 - f_2$), Cross-modulation.
- [ ] **Audio:** LFD (Audio Rectification). "Donald Duck" SSB, Clicks.
- [ ] **Transmitter:** Chirp, Key Clicks, Splatter.

### [9.2 Causes](docs/09_interference/06_Causes_of_Interference.md)
- [ ] **Emissions:** Harmonics, Spurious, Phase Noise.
- [ ] **Immunity:** Poor shielding, Pin 1 problem.
- [ ] **Paths:** Radiated vs Conducted (Mains, Coax shield).

### [9.3 Mitigation](docs/09_interference/07_Mitigation_Ontstoring.md)
- [ ] **Filtering:** LPF (TX), HPF (TV/Radio), Mains Filter.
- [ ] **Ferrites:** Common Mode Chokes (clamp-on/ring).
- [ ] **Decoupling:** Capacitors on audio lines.


## [Eindterm 10: Safety (Veiligheid)](docs/10_safety/)

### [10.1 Electrical Safety](docs/10_safety/01_Electrical_Safety.md)
- [ ] **Body Effects:** 10mA (Let-go), 30mA (Respiratory), 75mA (Fibrillation).
- [ ] **Mains:** Live (Brown), Neutral (Blue), Earth (Green/Yellow).
- [ ] **Protection:** Fuse (Fire), RCD (Shock, 30mA).

### [10.2 RF Safety](docs/10_safety/02_RF_Safety.md)
- [ ] **Risks:** Heating (Eyes/Testes), RF Burns.
- [ ] **SAR:** 0.08 W/kg (Public), 0.4 W/kg (Occupational).
- [ ] **Distance:** Calculation based on EIRP.

### [10.3 Equipment & Other](docs/10_safety/04_Equipment_Safety_Classes.md)
- [ ] **Classes:** Class I (Earthed), Class II (Double Insulated), Class III (SELV).
- [ ] **Lightning:** Disconnect antennas.
- [ ] **Chemical:** Lithium batteries, Beryllium Oxide (Toxic dust).
  - [ ] **Beryllium Oxide (BeO):** White ceramic in power transistors. Toxic dust if broken.
  - [ ] **Lead:** In solder. Wash hands.
  - [ ] **Etchants (Etsmiddelen):** Ferric Chloride etc. Corrosive.
- [ ] **Lightning:** Disconnect antennas during storms.


## [Eindterm 11: Rules & Procedures (Gebruiksregels)](docs/11_procedures.md)
- [ ] **Phonetic Alphabet:** Spelling callsigns (Alfa, Bravo...).
- [ ] **Q-Codes:** QTH (Location), QSL (Confirm), QRM (Interference), etc.
- [ ] **Abbreviations:** CQ, 73, DX, DE.
- [ ] **RST System:** Readability, Strength, Tone.
- [ ] **Emergency:** SOS (CW), MAYDAY (Voice). Do not obstruct genuine emergency traffic.


## [Eindterm 12: Regulations (Regelgeving)](docs/12_regulations/)

### [12.1 Organisations (Organisaties)](docs/12_regulations/01_International_Organisations.md)
- [ ] **ITU:** Radio Regulations, Regions (NL = Region 1).
- [ ] **CEPT:** Harmonisation (T/R 61-01 Guest op).
- [ ] **IARU:** Amateur interests, Band plans.
- [ ] **HAREC:** Exam standard.

### [12.2 Licensing (Machtiging)](docs/12_regulations/02_Licensing_in_the_Netherlands.md)
- [ ] **Registration:** RDI. Classes N and F.
- [ ] **Call Signs:** Prefix (PA-PH, PI, PD) + Suffix.
- [ ] **Identification:** Every 10 mins.

### [12.3 Rules (Voorschriften)](docs/12_regulations/03_Rules_&_Regulations.md)
- [ ] **Definition:** Non-commercial, self-training.
- [ ] **Status:** Primary vs Secondary (must not cause interference).
- [ ] **Emission Classes:** A1A (CW), J3E (SSB), F3E (FM).
- [ ] **Laws:** Telecommunicatiewet.


## [Eindterm 13: Conduct (Gedragsregels)](docs/13_conduct.md)
- [ ] **Social:** Be polite, helpful, tolerant.
- [ ] **Operating:** Listen before transmitting. Use minimum power.
- [ ] **Emergency:** DARES. Know when to help and when to stay clear.



## Acknowledgements (Dankwoord)
Special thanks to the **VRZA (Vereniging van Radio Zend Amateurs)** for their comprehensive course material which served as a primary resource for the detailed expansions in this guide.

*   [VRZA Cursus Radiozendamateur](https://cursus.vrza.nl/wp/2017/12/04/vrza-cursus-zendamateur-2017-2019/)
