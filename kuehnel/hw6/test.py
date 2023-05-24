from kmeans import my_kmeans
import numpy as np
from scipy.cluster.vq import kmeans

# Test 1
a = np.array([[1, 0], [0, 1], [0, 0], [1, 1]])
cents = np.array([[0, 0], [1, 1], [2, 2]])
cluster_ids, centroids, cluster_list, dist_error1 = my_kmeans(data=a, k=3)
c_ids_test, cs_test, c_dict_test, err = my_kmeans(data=a, k=3, centroids=cents)
print("fin Test 1")

# Test 2 (from the lecture)
print("Start Test 2")
rng = np.random.default_rng(seed=1234)
cl1 = rng.multivariate_normal([-2, -2], [[1, -0.5], [-0.5, 1]], size=100)
cl2 = rng.multivariate_normal([1, 0], [[1, 0], [0, 1]], size=150)
cl3 = rng.multivariate_normal([3, 2], [[1, -0.7], [-0.7, 1]], size=200)

pts = np.concatenate((cl1, cl2, cl3))
ctr, dist = kmeans(pts, 3)

print(f"Scipy ctr: {ctr},\n Scipy dist: {dist}")

c_ids, ctrs, c_dict, dist_err = my_kmeans(data=pts, k=3)

print(f"Scipy ctr: {ctrs},\n My dist error in L^1 Norm: {dist_err}")
