from numpy import random, mean
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


def initialise(N,n,x_l, x_u) :
    """
        Your docstr here
    """
    all_x = None
    all_eta = None

    return None # feel free to use this or not list(zip(all_x, all_eta))


def evaluate(pop, f) :
    """
        Your docstr here
    """

    return None


def mutate(pop) :
    """
        Your docstr here
    """

    n = None # get the dimension of the solution space here.
    N = None # the population size
    new_pop = []
    tau = None #
    tau_prime = None #

    for i in range(N) :
        print("Not implemented") # replase this by your own implementation of the mutation operator

    return new_pop


def select(pop, fitnesses, N, q=10) :
    """
        Your docstr here
    """
    seleted_pop = []


    return selected_pop


def dea(params):

    """
        Your docstr here
    """

    T = None # get the coresponding parameter from the params dict.
    prev_pop = params["init_pop"]

    t = None
    mean_fit = [mean(evaluate(prev_pop,params['f']))]
    while t< T:
        ## write your code here to implement the DEA. The steps should be 1. mutate, 2. evaluate, 3. select
        m = mean(evaluate(prev_pop,params['f']))
        mean_fit += [m]
        print(f"Mean fitness {t} : " ,m)

        t +=1
    return prev_pop, mean_fit



def parseArguments():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length' ,type=int, default=1, help= "The dimension of the solution space")
    parser.add_argument('-T', type=int, default=50, help='Number of generation of the DEA')
    parser.add_argument('-N', type=int, default=100, help='Population size')
    parser.add_argument('-xL', type=float, default=-3.,  help='Lower bound of the the solution space')
    parser.add_argument('-xU', type=float, default=3.,  help='Upper bound of the the solution space')
    parser.add_argument('-q', type=int, default=10,  help='number of mutants for parwise comparison')
    parser.add_argument('--verbose', action="store_true", default=False, help="Print the mean fitness evolution on a standard output " )
    parser.add_argument('-seed', type=int, default=None, help="Seed for the initial population")
    return parser.parse_args()


def main() :
    args = parseArguments()
    f = lambda x: sum(x**2) # Here you will define your obejective function

    params = {
        'n' : args.length,
        'T' : args.T ,
        'q' : args.q,
        'N' : args.N,
        'f' : f,
        'verbose': args.verbose,
        'xU': args.xU,
        'xL': args.xL
    }


    params['init_pop'] = initialise(args.N, args.length, args.xL, args.xU)

    best_pop, mean_fitnesses = dea(params)
    print("Best population : ", best_pop)
    plt.plot(mean_fitnesses, "o-")
    plt.title("Optimization of the function "+f.__doc__)
    plt.xlabel("Generation(t)")
    plt.ylabel("Population mean fitness")
    plt.show()



if __name__ =="__main__" :
    main()
