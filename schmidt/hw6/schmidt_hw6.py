import numpy as np
from typing import Tuple

def euclidean_distance(points: np.array, centroids: np.array) -> np.array:
    '''
    Calculates the euclidean distance between all point-centroid-combinations using broadcasting
    :param points:          numpy array containing the points to be clustered; Shape = (n, m)
    :param centroids:       numpy array containing the current centroids; Shape = (k, m)

    :return:                numpy array of shape (n, k) with the euclidean distance of each point to each centroid
    '''
    # 1. Create views on both arrays with an additional axisto use broadcasting
    points_expanded = points[:, np.newaxis, :]
    centroids_expanded = centroids[np.newaxis, :, :]

    # 2. Calculate the sum of squared differences for each point-centroid-combination
    # The sum is over axis=2, because axis=0 contains all points, axis=1 contains all centroids and axis=2 contains the respective coordinates
    sum_squared = np.sum((points_expanded - centroids_expanded) ** 2, axis=2)

    # 3. Return the square root of the sum of squared distances to get euclidean distance
    return np.sqrt(sum_squared)


def update_centroids(points: np.array, centroids: np.array, euc_dist: np.array) -> np.array:
    '''
    Updates the centroid coordinates based on the closest points (smallest euclidean distance)
    :param points:      numpy array containing the points to be clustered; Shape = (n, m)
    :param centroids:   numpy array containing the current centroids; Shape = (k, m)
    :param euc_dist:    numpy array of shape (n, k) with the euclidean distance of each point to each centroid

    :return:            Updated centroids based on the average coordinates of the closest points
    '''
    selected_centroids = np.argmin(euc_dist, axis=1)
    for i in range(centroids.shape[0]):
        cluster = points[selected_centroids == i]
        new_centroid = np.mean(cluster, axis=0)
        centroids[i, :] = new_centroid

    return centroids


def k_means(points: np.array, num_clusters: int) -> Tuple[np.array, float]:
    '''
    Applies k-Means as described in the Lloyd-Algorithm (https://en.wikipedia.org/wiki/K-means_clustering)
    :param points:          numpy array containing the points to be clustered; Shape = (n, m)
    :param num_clusters:    Number of clusters to form (Number of centroids)
    :return:                numpy array of the final centroids,
                            dist (average distance of all points to their closest centroid)
    '''
    # Randomly choose num_clusters centroids
    idx = np.random.randint(points.shape[0], size=num_clusters)
    centroids = points[idx]

    # Loop until convergence
    converged = False
    while not converged:
        old_centroids = np.copy(centroids)
        euc_dist = euclidean_distance(points, centroids)
        centroids = update_centroids(points, centroids, euc_dist)
        if np.array_equal(old_centroids, centroids):
            converged = True

    dist = np.mean(np.min(euc_dist, axis=1))
    return centroids, dist

if __name__ == '__main__':
    from scipy.cluster.vq import kmeans

    rng = np.random.default_rng(seed=1234)
    cl1 = rng.multivariate_normal([-2, -2], [[1, -0.5], [-0.5, 1]], size=100)
    cl2 = rng.multivariate_normal([1, 0], [[1, 0], [0, 1]], size=150)
    cl3 = rng.multivariate_normal([3, 2], [[1, -0.7], [-0.7, 1]], size=200)
    pts = np.concatenate((cl1, cl2, cl3))

    centroids, dist = k_means(points=pts, num_clusters=3)
    ctr, dst = kmeans(pts, 3)

    print('='*50)
    print('Own implementation')
    print('=' * 50)

    print('Centroids:')
    print(centroids)
    print(f'\nDistortion: {dist}')

    print('\n\n'+'=' * 50)
    print('Scipy')
    print('=' * 50)

    print('Centroids:')
    print(ctr)
    print(f'\nDistortion: {dst}')