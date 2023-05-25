
import numpy as np
import matplotlib.pyplot as plt


# generate n samples of uniformly distributed data with d dimensions
def random_data(n, d=2, low_lim=0, up_lim=100):
    data = np.random.uniform(low=low_lim, high=up_lim, size=(n, d))
    return data

# create clustering data according to slide 3 of the lecture
def data_slides(seed = 1234):
    rng = np.random.default_rng(seed = seed)
    cl1 = rng.multivariate_normal([-2,-2], [[1,-0.5],[-0.5,1]], size=100)
    cl2 = rng.multivariate_normal([1,0], [[1,0],[0,1]], size=150)
    cl3 = rng.multivariate_normal([3,2], [[1,-0.7],[-0.7,1]], size=200)
    pts = np.concatenate((cl1,cl2,cl3))
    return pts

# visualize two dimensional data in scatter plot
def viz_data_2d(data):
    plt.scatter(data[:, 0], data[:, 1], s=5 )
    plt.show()

# visualize k clusters with single color for each cluster 
def viz_cluster_2d(data, clusters, k, centroids, s_p = 5, s_c = 50):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    for i in range(k):
        c = data[clusters == i]
        label = "cluster " + str(i + 1)
        a = ax1.scatter(c[:, 0], c[:, 1], s = s_p, label = label, c = "C" + str(i))
        b = ax1.scatter(centroids[i, 0], centroids[i, 1], s = s_c, marker= "^", c = "C" + str(i))
    
    plt.legend(loc='upper left')
    plt.show()

# calculate the euclidean distance between the points p and q
def calc_euc_dist(p, q):
    s = 0
    for i in range(len(p)):
        s += (p[i] - q[i])**2

    res = np.sqrt(s)
    return res

# calc d dimensional centroids
def calc_centroid(cluster):
    d = cluster.shape[1]
    sum_axis = np.empty(d)
    for i in range(d):
        sum_axis[i] = np.sum(cluster[:, i])
    return sum_axis / cluster.shape[0]

# perform naive k-means algorithm on data with k clusters
def k_means(data, k, max_iter = 1000):

    # choose k data points at random as initial centroids
    centroids = data[np.random.choice(data.shape[0], k, replace=False), :]

    clusters = np.empty(data.shape[0])
    dists = np.zeros(k)
    data = data[:,:,np.newaxis]

    for i in range(max_iter):
        change = True

        for ii, dp in enumerate(data):
            # calc euclidean distance from each point to the centroids
            for iii, centroid in enumerate(centroids):
                dists[iii] = calc_euc_dist(dp, centroid)
            # get the closest centroid to point and add point to cluster
            close_k = np.argmin(dists)
            clusters[ii] = close_k

        for ii in range(k):
            # get each data point out of cluster k
            c = data[clusters == k]
            if len(c) >= 1:
                # calc new centroid
                new_centroid = calc_centroid(c)
                # if all centroids stay the same the optimal clustering has been found
                if new_centroid[0] != centroids[ii,0] or new_centroid[1] != centroids[ii,1]:
                    change = False
                centroids[ii] =  new_centroid

        if not change:
            print("found optimal clustering")
            break

    return data, clusters, centroids




def main():
    k = 3
    n = 100
    d = random_data(n)
    viz_data_2d(d)
    data, clusters, centroids = k_means(d, k, max_iter=100)
    viz_cluster_2d(data, clusters, k, centroids)
    
    d = data_slides()
    viz_data_2d(d)
    data, clusters, centroids = k_means(d, k, max_iter=100)
    viz_cluster_2d(data, clusters, k, centroids)

if __name__ == "__main__":
    main()

