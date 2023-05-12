# Homework 4
## Understanding the function
The function approximates pi as discussed in class:
1. Generate `N` random points in a square (with edge length `R`)
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


## Vectorization
### First loop
The first for loop can be vectorized using [`np.random.uniform`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html).
Simply provide `R` as the upper limit and `N` for the size:
```
array_x = np.random.uniform(low=0.0, high=R, size=(N,))
array_y = np.random.uniform(low=0.0, high=R, size=(N,))
```

### Second loop
The second loop can be vectorized in two steps:
1. Create the values on the curve of the quart-circle in one go using [`np.apply_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html)
```
array_curve = np.apply_along_axis(f, 0, array_x, R)
```

2. Compare the values on the curve with the coordinates for `y` and take the sum (Number of `True` values:
```
Ninf = np.sum(array_y < array_curve)
```

### Time comparison
The notebook [runtime_hw4.ipynb](./runtime_hw4.ipynb) compares the runtime of looped and vectorized implementation on a set of numbers.
There is a clear speed improvement due to vectorization (though it levels off for the last number):

```
Percentage reduction in time for each number N
1000: 0.6824696802646086
10000: 0.9721499617444529
100000: 0.972448158358876
1000000: 0.989382674335516
10000000: 0.9862882451860941
```
