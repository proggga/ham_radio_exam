# Eindterm 3: Circuits (Schakelingen)

### 3.1 Combinations (Combinatie van componenten)
- **Resistors:**
  - **Series:** R_total = R1 + R2. (Voltage divides, Current same).
  - **Parallel:** 1/R_total = 1/R1 + 1/R2. (Current divides, Voltage same).
    - Formula (2 resistors): R_total = (R1 * R2) / (R1 + R2).
    - **Equal Resistors:** R_total = R / n.
  - **Voltage Divider:** U_out = U_in * R2 / (R1 + R2).
  - **Wheatstone Bridge:** Measuring unknown resistance.
    - Balance condition: R1 / R2 = Rx / R3.
- **Capacitors:**
  - Series: like parallel resistors.
  - Parallel: Add up (C_total = C1 + C2).
- **Inductors:**
  - Series: Add up (L_total = L1 + L2).
  - Parallel: like parallel resistors.
- **Time Constants (tau):**
  - RC Circuit: tau = R * C (Time to charge to 63%).
  - RL Circuit: tau = L / R.
  - **Full Charge/Discharge:** 5 * tau (~99%).
- **Impedance (Z):** Vector sum of Resistance (R) and Reactance (X).
  - Series RC/RL: Z = sqrt(R^2 + X^2)
  - Parallel RC/RL: 1/Z = sqrt((1/R)^2 + (1/X)^2)


### 3.2 Analogue Filters (Analoge filters)
- **Resonant Circuits (LC):**
  - **Series LC:**
    - Impedance **Minimal** at resonance (Z = R_loss).
    - Acts as **Acceptor/Suction** circuit (Zuigkring).
    - Below f0: Capacitive. Above f0: Inductive.
  - **Parallel LC:**
    - Impedance **Maximal** at resonance (High Z).
    - Formula (High-Q approx): Z_dyn = L / (C * R_series).
    - Acts as **Rejector/Blocking** circuit (Sperkring).
    - Below f0: Inductive. Above f0: Capacitive.
  - **Resonant Frequency:** f0 = 1 / (2 * pi * sqrt(L * C)).
- **Filter Types:**
  - Low Pass (LPF), High Pass (HPF), Band Pass (BPF), Band Stop (Notch).
  - **Q-Factor (Kwaliteitsfactor):**
    - High Q -> Sharp peak -> Narrow Bandwidth.
    - Bandwidth B = f0 / Q.
  - **Crystal Filter:** Very High Q (thousands), very narrow bandwidth.
  - **Mechanical Filter:** Used in IF stages, very high Q (hundreds), narrow bandwidth, physically vibrates.
  - **Ceramic Filter:** Piezoelectric, medium Q, IF stages.
- **Decibels in Filters:**
  - **-3dB Point:** Cut-off frequency (Half Power point, Voltage x 0.707).
  - **-60dB Point:** Used to define Shape Factor (-60dB BW / -6dB BW).

### 3.3 Power Supply (Voeding)
- **Rectification:**
  - Half-wave (1 diode), Full-wave centre-tap (2 diodes), Bridge (4 diodes).
- **Smoothing:** Large capacitor to reduce Ripple (Rimpel). 
  - Capacitor charges to U_peak, discharges during gaps.
- **Stabilisation:**
  - **Zener:** Simple parallel regulator. Series resistor R = (U_in - U_zener) / (I_zener + I_load).
  - **Series Regulator:** Zener ref + Transistor (Emitter follower) for higher current.
  - **Integrated Circuits:** 78xx (Positive), 79xx (Negative).
- **Switch Mode (SMPS):** High efficiency, small, but creates RF noise (EMC).
  - **PWM:** Pulse Width Modulation controls output voltage.

### 3.4 Amplifiers (Versterker)
- **Coupling Methods:**
  - **RC Coupling:** Resistor + Capacitor. Audio/Wideband. Cheap.
  - **LC/Choke Coupling:** Higher efficiency for RF. DC voltage on collector = V_supply.
  - **Transformer:** Impedance matching, isolation. Used in RF and Push-Pull.
- **Operating Characteristics:**
  - **Load Line (Belastingslijn):** Graphical line on characteristic curves representing the load. Intersection with device curve is the Operating Point (Werkpunt).
  - **Dissipation:** Heat loss (P = U_ce * I_c). Must stay within the **Dissipation Hyperbola** (Safe Operating Area).
- **Feedback (Terugkoppeling):**
  - **Negative Feedback (Tegenkoppeling):** Reduces gain, reduces distortion, increases bandwidth. (e.g., unbypassed emitter resistor).
  - **Positive Feedback (Meekoppeling):** Increases gain, reduces bandwidth. Used in oscillators and regenerative receivers.
- **Classes:**
  - **Class A:** Conducts 100% (360 deg). Bias in middle of linear range. High linearity, low efficiency (max 25% with resistor, 50% with transformer).
  - **Class B:** Conducts 50% (180 deg). Bias at cut-off. Push-pull needed to avoid Crossover Distortion. Efficiency max 78.5%.
  - **Class AB:** Conducts >50% but <100%. Compromise between A and B. Reduced crossover distortion.
  - **Class C:** Conducts < 50%. Pulses. High efficiency (>80%). RF PA only (requires output tank circuit to restore sine wave).
- **Distortion:** Harmonic (multiples of freq), Intermodulation (mixing of two freqs).

### 3.5 Detectors (Detector)
- **AM Detector:** Simple Diode (Envelope detector).
- **Product Detector:** For SSB/CW. Mixes incoming signal with BFO (Beat Frequency Oscillator) to recover audio.
- **FM Detector:** Discriminator, Ratio Detector.

### 3.6 Oscillators (Oscillator)
- **Condition:** Barkhausen criterion (Loop gain = 1, Phase shift = 0 or 360 degrees). Positive Feedback.
- **LC Oscillators:**
  - **Meissner:** Inductive coupling (transformer feedback).
  - **Hartley:** Inductive voltage divider (Tapped coil).
  - **Colpitts:** Capacitive voltage divider.
  - **Butler:** Crystal oscillator variant with improved stability.
  - **Clapp:** Variation of Colpitts with series capacitor for better frequency stability.
- **Crystal Oscillators:** Piezoelectric effect. High Q, high stability.
  - **Pierce:** Crystal between Base and Collector (or Gate/Drain). Acts as inductor.
  - **Overtone:** Crystal vibrates at odd harmonic (3rd, 5th). Requires LC tank to select overtone.
  - **Temperature Compensation:** TCXO (Compensated), OCXO (Oven Controlled).
- **VCO:** Voltage Controlled Oscillator. Uses Varicap (Capaciteitsdiode) to tune frequency.
- **Phase Noise:** Jitter in time domain = noise sidebands in freq domain. Critical for digital modes and receiver selectivity.

### 3.7 PLL (Phase Locked Loop)
- **Components:**
  - **Reference Oscillator:** Stable crystal oscillator.
  - **Phase Detector (Fasevergelijker):** Compares reference phase with VCO phase. Output is Error Voltage.
  - **Loop Filter (LDF):** Low pass filter to smooth error voltage. Determines lock speed and stability.
  - **VCO:** Voltage Controlled Oscillator. Frequency adjusted by error voltage.
  - **Divider:** Divides VCO frequency for comparison (in synthesizers).
- **Use:** Frequency synthesis (stable variable frequency), FM demodulation, FM generation.

### 3.8 Mixers (Mengtrap)
- **Operation:** Non-linear device combining f1 and f2.
- **Output:** Sum (f1+f2) and Difference (f1-f2), plus originals and harmonics.
- **Image Frequency (Spiegelfrequentie):** Unwanted signal that mixes to the same IF.
  - Formula: f_image = f_wanted +/- (2 * IF).
  - Mitigation: High IF or Double Conversion (Dubbelsuper), Preselection filters.

### 3.9 DSP (Digitale signaalverwerking)
- **Sampling:**
  - **Nyquist-Shannon Theorem:** Sample rate must be > 2 * f_max_signal to avoid aliasing.
  - **Aliasing:** High frequencies masquerading as low frequencies. Blocked by Anti-Alias Filter (Low Pass) before ADC.
- **ADC / DAC:** Analogue-to-Digital / Digital-to-Analogue Converters.
  - **Quantisation Noise:** Noise due to finite bit resolution (rounding errors).
- **DDS (Direct Digital Synthesis):** Generating sine waves from a lookup table + DAC. Fast switching, high resolution.
- **FFT (Fast Fourier Transform):** Convert Time domain signals to Frequency domain (Spectrum display).
- **Digital Filters:**
  - **FIR (Finite Impulse Response):** Stable, linear phase.
  - **IIR (Infinite Impulse Response):** Feedback used, potential instability, acts like analog filter.
