# Eindterm 6: Antennas and Transmission Lines (Antennes en transmissielijnen)

### 6.1 Antenna Types (Antennetypen)
- **Isotropic Radiator (Isotrope straler):** Theoretical point source radiating equally in all directions (Sphere). 0 dBi.
- **Dipole:** Total length approx half-wavelength (1/2 lambda). Impedance approx 73 Ohm (free space).
  - **Voltage/Current:** Low Voltage / High Current at center (Low Z). High Voltage / Low Current at ends (High Z).
  - **Velocity Factor:** Actual length slightly shorter (x 0.95 or 0.98).
  - **Inverted V:** Center elevated, ends drooping. Lower radiation angle, less space.
  - **Trap Dipole:** Uses LC traps for multiband operation.
  - **Folded Dipole:** Impedance approx 300 Ohm. Bandwidth wider than simple dipole.
- **Ground Plane (GP):** Quarter-wave vertical element + radials. Impedance approx 36 Ohm (horiz. radials) to 50 Ohm (drooping radials). Omni-directional. Vertically polarised.
- **Vertical Monopole:** Quarter-wave with ground plane acting as mirror (creates image).
- **Loop Antenna:** Small loop (< lambda/10, low R_rad), Large loop (~1 lambda, efficient).
- **Yagi-Uda:** Beam antenna. Driven element + Reflector (approx 5% longer) + Directors (approx 5% shorter). High Gain, high Front-to-Back ratio.
- **End-fed (Zepp):** Voltage fed (High Z). Requires tuner or transformer (1:49 or 1:64 typical).
- **Dummy Load (Kunstantenne):** Non-radiating 50 Ohm resistor (Carbon, not wirewound) for testing.

### 6.2 Properties (Antenne-eigenschappen)
- **Velocity Factor (Antennas):** Physical length = lambda * VF.
  - Relevant for: End-fed, Coax-loaded antennas, Traps.
- **Reciprocity:** Antenna characteristics are identical for TX and RX.
- **Gain:**
  - **dBi:** Gain vs Isotropic radiator.
  - **dBd:** Gain vs Dipole. (dBd = dBi - 2.15).
  - **ERP (Effective Radiated Power):** Power relative to a Dipole. P_out - Losses + Gain(dBd).
  - **EIRP:** Power relative to Isotropic. P_out - Losses + Gain(dBi).
  - **Radiation Resistance (R_rad):** Equivalent resistance representing radiated power.
    - Low R_rad -> Poor efficiency (Short antennas).
  - **Efficiency:** eta = R_rad / (R_rad + R_loss).
- **Front-to-Back Ratio (Voor-achter verhouding):** Ratio of signal strength front vs back (in dB).
- **Beamwidth:** Angle between -3dB (half power) points on main lobe.
- **Near Field vs Far Field:**
  - **Near Field:** Reactive zone close to antenna. E and H fields not orthogonal.
  - **Far Field:** Radiating zone. Starts at approx 2 * D^2 / lambda (where D is antenna dimension).

### 6.3 Transmission Lines (Transmissielijnen)
- **Coaxial Cable:** Asymmetric (Unbalanced). Core + Shield. (RG58, RG213). Z0 = 50 Ohm or 75 Ohm.
  - **Velocity Factor (Verkortingsfactor, VF):** Speed of signal in cable / c.
    - Solid PE (Polyethylene): VF approx 0.66.
    - Foam PE: VF approx 0.80 - 0.82.
  - **Air/PTFE:** VF higher (>0.9).
  - **Skin Depth:** delta = sqrt(2 * rho / (omega * mu)). Depth where current falls to 37%.
  - **Attenuation:** Increases with frequency and SWR.
- **Open Wire (Kippenladder):** Symmetric (Balanced). Low loss. Z0 approx 300-600 Ohm. High VF (~0.95).
- **Impedance Transformation:**
  - **1/4 wave line:** Inverts impedance (Short -> Open, Open -> Short). Transformer: Z_in * Z_out = Z0^2.
  - **1/2 wave line:** Repeats impedance. Inverts phase.
- **Balun:** **Bal**anced to **Un**balanced.
  - **Choke Balun:** Mantelstroomfilter (Ferrite beads/coils).
    - Stops **Common-mode current** on outside of coax shield.
    - Causes: RF in shack, Pattern distortion, EMC issues.
  - **Transformer Balun:** 1:1 (Isolation), 1:4 (Impedance up/down).
- **SWR (Standing Wave Ratio):** Ratio of V_max / V_min on the line.
  - **SWR = 1:** Perfect match (Z_load = Z0). No reflection.
  - **Formula:** SWR = (1 + |Gamma|) / (1 - |Gamma|), where Gamma = (Z_L - Z0) / (Z_L + Z0).
  - **Power Loss:** Depends on both SWR and Line Loss.
  - **Return Loss:** Power reflected (dB). High return loss = Good match.
  - **Antenna Tuner (ATU):** Matches Transmitter to Feeder. **Does NOT fix SWR on the feeder line.** Only makes the TX happy.
- **Smith Chart:** Graphical impedance matching tool.
  - **Uses:** SWR visualization, Stub matching, Complex impedance transformation.
