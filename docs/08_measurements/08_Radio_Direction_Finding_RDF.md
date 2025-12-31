# Radio Direction Finding (RDF)

Radio Direction Finding is the process of determining the location of a radio transmitter by using a receiver and a directional antenna.

## Applications
*   **Fox Hunting (Vossenjacht)**: Amateur radio sport finding hidden transmitters.
*   **[Interference](../09_interference/03_Mixing_Products_Interference.md) Tracking**: Locating sources of QRM (jammers, faulty electronics).
*   **Search and Rescue (SAR)**: Locating emergency beacons (ELT/EPIRB).
*   **Military**: Locating enemy units ([Electronic Warfare](../09_interference/08_Electronic_Warfare_Jamming.md) Support).

## Techniques
1.  **Triangulation**: Taking bearings (Azimuths) from multiple known locations.
    *   **Azimuth/Bearing**: The direction to the transmitter (in degrees).
    *   **Cut**: The intersection of two bearings. Gives a general location.
    *   **Fix**: The intersection of three or more bearings. Gives a more precise location.
    *   **CEP (Circular Error of Probability)**: The radius of a circle around the fix where the transmitter is likely to be (accounting for inaccuracies).
2.  **Homing**: Moving toward the signal strength peak. "Sniffing" the signal.

## Equipment
*   **Directional [Antenna](../10_safety/03_Antenna_&_Tower_Safety.md)**: [Yagi](../06_antennas/08_Directional_Antennas_Beams.md), Quad, or Loop.
    *   *Null Method:* It is often more accurate to find the signal **null** (minimum strength) of a loop or dipole than the peak, as the null is sharper.
*   **Ferrite Loopstick**: Common in portable [AM](../01_electricity/32_Analogue_Modulation_&_AM.md) radios. Pattern is a Figure-8.
    *   *Bidirectional Ambiguity:* A loopstick has two nulls 180° apart. A **Sense [Antenna](../10_safety/03_Antenna_&_Tower_Safety.md)** (vertical whip) can be added to create a Cardioid pattern with a single null to resolve this.
*   **Adcock Array**: Two vertical dipoles connected out of phase. Responds to vertically polarized signals but cancels horizontally polarized skywave (good for [HF](../07_propagation/01_Propagation_Basics.md)).
*   **Doppler RDF**: Uses an array of antennas switched rapidly to simulate a rotating antenna. The perceived [Doppler Shift](../07_propagation/02_Doppler_Shift.md) of the incoming signal indicates the direction.
*   **Attenuator**: Essential when getting close to the transmitter to prevent receiver overload (which makes direction finding impossible).

## Factors Affecting Accuracy
*   **Reflections**: Signals bouncing off buildings/hills (Multipath).
*   **Polarization**: Cross-polarization can distort readings.
*   **Nearby Objects**: Metal fences/wires can re-radiate the signal.

---
[< Back to Section Index](README.md)