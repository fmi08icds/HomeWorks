# HW6

## K-Means Algorithm Time Complexity

The time complexity of the given *K-Means* clustering algorithm is  **O(i*m*n*k)**, where:

- **i** represents the maximum number of iterations ```(max_iter)``` allowed for the convergence of the algorithm.
- **m** denotes the number of data points in the dataset.
- **n** is the number of dimensions (features) per data point.
- **k** stands for the number of clusters (centroids) specified.

This time complexity is the result of key operations in the algorithm, as described below:

1. **Initialization of Centroids:** The algorithm randomly picks an initial centroid from the dataset, an operation which takes constant time, *O(1)*. The remaining centroids are then chosen based on distances from previous centroids, with a time complexity of *O(m*n*k)* due to the need to calculate Euclidean distances from each point to each centroid.

2. **Iteration Loop:** In each iteration, the algorithm assigns each data point to the nearest centroid and then recalculates the centroid locations. Both these operations have a time complexity of *O(m*n*k)*. The iteration continues until the centroids no longer change or the maximum number of iterations is reached. This results in a total time complexity of **O(i*m*n*k)**.

