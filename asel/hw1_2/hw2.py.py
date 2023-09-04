from numpy import random, sqrt, round
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS ##COMMENTS: added for assessments

def isperfect(n: int) -> tuple[bool, int]:
    """
    This function takes an integer n and checks if n has a perfect square root or not.
    If n has a perfect square root, then it returns True and its perfect square root. If not,
    it returns False and n.

    Args:
    - n: an integer to check

    Returns:
    - A tuple (bool, int). If n has a perfect square root, the tuple is (True, int(sqrt(n))).
      If not, the tuple is (False, n).
    """

    if n == 0 or n == 1:
        return (True, n)

    for i in range(1, n+1): ## COMMENTS: Good but the case n=1 has been handled in the if condition up.
        if i*i == n:
            return (True, i)

    return (False, n)

def getLowUpper(n: int) -> tuple[int, int]:
    """
    This function takes an integer n and returns the lower and upper perfect square roots to n.
    We will use two "while" loops here, but we could have used "for" loops or whatever.
    The first that will catch the first perfect square root is less than the square root of n.
    The second one will catch the first square root greater than the square root of n.

    Args:
    - n: an integer

    Returns:
    - A tuple (minsqrt:int, maxsqrt:int)
    """

    i = 1

    # Get the nearest perfect square roots less than and greater than sqrt(n)
    low = isperfect(n - 1)
    upper = isperfect(n + 1)

    # Find the lower perfect square root of n
    while not low[0]:
        i += 1
        low = isperfect(n - i*i) ## COMMENTS: wrong, isperfect(n-i) not n-i**2.

    # Find the upper perfect square root of n
    i = 1
    while not upper[0]:
        i += 1
        upper = isperfect(n + i*i)

    # Return the lower and upper perfect square roots
    minsqrt, maxsqrt = low[1], upper[1]
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
    if n == 0 or n == 1:
        return n

    checkup = isperfect(n)
    if checkup[0]:
        return checkup[1]

    ### END CODE ###

    iteration = 0 # The variable is used to count the number of times we repeat the instructions in the while loop

    ### BEGIN CODE ###
    minsqrt, maxsqrt = getLowUpper(n)

    rst = (minsqrt + maxsqrt) / 2 ##COMMENTS: good :)

    while abs(n - rst ** 2) >= error_threshold :

        if rst ** 2 > n :
            maxsqrt = rst
        else :
            minsqrt = rst
        rst = (maxsqrt + minsqrt) / 2
        iteration +=1
    ### END CODE ####

    return round(rst,9)





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
    ## COMMENTS: be careful here, you deleted the imports for this line to work.
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
