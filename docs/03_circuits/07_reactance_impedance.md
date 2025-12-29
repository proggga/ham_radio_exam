# Reactance and Impedance

## 1. Phase Relationships (Faseverschil)
In resistors, Voltage ($U$) and Current ($I$) are in phase. In reactive components (Capacitors and Inductors), they are shifted by $90^\circ$ ($\pi/2$ radians).

*   **Inductor ($L$):** Voltage leads Current by $90^\circ$.
    *   *Mnemonic:* **LUI** (L: U before I) or **ELI** (E leads I in L).
*   **Capacitor ($C$):** Current leads Voltage by $90^\circ$.
    *   *Mnemonic:* **CIU** (C: I before U) or **ICE** (I leads E in C).

## 2. Reactance (Reactantie)
Reactance is the opposition to AC current flow caused by capacitance or inductance. It depends on frequency.
*   **Symbol:** $X$
*   **Unit:** Ohm ($\Omega$)

### Inductive Reactance ($X_L$)
Increases with frequency.
$$X_L = 2\pi f L = \omega L$$
*   At DC ($0 Hz$): $X_L = 0$ (Short circuit).
*   At high freq: $X_L$ is high (Open circuit).

### Capacitive Reactance ($X_C$)
Decreases with frequency.
$$X_C = \frac{1}{2\pi f C} = \frac{1}{\omega C}$$
*   At DC ($0 Hz$): $X_C = \infty$ (Open circuit).
*   At high freq: $X_C$ is low (Short circuit).

## 3. Impedance (Impedantie)
Impedance is the total opposition to current flow in an AC circuit, combining Resistance ($R$) and Reactance ($X$).
*   **Symbol:** $Z$
*   **Unit:** Ohm ($\Omega$)
*   **Formula:** Vector sum of $R$ and $X$.

### Series RL / RC Circuits
In series, resistances and reactances add vectorially (at $90^\circ$).
$$Z = \sqrt{R^2 + X^2}$$

### Parallel RL / RC Circuits
In parallel, conductances and susceptances add vectorially.
$$\frac{1}{Z} = \sqrt{(\frac{1}{R})^2 + (\frac{1}{X})^2}$$

## 4. Vector Diagrams
AC quantities with different phases cannot be added arithmetically (e.g., $3V + 4V \neq 7V$). They must be added as vectors.
*   **Pythagoras:** If vectors are at $90^\circ$, the resultant is the hypotenuse.
    *   $Result = \sqrt{A^2 + B^2}$
    *   Example: $3V$ across $R$ and $4V$ across $L$ in series gives $5V$ total supply voltage.
