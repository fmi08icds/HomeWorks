
import numpy as np
import matplotlib.pyplot as plt
def kmeans(X, k, max_iters=100):
    # Initialisiere Zentroide zufällig
    centroids = X[np.random.choice(range(len(X)), size=k, replace=False)]

    for _ in range(max_iters):
        # Weise jedem Punkt den nächstgelegenen Zentroid zu
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=-1)
        labels = np.argmin(distances, axis=1)

        # Aktualisiere die Zentroide
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

        # Überprüfe Konvergenz
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return centroids, labels

def main():
    rng = np.random.default_rng(seed=1234)
    cl1 = rng.multivariate_normal([-2, -2], [[1, -0.5], [-0.5, 1]], size=100)
    cl2 = rng.multivariate_normal([1, 0], [[1, 0], [0, 1]], size=150)
    cl3 = rng.multivariate_normal([3, 2], [[1, -0.7], [-0.7, 1]], size=200)
    pts = np.concatenate((cl1, cl2, cl3))
    centroids = kmeans(pts, 3)
    print("Centroids:", centroids)

if __name__ == '__main__':
    main()


