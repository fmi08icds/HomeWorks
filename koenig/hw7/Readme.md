# Homework 7: Differential Evolutionary Algorithm

Author: Ralf König, 20 June 2023

## Sources
I used the template from
https://github.com/fmi08icds/Coding/blob/main/src/template_hw6.py

## Use of the program

Run program with arguments as given in the template.

To change between the three fitness functions, 
please uncomment lines in `def f(x):` AND adjust `n` via
command-line argument ``-n`` or in the default value of the
`params` dict to the correct number of dimensions (1, 2 or 3 
for fitness function 1, 2, and 3 respectively).

## Implementation

I used a `Population` class to have a common class where
all the relevant methods can be attached.

During mutation, values are clipped at the solution space
boundaries to keep the search on the region of interest.

Instead of the best population (which prints rather lengthy),
I output the best overall solution found. You can change
this via uncommenting the original line of code.

## Results

For all three functions, solutions are found that make 
sense and are near the global minimum.

###  `x**4 + x³ - x² - x`
Function from "Introduction to Computing in Data Science"
lecture slides.
True global minimum is at f(0.64039) = -0.61968.

### `x[0]² + x[1]²`
Sphere Model A.1 with function $f_1$ from book page 86.
True global minimum is at f(0,0) = 0.

###  Rosenbrock's function `f5` from book for n=3

This is the function $f_5$ from the book "Advances in Evolutionary
Computing", Chapter "Fast Evolutionary Algorithms", page 87, 
"Generalized Rosenbrock's Function". I used three dimensions 
as given during class.

The bounds are particularly important here. 
For xL, xU= (-3, 3), a point near the minimum is found 
with 50 generations and a population size of 100.

For xL, xU= (-30, 30), it is hard for the algorithm to find
a point close to the minimum with 50 generations 
and a population size of 100, as the function rises so
quickly and as there is *no* gradient descent.

True global minimum is at f(1,1,1) = 0.

###  Rosenbrock's function `f5` from book for n=30

* xL, xU = (-3, 3)
* 100 generations
* Population size: 100
* Number of opponents in selection: q = 10

The algorithm descends in mean fitness, and therefore improves,
but hardly ever finds any good solution near the true 
optimal one at f(1,...,1) = 0.

It is pretty much lost in solution space.

With wider bounds:

* xL, xU = (-30, 30)
* 200 generations
* Population size: 100
* Number of opponents in selection: q = 10

this shows a similar pattern: quickly improving fitness 
in the first ~50 generations, then lost in solution space.
