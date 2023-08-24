from numpy import random, sqrt, round
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
import time


sum_time_complexity = {"isperfect": 0,
                       "getLowUpper": 0,
                       "mysqrt": 0,
                       "main": 0
                       }

##COMMENTS: well presented. Something is wrong in your implementation since you can't computer the square root of 22470020 faster than 10000000
def time_complexity(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        timespan = end_time - start_time
        sum_time_complexity[func.__name__] += timespan
        print(f"Time taken by {func.__name__}: {timespan:.6f}s")
        return result
    return wrapper


@time_complexity
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

    # Set the search range to be the entire sequence from 0 to n
    left = 0
    right = n

    # Binary search loop
    while left <= right:
        # Calculate the middle index and the square of the middle element
        mid = (left + right) // 2
        mid_squared = mid * mid

        # If mid_squared equals n, we have found the perfect square root of n
        if mid_squared == n:
            return (True, mid)
        # If mid_squared is less than n, search in the right half of the sequence
        elif mid_squared < n:
            left = mid + 1
        # If mid_squared is greater than n, search in the left half of the sequence
        else:
            right = mid - 1

    return (False, n)


@time_complexity
def getLowUpper(n: int):
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
    # Find the lower perfect square root of n using binary search
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared <= n:
            left = mid + 1
            low = mid
        else:
            right = mid - 1

    # Find the upper perfect square root of n using binary search
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared >= n:
            right = mid - 1
            upper = mid
        else:
            left = mid + 1

    return low, upper


@time_complexity
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
    if n == 0 or n == 1 : ## Hint: remember to always start by basic case solution. for the square root problem, we have 0 and 1
        return n

    if n < 0:
        raise Exception("No numbers below zero - you can't compute square route with negative numbers!")
    ### END CODE ###



    ### BEGIN CODE ###
    checkup = isperfect(n) # Hint: use the one of the helpers you already coded.
    if checkup[0] : # How to access an element of the tuple?
        return checkup[1] #Choose the right index...
    ### END CODE ###

    iteration = 0 # The variable is used to count the number of times we repeat the instructions in the while loop

    ### BEGING CODE ###
    minsqrt, maxsqrt = getLowUpper(n) #Hint: use the second helper function.

    rst = (minsqrt + maxsqrt) / 2

    while abs(rst * rst - n) >= error_threshold:

            if rst * rst < n: # Hint: have a look at the first function.
                    minsqrt = rst
            else :
                    maxsqrt = rst
            rst = (minsqrt + maxsqrt) / 2
            iteration += 1
    ### END CODE ####

    return rst

@time_complexity
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

    first_test = random.randint(1, 100, 20)
    first_test_stat = 0
    for n in first_test:
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

    for d in sum_time_complexity:
        if d != "main":
            print(f"Total time taken by {d}: {sum_time_complexity[d]:.6f}s")



if __name__ == '__main__':
    main()
