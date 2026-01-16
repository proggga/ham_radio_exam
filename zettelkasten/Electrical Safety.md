id: 202301011246
title: "Electrical Safety"
tags: ["safety", "semiconductors"]
created: 2025-12-29
type: permanent-note
modified: 2025-12-29

aliases: ["Elektrische veiligheid"]

# Electrical Safety

## 1. The Human Body
*   **Resistance**: Varies with skin condition.
    *   Dry skin: High resistance ($\approx 100 k\Omega$).
    *   Wet/Broken skin: Low resistance ($\approx 1 k\Omega$ internal).
*   **Risk**: Current (Amperes) kills, voltage drives the current.
    *   **Path**: Hand-to-hand is dangerous (crosses heart). Hand-to-foot is also dangerous.

### Physiological Effects of Current (AC 50Hz)
| Current | Effect |
| :--- | :--- |
| **0.5 mA** | Threshold of perception (Tingling). |
| **10 mA** | Muscle contraction ("Let-go" threshold). You cannot release the wire. |
| **20 mA** | Respiratory paralysis (Suffocation). |
| **30 mA** | **RCD Trip Level**. Safe limit for short duration. |
| **75 mA** | **Ventricular Fibrillation**. Heart rhythm chaos. Fatal if not treated. |
| **> 1 A** | Cardiac Arrest (Heart stops), severe burns. |

## 2. Equipment Classes & Voltage Limits (IEC 62368-1)
*   **Permissible Touch Voltage (Toegelaten aanrakingsspanning)**: Voltages below these limits are considered safe to touch (SELV - Safety Extra Low Voltage).
    *   **AC**: $< 30 V$ RMS (or $50V$ in dry conditions).
    *   **DC**: $< 60 V$ (Ripple free) (or $120V$ in dry conditions).
*   **Class I**: **Earthed**. Metal chassis must be connected to Safety Earth (PE). Relies on fuse/RCD to disconnect if a fault occurs.
*   **Class II**: **Double Insulated**. No earth connection. Symbol: Square within a square.
*   **Class III (SELV)**: Equipment designed to operate safely within the SELV limits.

## 3. Mains Wiring (Europe/Netherlands)
*   **Brown**: Phase / Live (L) - Dangerous!
*   **Blue**: Neutral (N) - Return path. Considered live (can carry voltage if fault occurs).
*   **Green/Yellow**: Protective Earth (PE) - Safety ground. Connected to chassis.

## 4. Protection Devices
*   **Fuses (Smeltveiligheden)**: Protect wiring/equipment from fire.
    *   *Fast (F):* For semiconductors/resistive loads.
    *   *Slow (T - Träge):* For [[Transformers]]/Power Supplies (to handle inrush current).
*   **RCD (Aardlekschakelaar)**: Residual Current Device.
    *   Measures difference between $I_{Live}$ and $I_{Neutral}$.
    *   Trips at **30 mA** imbalance. Protects **people**.
*   **Bleeder [[Resistors]]**: [[Resistors]] connected across High Voltage capacitors to discharge them after power-off. (Safety requirement: $< 60V$ within seconds).

## 5. Lightning Protection
*   **Disconnect**: The only 100% safe method is to unplug Antennas and Mains during thunderstorms.
*   **Grounding**: Mast/[[Antenna & Tower Safety|Antenna]] should be grounded to conduct static/strike current to earth (outside the house).

## Related
*   [[Earthing Systems]]
*   [[RF Safety]]
*   [[Antenna & Tower Safety]]
*   [[Equipment Safety Classes]]
*   [[Station Setup Guidelines]]
*   [[Capacitors]] (High voltage safety)
*   [[Power Supply]] (Mains safety)