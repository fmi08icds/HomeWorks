from numpy import random, sqrt, round
from typing import Tuple
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


def has_perfect_sqrt(n: int) -> Tuple[bool, int]:
    """
    This function is the first helper. It takes an integer n and checks if
    n has a perfect square root or not. If n has a perfect square root,
    then it returns True and its perfect square root. If not, it returns
    False and n

    :param int n: The input number for which this method searches the
                  perfect square root
    :return: A tuple containing the boolean indicating if a perfect square
             root could be found and an integer that either represents the
             perfect square root if one was found or the
             original input argument
    :rtype: Tuple[bool, int]
    """

    if n == 0 or n == 1:
        return (True, n)

    for i in range(2, n):
        if i**2 == n:
            return (True, i)
    return (False, n)


def get_low_and_upper_perfect_sqrt(n: int) -> Tuple[float, float]:
    """
    This function is the second helper. It takes an integer n and returns
    the lower and upper perfect square root to n. We will use two "while"
    loops here, but we could have used "for" loops or whatever. The first
    that will catch the first perfect square root is less than the square
    root of n. The second one will catch the first square root greater than
    the square root of n

    :param int n: The input number for which this method searches the
                  square root
    :return: A tuple containing the upper and lower approximation of the
             square root of the give number
    :rtype: Tuple[float, float]
    """

    i = 1
    low = has_perfect_sqrt(n - i)
    upper = has_perfect_sqrt(n + i)

    while not low[0]:
        i += 1
        low = has_perfect_sqrt(n - i)

    i = 1
    while not upper[0]:
        i += 1
        upper = has_perfect_sqrt(n + i)

    minsqrt, maxsqrt = low[1], upper[1]

    return minsqrt, maxsqrt


def approximate_sqrt(n: int, error_threshold=0.000000001) -> float:
    """
    This function is the main function. It takes an integer n and returns the
    square root of n. We will use here the two helper functions we wrote
    previously.

    :param int n: The input number for which this method searches the square
                  root
    :param float error_threshold: The error delta that is allowed for the
                                  square root approximation
    :return: An approximation of the square root of the given number
    :rtype: float
    """

    if n == 0 or n == 1:
        return n

    checkup = has_perfect_sqrt(n)
    if checkup[0]:
        return checkup[1]

    iteration = 0

    minsqrt, maxsqrt = get_low_and_upper_perfect_sqrt(n)

    rst = (minsqrt + maxsqrt) / 2

    while abs(rst**2 - n) >= error_threshold:
        if rst**2 < n:
            minsqrt = rst
        else:
            maxsqrt = rst

        rst = (minsqrt + maxsqrt) / 2
        iteration += 1

    return rst


def main():
    doc_ = """
            Welcome to the first Python assignment!!!\n
            You will write your first Python script that computes the square root of a given integer n.
            The template_hw1 provides you with the basic structure of a Python script. Please do not add anything
            out of ### BEGIND CODE ### and ### END CODE ###.

            Feel free to use print for debugging but remember to clean them up before your submission.

            NB: Your performance will not only be evaluated on your capacity to output good results.
            Please make sure you understand each line you code.
            """

    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        argument_default=SUPPRESS,
        description=doc_,
    )
    parser.add_argument(
        "-n", type=int, help="An integer input for which we compute the sqrt root."
    )
    args = parser.parse_args()
    input_n = 16

    myvalue = approximate_sqrt(input_n)
    npvalue = sqrt(input_n)

    assert round(myvalue, 2) == round(
        myvalue, 2
    ), "Input test failled. Please, check your script again. your sqrt = {} and numpy sqrt = {}".format(
        myvalue, npvalue
    )

    print("The input is n = {}".format(input_n))
    print("Your square root of {} is {}".format(input_n, myvalue))
    print("The numpy square root of {} is {}".format(input_n, npvalue))
    print("The error precision is ", abs(myvalue - npvalue))

    first_test = random.randint(1, 100, 20)
    first_test_stat = 0
    for n in first_test:
        myvalue = approximate_sqrt(n)
        npvalue = sqrt(n)
        if round(myvalue, 2) == round(sqrt(n), 2):
            first_test_stat = first_test_stat + 1

    if first_test_stat == len(first_test):
        print("All tests past.")
        print("Congratulation on achieving your first assignment.")
    else:
        success_rate = first_test_stat * 100.0 / len(first_test)
        print("Only {}% of the tests past".format(str(success_rate)))
        print("Please, check your code and try it again.")


if __name__ == "__main__":
    main()
