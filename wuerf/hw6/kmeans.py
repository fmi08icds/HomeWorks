# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# Generate data
rng = np.random.default_rng(seed=1234)
cl1 = rng.multivariate_normal([-2, -2], [[1, -0.5], [-0.5, 1]], size=100)
cl2 = rng.multivariate_normal([1, 0], [[1, 0], [0, 1]], size=150)
cl3 = rng.multivariate_normal([3, 2], [[1, -0.7], [-0.7, 1]], size=200)

pts = np.concatenate((cl1, cl2, cl3))


# %%
def kmeans(points: np.array, amount_of_centroids: int, max_iterations=1000) -> tuple[np.array, np.array]:
    """
    Computes the centroids of the given points. The amount of centroids depends
    on the specified amount. The algorithm initializes the centroids and
    iteratively refines. The iterative refinement also includes an update of the
    assignment of each input point to its current cluster. In general the
    refinement loop contains two steps. First there is a assignment step 
    generating the current best clusters depending of the euclidean distance
    from each point to each centroid. The second step computes the new
    centroids by generating the means from the cluster assignments of the previous
    step.
    
    Args:
        points: The points that should be clustered
        amount_of_centroids: The amount of centroids that should be generated
        max_iterations: A limit for the amount of refinement steps the algorithm
                        performs

    Returns
        current_centroids: The centroids after the final refinement step
        min_distance_centroid_id: The cluster assignments after the final
                                  refinement step. Each entry of the array is a
                                  cluster id. The index of the entry corresponds
                                  to the index of the point in the input points
                                  argument to this function.

    """

    rng = np.random.default_rng(seed=1234)
    current_centroids = rng.multivariate_normal(
        [-2, 2], [[1, 1], [-0.5, 1]], size=amount_of_centroids
    )
    min_distance_centroid_id = None

    for i in range(max_iterations):
        # Assignment step
        distances = np.linalg.norm(
            np.expand_dims(pts, axis=0) - np.expand_dims(current_centroids, axis=1),
            axis=2,
        )
        min_distance_centroid_id = np.argmin(distances, axis=0)
        partition_masks = [
            min_distance_centroid_id == centroid_id
            for centroid_id in range(amount_of_centroids)
        ]
        current_partitions = np.split(
            points, np.cumsum([mask.sum() for mask in partition_masks[:-1]])
        )

        # Update step
        current_centroids = np.array(
            [np.mean(partition, axis=0) for partition in current_partitions]
        )

    return current_centroids, min_distance_centroid_id


# %%
centroids, point_idx_to_centroid = kmeans(pts, 3)

# %%

# Transform data do make plotting easy peasy
points_to_plot = pd.DataFrame()
points_to_plot["target"] = point_idx_to_centroid
points_to_plot["x"] = pts[:, 0]
points_to_plot["y"] = pts[:, 1]

centroids_to_plot = pd.DataFrame()
centroids_to_plot["target"] = range(3)
centroids_to_plot["x"] = centroids[:, 0]
centroids_to_plot["y"] = centroids[:, 1]

# %%
palette = sns.color_palette("hls", 10)
plt.figure(figsize=(16, 7))
# Plot points
sns.scatterplot(
    x="x", y="y", hue="target", palette=palette, data=points_to_plot, legend="full"
)
# Plot centroids
sns.scatterplot(
    centroids_to_plot, x="x", y="y", hue="target", palette=palette, s=1000, linewidth=10
)
