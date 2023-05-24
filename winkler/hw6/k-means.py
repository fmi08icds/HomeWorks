import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.vq import kmeans


from typing import Tuple, Union
from numpy.typing import NDArray


def generate_points(seed: int):
    """Generate an array of 2D points sampled from three different normal distributions that represent three clusters."""
    rng = np.random.default_rng(seed=seed)
    return np.concatenate((
        rng.multivariate_normal([-2, -2], [[ 1, -0.5], [-0.5, 1]], size=100),
        rng.multivariate_normal([ 1,  0], [[ 1,    0], [   0, 1]], size=150),
        rng.multivariate_normal([ 3,  2], [[ 1, -0.7], [-0.7, 1]], size=200)
    ))


def my_kmeans(points: NDArray, k_or_initial_points: Union[int, NDArray]) -> Tuple[NDArray, float]:
    """K-means clustering algorithm
    Parameters:
        points: List of two-dimensional points as a NumPy array of shape (N, 2) where N >= k
        k_or_initial_points: Number of cluster centroids or array of initial centroids
    
    Returns:
        centroids: Position of cluster centroids as a Numpy array of shape (k, 2)
        distortion: Mean euclidean distance of points to there respective cluster centroid
    """

    if isinstance(k_or_initial_points, int):
        # randomly choose initial centroids if k is just a number
        k = k_or_initial_points
        centroids = points[np.random.randint(points.shape[0], size=k)]
    elif isinstance(k_or_initial_points, np.ndarray):
        # use points from parameter k as initial centroids
        k = len(k_or_initial_points)
        centroids = k_or_initial_points.copy()
    else:
        raise TypeError("Argument `k_or_initial_points` must be of type int or ndarray")
    
    # make sure that input matrix has the expected shape
    if points.shape[0] < k or points.shape[1] != 2:
        raise ValueError(f"Argument `points` must be of shape (N, 2) where N >= {k}")

    prev_distortion = None
    for _ in range(20):
        # compute distance to centroids for all points
        distances = np.linalg.norm(centroids.reshape((1, k, 2)) - points.reshape((-1, 1, 2)), axis=2)
        # compute mean distance to closest centroids
        distortion = np.mean(np.min(distances, axis=1))
        # store index of closest centroid for each point 
        closest_cluster = np.argmin(distances, axis=1)
        # compute new centroids for each cluster
        for i in range(k):
            centroids[i] = np.mean(points[closest_cluster == i], axis=0)

        # stop early if distortion does not change significantly anymore
        if prev_distortion is None or np.abs(prev_distortion - distortion) > 1e-5:
            prev_distortion = distortion 
        else:
            break
    
    return centroids, distortion


def main():
    # generate random points
    points = generate_points(1234)
    
    # choose initial centroids such that both implementations converge to the same result
    initial_centroids = points[np.random.randint(points.shape[0], size=3)]

    # performing clustering with own function and scipy function    
    centroids1, distortion1 = my_kmeans(points, initial_centroids)
    centroids2, distortion2 = kmeans(points, initial_centroids)

    # print coordinates of centroids
    print("Centroids:")
    print(f"  own: {centroids1!r}")
    print(f"  scipy: {centroids2!r}")

    # print distortion metric for both runs
    print("Distortion:")
    print(f"  own:   {distortion1:.7f}")
    print(f"  scipy: {distortion2:.7f}")

    # generate visualization 
    fig, ax = plt.subplots(1, 1, figsize=(5, 4))
    ax.scatter(points[:,0], points[:,1], s=3, c="#ccc")
    ax.scatter(centroids1[:,0], centroids1[:,1], marker="x", c="red", s=56, label="Own implementation")
    ax.scatter(centroids2[:,0], centroids2[:,1], marker="+", c="green", s=56, label="SciPy implementation")
    ax.set_title("Cluster centroids determined by different\nimplementations of K-means clustering algorithm")
    ax.legend()
    fig.savefig("result.png")


if __name__ == "__main__":
    main()
    