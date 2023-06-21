---
marp: true
slideNumber: true
markdown.marp.enableHtml: true
title: Group 3 - Regression
header: "02.06.2023 | Group 3 | Regression"
footer: "Pieer A. | Philipp R. | Jerome W. | Johannes T. | Tomislav P."
transition: fade
paginate: true
---

# Analytical Solution for $f_1(x)$

Analytically find the global minimum of the following function:
$f_1(x)=x^4 + x^3 - x^2 - x$

## Solution

$f'(x)_1=4x^3 + 3x^2 - 2x - 1 = 0$

$4x^3 + 3x^2 - 2x = 1$

(x+1)(4x^2) = 0


f'(x) = (x+1)Q(x)

---

 4x^3 + 3x^2 - 2x - 1 / (x+1) = 4x^2
-4x^3 + 4x^2
        7x^2 - 2x - 1 / (x+1) = 7x
       -7x^2 + 7x
                5x - 1 / (x+1) = 5
               -5x + 5
                    -6 / (x+1) = -6
                     6x + 6

---


$\Delta = b^2 - 4ac = 9 - 4(4)(-1) = 25$
- for the polynomial to have a solution, $\Delta \geq 0$
- if result is a perfect square root ==> then it has exactly 1 real root
- if result is not a perfect square root ==> then it has 2 real roots and the solutions are symmetric.

$x_1 = \frac{-b + \sqrt{\Delta}}{2a} = \frac{-3 + 5}{8} = \frac{1}{2}$