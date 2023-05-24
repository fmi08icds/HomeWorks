import numpy as np
import matplotlib.pyplot as plt

count = 1

def is_numeric(obj):
    """
    returns wether the value is a numeric value. Numeric value means: int, float, complex (I think), numpy.int64 and so on. Not included are array/ lists (objects with the "__iter__"-attribute).
    """
    attrs = ['__add__', '__sub__', '__mul__', '__truediv__', '__pow__']
    return all(hasattr(obj, attr) for attr in attrs) and not hasattr(obj, '__iter__')


def eucl_norm(v):
    if is_numeric(v):
        return abs(v)
    return np.sqrt(np.sum([v_i**2 for v_i in v]))


def k_means_iteration(data, k_set):
    """
        returns a collection of k clusters with the data belonging to each centre and the set of the means. 
        :param data: The data that will be clustered. It has to be a collection of either numeric values (int or float) or a sets of numeric values.
        :param k_set: The k initial means of the centres.
        :return: The return value is a tuple consisting of the clustered data after the iteration and the calculated means. 
    """
    is_one_dim = True if is_numeric(data[0]) else False
    dim = 1 if is_one_dim else len(data[0])
    data_copy = np.asarray(data)
    k_set = np.asarray(k_set, dtype=float)
    k = len(k_set)
    k_data = [[] for i in range(k)]
    for i_data in range(len(data_copy)):
        best_i = 0
        best = np.inf
        for i in range(k):
            dist = eucl_norm(data_copy[i_data]-k_set[i])# if not is_one_dim else \
            if dist < best:
                best_i = i
                best = dist
        k_data[best_i].append(data_copy[i_data])
    new_k_set = k_set.copy()
    for i in range(k): 
        if len(k_data[i]) != 0:
            val = sum(k_data[i])/len(k_data[i])
        if len(k_data[i]) != 0:
            new_k_set[i] =  sum(k_data[i])/len(k_data[i])
    return k_data, new_k_set


def k_means(data, k_or_kset,seed=10, iter=100):
    """
    k_means will cluster the data using the k-means method. 
    :param data: The data that should be clustered.
    :param k_or_kset: Input may either be an integer or a collection. If it is a numeric value it randomly selects the initial means. If it is a collection then that will be used.
    :param seed: The seed number of numpy.random in order to get reproducable results. By default it is 10.
    :param iter: maximum number of iterations. If k_means_iter returns the same result back to back it stops early. By default it is 100.
    :return: The return value is a tuple consisting of the clustered data and the calculated means. 
    """
    if is_numeric(k_or_kset):
        k = k_or_kset
        np.random.seed(seed)
        perm = np.random.permutation(len(data))[:k]
        k_set = [data[i] for i in perm]
        #print(k_set)
    else:
        k_set = k_or_kset
        k = len(k_set)
    count = 0
    is_unchanged = False
    while count < iter and not is_unchanged:
        clusters, new_k = k_means_iteration(data, k_set)
        count += 1
        is_unchanged = np.asarray([k_set[i] == new_k[i] for i in range(k)]).all()
        k_set = new_k

    return clusters, k_set


def get_axis(data,axis):
    return [data[i][axis] for i in range(len(data))]


def plot(results_to_plot, fig_name=None):
    """
    results_to_plot is a collection of tuples. The cuple can be described as (clusters, means).
    The inputted results get plotted as long as they are 1D, 2D or 3D
    """
    global count
    color = ["b","r","g","m","c","y","k"]
    for result in results_to_plot:
        #result[1][0] refers to the first element of the list of means
        if is_numeric(result[1][0]) or len(result[1][0])==1:
            if fig_name is None:
                plt.figure(f"example {count}: 1D")
            else:
                plt.figure(fig_name)
            [plt.plot(result[0][i], np.zeros(len(result[0][i])), color[i] + "x") for i in range(len(result[1]))]
            [plt.plot(result[1][i], [0], color[i] + "o", markersize=7) for i in range(len(result[1]))]

        elif len(result[1][0])==2:
            if fig_name is None:
                plt.figure(f"example {count}: 2D")
            else:
                plt.figure(fig_name)
            [plt.plot(get_axis(result[0][i],0), get_axis(result[0][i],1), color[i] + "x") for i in range(len(result[1]))]
            [plt.plot(result[1][i][0], result[1][i][1], color[i] + "o", markersize=7) for i in range(len(result[1]))]

        elif len(result[1][0])==3:
            if fig_name is None:
                ax = plt.figure(f"example {count}: 3D").add_subplot(projection="3d")
            else:
                ax = plt.figure(fig_name).add_subplot(projection="3d")
            [ax.scatter(get_axis(result[0][i],0), get_axis(result[0][i],1), get_axis(result[0][i],2), marker="x", color=color[i]) for i in range(len(result[1]))]
            [ax.scatter(result[1][i][0],result[1][i][1], result[1][i][2], marker="o",s=49, color=color[i]) for i in range(len(result[1]))]
            ax.set_xlabel("x-Axis")
            ax.set_ylabel("y-Axis")
            ax.set_zlabel("z-Axis")
        else:
            print("Heute habe ich leider kein Foto für dich")
            print("Cluster: ", result[0])
            print("Means: ", result[1])
        count += 1
    #plt.show()

def main(show_examples=False):
    """
     It will plot three normal distribution consisting of 100 data points each clustered around a centre and will plot the result of the kmeans method. 
     Furthermore, by setting show_examples=True it will plot three further distributions showing examples for 1D, 2D and 3D
    """
    seed = (int)(np.random.random()*5)
    print("Seed number: ", seed)
    np.random.seed(seed)
    rng = np.random.default_rng(seed=seed)
    k = 3
    cl1 = rng.multivariate_normal([-2,-2],[[1,-.5],[-.5,1]], size=100)
    cl2 = rng.multivariate_normal([1,0],[[1,0],[0,1]], size=100)
    cl3 = rng.multivariate_normal([3,2],[[1,-.7],[-.7,1]], size=100)
    pts = np.concatenate((cl1,cl2,cl3))
    results = k_means(pts,k,seed=seed)
    data = [np.random.random()*100-50 for i in range(200)]
    res_1d = k_means(data,k,seed=seed)
    data = [np.random.random(2)*100-50 for i in range(500)]
    res_2d = k_means(data,k,seed=seed)
    data = [np.random.random(3)*100-50 for i in range(500)]
    res_3d = k_means(data,k,seed=seed)
    if show_examples:
        plot([res_1d,res_2d,res_3d])

    plt.figure("Three normal distributions")
    plt.plot([cl1[i][0] for i in range(len(cl1))], [cl1[i][1] for i in range(len(cl1))], "x")
    plt.plot([cl2[i][0] for i in range(len(cl2))], [cl2[i][1] for i in range(len(cl2))], "x")
    plt.plot([cl3[i][0] for i in range(len(cl3))], [cl3[i][1] for i in range(len(cl3))], "x")
    plot([results], fig_name="Clustering of three normal distribution")
    plt.show()


if __name__ == '__main__':
    main()
