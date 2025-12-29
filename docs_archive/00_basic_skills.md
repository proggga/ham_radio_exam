# Eindterm 0: Candidate Basic Skills (Basisvaardigheden van de kandidaat)

## Introduction
Radio engineering is essentially applied physics. To understand how radio works, you need a grasp of the fundamental tools of physics: quantities, units, and mathematics. This section covers the essential mathematical skills and standard units required for the Full License exam.

### Exam Tools
For the exam, you are not allowed to bring your own calculator. You will be provided with a standard scientific calculator (currently the **Casio fx-82NL**). It is highly recommended to practice with this specific model if possible, or at least be comfortable with scientific notation and log/trig functions on a standard calculator.

## Quantities and Units (Grootheden en Eenheden)
In physics, a number alone is meaningless. It must be tied to a unit to describe a physical quantity. We use the **SI System** (Système International), which is based on seven fundamental base units.

### SI Base Units
The most relevant base units for amateur radio are:
*   **Length:** meter (m)
*   **Mass:** kilogram (kg)
*   **Time:** second (s)
*   **Electric Current:** ampere (A). See [Ohm's Law](01_electricity/02_ohm_law.md).
*   **Temperature:** kelvin (K). Note: $0 \text{ K} = -273.15^\circ\text{C}$ (Absolute Zero). A difference of 1 K is equal to a difference of 1°C.

From these base units, we derive others like the [Volt ($V$)](01_electricity/02_ohm_law.md), [Watt ($W$)](01_electricity/04_power_energy.md), and [Hertz ($Hz$)](01_electricity/10_ac_signals.md).

### Prefixes (Voorvoegsels)
Radio electronics deals with numbers ranging from the massive (Gigahertz frequencies) to the tiny (microvolts). Instead of writing endless zeros, we use standard prefixes:

| Prefix | Symbol | Factor | Scientific | Example |
| :--- | :---: | :--- | :--- | :--- |
| **Tera** | T | Trillion | $10^{12}$ | |
| **Giga** | G | Billion | $10^9$ | GHz (Microwaves) |
| **Mega** | M | Million | $10^6$ | MHz (HF/VHF Bands) |
| **kilo** | k | Thousand | $10^3$ | km, kHz |
| | | 1 | $10^0$ | Base Unit |
| **milli** | m | Thousandth | $10^{-3}$ | mA (Current) |
| **micro** | $\mu$ | Millionth | $10^{-6}$ | $\mu$V, $\mu$F |
| **nano** | n | Billionth | $10^{-9}$ | nF (Capacitance) |
| **pico** | p | Trillionth | $10^{-12}$ | pF (Capacitance) |

*Note: There are others like Peta ($10^{15}$) and femto ($10^{-15}$), but the above are the bread and butter of radio.*

## Mathematical Concepts

### Scientific Notation
Numbers are often written as a value between 1 and 10 multiplied by a power of 10.
*   $275,000,000 = 2.75 \times 10^8$
*   $0.000000275 = 2.75 \times 10^{-7}$

### Rearranging Formulas (Vergelijkingen)
You must be comfortable manipulating equations. If $U = I \times R$ (See [Ohm's Law](01_electricity/02_ohm_law.md)):
*   To find $I$: divide both sides by $R \rightarrow I = U / R$
*   To find $R$: divide both sides by $I \rightarrow R = U / I$

### Logarithms & Decibels
Radio signals vary wildly in strength, often by factors of millions. The **Decibel (dB)** is a logarithmic unit used to express ratios (like gain or loss) in a manageable way.

*   **Logarithms:** The power to which 10 must be raised to get a number. $\log(100) = 2$ because $10^2 = 100$.
*   **The Decibel Formula:**
    *   **Power:** $dB = 10 \times \log_{10}(\frac{P_{out}}{P_{in}})$
    *   **Voltage:** $dB = 20 \times \log_{10}(\frac{U_{out}}{U_{in}})$ (assuming equal impedance)

**Rules of Thumb:**
*   **+3 dB** $\approx$ 2x Power
*   **+6 dB** $\approx$ 4x Power (2x Voltage)
*   **+10 dB** = 10x Power
*   **-3 dB** $\approx$ Half Power (0.5x)

### Number Systems
Computers and digital modes rely on non-decimal systems.
1.  **Decimal (Base 10):** Our daily system (0-9).
2.  **Binary (Base 2):** Uses only 0 and 1. Fundamental for digital logic.
    *   Example: $101_2 = 1\times4 + 0\times2 + 1\times1 = 5_{10}$.
3.  **Hexadecimal (Base 16):** Uses 0-9 and A-F. Used to represent bytes compactly.

### Percentages
A percentage (%) is simply a fraction of 100. In radio, it is often used to calculate **Efficiency** (Rendement).
*   **Formula:** $\text{Efficiency} = \frac{P_{out}}{P_{in}} \times 100\%$
*   *Example:* If a transmitter consumes 100 Watts of power ($P_{in}$) to produce 60 Watts of radio signal ($P_{out}$), its efficiency is $60\%$. The remaining 40% is lost as heat.

## Graphs and Data
Radio exams often require interpreting graphs to understand circuit behavior or propagation.
*   **Axes:** The horizontal X-axis typically represents the independent variable (like Frequency or Time), while the vertical Y-axis represents the dependent variable (like Voltage or Current).
*   **Linear vs. Logarithmic:**
    *   **Linear Scales:** Equal distances represent equal additions (1, 2, 3, 4). Used when values are in the same range.
    *   **Logarithmic Scales:** Equal distances represent equal multiplications (1, 10, 100, 1000). Essential in radio for plotting Frequency (which spans Hz to GHz) or Gain (decibels).

## Geometry and Trigonometry

### Pythagoras' Theorem
Essential for calculating [Impedance ($Z$)](03_circuits/07_reactance_impedance.md) in AC circuits, where Resistance ($R$) and Reactance ($X$) form a right-angled triangle.
*   **Formula:** $a^2 + b^2 = c^2$
*   **Application:** $Z = \sqrt{R^2 + X^2}$

### Sine, Cosine, and Phase
AC signals are sinusoidal waves. See [AC Signals](01_electricity/10_ac_signals.md).
*   **Sine & Cosine:** Ratios of sides in a right-angled triangle relative to an angle.
*   **Phase:** The time relationship between two waves.
*   **Radians:** The natural unit for angles in physics. A full circle ($360^\circ$) is $2\pi$ radians.
    *   $\omega$ (Angular Frequency) $= 2\pi f$ (radians per second). This connects frequency ($f$) to the math of rotating vectors.

## Physics Principles
Two key thermodynamic principles apply to electronics:
1.  **Conservation of Energy:** Energy cannot be created or destroyed, only transformed (e.g., electrical energy becomes radio waves and heat).
2.  **Entropy:** Order naturally tends toward disorder (heat). No system is 100% efficient; some energy is always lost as heat.

---
[Back to Index](INDEX.md) | [Back to Dashboard](../README.md)
