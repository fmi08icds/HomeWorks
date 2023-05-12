- the code in hw4.py is commented containing all the nessecary information

# Summary
- f(x,R) given a function for a circle around (0,0) with Radius R
- in the former NoName function, we integrate this function from 0 to R
- this gives us 1/4 of the area of a circle
- returning 4 times this integral gives us the area of the entire circle
- the circle are is given by pi times R^2
- with R fixed to 1 this just gives us pi
- in the main function we average over M runs M times and plot the resulting pi approximations

# Optimziation
- vectorized function is found in vectorized_approximate_pi
- the function is explained by comments in the code

# Runtime analysis
- results of the profiling are stored in out.txt and out_vec.txt
- runtime of unvectorised function: 58.40s
- runtime of vectorised function: 2.66s
- the vectorised version runs over 20x faster