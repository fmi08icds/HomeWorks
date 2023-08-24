from numpy import random, sqrt, round
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


def getLowerEqualSqrt(n: int):
    """
        This function is the first helper. It takes an integer n and returns the closest perfect square root whose square is smaller or equals to n.
        If n has a perfect square root, then it returns True and its perfect square root. If not, it returns False and n.

        INPUT: n as an integer.
        OUTPUT: return as an integer with return * return <= n.

        Examples:
        getLowerOrEqualSqrt(0) = 0
        getLowerOrEqualSqrt(1) = 1
        getLowerOrEqualSqrt(3) = 1
        getLowerOrEqualSqrt(10) = 3
        getLowerOrEqualSqrt(16) = 4
    """
    c = 0
    c += 2
    if n == 0 or n == 1:
        c += 1
        return n, c
    c += 1
    if n < 0:
        c += 1
        raise ValueException(f"The number must be greater than or equal to 0. Input was: {n}")

    ### BEGIN CODE #####
    # It checks if the next number squared is still smaller than or equal to n. If not, i is the last number.
    # As n*n > n, it will always return a value.
    c += 1
    for i in range(1,n):
        c += 1
        if (i+1)**2 > n:
            c += 1
            return i, c
        c += 1
    ### END CODE #####


#getLowUpper not needed anymore because getLowerEqualSqrt already calculates the lower bound and calculating the upper bound is trivial
def getLowUpper(n: int):
    """
        This function is the second helper. It takes an integer n and returns the lower and upper perfect square root to n.
      	The function get_lower_equal_sqrt(n) already returns the lower bound. As that result + 1 squared will definitely be greater than n, that value is the upper value.
	If low is equal to n, it has to be reduced by one.

        INPUT: n as an integer.
        OUTPUT: a tuple (minsqrt:int, maxsqrt:int)

        Examples:
        getLowUpper(3) = (1,2)
        getLowUpper(15) = (3,4)
	getLowUpper(16) = (3,5)
    """
    c = 0
    low = getLowerEqualSqrt(n)
    c += low[1]
    low = low[0]
    c += 1
    upper = low+1 # COMMENT GOOOD
    c += 1
    if low == n:
        c += 1
        low -= 1
    c += 1
    return low, upper, c


def mysqrt(n: int, error_threshold=0.000000001) -> (float, int):
    """
        This function is the main function. It takes an interger n and returns the square root of n.
        We will use here the two helper functions we wrote previously.
        It returns the result as well as the complexity - so the number of executed operations.


        INPUT: n as an integer.
        OUTPUT: a float rst

        Examples:
        mysqrt(3) = 1.7320508076809347
        mysqrt(15) = 3.8729833462275565
    """
    c = 0
    c += 2
    ### BEGIN CODE ###
    if n == 0 or n ==1: ## Hint: remember to always start by basic case solution. for the square root problem, we have 0 and 1
        c += 1
        return n, c
    ### END CODE ###



    ### BEGIN CODE ###
    lowerEqualTuple = getLowerEqualSqrt(n)
    lowOrEqual = lowerEqualTuple[0]
    c += lowerEqualTuple[1]
    c += 1
    if lowOrEqual **2 == n:
        c += 1
        return lowOrEqual, c
    ### END CODE ###

    iteration = 0 # The variable is used to count the number of times we repeat the instructions in the while loop

    ### BEGING CODE ###
    c += 1
    minsqrt = lowOrEqual
    c += 1
    maxsqrt = minsqrt + 1

    c += 1
    result = (minsqrt + maxsqrt) / 2.0

    c += 1
    while abs(n - result ** 2) >= error_threshold :

            c += 1
            if result ** 2 < n : # Hint: have a look at the first function.
                    c += 1
                    minsqrt = result
            else :
                    c += 1
                    maxsqrt = result
            c += 1
            result =  (minsqrt + maxsqrt) / 2.0
            iteration +=1
            c += 1
    ### END CODE ####
    #print(f"Runtime of improved version - n = {n}: {c}")
    return result, c



def main() :
    doc_ =  """
                Welcome to the first Python assignment!!!\n
                You will write your first Python script that computes the square root of a given integer n.
                The template_hw1 provides you with the basic structure of a Python script. Please do not add anything
                out of ### BEGIND CODE ### and ### END CODE ###.

                Feel free to use print for debugging but remember to clean them up before your submission.

                NB: Your performance will not only be evaluated on your capacity to output good results.
                Please make sure you understand each line you code.
            """
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS, description=doc_)
    parser.add_argument('--n', type=int, help="An integer input for which we compute the sqrt root.")
    args = parser.parse_args()
    input_n = args.n

    myvalue = mysqrt(input_n)[0]
    npvalue = sqrt(input_n)


    assert round(myvalue, 2) == round(myvalue, 2), "Input test failled. Please, check your script again. your sqrt = {} and numpy sqrt = {}".format(myvalue, npvalue)

    print("The input is n = {}".format(input_n))
    print("Your square root of {} is {}".format(input_n, myvalue))
    print("The numpy square root of {} is {}".format(input_n, npvalue))
    print("The error precision is ", abs(myvalue - npvalue))

    first_test =  random.randint(1, 100, 20)
    first_test_stat = 0
    for n in first_test :
        myvalue = mysqrt(n)[0]
        npvalue = sqrt(n)
        if round(myvalue, 2) == round(npvalue, 2):
            first_test_stat = first_test_stat + 1

    if first_test_stat == len(first_test):
        print("All tests past.")
        print("Congratulation on achieving your first assignment.")
    else :
        success_rate = first_test_stat*100./len(first_test)
        print("Only {}% of the tests past".format(str(success_rate)))
        print("Please, check your code and try it again.")


if __name__ == '__main__':
    main()
