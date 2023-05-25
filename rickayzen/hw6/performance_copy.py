import cProfile, pstats
import time
import kmeans
import numpy.random as npr
import numpy as np
from tabulate import tabulate
import scipy.cluster.vq as sp
from scipy.cluster.vq import whiten
profile = cProfile.Profile()
#Just a random seed number that gets iterated in order to get random numbers from different seeds while still being repeatable
#however, only data is repeatable as initial k is chosen randomly
seed_c = 5


def gen_data(n=100, dim=3,rng=20,seed=10):
    npr.seed(n)
#    data = np.empty(n,dtype=np.darray)
    return whiten(np.array([npr.random(dim)*rng for i in range(n)]))
    
    #profile.enable()

    #profile.disable()


def test_case(func, n=100, dim=1, rng=20, k=2):
    data = gen_data(n,dim,rng,seed_c)
    profile.enable()
    func(data, k,iter=100)
    profile.disable()
#    seed_c += 1


def execute_and_track(n,dim,rng,k):
    test_case(kmeans.k_means,n,dim,rng,k)
    stats_me = pstats.Stats(profile)
    test_case(sp.kmeans,n,dim,rng,k)
    stats_sp = pstats.Stats(profile)
    return stats_me.total_calls, stats_sp.total_calls


def main():
    complexity = {}

    n = 1000
    dim = 2
    rng = 50
    k = 2
    complexity[f"{n}-{dim}-{rng}-{k}"] = execute_and_track(n,dim,rng,k)

    n = 5000
    dim = 2
    rng = 50
    k = 2
    test_case(kmeans.k_means,n,dim,rng,k)
    stats = pstats.Stats(profile)
    complexity[f"{n}-{dim}-{rng}-{k}"] = stats.total_calls

    n = 10000
    dim = 2
    rng = 50
    k = 2
    stats = pstats.Stats(profile)
    test_case(kmeans.k_means,n,dim,rng,k)
    complexity[f"{n}-{dim}-{rng}-{k}"] = stats.total_calls
    
    n = 1000
    dim = 1
    rng = 50
    k = 2
    test_case(kmeans.k_means,n,dim,rng,k)
    stats = pstats.Stats(profile)
    complexity[f"{n}-{dim}-{rng}-{k}"] = stats.total_calls

    n = 1000
    dim = 3
    rng = 50
    k = 2
    test_case(kmeans.k_means,n,dim,rng,k)
    stats = pstats.Stats(profile)
    complexity[f"{n}-{dim}-{rng}-{k}"] = stats.total_calls

    n = 1000
    dim = 10
    rng = 50
    k = 2
    test_case(kmeans.k_means,n,dim,rng,k)
    stats = pstats.Stats(profile)
    complexity[f"{n}-{dim}-{rng}-{k}"] = stats.total_calls

    n = 1000
    dim = 2
    rng = 50
    k = 5
    test_case(kmeans.k_means,n,dim,rng,k)
    stats_me = pstats.Stats(profile)
    test_case(sp.kmeans,n,dim,rng,k)
    stats_sp = pstats.Stats(profile)
    complexity[f"{n}-{dim}-{rng}-{k}"] = stats.total_calls

    n = 1000
    dim = 2
    rng = 50
    k = 10
    test_case(kmeans.k_means,n,dim,rng,k)
    stats = pstats.Stats(profile)
    complexity[f"{n}-{dim}-{rng}-{k}"] = stats.total_calls

    n = 1000
    dim = 2
    rng = 50
    k = 20
    test_case(kmeans.k_means,n,dim,rng,k)
    stats = pstats.Stats(profile)
    complexity[f"{n}-{dim}-{rng}-{k}"] = stats.total_calls

    n = 1000
    dim = 5
    rng = 50
    k = 5
    test_case(kmeans.k_means,n,dim,rng,k)
    stats = pstats.Stats(profile)
    complexity[f"{n}-{dim}-{rng}-{k}"] = stats.total_calls

    n = 1000
    dim = 5
    rng = 50
    k = 10
    test_case(kmeans.k_means,n,dim,rng,k)
    stats = pstats.Stats(profile)
    complexity[f"{n}-{dim}-{rng}-{k}"] = stats.total_calls
    
    print(tabulate(complexity.items(), headers=["n-dimension-range-k","total calls"]))
#    for key in complexity.keys():
#        print(key,":\t\t",complexity[key])


if __name__ == '__main__':
    main()
