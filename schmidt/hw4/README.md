# Homework 4
## Understanding the function
The function approximates pi as discussed in class:
1. Generate random points in a square (with edge length `R`)
   - Create empty lists of `x` and `y` coordinates: `list_x` and `list_y`
   - Generate points uniformly at random with coordinates between `0` and `R=1`
   
2. Count number of points in a quarter-circle (within the square and with radius `R`)
   - For all points, check if they fall into the quarter circle using the function `f(x, R)`
   - `f` takes the equation for points on the curve of a circle, `y^2 + x^2 = R^2` and solves for `y`: `y=np.sqrt(abs(x^2-R^2))`
   - So, for all random points `i`, it is checked if the value for `y` is smaller than that for a point on the curve the circle. If so, the point is in the circle and added to `list_accepted_x`
   
3. Calculate ratio of points inside the quarter-circle to all points approximates pi
   - Count number of points in the circle: `Ninf = len(list_accepted_x)`
   - Divide this number by all points `fin = Ninf/float(N)`
   - Return `4*fin` for the estimate of pi as a quarter circle was used

Specifically, it is an implementation of the Monte-Carlo method for estimating pi as described [here](https://groups.uni-paderborn.de/reiss/AnalyseBuch/Grundlagen/Geometrie/pi/area.html?i=index) (in German).


