import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.vq import kmeans

rng = np.random.default_rng(seed = 1234)
cl1 = rng.multivariate_normal([-2,-2], [[1,-0.5],[-0.5,1]], size=100)
cl2 = rng.multivariate_normal([1,0], [[1,0],[0,1]], size=150)
cl3 = rng.multivariate_normal([3,2], [[1,-0.7],[-0.7,1]], size=200)
pts = np.concatenate((cl1,cl2,cl3))

ctr, dist = kmeans(pts, 3)
print("scipy kmeans centroids")
print(ctr)

def make_clusters(pts: np.ndarray, centroids: np.ndarray):
    """ Get an array of points for each cluster and the sizes of the arrays """
    D = 2

    assert len(pts.shape) == 2
    assert pts.shape[1] == D

    k = centroids.shape[0]
    n = pts.shape[0]

    clusters = np.full((k, n, D), np.nan, dtype=np.float64)
    sizes = np.zeros(k, dtype=np.int32)

    for i, point in enumerate(pts):
        # Find the closest centroid
        distances = [np.linalg.norm(point - centroid) for centroid in centroids]
        closest_centroid = np.argmin(distances)
        clusters[closest_centroid][i] = point
        sizes[closest_centroid] += 1

    return clusters, sizes

def my_kmeans(pts: np.ndarray, k: int):
    """ Custom kmeans implementation """
    D = 2
    assert len(pts.shape) == 2
    assert pts.shape[1] == D

    # Init k clusters
    indices = np.random.randint(pts.shape[0], size=k)
    centroids = pts[indices]

    clusters, _ = make_clusters(pts, centroids)
    for _ in range(10000):
        # Get a an array of points for each cluster
        clusters, _ = make_clusters(pts, centroids)

        # Calculate new centroids
        new_centroids = np.nanmean(clusters, axis=1)

        if np.array_equal(centroids, new_centroids):
            break
        centroids = new_centroids

    return centroids, clusters

my_centroids, clusters = my_kmeans(pts, 3)
print("own implementation centroids")
print(my_centroids)

# Plot the points
x = pts[:, 0]
y = pts[:, 1]

colors = np.sum(clusters, axis=2)
colors[~np.isnan(colors)] = 1.
colors = np.nansum(colors * np.array([0., 1., 2.])[:, np.newaxis], axis=0)

plt.scatter(x, y, c=colors)
plt.show()
