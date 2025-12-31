# Doppler Shift

Doppler Shift is the change in frequency of a wave in relation to an observer who is moving relative to the wave source.

## Mechanism
*   **Approaching Source**: Waves are compressed $\rightarrow$ Frequency **Increases** (Pitch goes up).
*   **Receding Source**: Waves are stretched $\rightarrow$ Frequency **Decreases** (Pitch goes down).

## Amateur Radio Applications
### 1. Satellites
As a Low Earth Orbit (LEO) satellite passes overhead:
*   **AOS (Acquisition of Signal)**: Satellite approaching. Frequency is **High**.
*   **TCA (Time of Closest Approach)**: Frequency is nominal.
*   **LOS (Loss of Signal)**: Satellite moving away. Frequency is **Low**.
*   **Correction**: The operator must tune the receiver *down* during the pass to follow the signal. [UHF](07_VHFUHF_Bands_6m,_2m,_70cm.md) shifts more than VHF.

### 2. EME (Moonbounce)
*   The Moon moves relative to the Earth.
*   [EME](../11_procedures.md) signals shift by several kHz at 1296 MHz.

## Formula
$$\Delta f = \frac{v}{c} \times f$$
Where $v$ is relative velocity, $c$ is speed of light, $f$ is frequency.

---
[< Back to Section Index](README.md)