# The Superheterodyne Receiver

## 1. Principle
The "Superhet" converts any incoming RF signal to a fixed **Intermediate Frequency (IF)** (Middenfrequent) before amplification and detection.

### Block Diagram
1.  **RF Amplifier / Preselector:** Filters and amplifies the antenna signal. Improves Signal-to-Noise ratio and Image Rejection.
2.  **Mixer (Mengtrap):** Combines RF with Local Oscillator.
3.  **Local Oscillator (VFO/PLL):** Generates $f_{LO}$. Tuned so that $|f_{RF} \pm f_{LO}| = f_{IF}$.
4.  **IF Filter:** Determines the main selectivity (Bandwidth) of the receiver.
5.  **IF Amplifier:** Provides most of the receiver's gain at a fixed frequency.
6.  **Detector:** Demodulates the signal.
7.  **Audio Amplifier:** Drives the speaker.

## 2. Image Frequency (Spiegelfrequentie)
A major disadvantage of the superhet. The mixer produces the IF from *two* possible RF frequencies:
$$f_{RF} \text{ and } f_{Image}$$
If $f_{LO} = f_{RF} + f_{IF}$, then an unwanted signal at $f_{Image} = f_{LO} + f_{IF} = f_{RF} + 2 \cdot f_{IF}$ will also produce the IF.

### Mitigation
*   **Preselector:** An RF filter before the mixer to reject the image frequency.
*   **High IF:** Moves the image frequency further away, making it easier to filter.
*   **Double Conversion (Dubbelsuper):** Uses two IF stages.
    *   *1st IF (High):* Good Image Rejection (Veraf-selectiviteit).
    *   *2nd IF (Low):* Good Adjacent Channel Selectivity (Nabij-selectiviteit).

## 3. Automatic Gain Control (AGC / AVR)
Keeps the audio volume constant despite fading or differences in signal strength.
*   **Operation:** A DC voltage derived from the detector (proportional to signal strength) is fed back to reduce the gain of RF and IF amplifiers.
