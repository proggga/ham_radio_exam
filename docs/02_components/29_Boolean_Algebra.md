# Boolean Algebra

Boolean algebra provides the rules for simplifying digital logic circuits.
*   **1** = True / High
*   **0** = False / Low
*   **+** = OR
*   **.** = AND
*   **$\bar{A}$** = NOT A

## Identities (Rekenregels)
*   **NOT:** $\bar{\bar{A}} = A$
*   **AND:**
    *   $A \cdot A = A$
    *   $A \cdot 1 = A$
    *   $A \cdot 0 = 0$
    *   $A \cdot \bar{A} = 0$
*   **OR:**
    *   $A + A = A$
    *   $A + 0 = A$
    *   $A + 1 = 1$
    *   $A + \bar{A} = 1$
*   **Commutative:** $A \cdot B = B \cdot A$ and $A + B = B + A$
*   **Distributive:** $A \cdot (B + C) = A \cdot B + A \cdot C$
*   **Absorption:**
    *   $A + A \cdot B = A$
    *   $A \cdot (A + B) = A$
    *   $A + \bar{A} \cdot B = A + B$

## De Morgan's Laws
These laws allow converting between AND and OR logic using inversion.
1.  **NAND equivalency**: $\overline{A \cdot B} = \bar{A} + \bar{B}$
    *   "Break the line, change the sign."
2.  **NOR equivalency**: $\overline{A + B} = \bar{A} \cdot \bar{B}$

---
[< Back to Section Index](README.md)