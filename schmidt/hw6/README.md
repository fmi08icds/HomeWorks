# Homework 6
## Complexity assessment
In the following, I will make estimates for the runtime complexity of kmeans.
The driving variables are number of points `n`, number of centroids `m`, and iterations until convergence `k`

### Vectorized implementation
My implementation uses vectorization. Hence, the runtime complexity is a bit more difficult to assess.
#### Function `euclidean_distance`
The euclidean distance is calculated using broadcasting. While the computation time will increase proportionally with `n` and `m`, the effect is far lower than with a looped implementation.

#### Function `update_centroids`
This function loops over each centroid to find the points with the lowest distance to it.
All other functions are vectorized or elementary operations.
Consequently, its runtime complexity is in `O(m)`

#### Function `k_means`
This function calls both `euclidean_distance` and `update_centroids` for each iteration in the while loop until convergence.
As the number of steps to convergence cannot directly be inferred from the number of points or centroids, I will use `k` to denote steps to convergence.
Given the complexity of `update_centroids`, the runtime complexity of `k_means` is `O(k*m)`

### Looped implementation
Assuming an implementation with loops and some usage of numpy arrays, I arrive at the following complexity estimates.

#### Function `euclidean_distance`
Loop over each point and within that loop over each centroid to calculate the distances: `O(n*m)`

#### Function `update_centroids`
Assuming that the previous function stores all points assigned to a centroid in an array, the runtime complexity is only dependent on `m`.
We loop over all centroids and find the mean of all points in the related cluster: `O(m)`

#### Function `k_means`
Similar to the vectorized implementation, we need to loop until convergence and call `euclidean_distance` and `update_centroids` in each iteration.
However, now `euclidean_distance` is the main driver of complexity with `O(n*m)`. 
Hence, the overall runtime complexity is in `O(k*n*m)`