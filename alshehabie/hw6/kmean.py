import numpy as np
import matplotlib.pyplot as plt

def kmeans(X, n_clusters, max_iters=100):
    # Initialize cluster centers randomly
    centers = X[np.random.choice(range(X.shape[0]), size=n_clusters, replace=False)]

    for _ in range(max_iters):
        # Assign each data point to the nearest cluster center
        distances = np.linalg.norm(X[:, np.newaxis] - centers, axis=-1)
        labels = np.argmin(distances, axis=1)

        # Update cluster centers
        new_centers = np.array([X[labels == k].mean(axis=0) for k in range(n_clusters)])

        # Check convergence
        if np.all(centers == new_centers):
            break

        centers = new_centers

    return labels, centers

# Generate some sample data
np.random.seed(100)
X = np.concatenate([np.random.normal(loc=(5, 5), size=(75, 2)),
                    np.random.normal(loc=(-5, -5), size=(75, 2))])

# Apply K-Means clustering
n_clusters = 5
labels, centers = kmeans(X, n_clusters)

# Plotting the clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centers[:, 0], centers[:, 1], marker='*', color='red', s=75)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-Means Clustering')

plt.show()
