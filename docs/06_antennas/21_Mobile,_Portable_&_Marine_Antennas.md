# Mobile, Portable & Marine Antennas

Operating radio equipment from vehicles or boats presents unique challenges due to limited space and the lack of a traditional earth ground.

## Mobile HF Antennas (Vehicles)
Mobile HF antennas are almost always vertical whips that are physically short compared to the wavelength (e.g., an 8ft whip on 80m).

### Loading Coils
Because the whip is short ($< \lambda/4$), it is highly capacitive. An **Inductive Loading Coil** is added to resonate the antenna.
*   **Base Loading**: Coil at the bottom. Mechanically strong but least efficient (current is lowest at the top).
*   **Center Loading**: Coil in the middle. Better efficiency as the high-current portion of the radiator is below the coil. Most common design.
*   **Top Loading**: Capacity hat at the top. Improves efficiency but mechanically difficult.
*   **Continuous Loading**: Wire wound helically along the entire fiberglass rod (e.g., "Hamstick").

### High Q and Bandwidth
Short, loaded antennas have a very high **[Quality Factor (Q)](../03_circuits/06_Quality_Factor_Q.md)**.
*   **Effect**: Bandwidth is extremely narrow (e.g., 20-40 kHz on 80m).
*   **Tuning**: Frequent retuning is required when changing frequency.
    *   *Manual*: Moving a tap or adjusting a stinger tip (stopped vehicle).
    *   *Remote*: "Screwdriver" antennas use a motor to move the coil inside the base, allowing tuning from the driver's seat.

## Portable Antennas
For temporary operation (parks, hotels).
*   **Telescopic Whips**: Adjustable length to find resonance.
*   **Window-Sill Antennas**: Clamped to a window frame. Requires a counterpoise wire thrown on the floor.
*   **Magnetic Loops**: Excellent for portable use due to small size and noise rejection (see [Loop Antennas](04_Loop_Antennas.md)).

## Marine Antennas (Boats)
Salt water is an excellent conductor, making it a perfect RF ground.

### Grounding
*   **Connection**: Ground strap connected to the engine block, metal keel, or a specialized **Dynaplate** (sintered bronze plate) on the hull.
*   **Electrolysis**: Great care must be taken to block DC current between the radio ground and the boat's bonding system to prevent rapid corrosion of underwater metals (zinc anodes are essential).

### Antenna Types
*   **Marine Whips**: Usually longer than car antennas (no height restrictions at sea).
*   **Backstay Antenna**: On sailboats, the rear rigging wire (backstay) is insulated at top and bottom and fed as a random wire antenna. Requires a good **Antenna Tuner (ATU)** at the base.

---
[< Back to Section Index](README.md)