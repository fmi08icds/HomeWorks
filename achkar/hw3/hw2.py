from numpy import random, sqrt, round
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS

# def isperfect(n: int):
#     """
#         This function is the first helper. It takes an integer n and checks if n has a perfect square root or not.
#         If n has a perfect square root, then it returns True and its perfect square root. If not, it returns False and n.

#         INPUT: n as an integer.
#         OUTPUT: a tuple (bool, int).

#         Examples:
#         isperfect(0) = (True, 0)
#         isperfect(1) = (True, 1)
#         isperfect(3) = (False, 3)
#         isperfect(16) = (True, 4)
#     """
#     if n == 0 or n == 1: #time complexity O(1)
#         return (True, n)

#     ### BEGIN CODE #####
#     for i in range(n):  # Hint: you can use the range, or any sequence type. if you don't remember how it works, have a look at the documentation.
#         if i * i == n : # replace None by the appropriate code.
#             return True, i
#     return False, n # time complexity O(n)
#     ### END CODE #####'

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
    lo = 1
    hi = num

    # Binary Search
    while (hi - lo > 1) :    #### <------ the worst case complexity still remains you could eliminate this while loop. 
        mid = (int)((hi + lo) / 2)
        if (num == 0 or num == 1):
            return True, num
        elif (mid * mid == num) :
            return True, mid
        elif (mid * mid > num) :
            hi = mid
        elif (mid * mid < num) :
            lo = mid

    if (lo * lo == num):
        return True, lo
    elif (hi * hi == num):
        return True, hi
    else:
        return False, num
    # time complexity O(log(n))

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
    i = 1
    ### BEGIN CODE ####
    low = isperfect_improved(n-i) # old time complexity O(n) / new time complexity O(log(n))
    upper = isperfect_improved(n+i) # old time complexity O(n) / new time complexity O(log(n))

    while not low[0]: ## Hint: look at the second while loop.
        i += 1
        low = isperfect_improved(n-i) # old time complexity O(n) / new time complexity O(log(n))

    i = 1
    while not upper[0]:
        i += 1
        upper = isperfect_improved(n+i) # old time complexity O(n) / new time complexity O(log(n))

    minsqrt, maxsqrt = low[1], upper[1] # Hint: remember what is the output of helper 1.
    # old time complexity O(n) / new time complexity O(log(n))
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
    if n == 0 or n == 1 : ## Hint: remember to always start by basic case solution. for the square root problem, we have 0 and 1
        return n # time complexity O(1)
    ### END CODE ###

    ### BEGIN CODE ###
    checkup = isperfect_improved(n) # Hint: use the one of the helpers you already coded.
    if checkup[0] : # How to access an element of the tuple?
        return checkup[1] #Choose the right index...
                    # old time complexity O(n) / new time complexity O(log(n))
    ### END CODE ###

    iteration = 0 # The variable is used to count the number of times we repeat the instructions in the while loop

    ### BEGING CODE ###
    minsqrt, maxsqrt = getLowUpper(n) #Hint: use the second helper function.
    # old time complexity O(n) / new time complexity O(log(n))

    rst =  (minsqrt + maxsqrt) / 2  # time complexity O(1)

    while abs(rst*rst - n) >= error_threshold :

            if rst*rst < n : # Hint: have a look at the first function.
                    minsqrt = rst
            else :
                    maxsqrt = rst
            rst = (minsqrt + maxsqrt) / 2
            iteration +=1 # time complexity O(log(n)
    ### END CODE ####

    return rst # old time complexity O(n) / new time complexity O(log(n))

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
