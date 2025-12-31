# 00 Basic Skills

[< Back to Main Index](README.md)


# Candidate Basic Skills

Radio engineering is applied physics. This map covers the fundamental mathematical tools and physical concepts required for the exam.

## Fundamental Units & Math
*   **[SI Units & Prefixes](00_basic_skills.md)** - The language of measurement (Volts, Amps, Hz).
*   **[Mathematical Concepts for Radio](00_basic_skills.md)** - Scientific notation, formulas, and percentages.
*   **[Graphs and Data](00_basic_skills.md)** - Understanding linear vs. logarithmic scales.

## Radio Math
*   **[Decibels & Logarithms](00_basic_skills.md)** - Calculating gain and signal strength ratios.
*   **[Geometry & Trigonometry](00_basic_skills.md)** - Essential for AC theory (Pythagoras, Sine/Cosine).
*   **[Number Systems](00_basic_skills.md)** - Binary and Hexadecimal for digital modes.

## Physics
*   **[Physics Principles](00_basic_skills.md)** - Conservation of energy and efficiency.

---


# SI Units & Prefixes

In physics and radio engineering, a number alone is meaningless. It must be tied to a unit to describe a physical quantity. We use the **SI System** (Système International).

## SI Base Units
The most relevant base units for amateur radio are:
*   **Length**: meter (m)
*   **Mass**: kilogram (kg)
*   **Time**: second (s)
*   **Electric Current**: ampere (A). See [Voltage, Current, and Ohm's Law](01_electricity/07_Voltage,_Current,_and_Ohm's_Law.md).
*   **Temperature**: kelvin (K).
    *   Note: $0 \text{ K} = -273.15^\circ\text{C}$ (Absolute Zero).
    *   A change of 1 K is equal to a change of 1°C.

From these, we derive units like **Volt** (V), **Watt** (W), and **Hertz** (Hz).

## Prefixes (Voorvoegsels)
Radio deals with values from the massive (Gigahertz) to the tiny (microvolts). We use standard prefixes to simplify notation.

| Prefix | Symbol | Factor     | Power of 10 | Example            |
| :---   | :---:  | :---       | :---        | :---               |
| **Tera**   | T      | Trillion   | $10^{12}$   |                    |
| **Giga**   | G      | Billion    | $10^9$      | GHz (Microwaves)   |
| **Mega**   | M      | Million    | $10^6$      | MHz ([HF](07_propagation/01_Propagation_Basics.md)/[VHF](07_propagation/07_VHFUHF_Bands_6m,_2m,_70cm.md) Bands) |
| **kilo**   | k      | Thousand   | $10^3$      | km, kHz            |
| **milli**  | m      | Thousandth | $10^{-3}$   | mA (Current)       |
| **micro**  | $\mu$  | Millionth  | $10^{-6}$   | $\mu$V, $\mu$F     |
| **nano**   | n      | Billionth  | $10^{-9}$   | nF (Capacitance)   |
| **pico**   | p      | Trillionth | $10^{-12}$  | pF (Capacitance)   |

---


# Mathematical Concepts for Radio

Radio engineering relies on several key mathematical tools.

## Scientific Notation
Numbers are often written as a value between 1 and 10 multiplied by a power of 10. This makes handling very large or very small numbers easier.
*   $275,000,000 = 2.75 \times 10^8$
*   $0.000000275 = 2.75 \times 10^{-7}$

## Rearranging Formulas
You must be comfortable manipulating equations.
Example: [Ohm's Law](01_electricity/07_Voltage,_Current,_and_Ohm's_Law.md) $U = I \times R$
*   To find $I$: divide both sides by $R \rightarrow I = U / R$
*   To find $R$: divide both sides by $I \rightarrow R = U / I$

## Percentages
A percentage (%) is a fraction of 100. In radio, it is often used to calculate **Efficiency** (Rendement).

**Formula**: $\text{Efficiency} = \frac{P_{out}}{P_{in}} \times 100\%$

*Example*: If a transmitter consumes 100 Watts ($P_{in}$) to produce 60 Watts of RF ($P_{out}$):
$\frac{60}{100} \times 100\% = 60\%$ efficiency.

---


# Graphs and Data

Radio exams often require interpreting graphs to understand circuit behavior (like filter response) or propagation conditions.

## Axes
*   **X-axis (Horizontal)**: Typically the independent variable (e.g., Frequency or Time).
*   **Y-axis (Vertical)**: Typically the dependent variable (e.g., Voltage, Current, or Gain).

## Scales
*   **Linear Scale**: Equal distances represent equal additions (1, 2, 3, 4). Used when values are in a relatively small range.
*   **Logarithmic Scale**: Equal distances represent equal multiplications (1, 10, 100, 1000). Essential in radio for plotting **Frequency** (spanning Hz to GHz) or **Gain** (in [dB](00_basic_skills.md)).

---


# Decibels & Logarithms

Radio signals vary wildly in strength, often by factors of millions. The **Decibel (dB)** is a logarithmic unit used to express ratios (like gain or loss) in a manageable way.

## Logarithms
The logarithm is the power to which 10 must be raised to get a number.
*   $\log(100) = 2$ because $10^2 = 100$.
*   $\log(1000) = 3$.

## The Decibel Formula
*   **Power**: $dB = 10 \times \log_{10}(\frac{P_{out}}{P_{in}})$
*   **Voltage**: $dB = 20 \times \log_{10}(\frac{U_{out}}{U_{in}})$ (assuming equal impedance)

## Rules of Thumb
Calculating exact logs in your head is hard, but these rules cover most exam questions:
*   **+3 dB** $\approx$ 2x Power
*   **+6 dB** $\approx$ 4x Power (2x Voltage)
*   **+10 dB** = 10x Power
*   **-3 dB** $\approx$ Half Power (0.5x)
*   **-10 dB** = 1/10th Power (0.1x)

---


# Geometry & Trigonometry

Basic geometry is essential for understanding AC circuits, especially impedance.

## Pythagoras' Theorem
In a right-angled triangle, the square of the hypotenuse ($c$) equals the sum of the squares of the other two sides ($a$ and $b$).
*   **Formula**: $a^2 + b^2 = c^2$
*   **Application**: In AC circuits, Resistance ($R$) and [Reactance](02_components/07_Reactance_Reactantie.md) ($X$) are at right angles. The total [Impedance](01_electricity/21_Impedance_Impedantie.md) ($Z$) is the hypotenuse:
    $Z = \sqrt{R^2 + X^2}$

## Sine, Cosine, and Phase
AC signals are sinusoidal waves.
*   **Sine & Cosine**: Ratios of sides in a right-angled triangle relative to an angle.
*   **Phase**: The time relationship between two waves.
*   **Radians**: The natural unit for angles in physics. A full circle ($360^\circ$) is $2\pi$ radians.
    *   $\omega$ (Angular Frequency) $= 2\pi f$ (radians per second).

---


# Number Systems

Computers and digital modes rely on non-decimal systems.

## Systems
1.  **Decimal (Base 10)**: Our daily system (digits 0-9).
2.  **Binary (Base 2)**: Uses only 0 and 1. Fundamental for digital logic and computing.
    *   **Bit**: Binary Digit (0 or 1).
    *   **Byte**: 8 bits ($2^8 = 256$ values).
    *   **MSB**: Most Significant Bit (leftmost).
    *   **LSB**: Least Significant Bit (rightmost).
3.  **Hexadecimal (Base 16)**: Uses 0-9 and A-F. Used to represent binary data compactly (one hex digit = 4 binary bits).
    *   A=10, B=11, C=12, D=13, E=14, F=15.

## Conversions (Exam Topic)

### Decimal to Binary
Method: Repeated division by 2.
1.  Is the number odd? If yes, LSB = 1. If no, LSB = 0.
2.  Subtract the bit value (0 or 1), divide by 2.
3.  Repeat for the result until 0 is reached.
*   *Example:* 5. Odd $\to$ 1. (5-1)/2 = 2. Even $\to$ 0. (2-0)/2 = 1. Odd $\to$ 1. (1-1)/2 = 0. Result: **101**.

### Binary to Decimal
Sum the weights of the positions where the bit is 1.
*   Positions: $... 2^3 (8) \mid 2^2 (4) \mid 2^1 (2) \mid 2^0 (1)$
*   *Example:* $101_2 = 1\times4 + 0\times2 + 1\times1 = 5_{10}$.

## Binary Arithmetic
*   **Addition**:
    *   $0+0=0$
    *   $0+1=1$
    *   $1+0=1$
    *   $1+1=10$ (0 carry 1)
*   **Subtraction**:
    *   $1-0=1$
    *   $1-1=0$
    *   $10-1=1$
*   **Multiplication**: Equivalent to left shift.
*   **Division**: Equivalent to right shift.

---


# Physics Principles

Two fundamental principles of physics apply to all electronics and radio systems.

## Conservation of Energy
[Energy](01_electricity/08_Power_and_Energy.md) cannot be created or destroyed, only transformed from one form to another.
*   In a transmitter, electrical energy from the power supply is transformed into radio frequency (RF) energy and heat.
*   $Energy_{in} = Energy_{useful} + Energy_{waste}$

## Entropy & Heat
Order naturally tends toward disorder. In practical terms, no system is 100% efficient.
*   Some energy is always lost as heat due to resistance and other inefficiencies.
*   This is why high-power transmitters require heat sinks and cooling fans.

---


# Soldering & Connections

Reliable electrical connections are the foundation of a working radio station. Soldering is the process of joining metals using a filler metal (solder) with a lower melting point.

## Solder Types
*   **Rosin-Core**: The standard for electronics. The flux (rosin) cleans oxides from the metal during heating.
*   **Acid-Core**: **NEVER** use for electronics. It causes corrosion. Only for plumbing.
*   **Lead-Free (Sn/Cu/Ag)**: Modern standard (RoHS). Higher melting point than leaded solder.
*   **Leaded (Sn/Pb 60/40)**: Easier to work with (lower melting point), but poses health risks (wash hands).

## The Perfect Joint
1.  **Mechanical Strength**: The wire should be mechanically secure before soldering.
2.  **Appearance**:
    *   **Good**: Shiny (for leaded) or smooth satin (for lead-free), concave fillet (meniscus).
    *   **Bad ("Cold" Joint)**: Dull, grainy, rough, or lumpy. Caused by insufficient heat or moving the joint while cooling. High resistance or intermittent connection.

## Technique
1.  **Heat the Work**: Apply the iron tip to the *parts* (wire and pad), not just the solder.
2.  **Apply Solder**: Feed solder into the joint, not the iron.
3.  **Clean**: Keep the iron tip tinned (shiny) and clean.

## Connectors
*   **Crimping**: Often superior to soldering for coaxial connectors (PL-259, BNC) and power lugs (Anderson Powerpoles) if the correct ratcheting tool is used.
*   **Waterproofing**: Outdoor connections must be sealed with:
    1.  Electrical Tape.
    2.  **Self-Amalgamating Tape** (Rubber splicing tape).
    3.  Final layer of Electrical Tape (UV protection).

---