# RF Measurements

This map covers the instruments used to test and maintain radio equipment.

## Transmitter Testing
*   **[SWR Meter](04_SWR_Meter.md)** - Checking antenna match.
*   **[Dummy Load](../06_antennas/11_Dummy_Load.md)** - Safe non-radiating test load.
*   **[Antenna](../10_safety/03_Antenna_&_Tower_Safety.md) Analyzer** - A handheld instrument that generates a low-power signal to measure [SWR](../06_antennas/19_Standing_Wave_Ratio_SWR.md), resistance ($R$), and reactance ($X$) of an antenna system across a range of frequencies without using a transmitter.

## Circuit Analysis
*   **[Dip Meter](05_Dip_Meter.md)** - Finding resonance of passive circuits.
*   **[Frequency Counter](06_Frequency_Counter.md)** - Measuring exact frequency.

## Receiver Testing
*   **[Signal Generator](07_Signal_Generator.md)** - Injecting test signals.

### Calculation Example: Power Measurement
**Scenario:** You measure 8 Watts on a power meter. The setup includes an attenuator (10 [dB](../00_basic_skills.md)), a disabled amplifier acting as a load (1 [dB](../00_basic_skills.md) loss), and cable/connector losses (2 [dB](../00_basic_skills.md)). What is the transmitter output power?
1.  **Total Loss/Attenuation:** $10 \text{ dB} + 1 \text{ dB} + 2 \text{ dB} = 13 \text{ dB}$.
2.  **Calculate Factor:** $13 \text{ dB} \approx 20\times$ ($10 \text{ dB} = 10\times$, $3 \text{ dB} = 2\times$, so $10 \times 2 = 20$).
3.  **Calculate Source Power:** $P_{source} = P_{measured} \times \text{Factor} = 8 \text{ W} \times 20 = 160 \text{ W}$.

---
[< Back to Section Index](README.md)