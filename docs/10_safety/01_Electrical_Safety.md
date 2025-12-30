# Electrical Safety

## 1. The Human Body
*   **Resistance:** Varies with skin condition. See Ohm's Law.
    *   Dry skin: High resistance (~100 k$\Omega$).
    *   Wet/Broken skin: Low resistance (~1 k$\Omega$ internal).
*   **Risk:** Current (Amperes) kills, voltage drives the current.

### Physiological Effects of Current (AC 50Hz)
See AC Signals.
| Current | Effect |
| :--- | :--- |
| **0.5 mA** | Threshold of perception (Tingling). |
| **10 mA** | Muscle contraction ("Let-go" threshold). You cannot release the wire. |
| **30 mA** | Respiratory paralysis (Suffocation). |
| **75 mA** | **Ventricular Fibrillation**. Heart rhythm chaos. Fatal if not treated. |
| **> 1 A** | Cardiac Arrest (Heart stops), severe burns. |

## 2. Voltage Limits (IEC 62368-1)
*   **Safe Extra Low Voltage (SELV / Klasse III):**
    *   $< 60 V$ DC (Ripple free).
    *   $< 30 V$ RMS AC.
    *   Safe to touch.
*   **Dangerous Voltage:** Anything above SELV limits requires protection (Insulation/Barriers).

## 3. Mains Wiring (Europe/Netherlands)
*   **Brown:** Phase / Live (L) - Dangerous!
*   **Blue:** Neutral (N) - Return path.
*   **Green/Yellow:** Protective Earth (PE) - Safety ground.

## 4. Protection Devices
*   **Fuses (Zekeringen):** Protect wiring/equipment from fire due to overcurrent.
    *   *Fast (F):* Semiconductors.
    *   *Slow (T - Träge):* Transformers/Motors (inrush current).
*   **RCD (Aardlekschakelaar):** Residual Current Device.
    *   Detects imbalance between Live and Neutral (current leaking to Earth).
    *   Trips at **30 mA**. Protects **people** from lethal shock.
*   **Safety Earth:** Low resistance path (< 0.1 $\Omega$) to trip the fuse/RCD if a live wire touches the chassis.

---
[< Back to Section Index](README.md)