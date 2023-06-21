"""
source: https://towardsdatascience.com/create-your-own-k-means-clustering-algorithm-in-python-d7d4c9077670
"""

import numpy as np
import random

def euclidean(point, data):
    """
    Euclidean distance between point & data.
    Point has dimensions (m,), data has dimensions (n,m), and output will be of size (n,).

    Parameters
    ----------
    point : numpy.ndarray
        The point to calculate the distance from.
    data : numpy.ndarray
        The data to calculate the distance to.
    """
    return np.sqrt(np.sum((point - data)**2, axis=1))

class KMeans:
    """ K-Means clustering algorithm, using Euclidean distance as the metric.

    Parameters
    ----------
    n_clusters : int, default=8
        The number of clusters to form as well as the number of centroids to generate.
    
    max_iter : int, default=300
        Maximum number of iterations of the k-means algorithm for a single run.
    """
    def __init__(self, n_clusters=8, max_iter=300):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X_train):
        """
        Fit the K-Means model to the data.

        Parameters
        ----------
        X_train : numpy.ndarray
            The data to fit the model to.
        """
        # Choose initial centroids randomly
        self.centroids = [random.choice(X_train)]

        # Choose remaining centroids based on distance from previous centroids
        for _ in range(self.n_clusters-1): 
            # Calculate distances from points to the centroids
            dists = np.sum([euclidean(centroid, X_train) for centroid in self.centroids], axis=0) 
            # Normalize the distances
            dists /= np.sum(dists)
            # Choose remaining points based on their distances
            new_centroid_idx, = np.random.choice(range(len(X_train)), size=1, p=dists)
            self.centroids += [X_train[new_centroid_idx]]

        # Iterate until convergence or max iterations
        iteration = 0
        prev_centroids = None
        while np.not_equal(self.centroids, prev_centroids).any() and iteration < self.max_iter:
            # Sort each datapoint, assigning to nearest centroid
            sorted_points = [[] for _ in range(self.n_clusters)]
            for x in X_train:
                dists = euclidean(x, self.centroids)
                centroid_idx = np.argmin(dists)
                sorted_points[centroid_idx].append(x)

            # Push current centroids to previous, reassign centroids as mean of the points belonging to them
            prev_centroids = self.centroids
            self.centroids = [np.mean(cluster, axis=0) for cluster in sorted_points]
            for i, centroid in enumerate(self.centroids):
                if np.isnan(centroid).any():  # Catch any np.nans, resulting from a centroid having no points
                    self.centroids[i] = prev_centroids[i]
            iteration += 1
        

    def evaluate(self, X):
        """
        Evaluate the K-Means model on the data.

        Parameters
        ----------
        X : numpy.ndarray
            The data to evaluate the model on.
        """
        centroids = []
        centroid_idxs = []
        # Sort each datapoint, assigning to nearest centroid
        for x in X:
            dists = euclidean(x, self.centroids)
            centroid_idx = np.argmin(dists)
            centroids.append(self.centroids[centroid_idx])
            centroid_idxs.append(centroid_idx)
        return centroids, centroid_idxs
    

