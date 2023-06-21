from numpy import random, mean, sqrt, exp
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


def initialise(N,n,x_l, x_u) :
    """
        Initialize the first population of solutions for the dea
        
        ## Params:
            N: Size of population\n
            n: Number of chromosoms/Attributes/Solution-Space\n
            x_l: lower-bound of the number to be generated for every n\n
            x_u: upper-bound of the number to be generated for every n\n

        ## Returns:
            list of values for every N in the form of [(x,eta),...]
    """
    all_x = (random.uniform(size=(N,n)) * (x_u-x_l)) + x_l
    all_eta = (random.uniform(size=(N,n)) * (x_u-x_l)) + x_l

    return list(zip(all_x, all_eta)) # feel free to use this or not list(zip(all_x, all_eta))


def evaluate(pop, f) :
    """
        Evaluated a population on a specific given function
        
        ## Params:
            pop: population in form of [(x,eta),...]\n
            f: lambda function for the population to be evaluated at\n
        
        ## Results:
            Array of fitness values in the form of a pop-sized Array of float values

    """

    results = [float(f(pop[x][0])) for x in range(len(pop))]

    return results


def mutate(pop) :
    """
        Mutates the given population\n
        New x-value: x_i+eta_i*N_i(0,1)
        New eta-value: eta_i * exp(tau'*N(0,1)+tau*N_i(0,1))

        ## Params:
            pop: population in form of [(x,eta),...]\n
        ## Results:
            new_pop: mutated population in the same form as pop
    """

    n = len(pop[0][0]) # get the dimension of the solution space here.
    N = len(pop) # the population size
    new_pop = []
    tau = 1 / (sqrt(2*sqrt(n))) # sqrt(2)*sqrt(n)^-1
    tau_prime = 1 / sqrt(2*n) # sqrt(2n)^-1

    for i in range(N) :
        x_i = pop[i][0] + pop[i][1] * random.standard_normal(size=n)
        eta_i = pop[i][1] * exp(tau_prime*random.standard_normal()+tau*random.standard_normal(size=n))
        new_pop.append((x_i, eta_i))

    return new_pop


def select(pop, fitnesses, N, q=10) :
    """
        Select the "fittest" solutions for the next Generation

        ## Params:
            pop: population in form of [(x,eta),...]\n
            fitnesses: Array of fitness values in the form of a pop-sized Array of float values\n
            N: Population size (for the next population)\n
            q: default=10, Number of opponents each individual has to face\n

        ## Results:
            selected_pop: The new population with the fittest N members
    """

    wins = []
    for i in range(len(pop)):
        opponents = random.choice(a=fitnesses,size=q)
        # get the number of wins
        wins.append((pop[i],sum([1 for j in opponents if fitnesses[i] < j])))

    wins.sort(key=lambda x: x[1],reverse=True)
    selected_pop = [wins[x][0] for x in range(len(wins))][:N]

    return selected_pop


def dea(params):
    """
        A special diffrential evolutionary algorithm without crossover
        
        steps:\n
            1. initialize population
            repeat T times:\n
                \t2. mutate
                \t3. evaluate
                \t4. select 

        ## Params:
            params = {
                    'n' : attributes of individual, \n
                    'T' : max iteration ,\n
                    'q' : number of opponents,\n
                    'N' : Population size,\n
                    'f' : function to be evaluated,\n
                    'verbose': verbose mode,\n
                    'xU': upper bound of Solutions generated,\n
                    'xL': lower bound of Solutions generated\n
                }
        ## Results:
            prev_pop: best population\n
            mean_fit: Array of mean fitness values
    """

    T = params["T"] # get the coresponding parameter from the params dict.
    prev_pop = params["init_pop"]

    t = 0
    mean_fit = [mean(evaluate(prev_pop,params['f']))]
    while t< T:
        ## write your code here to implement the DEA. The steps should be 1. mutate, 2. evaluate, 3. select
        # Mutate
        new_pop = mutate(prev_pop)
        eval_pop = new_pop + prev_pop

        # Evaluate
        fitness_all = evaluate(eval_pop,params['f'])

        #Select
        prev_pop = select(eval_pop,fitness_all,params['N'],params['q'])

        # Verbose mode?
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
    #f = lambda x: sum(x**2) # Here you will define your obejective function
    #f = lambda x: x**4+x**3-x**2-x
    f = lambda x: sum(100*(x[i-1]-x[i]**2)**2+(x[i]-1)**2 for i in range(1,args.length))

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
    print("Best population : ", best_pop[0])
    plt.plot(mean_fitnesses, "o-")
    plt.title(f"Optimization of the function {str(f)}") #changed this part as it was causing an Error
    plt.xlabel("Generation(t)")
    plt.ylabel("Population mean fitness")
    plt.show()



if __name__ =="__main__" :
    main()
