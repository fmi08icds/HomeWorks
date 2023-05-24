import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def myplot(data, cluster_list):
    n = len(cluster_list)
    cmap = plt.get_cmap('tab10')
    colors = [cmap(i) for i in range(n)]
    
    for i, cluster in enumerate(set(cluster_list)):
        x = data[:, 0][cluster_list == cluster]
        y = data[:, 1][cluster_list == cluster]
        plt.scatter(x, y, color=colors[i])
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()


def generatedatapoints():
    # Generate Datapoints: O(n)
    rng = np.random.default_rng(seed = 1234)
    cl1 = rng.multivariate_normal([-2,-2], [[1,-0.5],[-0.5,1]], size=100)
    cl2 = rng.multivariate_normal([1,0], [[1,0],[0,1]], size=150)
    cl3 = rng.multivariate_normal([3,2], [[1,-0.7],[-0.7,1]], size=200)
    pts = np.concatenate((cl1,cl2,cl3))

    return pts


def init_data_centroide(k_cluster):
    """
    This function initializes k centroids as a subset of the generated datapoints.
    So that the random initialized centroids are not initialized too far from the data.
    Time Complexity: O(k) - k cluster
    """
    pts = generatedatapoints()
    centroids = random.sample(tuple(pts),k_cluster)

    return pts, centroids


def assigntoCluster(data, centroids):
    """
    Here for each datapoint the Euclidean distance is calculated for each centroid and stored in the dist_matrix. 
    Then the minimal distance for each datapoint is calculated and its indexes stored in the cluster_list.
    Time Complexity: O (n*k) - n datapoints, k cluster
    """
    dist_matrix = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
    cluster_list = np.argmin(dist_matrix, axis=1)
    
    return cluster_list


def kmeans(data, centroide, k_clusters):
    """
    The kmeans function is taken generated data, random initialized centroids and a defined number of clusters.
    Every datapoint is asigned to a cluster and the centroids are recalculated.
    This is repeated as long as the centroids are not changing anymore.
    Time Complexity: O(n*k*m) - n datapoints, k cluster/centroids, m dimensionaliyt of datapoints
    """
    old_centroide = centroide

    while True:

        cluster_list = assigntoCluster(data, old_centroide)
        new_centroide = [np.mean(data[np.where(cluster_list == cluster)], axis=0) for cluster in range(k_clusters)]
        myplot(data, cluster_list)

        if np.array_equal(old_centroide,new_centroide):
            break

        old_centroide = new_centroide

    return cluster_list


def main():
    
    k_cluster = 3  # Select k amount of clusters
    data, centroids = init_data_centroide(k_cluster)
    result = kmeans(data,centroids,k_cluster)

    return result
    

if __name__== '__main__':
    main()
