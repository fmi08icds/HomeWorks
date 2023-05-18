import numpy as np

# custom kmeans Implementation
# as a homework.
# first, implement the kmeans algorithm
# then, implement the kmeans++ algorithm
# finally, implement the kmeans|| algorithm.
def my_kmeans(input_data:np.ndarray, k:int, max_iter:int=100, tol:float=1e-4):
    """
    input_data: numpy array of shape (n_samples, n_features)
    k: number of clusters
    max_iter: maximum number of iterations
    tol: tolerance for stopping criteria
    """

    ## assign each data point to a cluster
    if input_data.shape[0] < k:
        raise ValueError("Number of clusters cannot be greater than number of data points")
    # initialize centroids
    centroids = input_data[np.random.choice(input_data.shape[0], k, replace=False)]
    # initialize cluster assignments, all zeros
    cluster_assignments = np.zeros(input_data.shape[0])
    # initialize distance matrix, all zeros, n x k matrix.
    distance_matrix = np.zeros((input_data.shape[0], k))
    # initialize old centroids, remember them.
    old_centroids = np.zeros(centroids.shape)
    # initialize error, for stopping criteria
    error = np.linalg.norm(centroids - old_centroids)
    # initialize iteration counter
    iteration = 0
    # loop until error is less than tolerance or max iterations is reached
    while error > tol and iteration < max_iter:
        # update old centroids
        old_centroids = centroids
        # update distance matrix
        for i in range(k):
            # for each point, compute the distance to each centroid
            distance_matrix[:, i] = np.linalg.norm(input_data - centroids[i], axis=1)
        # update cluster assignments, checks which entry in matrix is the smallest and assigns that cluster
        cluster_assignments = np.argmin(distance_matrix, axis=1)
        # update centroids, take the mean of all points in each cluster
        for i in range(k):
            centroids[i] = np.mean(input_data[cluster_assignments == i], axis=0)
        # update error // stopping criteria
        error = np.linalg.norm(centroids - old_centroids)
        # update iteration counter
        iteration += 1
    # return cluster assignments and centroids
    return cluster_assignments, centroids
