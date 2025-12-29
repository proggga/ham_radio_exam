# Mitigation (Ontstoring)

## 1. At the Transmitter (Source)
*   **Low Pass Filter (LPF):** Place between Transmitter and Antenna. Attenuates Harmonics (frequencies *above* the cutoff).
*   **Power Level:** Use the minimum power necessary for the contact (QRP).
*   **Clean Signal:** Avoid overmodulation (ALC) and ensure stable keying (Chirp-free).

## 2. At the Victim (Immunity)
*   **High Pass Filter (HPF):** Place on TV/Radio antenna inputs to block HF amateur signals (frequencies *below* the cutoff).
*   **Band Stop Filter (Notch):** Blocks a specific interfering frequency.

## 3. Cable Filtering
*   **Ferrites (Ferrietkernen):**
    *   **Clamp-on (Ferrietklem):** Easy to add to existing cables.
    *   **Ring (Toroid):** Wind the cable through the ring multiple times for higher inductance.
    *   **Function:** Acts as a **Common Mode Choke**. It presents a high impedance to RF currents flowing on the outside of the cable (shield) without affecting the signal inside (differential mode).
    *   *Placement:* Place as close to the equipment (TX or Victim) as possible.

## 4. Decoupling (Ontkoppelen)
Using capacitors to short RF to ground.
*   **Capacitors:** Small values (1nF - 10nF) ceramic capacitors.
*   **Placement:** Across speaker terminals, audio inputs, or mains pins.
*   **Function:** Low impedance path for RF to bypass the sensitive circuitry.

## 5. Mains Filtering
*   **Mains Filter:** A combination of Inductors and Capacitors (L-C) built into a module (often the IEC power socket). Blocks RF from entering/leaving via the power line.
