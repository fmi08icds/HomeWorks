import numpy as np


def k_means(data, k):
    """
    data: input data as an ndarray
    k:    number of intended clusters
    :return:
    centroids: a list of k centroids
    """
    # initialize centroids with the first k data points
    new_centroids = np.array(data[0:k])
    old_centroids = new_centroids + 1
    distances = np.empty(shape=(k, len(data)))
    while not np.array_equal(old_centroids, new_centroids):
        # calculate distances from the centroids
        for i in range(k):
            distances[i] = np.linalg.norm(data - new_centroids[i], axis=1)
        # assign each point to best cluster
        clusters = np.argmin(distances, axis=0)

        old_centroids = np.copy(new_centroids)
        # calculate new centroids
        for i in range(k):
            new_centroids[i] = np.mean(data[np.equal(clusters, i)], axis=0)
    return new_centroids


def main():
    rng = np.random.default_rng(seed=1234)
    cl1 = rng.multivariate_normal([-2, -2], [[1, -0.5], [-0.5, 1]], size=100)
    cl2 = rng.multivariate_normal([1, 0], [[1, 0], [0, 1]], size=150)
    cl3 = rng.multivariate_normal([3, 2], [[1, -0.7], [-0.7, 1]], size=200)
    pts = np.concatenate((cl1, cl2, cl3))
    centroids = k_means(pts, 3)
    print(centroids)


if __name__ == '__main__':
    main()
