import kmeans
import matplotlib.pyplot as plt
import numpy as np
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

def get_axis(data, k, axis):
    return [data[k][i][axis] for i in range(len(data[k]))]


def plot(data, means):
    colors = ["r","b","g","m","y","k","c"]
    if kmeans.is_numeric(means[0]) or len(means[0]) == 1:
        [plt.plot(data[i],np.zeros(len(data[i])), colors[i]+"x", means[i], [0], colors[i]+"o") for i in range(len(means))]
    elif len(means[0]) == 2:
        [plt.plot(get_axis(data, i, 0), get_axis(data,i,1),colors[i]+"x", means[i][0], means[i][1], colors[i] + "o") for i in range(len(means))]
    elif len(means[0]) == 3:
        ax = plt.figure().add_subplot(projection="3d")
        [ax.scatter(get_axis(data,i,0),get_axis(data,i,1),get_axis(data,i,2),marker="x",color=colors[i]) for i in range(len(means))]
        [ax.scatter(means[i][0],means[i][1],means[i][2],marker="o",color=colors[i]) for i in range(len(means))]
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
    plt.show()


def main(dimension=2,k=5,size=20,sample_size=100,seed_number=10):
    doc_="""
        max 7 clusters
        plotting only for dimensions 1 to 3
    """
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, description=doc_)
    parser.add_argument("--k", type=int, default=k, help="Amount of clusters")
    parser.add_argument("--d", type=int, default=dimension, help="Amount of dimensions")
    parser.add_argument("--r", type=int, default=size, help="range of the values (starting from 0)")
    parser.add_argument("--n", type=int, default=sample_size, help="Sample size")
    parser.add_argument("--s", type=int, default=seed_number, help="Seed number (to reproduce results)")
    args = parser.parse_args()
    k = args.k
    dimension = args.d
    size = args.r
    sample_size = args.n
    seed_number = args.s
    np.random.seed(seed_number)
    data = [np.random.random(dimension)*size for i in range(sample_size)]
    cluster, means = kmeans.k_means(data, k)
    #print(means)
    #[print(c)for c in cluster]
    plot(cluster,means)


if __name__ == "__main__":
    main()
