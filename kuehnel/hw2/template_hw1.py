import numpy as np
from numpy import random, sqrt, round
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS

## COMMENTS: instructed to not add any code out of the BEGIN and END CODE.
def is_perfect(n: int):
    """
        This function is the first helper. It takes an integer n and checks
        if n has a perfect square root or not.
        If n has a perfect square root, then it returns True and its
        perfect square root. If not, it returns False and n.

        INPUT: n as an integer.
        OUTPUT: a tuple (bool, int).

        Examples:
        is_perfect(0) = (True, 0)
        is_perfect(1) = (True, 1)
        is_perfect(3) = (False, 3)
        is_perfect(16) = (True, 4)
    """
    if n == 0 or n == 1:
        return True, n

    for i in range(n): ## COMMENTS: range should start at 2 since n=0 and n= 1 hace already been considered in the if statement.
        if (i**2) == n:
            return True, i
    return False, None


def get_lower_upper(n: int):
    """
        This function is the second helper. It takes an integer n and returns
        the lower and upper perfect square root to n. We will use two "while"
        loops here, but we could have used "for" loops or whatever.
        The first that will catch the first perfect square root is less than
        the square root of n.
        The second one will catch the first square root greater than
        the square root of n.

        INPUT: n as an integer.
        OUTPUT: a tuple (min_sqrt:int, max_sqrt:int)

        Examples:
        get_lower_upper(3) = (1,2)
        get_lower_upper(15) = (3,4)
    """
    if n <= 0:
        return None, None

    i = 1
    lower = is_perfect(n - i)
    upper = is_perfect(n + i)

    while not lower[0]:
        i += 1
        lower = is_perfect(n - i) ## COMMENTS: good!

    i = 1
    while not upper[0]:
        i += 1
        upper = is_perfect(n + i)

    return lower[1], upper[1]


def my_sqrt(n: int, error_threshold=0.000000001) -> float:
    """
        This function is the main function. It takes an integer n
        and returns the square root of n.
        We will use here the two helper functions we wrote previously.


        INPUT: n as an integer.
        OUTPUT: a float rst

        Examples:
        my_sqrt(3) = 1.7320508076809347
        my_sqrt(15) = 3.8729833462275565
    """
    # Hint: remember to always start by basic case solution.
    # for the square root problem, we have 0 and 1
    if n < 0:
        return np.NaN
    if n == 0 or n == 1:
        return n

    checkup = is_perfect(n)
    if checkup[0]:  # If n is a perfect square root, return it.
        return checkup[1]

    min_sqrt, max_sqrt = get_lower_upper(n)
    rst = (min_sqrt + max_sqrt) / 2. ## COMMENTS: good
    rst_squared = rst**2 ## COMMENTS: no need to creat new variable
    # The variable is used to count the number of times
    # we repeat the instructions in the while loop
    iteration = 0
    while abs(n - rst_squared) >= error_threshold: ##COMENTS: maxsqrt-minsqrt >= error_threshold should be enough
        if rst_squared < n:  # Hint: have a look at the first function.
            min_sqrt = rst ## COMMENTS: good
        else:
            max_sqrt = rst
        # calculate new rst and rst_squared values
        rst = (min_sqrt + max_sqrt) / 2.
        rst_squared = rst**2
        iteration += 1
    # print(f"my_sqrt took {iteration} iterations to calculate the solution.")
    return rst


def main():
    doc_ = """
                Welcome to the first Python assignment!!!\n
                You will write your first Python script that computes
                the square root of a given integer n.
                The template_hw1 provides you with the basic structure of
                a Python script. Please do not add anything
                out of ### BEGIND CODE ### and ### END CODE ###.

                Feel free to use print for debugging but remember
                to clean them up before your submission.

                NB: Your performance will not only be evaluated on your capacity
                to output good results.
                Please make sure you understand each line you code.
            """
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter,
                            argument_default=SUPPRESS, description=doc_)
    parser.add_argument('--n', type=int,
                        help="An integer for which to compute the square root.")
    args = parser.parse_args()
    input_n = args.n

    myvalue = my_sqrt(input_n)
    npvalue = sqrt(input_n)
    error_msg = "Input test failed. Please, check your script again. " \
                "your sqrt = {} and numpy sqrt = {}".format(myvalue, npvalue)

    assert round(myvalue, 2) == round(myvalue, 2), error_msg

    print("The input is n = {}".format(input_n))
    print("Your square root of {} is {}".format(input_n, myvalue))
    print("The numpy square root of {} is {}".format(input_n, npvalue))
    print("The error precision is ", abs(myvalue - npvalue))

    first_test = random.randint(1, 100, 20)
    first_test_stat = 0
    for n in first_test:
        myvalue = my_sqrt(n)
        if round(myvalue, 2) == round(sqrt(n), 2):
            first_test_stat = first_test_stat + 1

    if first_test_stat == len(first_test):
        print("All tests past.")
        print("Congratulation on achieving your first assignment.")
    else:
        success_rate = first_test_stat * 100. / len(first_test)
        print("Only {}% of the tests past".format(str(success_rate)))
        print("Please, check your code and try it again.")


if __name__ == '__main__':
    main()
