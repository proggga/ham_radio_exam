# Station Accessories

Beyond the transceiver, several accessories improve station performance and capability.

## RF Power Amplifiers (Amplifiers)
*   **Function**: Increases the transmitted output power.
*   **Usage**: Useful for weak signal work (SSB/CW) or overcoming feedline loss.
*   **Key Controls**:
    *   **SSB/CW-FM Switch**:
        *   *SSB/CW*: Adds a delay to the T/R relay to prevent it from dropping out between words (VOX delay). Linear amplification.
        *   *FM*: No delay, instant switching. Class C (non-linear) amplification often used for efficiency.

## Transverters
*   **Function**: Converts the RF input and output of a transceiver to another band.
*   **Operation**:
    *   *Transmit*: Down-converts HF (e.g., 28 MHz) to IF, or Up-converts IF to VHF/UHF/Microwave.
    *   *Receive*: Down-converts VHF/UHF signals to the HF band (e.g., 28 MHz) for the transceiver to process.
*   **Application**: Allows an HF radio to operate on VHF/UHF/Microwave bands (e.g., 1296 MHz) while retaining the HF radio's advanced features (filters, DSP).

## RF Preamplifiers (Preamps)
*   **Function**: Amplifies weak signals *before* they reach the receiver.
*   **Placement**: Best installed **at the antenna** to amplify the signal before feedline loss adds noise.
*   **Trade-off**: Increases noise as well as signal. Can cause receiver overload in strong signal environments.

## Mixers
*   **Function**: Circuits that convert a signal from one frequency to another by combining it with a local oscillator signal.
*   **Output**: Sum and Difference frequencies ($f_1 + f_2$ and $f_1 - f_2$).

## Antenna Tuning Units (ATUs)
*   **Function**: Matches the impedance of the antenna system to the transceiver (usually $50 \Omega$).
*   **Note**: It does *not* tune the antenna itself (does not change resonant frequency), only the impedance seen by the radio.
*   See Antenna Tuning Unit (ATU) for details.

---
[< Back to Section Index](README.md)