import numpy as np

from random import sample

# x1 (2, 3), x2 (2, 5)
def distance(x1, x2, dim=2):
    sum = 0
    for d in range(dim):
        sum += (x2[d] - x1[d]) ** 2

    dist = np.sqrt(sum)
    return dist

# [(1,2), (2,3), (4,3)]
def centroid(cluster):
    centro1 = 0
    centro2 = 0
    for i in cluster:
        c1 = i[0]
        c2 = i[1]

        centro1 += (c1)
        centro2 += (c2)

    centro1 = centro1/len(cluster)
    centro2 = centro2/len(cluster)

    return (centro1,centro2)

# O(N*I*k) N = datapoints, I = iterations, k = number of cluster
def k_means(datapoints, max_iteration = 5, k = 3):

    centroids = sample(datapoints, k) ## COMMENTS: sample works only on sequences data. So, use the indexes instead.
    ## COMMENTS: replace this by datapoints[sample(range(datapoints.shape[0]), k)]
    # centroids = [(3,4), (2,2), (5,2)]


    iter = 0
    while iter < max_iteration:
        cluster = [[] for _ in range(k)]
        centroids_old = [c for c in centroids]
        dist_all = []
        for r in range(len(centroids)):
            distances = []
            for i in range(len(datapoints)):
                distances.append(distance(datapoints[i], centroids[r]))
            dist_all.append(distances)

        for r in range(len(datapoints)):
            col = [dist_all[c][r] for c in range(len(centroids))]
            min_d = min(col)
            cluster_num = col.index(min_d)
            cluster[cluster_num].append(datapoints[r])

        for r in range(len(cluster)):
            centroids[r] = centroid(cluster[r])

        iter += 1
        if np.all(centroids_old == centroids):
            break


    return cluster, centroids ##COMMENTS: important to return the optiomum centroids

# rng=np.random.default_rng(seed=1234)
# cl1=rng.multivariate_normal([-2,-2],[[1,-0.5],[-0.5,1]],size =100)
# cl2=rng.multivariate_normal([1,0],[[1,0],[0,1]],size=150)
# cl3=rng.multivariate_normal([3,2],[[1,-0.7],[-0.7,1]],size =200)
# pts=np.concatenate((cl1,cl2,cl3))
# print(pts)

print(k_means([(4,10),(7,10),(4,8),(6,8),(3,4),(2,2),(5,2),(10,5),(12,6),(11,4),(9,3),(12,3)], 3))
# print(k_means(pts, 3))
