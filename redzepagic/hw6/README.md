# Complexity
    The complexity of the k-means algorithm highly depends on the dimensionality of the data-points and on the amount of clusters k
    In this case k = 3 and d = 2
    1. calc_clusters:
        - calculates the distances of all points to all centroids => O(n*k*d)
        - checks which distance is the smallest => O(n*k)
    2. calc_centroids:
        - calculates the mean of all k clusters, which contain all in all n points => O(n*d)
    3. loop in main:
        - I cannot really say how many steps the algorithm needs until it converges
        - This highly depends on the initially chosen centroids
        - I put a limit of 500 iterations on it so in worst case O(500)
    4. all in all:
        - since the worst complexity here is O(n*k*d), this is the complexity of this algorithm