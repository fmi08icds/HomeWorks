# HW4

## Code Explanation:

The function ```uniform(a,b)``` generates a random number between *a* and *b* using the uniform distribution. The two input arguments *a* and *b* represent the lower and upper bounds of the uniform distribution. The expression *(b-a)*np.random.random()* generates a random number between *0* and *b-a*, which is then shifted by *a* to generate a random number between *a* and *b*.

The function ```f(x,R)``` calculates the height of a quarter-circle with radius *R* at a given x-coordinate *x* using the Pythagorean theorem. It takes two input arguments *x* and *R*, where *x* is the x-coordinate of the point and *R* is the radius of the quarter-circle. The expression *(x * x - R * R)* calculates the distance between the point (x,0) and the right endpoint of the quarter-circle (R,0). The ```abs()``` function takes the absolute value of the distance to ensure that it is positive. The ```np.sqrt()``` function calculates the square root of the distance, which represents the height of the quarter-circle at the given x coordinate.

The function ```NoName(N)``` function uses the Monte Carlo method to estimate the value of *pi* by generating *N* random points and checking how many of them fall within a quarter-circle with radius *R*. The method relies on the fact that the ratio of the area of the quarter-circle to the area of the square that encloses it is equal to *pi/4*, so the estimated value of *pi* can be calculated by multiplying the ratio by *4*. 

Running the function as it is took around **60.91** seconds. 

## Optimizing the Code:
The ```MonteCarlo_vec``` function avoids using for-loops and lists to generate the random *x* and *y* coordinates. Instead, it uses the vectorized ```numpy.random.uniform``` function to generate the coordinates directly as arrays, which is more efficient because it is implemented in low-level code and can generate random numbers in batches, rather than one at a time.

Using for-loops and lists to generate the coordinates requires the program to constantly allocate and deallocate memory for the growing lists, which can be slow and memory-intensive. In contrast, generating the coordinates as arrays using ```numpy.random.uniform``` is much faster because it can generate all the coordinates in one go, without the overhead of allocating memory for each coordinate one at a time. 

Similarly, the *list_accepted_x* array that stores the accepted *x* coordinates is also generated using **vectorized boolean indexing**. This avoids the need for a for-loop to iterate over all the generated *x* and *y* coordinates and test each one. Instead, the numpy boolean indexing selects only the x values that correspond to the y values that fall below the curve defined by the ```f``` function, which is much faster and more memory-efficient.

Running the ```MonteCarlo_vec``` function took around **1.16** seconds, which is a significant improvement over the original function. The improvment rate is around **98.1%**.