# Amplifiers (Versterkers)

## 1. Operating Principle
An amplifier increases the amplitude of a signal (Voltage, Current, or Power) without changing its shape (ideally). It uses an active device (Transistor, FET, Tube) to control a power source.

### Biasing (Instelling)
To work correctly, the active device must be set to a specific "Operating Point" (Werkpunt or Instelpunt) using DC voltages and currents.
*   **Purpose:** To ensure the device operates in its linear region (for Class A) or appropriate cutoff point (Class B/C).
*   **Methods:**
    *   **Base/Gate Resistors:** Set the DC voltage.
    *   **Emitter/Source/Cathode Resistor:** Provides self-bias and thermal stability (negative feedback for DC).

### Load Line (Belastingslijn)
A graphical tool to visualize amplifier operation.
*   Plots **Collector Current ($I_c$)** vs **Collector-Emitter Voltage ($U_{ce}$)**.
*   **Line:** Connects the saturation point ($I_{max} = U_{supply}/R_{load}$) and cutoff point ($U_{max} = U_{supply}$).
*   **Operating Point ($P$):** The DC bias point on this line.
    *   For **Class A**, $P$ is in the middle (allows max swing up and down).
    *   For **Class B**, $P$ is at cutoff ($I_c = 0$).

## 2. Amplifier Classes
Classes describe the conduction angle (bias point) of the amplifying device.

| Class | Conduction | Linearity | Efficiency | Use |
| :--- | :--- | :--- | :--- | :--- |
| **Class A** | $360^\circ$ (100%) | Highest | Low (25-50%) | Audio, Pre-amps |
| **Class B** | $180^\circ$ (50%) | Low | Medium (~78%) | Push-Pull Audio/RF |
| **Class AB**| $180^\circ - 360^\circ$| Good | Good | SSB Linear Amps |
| **Class C** | $< 180^\circ$ (Pulses)| Very Low | High (>80%) | FM/CW RF PA |

*   **Push-Pull:** Two devices working alternately (Class B/AB). Eliminates **even** harmonics. Requires phase-splitting (e.g., transformer).

## 3. Coupling Methods
How stages are connected.
*   **RC Coupling:** Capacitor blocks DC, passes AC. Resistors set bias.
    *   *Calculation:* The capacitor forms a High Pass Filter with the input impedance of the next stage. $X_c$ must be low at the lowest frequency ($f_{min}$).
*   **Transformer:** Matches impedance ($Z_p/Z_s = (N_p/N_s)^2$).
    *   *Pros:* Efficient, Tuned (IF strips).
    *   *Cons:* Heavy, Bandwidth limited.
*   **LC/Choke Coupling:** Uses an inductor as the collector load.
    *   *Pros:* High efficiency for RF (DC voltage at collector $\approx V_{supply}$).
*   **Direct:** DC coupled (no capacitor). Used in Op-amps.

## 4. Feedback (Terugkoppeling)
*   **Negative Feedback:** Part of output subtracted from input.
    *   Reduces Gain.
    *   **Reduces Distortion.**
    *   Increases Bandwidth.
    *   Increases Stability.
*   **Positive Feedback:** Part of output added to input.
    *   Increases Gain (Regenerative receiver).
    *   Causes **Oscillation** (if loop gain $\ge 1$).

## 5. Distortion and Dissipation
*   **Dissipation:** Power lost as heat in the active device ($P = U_{ce} \times I_c$).
    *   Must stay within the **Dissipation Hyperbola** (Safe Operating Area).
*   **Harmonic Distortion:** Creates multiples of the fundamental frequency ($2f, 3f$).
*   **Intermodulation Distortion (IMD):** Mixing of two signals ($f_1, f_2$) creating sum/difference products ($2f_1 - f_2$, etc.). Causes "splatter" in SSB.
