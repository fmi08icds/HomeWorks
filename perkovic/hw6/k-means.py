import numpy as np

# Set the random seed
rng = np.random.default_rng(seed=1234)

# Generate the data points
cl1 = rng.multivariate_normal([-2, -2], [[1, -0.5], [-0.5, 1]], size=100)
cl2 = rng.multivariate_normal([1, 0], [[1, 0], [0, 1]], size=150)
cl3 = rng.multivariate_normal([3, 2], [[1, -0.7], [-0.7, 1]], size=200)
pts = np.concatenate((cl1, cl2, cl3))

# Define the number of clusters
k = 3

# Initialize the centroids randomly
centroids = []
for _ in range(k):
    centroid = [rng.uniform(-5, 5), rng.uniform(-5, 5)]
    centroids.append(centroid)

# Iterate until convergence
iterations = 100
for _ in range(iterations):
    # Assign each point to the nearest centroid
    labels = []
    for point in pts:
        distances = [np.linalg.norm(point - centroid) for centroid in centroids]
        label = np.argmin(distances)
        labels.append(label)

    # Update the centroids based on the mean of the assigned points
    for i in range(k):
        cluster_pts = [pts[j] for j in range(len(pts)) if labels[j] == i]
        if cluster_pts:
            centroids[i] = np.mean(cluster_pts, axis=0)

# Print the cluster labels and centroids
print("Cluster Labels:")
print(labels)
print("Cluster Centroids:")
print(centroids)
