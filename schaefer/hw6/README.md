# Homework 6

## complexity of k-means

The complexity of the k-means-algorithm can be divided into 2 main iterations:

1. initialization of the cluster centers: 
   1. The initialization starts with a random selection of data points. This requires on average, as many operations as there are clusters O(num_clusters).
   2. The iteration of the distance between every data point and the initiated cluster centers needs O(num_clusters * num_data_points * num_dimensions) Operations because we need the distance for every data point and the cluster centres.
2. iteration loop for updating the cluster centers:
   1. the iteration loop gets executed for at max 'max_iterations' times
   2. In each iteration, the assignments of the data points to the clusters are recomputed, which requires O(num_data_points * num_clusters * num_dimensions) operations.
   3. Updating the cluster centers by the average of their data points requires O(num_clusters * num_data_points * num_dimensions) operations.
   4. The convergence check is done by comparing the old and new cluster centers, which requires O(num_clusters * num_dimensions) operations.

So the overall complexity depends on these factors:

- number of clusters (num_clusters)
- number of data points (num_data_points)
- number of dimensions (num_dimensions)
- max number of iterations (max_iterations)

Which leads to the following complexity:
O(max_iterations * num_data_points * num_clusters * num_dimensions)
