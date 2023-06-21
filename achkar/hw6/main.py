import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from k_means import KMeans

# Generate data
rng = np.random.default_rng(seed = 1234)
cl1 = rng.multivariate_normal([-2,-2], [[1,-0.5],[-0.5,1]], size
=100)
cl2 = rng.multivariate_normal([1,0], [[1,0],[0,1]], size=150)
cl3 = rng.multivariate_normal([3,2], [[1,-0.7],[-0.7,1]], size
    =200)
pts = np.concatenate((cl1,cl2,cl3))

def main():
    centers = 3
    kmeans = KMeans(n_clusters=centers)
    kmeans.fit(pts)

    # View results
    class_centers, classification = kmeans.evaluate(pts)
    sns.scatterplot(x=pts[:,0], y=pts[:,1], hue=classification, palette='deep')
    sns.scatterplot(x=np.array(class_centers)[:,0], y=np.array(class_centers)[:,1], color='black', marker='x', s=100)

    # show the plot
    plt.show()

if __name__ == "__main__":
    main()