from numpy import random, sqrt, round, floor, ceil, int16
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS

## COMMENTS: surprisingly your first implementation of the sqrt function in hw2/ does not work.
## COMMENTS: so, where did you take this code in hw3 from?


def isperfect(n: int):
    """
        This function is the first helper. It takes an integer n and checks if n has a perfect square root or not.
        If n has a perfect square root, then it returns True and its perfect square root. If not, it returns False and n.
        INPUT: n as an integer.
        OUTPUT: a tuple (bool, int).
        Examples:
        isperfect(0) = (True, 0)
        isperfect(1) = (True, 1)
        isperfect(3) = (False, 3)
        isperfect(16) = (True, 4)
    """
    if n == 0 or n == 1:
        return (True, n)

    ### BEGIN CODE #####
    for i in range(int16(floor((n+1)/2))+1): # Hint: you can use the range, or any sequence type. if you don't remember how it works, have a look at the documentation.
        if i*i == n :
            return True, i
    return (False, n)
    ### END CODE #####

def isperfect_improved(num: int):
    """
        This function is the first helper. It takes an integer n and checks if n has a perfect square root or not using binary search.
        If n has a perfect square root, then it returns True and its perfect square root. If not, it returns False and n.
        INPUT: n as an integer.
        OUTPUT: a tuple (bool, int).
        Examples:
        isperfect_improved(0) = (True, 0)
        isperfect_improved(1) = (True, 1)
        isperfect_improved(3) = (False, 3)
        isperfect_improved(16) = (True, 4)
    """

    ### COMMENTS: This function is empty


def getLowUpper(n: int): ##COMMENTS: this function as well could be optimised.
    """
        This function is the second helper. It takes an integer n and returns the lower and upper perfect square root to n.
        We will use two "while" loops here, but we could have used "for" loops or whatever.
        The first that will catch the first perfect square root is less than the square root of n.
        The second one will catch the first square root greater than the square root of n.
        INPUT: n as an integer.
        OUTPUT: a tuple (minsqrt:int, maxsqrt:int)
        Examples:
        getLowUpper(3) = (1,2)
        getLowUpper(15) = (3,4)
    """
    i = 1
    ### BEGIN CODE ####
    low = isperfect(n-1)
    upper = isperfect(n+1)

    ## these loops are executed as long as they do not find a perfect root.
    ## once they find the perfect root that is closest to n, they stop.
    while not low[0]:
        i += 1
        low = isperfect(n - i)

    i = 1
    while not upper[0]:
        i += 1
        upper = isperfect(n + i)

    minsqrt, maxsqrt = low[1], upper[1]
    ### END CODE ####

    return minsqrt, maxsqrt



def mysqrt(n: int, error_threshold=0.000000001) -> float:
    """
        This function is the main function. It takes an interger n and returns the square root of n.
        We will use here the two helper functions we wrote previously.
        INPUT: n as an integer.
        OUTPUT: a float rst
        Examples:
        mysqrt(3) = 1.7320508076809347
        mysqrt(15) = 3.8729833462275565
    """

    ### BEGIN CODE ###
    if n == 1 or n == 0 : ## Hint: remember to always start by basic case solution. for the square root problem, we have 0 and 1
        return n
    ### END CODE ###



    ### BEGIN CODE ###

    ## solve for special cases.
    if n == 0 or n == 1:
        return n

    checkup = isperfect(n) # Hint: use the one of the helpers you already coded.
    if checkup[0] : # How to access an element of the tuple?
        return checkup[1] #Choose the right index...
    ### END CODE ###

    iteration = 0 # The variable is used to count the number of times we repeat the instructions in the while loop

    ### BEGING CODE ###
    minsqrt, maxsqrt = getLowUpper(n) #Hint: use the second helper function.

    rst =  (minsqrt + maxsqrt) / 2.0

    while abs(rst**2 - n) > error_threshold:

            if rst**2 < n : # Hint: have a look at the first function.
                    minsqrt = rst
            else :
                    maxsqrt = rst
            rst = (minsqrt + maxsqrt) / 2.0

            iteration +=1
    ### END CODE ####
    return rst

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

    myvalue = mysqrt(input_n)
    npvalue = sqrt(input_n)


    assert round(myvalue, 2) == round(myvalue, 2), "Input test failled. Please, check your script again. your sqrt = {} and numpy sqrt = {}".format(myvalue, npvalue)

    print("The input is n = {}".format(input_n))
    print("Your square root of {} is {}".format(input_n, myvalue))
    print("The numpy square root of {} is {}".format(input_n, npvalue))
    print("The error precision is ", abs(myvalue - npvalue))

    first_test =  random.randint(1, 100, 20)
    first_test_stat = 0
    for n in first_test :
        myvalue = mysqrt(n)
        npvalue = sqrt(n)
        if round(myvalue, 2) == round(sqrt(n), 2):
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




'''import cProfile
import pstats
from pstats import SortKey
from template_hw1 import *
import numpy as np

def main():
    input_range = range(1, 10001, 100)

    for num in input_range:
        with cProfile.Profile() as pr:
            mysqrt(num)
        stats1 = pstats.Stats(pr).sort_stats(SortKey.TIME)

        with cProfile.Profile() as pr:
            np.sqrt(num)
        stats2 = pstats.Stats(pr).sort_stats(SortKey.TIME)

        print(f"Input: {num}")
        print("mysqrt:")
        stats1.print_stats()
        print("np.sqrt:")
        stats2.print_stats()
        print("========================================")


if __name__ == '__main__':
    main()
'''
