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

from hw6.my_kmeans import mykmeans
cluster_assignments = mykmeans(pts, 3, max_iter=100, tol=1e-4)

cluster_assignments
## introduction to pandas


import pandas as pd

a=pd.Series([1,2,3,4])

b=pd.Series(['A','B','C','D'])

c=pd.Series(['C', 'D', 'E', 'F'])

d=pd.Series(range(5))

e=pd.Series(['A',1,True])

f=pd.Series([4,2,1,3], index=['a','b','c','d'])

for i in [a,b,c,d,e,f]:
    print(f'dtype:{i.dtype}')
    print(f':{i}')


e.array

# print out each elem in f
[print(elem) for elem in f.truncate.__dir__()]


np.log(f) * 2


## f['a','b'] does not work. 
f[['a','b']]


m = pd.Series([1,2,3,4], index=['a','b','c','d'])
n = pd.Series([4,3,2,1], index=['d','c','b','a'])
o = pd.Series([1,1,1,1,1], index=['a','b','c','d','e'])

# these work just fine. since characters are ordered by nature, both m+n and n+m will return the same result.
m+n
n+m

# careful,if 'e' is not in m, then m+o will return NaN
m+o

d = {"anna": "A+", "bob": "B-", "carol": "C", "dave": "D+"}
d = pd.Series(d)
e = pd.Series(d, index=['bob','carol','dave','anna'])
e.index = ['a','b','c','d']