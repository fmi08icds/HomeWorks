import numpy as np
import matplotlib.pyplot as plt

def initialize_clusters(data, num_clusters):
    # Initialize clusters randomly by randomly choosing 'num_clusters' data points from 'data'.
    rng = np.random.default_rng()
    centers = rng.choice(data, size=num_clusters, replace=False)
    return centers

def assign_data_to_clusters(data, centers):
    # Assign each data point to the cluster with the smallest distance (Euclidean distance) to its center.
    distances = np.linalg.norm(data[:, np.newaxis] - centers, axis=-1)
    labels = np.argmin(distances, axis=1) ##COMMENTS: good
    return labels

def update_clusters(data, labels, num_clusters):
    # Update the cluster centers based on the current assignment of data points to clusters.
    new_centers = []
    for k in range(num_clusters):
        if np.sum(labels == k) > 0:
            # If the cluster is not empty, calculate the mean of all data points assigned to it as the new center.
            new_centers.append(data[labels == k].mean(axis=0))
        else:
            # If the cluster is empty, choose a new data point at random as the new center.
            new_centers.append(np.random.choice(data))
    new_centers = np.array(new_centers)
    return new_centers

def kmeans(data, num_clusters, max_iterations=10000):
    # Perform k-means clustering to find cluster centers.

    # Step 1: Initialize cluster centers randomly.
    centers = initialize_clusters(data, num_clusters)

    for _ in range(max_iterations):
        # Step 2: Assign data points to the cluster with the smallest distance to its center.
        labels = assign_data_to_clusters(data, centers)

        # Step 3: Update cluster centers based on the current assignment of data points to clusters.
        new_centers = update_clusters(data, labels, num_clusters)

        # Check if the cluster centers no longer change (convergence criterion).
        if np.all(centers == new_centers):
            break

        # Update the cluster centers for the next iteration.
        centers = new_centers

    return centers, labels

# Generate random data points in three clusters.
rng = np.random.default_rng(seed=1234)
cl1 = rng.multivariate_normal([-2, -2], [[1, -0.5], [-0.5, 1]], size=100)
cl2 = rng.multivariate_normal([1, 0], [[1, 0], [0, 1]], size=150)
cl3 = rng.multivariate_normal([3, 2], [[1, -0.7], [-0.7, 1]], size=200)
data = np.concatenate((cl1, cl2, cl3))

num_clusters = 3
# Perform k-means clustering on the data.
centers, labels = kmeans(data, num_clusters)

# Visualize the data points and cluster centers using a scatter plot.
plt.scatter(data[:, 0], data[:, 1], c=labels) ## COOMENTS: good :)
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=100)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Clustering with k-means algorithm')

plt.show()
