import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = 1234)
cl1 = rng.multivariate_normal([-2,-2], [[1,-0.5],[-0.5,1]], size
=100)
cl2 = rng.multivariate_normal([1,0], [[1,0],[0,1]], size=150)
cl3 = rng.multivariate_normal([3,2], [[1,-0.7],[-0.7,1]], size
=200)

pts = np.concatenate((cl1,cl2,cl3))
length = len(pts)
k = 3

def init():
    centroids = pts[np.random.choice(pts.shape[0], k, replace=False)]
    return centroids

def calc_clusters(centroids):
     dist1 = np.linalg.norm(pts - centroids[0], axis=1)
     dist2 = np.linalg.norm(pts - centroids[1], axis=1)
     dist3 = np.linalg.norm(pts - centroids[2], axis=1)
     cl1 = np.empty((0, 2))
     cl2 = np.empty((0, 2))
     cl3 = np.empty((0, 2))
     for i in range (0, length):
        if  dist1[i] <= dist2[i] and dist1[i] <= dist3[1]:
             cl1 = np.append(cl1, [pts[i]], axis=0)
        elif dist2[i] <= dist1[i] and dist2[i] <= dist3[i]:
             cl2 = np.append(cl2, [pts[i]], axis=0)
        elif dist3[i] <= dist1[i] and dist3[i] <= dist2[i]:
             cl3 = np.append(cl3, [pts[i]], axis=0)

     return cl1, cl2, cl3

def calc_centroids(cl1, cl2, cl3):
     cent1 = np.mean(cl1, axis=0)
     cent2 = np.mean(cl2, axis=0)
     cent3 = np.mean(cl3, axis=0)
     centroids = np.array([cent1, cent2, cent3])
     return centroids

def main () :
    count = 0
    centroids = init()
    old_centroids = np.empty((3, 2))

    while True:
        count += 1
        old_centroids = centroids
        cl1, cl2, cl3 = calc_clusters(centroids)
        centroids = calc_centroids(cl1, cl2, cl3)
        if np.array_equal(centroids, old_centroids) or count >= 500:
             break

    print(centroids)

    # Remove the comments to see the plot
    ## COMMENTS: it does not show data point on the plot at the second run.
    colors = ['r', 'g', 'b']
    symbols = ['o', 's', 'D']

    for i, cluster in enumerate([cl1, cl2, cl3]):
        plt.scatter(cluster[:, 0], cluster[:, 1], c=colors[i], marker=symbols[i])

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Cluster Plot')
    plt.legend(['Cluster 1', 'Cluster 2', 'Cluster 3'])
    plt.grid(True)
    plt.show()



if __name__ =="__main__" :
        main()
