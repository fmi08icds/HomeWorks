import numpy as np
import matplotlib.pyplot as plt


def uniform(a, b, size):
    return (b-a)*np.random.random(size) + a


def f(x, R):
    return np.sqrt(np.abs(x*x-R*R))


def approximationOfPi(N):
    R = 1.0

    list_x = uniform(0, R, N)
    list_y = uniform(0, R, N)

    mask = list_y < f(list_x, R)
    list_accepted_x = list_x[mask]

    Ninf = len(list_accepted_x)
    fin = Ninf/N

    return 4*fin


def main():
    M = 100
    N = 1000

    list_rst = np.array([approximationOfPi(N) for _ in range(M)])

    list_mu = np.mean(list_rst)
    list_sigma = np.std(list_rst)

    plt.hist(list_rst, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ =="__main__":
    main()
