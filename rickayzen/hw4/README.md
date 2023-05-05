# Structure
Project consists of the og script as well as the script that was improved through the vectorisation. Both scripts execute performance tests with the argument --p. The performance tests prints the execution time and also writes it in its according performance files.
# Performance
The improved version is roughly twice as fast

| n        | time (s) old | time (s) new | 
|----------|--------------|--------------|
| 100      | 0.000179     | 0.000203     |
| 1000     | 0.001438     | 0.000968     |
| 10000    | 0.014132     | 0.007782     |
| 100000   | 0.140603     | 0.086775     |
| 1000000  | 1.496187     | 0.861669     |
| 10000000 | 15.37732     | 8.424660     |
| 50000000 | 76.29096     | 42.74579     |
# Explanation of function
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

