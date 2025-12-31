# Software Defined Radio (SDR)

A Software Defined Radio (SDR) is a radio communication system where components that have been traditionally implemented in hardware (e.g., mixers, [filters](../03_circuits/03_Filters_&_Resonance.md), amplifiers, modulators/demodulators, detectors) are instead implemented by means of software on a personal computer or embedded system.

## Architecture
Traditional radios use analog hardware ([Superheterodyne Receiver](02_Superheterodyne_Receiver.md)). SDRs use mathematics.
1.  **RF Front End**: [Antenna](../10_safety/03_Antenna_&_Tower_Safety.md) and simple band-pass filter.
2.  **[ADC](../01_electricity/39_Digital_Processing_Techniques.md) (Analog-to-Digital Converter)**: Digitizes the incoming RF signal directly (Direct [Sampling](../01_electricity/40_Sampling_Theory.md)) or after down-conversion.
3.  **[Digital Signal Processing (DSP)](../01_electricity/38_Digital_Signal_Processing_DSP.md)**: A processor (FPGA, CPU, or [DSP](../01_electricity/38_Digital_Signal_Processing_DSP.md) chip) performs:
    *   **Filtering**: Extremely sharp digital filters.
    *   **Demodulation**: Converting I/Q data into Audio ([AM](../01_electricity/32_Analogue_Modulation_&_AM.md), [FM](../01_electricity/35_Frequency_Modulation_FM.md), [SSB](../01_electricity/34_Single_Sideband_SSB.md)) or Digital Data.
    *   **[Noise](../01_electricity/26_AC_Signals_&_Noise.md) Reduction**: Mathematical subtraction of noise.

## Advantages
*   **Visualisation**: Allows for a **Waterfall Display** or **Panadapter**, showing a wide slice of the band (spectrum) at once. You can "see" signals before you hear them.
*   **Flexibility**: Changing modes (e.g., from [FM](../01_electricity/35_Frequency_Modulation_FM.md) to [SSB](../01_electricity/34_Single_Sideband_SSB.md) to a new digital mode) is just a software update, not a soldering job.
*   **Performance**: Digital filters can have nearly perfect "brick-wall" shapes, rejecting adjacent interference better than analog crystal filters.

## Common SDRs
*   **RTL-SDR**: Low-cost USB dongles (originally TV tuners) used as wideband receivers.
*   **Direct Sampling Transceivers**: Modern ham radios (e.g., Icom IC-7300) where the SDR technology is built into a standalone box.
*   **WebSDR**: Receivers connected to the internet allowing multiple users to listen and tune independently via a web browser.

---
[< Back to Section Index](README.md)