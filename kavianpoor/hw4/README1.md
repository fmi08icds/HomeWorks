##Analysis the code

The code is performing Monte Carlo simulation to estimate the value of pi using the method of finding the area of a quarter circle of radius 1 by generating random points within a square of side length 1 and counting the fraction of points that fall inside the quarter circle. The program generates M sets of N random points, calculates the fraction of points inside the quarter circle for each set, and uses these to calculate the mean and standard deviation of the estimator of pi. Finally, the code produces a histogram of the means.


##Analysis and optimization


The computational time for the non-vectorized version is 
1.0620510130029288 seconds, and for the vectorized version is 0.004999551005312242 seconds. As we can see, the vectorized version is significantly faster than the non-vectorized version. This is because the vectorized version is utilizing the built-in capabilities of numpy to perform operations on arrays, whereas the non-vectorized version is using for loops to iterate over individual elements. Using vectorized operations in numpy can significantly improve the performance of numerical computations.



local/bin/python3 /Users/sepidehkavianpoor/Desktop/NoName_Vector.py
/Users/sepidehkavianpoor/Desktop/NoName_Vector.py:48: DeprecationWarning: The truth value of an empty array is ambiguous. Returning False, but in future this will result in an error. Use `array.size > 0` to check that an array is not empty.
  if (list_y[i]< f(list_x[i],R)) :
Non-vectorized time: 1.0620510130029288
Vectorized time: 0.004999551005312242
Mean of the means: 0.0
Std of the means: 0.0
Mean of the stds: 0.0
Std of the stds: 0.0