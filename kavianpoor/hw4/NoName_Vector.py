import timeit
import numpy as np



def NoName_vec(N):
    Ninf = 0
    R = 1.0

    list_x = np.random.uniform(0, R, size=N)
    list_y = np.random.uniform(0, R, size=N)

    list_accepted_x = list_x[list_y < np.sqrt(np.abs(list_x**2 - R**2))]

    Ninf = len(list_accepted_x)
    fin = Ninf / N

    return 4 * fin

N = 1000
M = 100

def uniform(a, b, size):
    return (b-a)*np.random.random(size=size) + a

def f(x, R):
    return np.sqrt(abs(x*x-R*R))



def NoName(N) :
    """
     This is a no name function. after figuring out what it does you're allowed to rename
    """
    Ninf = 0
    R = 1.0

    list_x = []
    list_y = []

    for i in range(N) :
            list_x.append(uniform(0,R,size=Ninf))
            list_y.append(uniform(0,R, size=Ninf))

    list_accepted_x = []

    for i in range(N) :
            if (list_y[i]< f(list_x[i],R)) : ## COMMENTS: problem here!
                    list_accepted_x.append(list_x[i])



    Ninf = len(list_accepted_x)
    fin = Ninf/float(N)


    return 4*fin

# Measure time for non-vectorized version
t1 = timeit.timeit(lambda: [NoName(N) for _ in range(M)], number=1) ##COMMENTS: what is this piece of code doing here?

# Measure time for vectorized version
t2 = timeit.timeit(lambda: [NoName_vec(N) for _ in range(M)], number=1)

print(f"Non-vectorized time: {t1}")
print(f"Vectorized time: {t2}")

def main () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma= []


    for i in range(M) :

        list_rst = [NoName(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))

    print(f"Mean of the means: {np.mean(list_mu)}")
    print(f"Std of the means: {np.std(list_mu)}")
    print(f"Mean of the stds: {np.mean(list_sigma)}")
    print(f"Std of the stds: {np.std(list_sigma)}")


if __name__ =="__main__" :
        main()
