## uniform(a,b)
It returns a random number between a and b - so [a,b).

## f(x,R)
This function calculates the positive y-value of a centered circle with radius R at position x.
<br>
Condition: x has to be a valid x-value on the circle. If not the function returns a nonsensical y-value.
## calculate_pi(N)
This function estimates pi experimentally.
<br>
N points (x,y) with x,y in [0,1) get generated. x² + y² = 1 is a function that describes a circle with radius 1 and centre 0. In the list 'list_accepted' x-values get added where y \< (1-x²). By limiting the x and y values to positive numbers we only look at a quarter of the circle (first quadrant). So we generate points in a one by one square and see whether they lie within the quarter circle. The probability of this happening is (pi\*1²/4)/1². Conversely, pi = 4\*p.
<br>
The probability gets approximated by dividing the number of accepted values by the total number of points. (To note: The bigger the input N the more accurate the approximation will become). Finally, p gets multiplied by 4 to get pi.

## main
We generate M=100 samples where for each sample pi gets estimated with N=1000. Out of these samples we calculate the mean and standard deviation which get added to the appropriate lists. We repeat this M times and finally plot a histogram based on the means. 

