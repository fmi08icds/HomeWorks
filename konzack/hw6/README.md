# Complexity of make_clusters
- nested iteration over every point and every centroid
- complexity of the distance computation depends on the dimensionality of the point 
- in total:  O(k\*n\*d) (k: number of clusters, n: number of data points, d: dimensionality)

# Complexity of the centroid update
- sum over 2d array
- O(n\*d)

# Complexity until convergence
- unknown amount of iterations required until the centroids converge
- capped at 10,000 iterations to prevent an inifite loop
- O(10,000)

# Total complexity
- putting all these steps together we get a total complexity of O(10,000\*k\*n\*d) which is O(k\*n\*d)