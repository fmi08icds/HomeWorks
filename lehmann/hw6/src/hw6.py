import numpy as np
import random
import time

def kmeans(pts,k=3,max_iter=1000):
    '''
    This Function calculates a simple intuitve kmeans

    # Parameters:
        pts: numpy array like

        k (int): Number of centroids

        max_iter (int): Maximum number of iterations

    # Returns:
        centroids: array of centroids

        clusters: python dictionary of clusters
            index = index of cluster
            value = array of points assigned to the cluster

        k: number of clusters used
    '''

    # init centroids
    centroids = [pts[int(len(pts) * random.random())] for _ in range(k)]
    last_centroids = []


    for _ in range(max_iter):
        clusters = {}

        # init dictionary with empty arrays
        for i in range(k):
            clusters[i] = []

        # nested for loop appends smallest euclidean distance and assigns it to the corresponding cluster
        for pt in pts:
            dist = []
            for centroid in centroids:
                dist.append(np.linalg.norm(pt-centroid))
            clusters[dist.index(min(dist))].append(pt)

        # calculate new centroids
        for i in range(len(clusters)):
            # check if there is an empty cluster to avoid division/0 and numpy warning "RuntimeWarning: invalid value encountered in double_scalars"
            # cant pop out specific centroid, as i work with index=centroid, so i just restart the algorithm with k-1 and output the number of clusters used
            if len(clusters[i]) == 0:
                return kmeans(pts,k=i-1,max_iter=max_iter)
            centroids[i] = np.average(clusters[i], axis=0)

        # avoid unnecessary calculation by checking if all cluster are already in the perfect spot
        if np.array_equal(centroids,last_centroids): # GOOD
            break
        else:
           last_centroids = np.copy(centroids)

    return centroids, clusters, k

def main():
    # Define example points from lecture
    rng = np.random.default_rng(seed = 1234)
    cl1 = rng.multivariate_normal([-2,-2], [[1,-0.5],[-0.5,1]], size
    =100)
    cl2 = rng.multivariate_normal([1,0], [[1,0],[0,1]], size=150)
    cl3 = rng.multivariate_normal([3,2], [[1,-0.7],[-0.7,1]], size
    =200)
    pts = np.concatenate((cl1,cl2,cl3))

    # calculate kmeans
    start = time.time()
    centroids, clusters, k = kmeans(pts,k=3)
    end = time.time()

    # calculate distortion as simple quality measure (sum of squared distances)
    distortion = 0
    for i in range(len(centroids)):
        distortion += np.sum((clusters[i] - centroids[i] )**2) # Very good

    ## COMMENTS ###
    # a plot would have been an added value to illustrate your results.

    print(f"distortion: {distortion}\ntime: {end -start}\nnumber of cluster: {k}")

if __name__ == "__main__":
    main()
