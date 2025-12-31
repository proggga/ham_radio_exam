# LED (Light Emitting Diode)

A diode that emits light when current flows through it in the forward direction.

## Characteristics
*   **Material**: Gallium Arsenide (GaAs) compounds, not Silicon or Germanium.
*   **Forward Voltage ($U_F$)**: Higher than standard diodes.
    *   **Red**: ~1.6V - 2.0V
    *   **Green/Yellow**: ~2.0V - 2.4V
    *   **Blue/White**: ~3.0V - 4.0V
*   **Current**: Typically 10-20 mA for indication.

## Usage
*   **Current Limiting**: LEDs must **always** have a series resistor to limit current, as they have low internal resistance once conducting.
    *   Formula: $R_{series} = \frac{U_{source} - U_{LED}}{I_{LED}}$

---
[< Back to Section Index](README.md)