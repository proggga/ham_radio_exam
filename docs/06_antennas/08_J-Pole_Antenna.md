# J-Pole Antenna

The **J-Pole** is a popular, omnidirectional vertical antenna used primarily for [VHF](../07_propagation/08_VHFUHF_Bands_6m,_2m,_70cm.md) and [UHF](../07_propagation/08_VHFUHF_Bands_6m,_2m,_70cm.md). It is named for its J-shape.

## Principle
*   **Structure**: It consists of a **Half-Wave Radiator** ($\lambda/2$) fed by a **Quarter-Wave Matching Section** ($\lambda/4$) stub.
*   **Total Height**: Approximately $3/4 \lambda$.
*   **Operation**:
    *   The $\lambda/2$ radiator has a high impedance feedpoint at the bottom.
    *   The $\lambda/4$ parallel line stub acts as an impedance transformer (Stub Match), transforming the high impedance of the radiator down to $50 \Omega$ at the feedpoint.

## Characteristics
*   **Gain**: Slightly higher than a Ground Plane ($\approx 2-3$ dBi) due to the lower [angle of radiation](17_Take-Off_Angle.md).
*   **Pattern**: Omnidirectional.
*   **Grounding**: The bottom of the stub is a voltage node (zero voltage) and can be grounded directly to the mast (DC grounded), providing some lightning protection.
*   **No Radials**: Unlike a Ground Plane, it does not require ground radials, making it less wind-resistant and easier to mount.

## Variants
*   **Slim Jim**: A folded dipole version of the J-Pole. Offers slightly better low-angle radiation (higher gain at the horizon).
*   **Roll-up J-Pole**: Made from 300-ohm twin-lead cable (ladder line). Portable, can be hung from a tree.

## Pros & Cons
*   **Pros**: Simple, no radials, robust, DC grounded.
*   **Cons**: Can suffer from **Common Mode Current** on the feedline if not properly choked (feedline becomes part of the radiating element).

---
[< Back to Section Index](README.md)