import numpy as np
import matplotlib.pyplot as plt

def kmeans(data, num_clusters, max_iterations=10000): # k-means algorithm to find cluster centers

    # first initialize clusters randomly
    rng = np.random.default_rng()
    centers = rng.choice(data, size=num_clusters, replace=False)

    for _ in range(max_iterations):

        # assign the cluster with the smallest distance to each data point
        distances = np.linalg.norm(data[:, np.newaxis] - centers, axis=-1)
        labels = np.argmin(distances, axis=1)

        # update cluster centres but first check if the cluster is empty
        new_centers = []
        for k in range(num_clusters):
            if np.sum(labels == k) > 0: # check if the cluster is empty
                new_centers.append(data[labels == k].mean(axis=0)) #
            else:
                new_centers.append(rng.choice(data)) # if it's empty then choose a new data point as a cluster centre
        new_centers = np.array(new_centers)


        # check if the cluster centers no longer change
        if np.all(centers == new_centers):
            break

        centers = new_centers

    return centers, labels

# create the data points
rng = np.random.default_rng(seed=1234)
cl1 = rng.multivariate_normal([-2, -2], [[1, -0.5], [-0.5, 1]], size=100)
cl2 = rng.multivariate_normal([1, 0], [[1, 0], [0, 1]], size=150)
cl3 = rng.multivariate_normal([3, 2], [[1, -0.7], [-0.7, 1]], size=200)
data = np.concatenate((cl1, cl2, cl3))

num_clusters = 3
centers, labels = kmeans(data, num_clusters)

plt.scatter(data[:, 0], data[:, 1], c=labels)
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=100)

#plt.scatter(cl1[:,0], cl1[:,1], marker="*", label="cl1")
#plt.scatter(cl2[:,0], cl2[:,1], marker="+", label="cl2")
#plt.scatter(cl3[:,0], cl3[:,1], marker=".", label="cl3")

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Clustering with k-means algorithm')
#plt.legend
plt.show()
