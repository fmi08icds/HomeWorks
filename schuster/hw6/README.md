# HW 6 - implementation of kMeans

## time complexity of the code hw6_kmeans.py

### euclidean(centroid, data)
- time complexity of O(n) for computing the distance of one data point and the centroid
- time complexity of O(n*m) for computing the distance for all data points

### compute_centroid(cluster)
- sums the coordinates and devides by number of points
- time complexity is O(d * n_i) with d ias dimensionality of data, n_i as number of data points in cluster

### kMeans
- time determined by:
    - number of data points (n)
    - number of clusters (k)
    - maximum number of iterations (max_iter)
- time complexity: O(n * k *  max_iter)

## Computational time
- using profile with python -m profile -s cumtime hw6_kmeans.py, results are in hw6.txt
- programm needs around 3.5 seconds while using profile