---
id: 202512310009
title: Radio Direction Finding (RDF)
tags: ["ham-radio", "operating", "measurement", "military"]
created: 2025-12-31
type: permanent-note
modified: 2025-12-31
---

# Radio Direction Finding (RDF)

Radio Direction Finding is the process of determining the location of a radio transmitter by using a receiver and a directional antenna.

## Applications
*   **Fox Hunting (Vossenjacht)**: Amateur radio sport finding hidden transmitters.
*   **[[Mixing Products (Interference)|Interference]] Tracking**: Locating sources of QRM (jammers, faulty electronics).
*   **Search and Rescue (SAR)**: Locating emergency beacons (ELT/EPIRB).
*   **Military**: Locating enemy units ([[Electronic Warfare (Jamming)|Electronic Warfare]] Support).

## Techniques
1.  **Triangulation**: Taking bearings (Azimuths) from multiple known locations.
    *   **Azimuth/Bearing**: The direction to the transmitter (in degrees).
    *   **Cut**: The intersection of two bearings. Gives a general location.
    *   **Fix**: The intersection of three or more bearings. Gives a more precise location.
    *   **CEP (Circular Error of Probability)**: The radius of a circle around the fix where the transmitter is likely to be (accounting for inaccuracies).
2.  **Homing**: Moving toward the signal strength peak. "Sniffing" the signal.

## Equipment
*   **Directional [[Antenna & Tower Safety|Antenna]]**: [[Directional Antennas (Beams)|Yagi]], Quad, or Loop.
    *   *Null Method:* It is often more accurate to find the signal **null** (minimum strength) of a loop or dipole than the peak, as the null is sharper.
*   **Attenuator**: Essential when getting close to the transmitter to prevent receiver overload (which makes direction finding impossible).
*   **Doppler RDF**: Uses an array of antennas switched rapidly to simulate a rotating antenna, using the Doppler effect to indicate direction electronically.

## Factors Affecting Accuracy
*   **Reflections**: Signals bouncing off buildings/hills (Multipath).
*   **Polarization**: Cross-polarization can distort readings.
*   **Nearby Objects**: Metal fences/wires can re-radiate the signal.

## Related
*   [[Amateur Radio Activities]]
*   [[Antenna Characteristics]]
*   [[Electronic Warfare (Jamming)]]
