import numpy as np
from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score


def define_data():
    # generate data
    # points without targets
    rng = np.random.default_rng(seed=1234)

    cl1 = rng.multivariate_normal([-2, -2], [[1, -0.5], [-0.5, 1]], size=100)
    cl2 = rng.multivariate_normal([1, 0], [[1, 0], [0, 1]], size=150)
    cl3 = rng.multivariate_normal([3, 2], [[1, -0.7], [-0.7, 1]], size=200)
    data1 = np.concatenate((cl1, cl2, cl3))
    data1_y_true = np.repeat([0, 1, 2], [100, 150, 200])

    return data1, data1_y_true


def k_means_build(data, k):
    current_centr = data[np.random.choice(
        range(data.shape[0]), size=k, replace=False)]

    while True:
        targ = np.argmin(np.linalg.norm(
            data[:, np.newaxis] - current_centr, axis=-1), axis=-1)
        updated_centr = np.array(
            [data[targ == i].mean(axis=0) for i in range(k)])
        if np.all(current_centr == updated_centr):
            break

        current_centr = updated_centr

    return current_centr, targ


if __name__ == "__main__":
    #data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    #data, target = data1, data1_y_true
    #k = int(input())
    k = 3
    #k_means_build(data, k)
    data1, data1_y_true = define_data()
    centroids, data1_y_pred = k_means_build(data1, k)
    print('Acc:', accuracy_score(data1_y_true, data1_y_pred))

'''
def init_centroids(data_shape, k):
    centroids = np.random.randint(0, data_shape, k, 'int')
    centroids = np.sort(centroids)
    return centroids

def update_centroids(centroids_list):
    centroids_each = []
    centroids_each = np.array(centroids_each)
    indices = []  # New list to keep track of indices
    for dot_group in centroids_list:
        print(dot_group)
        dot_group_mean = sum(dot_group)/len(dot_group)
        min_dist = abs(dot_group_mean-dot_group[0])
        min_dist_index = 0
        for dot_group_index, dot_group_item in enumerate(dot_group):
            if sum(abs(dot_group_mean-dot_group_item)) < sum(min_dist):
                min_dist = abs(dot_group_mean-dot_group_item)
                min_dist_index = dot_group_index
        np.append(centroids_each, min_dist_index)
        indices.append(dot_group[min_dist_index])  # Append the centroid to the list
    updated_centroids = [sub[idx] for sub, idx in zip(centroids_list, centroids_each)]
    updated_centroids = np.array(updated_centroids)
    return updated_centroids, indices


def eukl_dist_build(data, centroids, k):
    centroids = data[centroids]
    centroids_list = [[] for _ in range(k)]
    for dot in data:
        min_dist = sum(abs(centroids[0]-dot))
        min_dist_index = 0
        for centroid_index, centroid_item in enumerate(centroids):
            if sum(abs(centroid_item - dot)) < min_dist:
                min_dist = sum(abs(centroid_item - dot))
                min_dist_index = centroid_index
        centroids_list[min_dist_index].append(np.array(dot))
    return centroids_list

def k_means_build(data, k):
    if not isinstance(k, int) or k>data.shape[0]:
        print('Not a valid input.')
        return 0
    centroids = init_centroids(data.shape[0], k)
    while True:
        centroids_list = eukl_dist_build(data, centroids, k)
        updated_centroids, centroid_indices = update_centroids(centroids_list)
        print('centroids_list', centroids_list)
        # print('centroids_list_shape')
        print('centroids', centroids)
        #print('centroids_list[i]', centroids_list[[centroids]])
        current_centroids = [centroids_list[i] for i in centroid_indices]
        print('current_centroids', current_centroids)
        print('updated_centroids', updated_centroids)
        print('??', all(np.array_equal(a, b) for a, b in zip(current_centroids, updated_centroids)))
        if all(np.array_equal(a, b) for a, b in zip(current_centroids, updated_centroids)):
            print('Finished')
            break
        else:
            print('Failed')
        print('New centroids:', updated_centroids)


    print(centroids)
    print(data[centroids])
    print(data.shape[0])

if __name__=="__main__"
    #data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    data, target = data1, data1_y_true
    k = 2 #int(input())
    k_means_build(data, k)
'''
