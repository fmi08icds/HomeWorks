import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=1234)
cl1 = rng.multivariate_normal([-2, -2], [[1, -0.5], [-0.5, 1]], size=100)
cl2 = rng.multivariate_normal([1, 0], [[1, 0], [0, 1]], size=150)
cl3 = rng.multivariate_normal([3, 2], [[1, -0.7], [-0.7, 1]], size=200)
pts = np.concatenate((cl1, cl2, cl3))


def k_means(pts, k, iterations=100):
    centers = pts[np.random.choice(range(len(pts)), size=k, replace=False)]
    clusters = np.zeros(len(pts))

    for _ in range(iterations):
        for i, pt in enumerate(pts):
            distances = np.linalg.norm(centers - pt, axis=1)
            clusters[i] = np.argmin(distances)

        for j in range(k):
            cluster_pts = pts[clusters == j]
            centers[j] = np.mean(cluster_pts, axis=0)

    return clusters, centers


k = 3
clusters, centers = k_means(pts, k)
plt.scatter(pts[:, 0], pts[:, 1], c=clusters, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('k-means Clustering')

plt.show()