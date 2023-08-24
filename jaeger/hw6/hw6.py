import numpy as np


def k_means(pts, k, max_iterations=100):
    # Randomly initialize the centroids
    centroids = pts[np.random.choice(range(len(pts)), k, replace=False)]

    for _ in range(max_iterations):
        # Assign each data point to the closest centroid
        labels = assign_labels(pts, centroids)

        # Update the centroids based on the assigned data points
        new_centroids = update_centroids(pts, labels, k)

        # Check if the centroids have converged
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    distance = calc_distance(centroids, pts, labels)

    return centroids, distance


def assign_labels(pts, centroids):
    # Compute the Euclidean distance between each data point and each centroid
    distances = np.sqrt(np.sum((pts[:, np.newaxis] - centroids) ** 2, axis=2))

    # Assign each data point to the closest centroid
    labels = np.argmin(distances, axis=1)

    return labels


def update_centroids(pts, labels, k):
    new_centroids = np.zeros((k, pts.shape[1]))

    # Update each centroid by computing the mean of the assigned data points
    for i in range(k):
        cluster_data = pts[labels == i]
        new_centroids[i] = np.mean(cluster_data, axis=0)

    return new_centroids


def calc_distance(centroids, pts, labels):
    # Calculate the mean Euclidean distance between observations and centroids
    distances = []
    for i in range(len(centroids)):
        cluster_data = pts[labels == i]
        centroid = centroids[i]
        cluster_distance = np.mean(np.sqrt(np.sum((cluster_data - centroid) ** 2, axis=1)))
        distances.append(cluster_distance)

    mean_distance = sum(distances) / len(distances)
    return mean_distance


def main():
    rng = np.random.default_rng(seed=1234)
    cl1 = rng.multivariate_normal([-2, -2], [[1, -0.5], [-0.5, 1]], size=100)
    cl2 = rng.multivariate_normal([1, 0], [[1, 0], [0, 1]], size=150)
    cl3 = rng.multivariate_normal([3, 2], [[1, -0.7], [-0.7, 1]], size=200)
    pts = np.concatenate((cl1, cl2, cl3))

    # Apply k-means clustering with k=3
    ctr, dist = k_means(pts, k=3)

    ## COMMENTS: a plot would have illustrated your results better
    # Print mean distance and centroids
    print("Ctr:", ctr)
    print("Dist:", dist)


if __name__ == '__main__':
    main()
