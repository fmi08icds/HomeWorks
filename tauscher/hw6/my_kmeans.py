import numpy as np
from math import sqrt
import timeit
import cProfile
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import pandas as pd
from scipy import stats
from scipy.linalg import sqrtm
import logging

logging.basicConfig(level=logging.INFO)


def mykmeans(data: np.ndarray, k_or_guess, max_iter: int =100, tol: float=1e-4):
    '''
    Given a set of observations (x1, x2, ..., xn),
    where each observation is a d-dimensional real vector,
    k-means clustering aims to partition the n observations
    into k (≤ n) sets S = {S1, S2, ..., Sk} so as to
    minimize the within-cluster sum of squares (WCSS)
    (i.e. variance).
    gets:
    @data: the data to cluster
    @k_or_guess: either the number of clusters or an initial guess for the centroids
    @max_iter: the maximum number of iterations
    @tol: the tolerance for the stopping criteria

    returns:
    @centroids: the centroids of the clusters
    @clustering: the cluster assignments of each data point
    @tol: the tolerance for the stopping criteria
    @i: the number of iterations until the stopping criteria was reached
    '''
    # initialize centroids, here k points from the given data are chosen to be the 
    # centroids.
    if isinstance(k_or_guess, int):
        centroids = data[np.random.choice(data.shape[0], k_or_guess, replace=False)]
    else:
    # here, the user specified the centroids as a parameter.
        centroids = k_or_guess


    # check for each data point which centroid is closest with a
    # specified distance function. This is repeated until 
    # either maxiter is reached, or the centroids do not change
    # more than a specified tolerance.
    intermediate_res = []

    i=0
    while(True):

        i+=1
        old = centroids
        

        ## assign each data point to a cluster
        clustering = distance_fun(data, centroids)

        ## save for plotting
        intermediate_res.append({'iteration':i,'cluster_assignments':clustering,'centroids':centroids})
        ## update centroids
        ## check if there are empty clusters
        ## if so, reduce the number of clusters by one and run mykmeans again
        if (np.unique(clustering).shape[0] < centroids.shape[0]):
            logging.info("empty cluster detected, reducing number of clusters by one")
            return mykmeans(data=data, k_or_guess=centroids.__len__()-1, max_iter=100, tol=1e-4)

        ## check if there are empty clusters
        ## if so, 
        centroids = np.array([np.mean(data[clustering == i], axis=0) for i in range(len(centroids))])
    
        ## check if the centroids have changed more than the tolerance or if max_iter is reached
        if (np.all((old - centroids < np.full(fill_value=tol,shape= centroids.shape)))==True or i>max_iter):
            break
    return centroids, clustering, tol, i, intermediate_res, centroids.shape[0]
## 3 test centroids


def distance_fun(data, centroids):
    '''
    This function calculates the distance between each point in the data
    and each centroid. The output is an array of length data.shape[0] with
    the index of the closest centroid for each point.
    '''
    distances = np.zeros(data.shape[0])
    for i in range(data.shape[0]):
        distances[i] = np.argmin([np.linalg.norm(data[i] - centroids[j]) for j in range(centroids.shape[0])])
    return distances




    
## main to test the functions
if __name__ == "__main__":

    ## 100 data points with 3 dimensions, example data to test mykmeans
    dimensions=5
    points= 10_000
    kcluster= 15
    data = np.random.randn(points, dimensions)
    cov_shape = (dimensions, dimensions)
    cov_diag = np.diag(np.random.rand(dimensions)**2)
    cov_rest_u = np.diag(np.random.rand(dimensions-1),k=(dimensions-1))
    

    # Generate a random matrix
    random_matrix = np.random.uniform(-100,100,size=dimensions*dimensions).reshape(dimensions,dimensions)

    # Compute the covariance matrix
    covariance_matrix = random_matrix @ random_matrix.T

    # Perform the Cholesky decomposition
    cholesky_matrix = sqrtm(covariance_matrix)

    # Construct the positive semidefinite matrix
    positive_semidefinite_matrix = cholesky_matrix @ cholesky_matrix.T
    

    data = stats.multivariate_normal(mean=np.random.uniform(-100,100, size=dimensions), cov=positive_semidefinite_matrix).rvs(points)
    
    ## one guess for both functions. 
    k_or_guess = np.random.randn(kcluster, dimensions)
    tol=1e-4
    max_iter=100

    ## test mykmeans2
    centroids, clustering, tol, i, intermediate_res, res_clusters = mykmeans(
        data, k_or_guess, max_iter, tol)
    print("mykmeans2:")
    print("centroids: ", centroids)
    print("clustering: ", clustering)
    print("tol: ", tol)
    print("i: ", i)

    ## check if results are the same
    M = 50
    profiler = cProfile.Profile()
    profiler.enable()
    for i in np.arange(M):
        mykmeans(np.random.randn(100, 5), np.random.randn(3, 5), 100, 0.001)
    profiler.disable()
    profiler.dump_stats("./mykmeans.stats")

    profiler.print_stats()

    ## plot the results
    plt_data = pd.DataFrame(intermediate_res)

    ## plot the intermediate results of mykmeans2 where a slider can be used to change the iteration and update the plot
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.set_title("mykmeans results")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.subplots_adjust(bottom=0.5) 

    
    # Define the position and size of the slider
    # kwargs = left bottom width height
    left, width, height = 0.2, 0.7, 0.05
    bottom = 0.1
    offset = 0.05
    
    # Create the slider with the specified range and initial value and bind it.
    slider_axc = plt.axes([left, bottom, width, height])  
    slider_it = Slider(slider_axc, 'Iteration', 1, plt_data['iteration'].max(), valinit=1, valstep=1)
    
    slider_axx = plt.axes([left, bottom+height+offset, width, height])  
    slider_xdim = Slider(slider_axx, 'x_dim', 0, data.shape[1]-1, valinit=0, valstep=1) 
    
    slider_axy = plt.axes([left, bottom+height*2+offset*2, width, height])  
    slider_ydim = Slider(slider_axy, 'y_dim', 0, data.shape[1]-1, valinit=1, valstep=1) 
    
    def update(val):
        ax.clear()  # Clear the previous plot
        ax.scatter(data[:,int(slider_xdim.val)], data[:,int(slider_ydim.val)], c=plt_data['cluster_assignments'][slider_it.val-1], cmap='rainbow')
        # the three centroids are plotted as black stars, changes with the dimension and iteration
        for k in range(res_clusters):
            ax.plot(plt_data['centroids'][int(slider_it.val-1)][k][slider_xdim.val],
                    plt_data['centroids'][int(slider_it.val-1)][k][slider_ydim.val],
                    marker="*",c='yellow',markersize=15,markeredgecolor="black")
            ax.text(plt_data['centroids'][int(slider_it.val-1)][k][slider_xdim.val],
                    plt_data['centroids'][int(slider_it.val-1)][k][slider_ydim.val],
                    str(k), fontsize=15, color='black')
        fig.canvas.draw_idle()  # Redraw the plot

    slider_it.on_changed(update)  # Connect the update function to the slider
    slider_ydim.on_changed(update)  # Connect the update function to the slider
    slider_xdim.on_changed(update)  # Connect the update function to the slider
    update(1)  # Call update to set the initial plot.

    plt.show()

    

