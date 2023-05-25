import numpy as np
from random import randint


def my_kmeans(data: np.ndarray, k=2, centroids: np.ndarray = None, max_iter=99):
    """
    A simple implementation of k-means using only numpy.
    This implementation uses the L^1 metric (aka manhattan distance)!
    :param data: an (n,d) numpy.ndarray where n is the number of data points
    and d is the dimension of each point
    :param k: the number of clusters one wants to cluster the data to
    :param centroids: initial centroids as (k, d) ndarray.
    Will be randomly chosen by default.
    :param max_iter: max number of iterations of calculating new centroids
    :return: A tuple of three:
    1. cluster-id array (cluster label for each data point in input-data)
    2. cluster-dictionary containing the data points for each cluster label
    3. the overall error this clustering has
    """
    # Get and check the right shape
    n, d = data.shape  # n is the number of data points, d is a points dimension
    if k >= n:
        if k == n:
            return data
        else:
            raise ValueError("k is greater than the number of data points!")
    # Get the right centroids-array shape
    c_shape = (k, d)

    if centroids is None or centroids.shape != c_shape:
        # Randomly initialize k centroids
        centroids = np.empty(shape=c_shape)
        i = 0
        while i < k:
            rand_idx = randint(0, n - 1)
            # If not already contained in centroids, add it
            if not (data[rand_idx] == centroids).all(axis=1).any():
                centroids[i] = data[rand_idx]
                i += 1

    # Start the clustering iteration:
    i = 0
    while True:
        # I use the L^1 (or "manhattan") metric
        # as its computation is faster and more stable than the Euclidean one,
        # and it is perfectly sufficient for k-means.
        dists = (np.abs(data[None, :, :] - centroids[:, None, :])).sum(axis=2)

        c_ids = dists.argmin(axis=0)  # Cluster ids/labels {0,...,k}.

        dist_error = dists.min(axis=0).sum()  # Accumulated distance (the error)

        # Get the clusters and update centroids:
        cluster_dict = dict()
        new_centroids = centroids.copy()
        for c_index in range(k):
            cluster = data[c_ids == c_index]
            if cluster.shape == (0, d):
                continue  # May be empty if initial clusters were set far away..
            cluster_dict[c_index] = cluster  # c_index'th cluster
            # Calculate the new centroids
            new_centroids[c_index] = np.mean(cluster_dict[c_index], axis=0)
        # Stop if centroids did not change.
        if (centroids == new_centroids).all() or i > max_iter:
            break  # Stop the while loop.
        centroids = new_centroids
        i += 1

    return c_ids, centroids, cluster_dict, dist_error
