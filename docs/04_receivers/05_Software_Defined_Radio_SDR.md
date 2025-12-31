# Software Defined Radio (SDR)

A Software Defined Radio (SDR) is a radio communication system where components that have been traditionally implemented in hardware (e.g., mixers, [filters](../03_circuits/03_Filters_&_Resonance.md), amplifiers, modulators/demodulators, detectors) are instead implemented by means of software on a personal computer or embedded system.

## Architecture
Traditional radios use analog hardware ([Superheterodyne Receiver](02_Superheterodyne_Receiver.md)). SDRs use mathematics.
1.  **RF Front End**: Antenna and simple band-pass filter.
2.  **ADC (Analog-to-Digital Converter)**: Digitizes the incoming RF signal directly (Direct Sampling) or after down-conversion.
3.  **[Digital Signal Processing (DSP)](../01_electricity/38_Digital_Signal_Processing_DSP.md)**: A processor (FPGA, CPU, or DSP chip) performs:
    *   **Filtering**: Extremely sharp digital filters.
    *   **Demodulation**: Converting I/Q data into Audio (AM, FM, SSB) or Digital Data.
    *   **Noise Reduction**: Mathematical subtraction of noise.

## Advantages
*   **Visualisation**: Allows for a **Waterfall Display** or **Panadapter**, showing a wide slice of the band (spectrum) at once. You can "see" signals before you hear them.
*   **Flexibility**: Changing modes (e.g., from FM to SSB to a new digital mode) is just a software update, not a soldering job.
*   **Performance**: Digital filters can have nearly perfect "brick-wall" shapes, rejecting adjacent interference better than analog crystal filters.

## Common SDRs
*   **RTL-SDR**: Low-cost USB dongles (originally TV tuners) used as wideband receivers.
*   **Direct Sampling Transceivers**: Modern ham radios (e.g., Icom IC-7300) where the SDR technology is built into a standalone box.
*   **WebSDR**: Receivers connected to the internet allowing multiple users to listen and tune independently via a web browser.

---
[< Back to Section Index](README.md)