# HW 4

- in hw4.py is the non-vectorized template
- hw4_improved.py is the vectorized version

## description of the code 

### uniform(a,b)
- function returns a random  number in [a, b) if a < b
- if a < b then a and b are lower and upper bound of the calculated random number
    - substraction of a-b : calculates range between b and a
    - random number with np.random.random(): returns random number in [0, 1)
    - adding a : adds the lower bound to calculated random number 

### f(x,R)
- is a function for a circle
- calculates and returns the square root of the absolut difference between the square of the given numbers x and R
- circle equation: $x^2 + y^2 = r^2$ -> f(x,R) is computing y 

### NoName(N)
- has a input value N -> Number of points that the function should generate
- creates two empty lists "list_x" and "list_y" -> storage for the created 2D points (x and y axis)
- list_accepted_x gets a new element if the ith value (i from 0 to N-1) of list_y is smaller then f(list_x[i], R), which means smaller than the y value from the ith value of list_x and R (where R = 1.0) -> points that are in the circle -> in the area under the curve
- fin is a integral / area under the curve
- in the end the function returns $4*fin$ -> a full circle area (4 * 1/4 circle area) -> $\pi*R*R$ where $R = 1.0$
- **function returns an approximation for $\pi$ with Monte Carlo simulation**
    - if $R \neq 1$ the funcion computes the area of a circle with the radius R
- new name: approxPi(N) 

## Comparison of the computational time
- using profile, results are in hw4.txt and hw4_improved.txt
- hw4.py as the non-vectorized version took 219.641 seconds in total

        ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        10000   68.656    0.007  216.031    0.022 hw4.py:16(approxPi)

- hw4_improved.py as the vectorized version took 3.797 seconds in total

        ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        10000    0.203    0.000    0.469    0.000 hw4_improved.py:16(approxPi)

- time savings of 98.25 %
    - time differenz: $219.641 s - 3.797 s = 215.844 s$
    - time savings: $(215.844 s / 219.641 s) * 100 = 98.25 \%$ 
- using numpy arrays is way faster than using for-loops