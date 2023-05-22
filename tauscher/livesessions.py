import numpy as np

# braodcasting example
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a * b

print(c)

# 2D array

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])
c = a * b

print(c)

# 3D array

a = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
b = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
c = a * b

print(c)



print('test')



### Sci-Py Introduction 

# Path: livesessions.py
import numpy as np
from scipy import cluster, odr, constants, optimize, fftpack, signal, integrate, sparse, interpolate, spatial
rng = np.random.default_rng(seed = 1234)
cl1 = rng.multivariate_normal([-2,-2], [[1,-0.5],[-0.5,1]], size=100)
cl2 = rng.multivariate_normal([1,0], [[1,0],[0,1]], size=150)
cl3 = rng.multivariate_normal([3,2], [[1,-0.7],[-0.7,1]], size=200)
pts = np.concatenate((cl1,cl2,cl3))

from scipy.cluster.vq  import kmeans
ctr, dist = kmeans(pts,k_or_guess= 3,iter=20)  
ctr.shape
dist
cl1.mean(axis=0)

import matplotlib.pyplot as plt
# plot the cluster result
plt.scatter(pts[:,0], pts[:,1], s=10)
plt.show()

from scipy.integrate import quad
quad(lambda x: x, 0, 1)


def norm_pdf(x, mu, sigma):
    return (1/(sigma * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((x -mu)/sigma)**2)

quad(norm_pdf, -np.inf, np.inf, args=(0,1))

from hw6.my_kmeans import my_kmeans
cluster_assignments, centroids = my_kmeans(pts, 3, max_iter=100, tol=1e-4)
