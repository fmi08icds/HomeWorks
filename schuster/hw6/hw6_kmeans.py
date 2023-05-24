"""
Implementation of k-means
Implementation of the two steps from page 5 of presentation day6
    -> initial set of k clusters is given

there are two steps before the k-mean algorithm can alternate between the steps from the presentation -> in total there are 4 steps

1. set k as the number of clusters one likes to find
2. initialize k centroids (e.g. choose randomly k points from the data to start with)
repeat
    3. assign each point to its closest centroid
    4. compute the new centoids based on the assigned points
until the centroids do not change anymore
"""

import numpy as np
import matplotlib.pyplot as plt

# Euclidean distance to compute which point belongs to which centroid, distance between centroid & data
def euclidean(centroid, data):
    return np.sqrt(np.sum((centroid - data) ** 2, axis=1))

# Compute centroid as the mean of cluster points
def compute_centroid(cluster):
    centroid = np.mean(cluster, axis=0)
    return centroid

def kmeans(data: np.ndarray, k_clusters: int, max_iter: int = 100):
    """
    data: data where kMeans is computed on
    k_clusters: number of clusters
    max_iter: maximum number of iterations, else risk of infinite loop
    """

    centroids = np.zeros((k_clusters, data.shape[1])) # compute k empty clusters

    # Step 2: initialize k centroids randomly
    # sample random points (rows) from array with numpy.random.permutation to shuffle the indices, selecting first k points
    indices = np.random.permutation(data.shape[0])[:k_clusters]
    centroids = data[indices]

    iteration = 0
    change = True # Centroids do change

    while iteration < max_iter and change:
        iteration += 1
        change = False #to end the while loop if the centroids do not change anymore

        # Assign each data point to the nearest centroid
        clusters = [[] for _ in range(k_clusters)] #creates list of k empty lists, Each list represents cluster
        for point in data:
            distances = euclidean(point, centroids)
            nearest_centroid = np.argmin(distances)
            clusters[nearest_centroid].append(point)

        # Update centroids
        for i in range(k_clusters):
            new_centroid = compute_centroid(clusters[i])
            if not np.array_equal(new_centroid, centroids[i]):
                change = True
                centroids[i] = new_centroid

    return centroids

def main() :
    # small Example 
    data = [[1, 2], [2, 1], [4, 5], [5, 4], [9, 10], [10, 9]]
    # centroids = kmeans(data, 2)
    # print("Centroids:", centroids)

    # Eample from lectures
    rng = np.random.default_rng(seed = 1234)
    cl1 = rng.multivariate_normal([-2,-2], [[1,-0.5],[-0.5,1]], size=100)
    cl2 = rng.multivariate_normal([1,0], [[1,0],[0,1]], size=150)
    cl3 = rng.multivariate_normal([3,2], [[1,-0.7],[-0.7,1]], size=200)
    pts = np.concatenate((cl1,cl2,cl3))

    centroids = kmeans(pts, 3)
    print("Centroids:", centroids)

    fig, ax = plt.subplots()
    #plt.grid(True)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    plt.scatter(cl1[:,0], cl1[:,1], marker="*", label="cl1")
    plt.scatter(cl2[:,0], cl2[:,1], marker="+", label="cl2")
    plt.scatter(cl3[:,0], cl3[:,1], label="cl3")
    plt.plot(centroids[:,0],centroids[:,1],"x", color="black",markersize=10)
    plt.legend()
    plt.show()
    #plt.savefig("../images/kmeans_data.pdf")

if __name__ == '__main__':
    main()