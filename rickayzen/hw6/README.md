# Overview
kmeans contains the implemented k\_means method and its helper functions. The helper functions have been tested with test/test.py. Executing the kmeans script will also generate examples for 1D-, 2D- and 3D-data. The data is generated through np.random whose seed number will be printed out.
<break>
Also added the two further plots: A plot containing data samples around three clusters as well as a plot of the data which was clustered using my method.
<break>
performance.py monitors the performance through cProfiler by altering the n-, dim-, and k-value and compares the performance to scipy.

# Performance
My method and scipy's method return the same complexity. In general mine returns slightly better numbers although I imagine it's because my initial means are chosen randomly while scipy's is probably determined through a probabilistic method that increases the distance between the initial means in order to improve the results.

| n-dimension-range-k   |   total calls (kmeans) |   total calls (scipy) |
|-----------------------|------------------------|-----------------------|
| 1000-2-50-2           |                 583449 |                656594 |
| 5000-2-50-2           |                4632199 |               4696984 |
| 10000-2-50-2          |               14237706 |              14301666 |
| 1000-1-50-2           |               14938154 |              14975989 |
| 1000-3-50-2           |               15612477 |              15680232 |
| 1000-10-50-2          |               17324461 |              17460746 |
| 1000-2-50-5           |               19033450 |              19113305 |
| 1000-2-50-10          |               27207022 |              27332692 |
| 1000-2-50-20          |               38797946 |              38928016 |
| 1000-5-50-5           |               45218772 |              45365837 |
| 1000-5-50-10          |               59203468 |              59367803 |
