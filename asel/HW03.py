# README.md uploaded



import numpy as np
import argparse
import cProfile
import timeit

def is_perfect_square(n):
    """
    Checks if n is a perfect square and returns the result along with the square root.
    """
    if n == 0 or n == 1:
        return True, n

    low = 1
    high = n // 2

    while low <= high:
        mid = (low + high) // 2

        if mid * mid == n:
            return True, mid

        elif mid * mid < n:
            low = mid + 1

        else:
            high = mid - 1

    return False, n


def get_low_upper(n): ##COMMENTS: this function would have been improved as well
    """
    Returns the lower and upper perfect square root of n using two while loops.
    """
    i = 1
    low = is_perfect_square(n - i)
    upper = is_perfect_square(n + i)

    while not low[0]:
        i += 1
        low = is_perfect_square(n - i) ##COMMENTS: but it was not correct in the hw2, where did you get it right from?

    i = 1
    while not upper[0]:
        i += 1
        upper = is_perfect_square(n + i)

    return low[1], upper[1]


def my_sqrt(n, error_threshold=0.000000001):
    """
    Calculates the square root of n using binary search and helper functions.
    """
    if n == 0 or n == 1:
        return n

    checkup = is_perfect_square(n)
    if checkup[0]:
        return checkup[1]

    minsqrt, maxsqrt = get_low_upper(n)
    rst = (minsqrt + maxsqrt) / 2

    while abs(rst * rst - n) >= error_threshold:
        if rst * rst < n:
            minsqrt = rst
        else:
            maxsqrt = rst
        rst = (minsqrt + maxsqrt) / 2

    return rst


def main():
    doc_ = """
        Welcome to the first Python assignment!!!
        You will write your first Python script that computes the square root of a given integer n.
        The template_hw1 provides you with the basic structure of a Python script. Please do not add anything
        out of ### BEGIND CODE ### and ### END CODE ###.
        Feel free to use print for debugging but remember to clean them up before your submission.
        NB: Your performance will not only be evaluated on your capacity to output good results.
        Please make sure you understand each line you code.
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, description=doc_)
    parser.add_argument('--n', type=int, help="An integer input for which we compute the sqrt root.")
    args = parser.parse_args()
    input_n = args.n

    my_value = my_sqrt(input_n)
    np_value = np.sqrt(input_n)

    assert round(my_value, 2) == round(np_value, 2), "Input test failed. Please, check your script again. Your sqrt = {} and numpy sqrt = {}".format(my_value, np_value)

    print("The input is n =", input_n)
    print("Your square root of {} is {}".format(input_n, my_value))
    print("The numpy square root of {} is {}".format(input_n, np_value))
    print("The error precision is ", abs(my_value - np_value))

    first_test = np.random.randint(1, 100, 20)
    first_test_stat = 0
    for n in first_test:
        my_value = my_sqrt(n)
        np_value = np.sqrt(n)
        if round(my_value, 2) == round(np.sqrt(n), 2):
            first_test_stat += 1

    if first_test_stat == len(first_test):
        print("All tests passed.")
        print("Congratulations on achieving your first assignment.")
    else:
        success_rate = first_test_stat * 100. / len(first_test)
        print("Only {:.2f}% of the tests passed".format(success_rate))
        print("Please, check your code and try it again.")


if __name__ == '__main__':
    cProfile.run('main()')
    elapsed_time = timeit.timeit(lambda: my_sqrt(1234), number=1000)
    print("Elapsed time:", elapsed_time)

    main()
