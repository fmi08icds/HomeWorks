import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans

def km_means(data, number_of_clusters, initail_centroids=None):
    '''
    Given an initial choice of k centroids (or randomly generated), all
    points should be added to the cluster with the nearest centroid.
    Repeat until convergence (no changes):
    - Recalculation of centroids
    - Assignment of all points to the cluster with nearest centorids.

    inputs:
    @data: the datat that should be clustered
    @number_of_clusters: the number of clusters
    @initail_centroides: either the initail is given or they get randomly initalized.

    returns:
    @cluster_assignments: the cluster assignment of each data point
    @centroids: the final centroids of the clusters
    '''

    # Checks , if the initail_centroids are provided explicitly
    if initail_centroids is not None:
        centroids = initail_centroids
    else:
        # Randomly choose the centroids
        random_centroids_indices = np.random.choice(data.shape[0], number_of_clusters, replace=False)
        centroids = data[random_centroids_indices]


    # Iterate until convergence
    while True:

        # Calculate the distance between all points and the centroids
        distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)

        # Assign points to the centroid with the smallest distance
        assignments = np.argmin(distances, axis=1)

        old_centroids = centroids.copy()

        # Calculate the mean of each assignment group
        means = [np.mean(data[assignments == i], axis=0) for i in range(len(centroids))]

        # update the centroids
        centroids = np.array(means)

        # Check for convergence
        if np.array_equal(centroids, old_centroids):
            break


    return assignments, centroids





if __name__ == "__main__":

    # Set the seed for reproducibility
    rng = np.random.default_rng(seed = 1234)

    # Generate data for three clusters
    cl1 = rng.multivariate_normal([-2,-2], [[1,-0.5], [-0.5,1]],size= 100)
    cl2 = rng.multivariate_normal([1,0],[[1,0],[0,1]], size= 150)
    cl3 = rng.multivariate_normal([3,2],[[1,-0.7],[-0.7,1]],size=200)

    # Concatenate the data points from all clusters
    pts = np.concatenate((cl1,cl2,cl3))

    # Perform k-means clustering on the data with 3 clusters
    assignments, centroids = km_means(pts,3)

    df = pd.DataFrame(pts, columns = ['x', 'y'])

    df['cluster'] = assignments

    # Get the unique assignment values
    unique_assignments = np.unique(assignments)

   # Set up colors for each assignment value
    colors = ['red', 'blue', 'green']

    # Get unique assignments
    unique_assignments = df['cluster'].unique()

    # Plot the points with different colors based on assignment value
    plt.figure(figsize=(8, 6))
    for i, assignment in enumerate(unique_assignments):
        subset = df[df['cluster'] == assignment]
        plt.scatter(subset['x'], subset['y'], color=colors[assignment], label=f'Cluster {i + 1}')
        ## COMMENTS: plot also the centroids values for verification
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Data points by Assignment')
    plt.legend()
    plt.show()
