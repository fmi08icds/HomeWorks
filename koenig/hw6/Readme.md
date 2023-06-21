# Home work 6

Ralf König, 24.05.2023

# K-Means Clustering

The code is in ``k_means.py``.
This is a simple Python file that can be started right away and does
k-means processing on the sample data from ``day6.pdf``, page 3.

# Complexity estimate

O(`n*k`)

* `n` is length of input vector ``data``
* `k` is number of clusters.

Inside the while loop, there are two loops over k that I did not 
know how to vectorize any further.

The other calculations are vectorized using numpy functions.

No real statement can be made on the number of the repetitions in
the while loop as this depends on the data. The algorithm however
gets quickly to some solution.

# Test results

The result:

``[ 0.85818897, -0.16375323]``

``[-2.05529581, -1.89758246]``

``[ 2.87600351, 1.942986  ]]``

matches quite well with the centroids of the distributions in the 
simulated data:

``[ 1, 0]``

``[-2, -2]``

``[ 3, 2  ]]``
