from numpy import random, sqrt, round, floor, ceil, int16, arange, searchsorted
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS

## COMMENTS: please rename your assignement file properly. template_hw1 is not coherent.

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
    ### BEGIN CODE #####
    for i in range(int16(floor((n+1)/2))+1): # Hint: you can use the range, or any sequence type. if you don't remember how it works, have a look at the documentation.
        if i*i == n :
            return True, i
    return (False, n)
    ### END CODE #####


## COMMENTS optimize without renaming the functions in the template
def vec_isperfect(n:int):
    """
        This function is the suggested optimal version instead of the first helper. It takes an integer n and checks if n has a perfect square root or not.
        If n has a perfect square root, then it returns True and its perfect square root. If not, it returns False and n.
        It does this by creating an numpy array from 1 to (n+1/2)/2 which is always larger than sqrt(n) but smaller than n and then performs a binary search
        on the squared entrys of that vector looking for n. If it finds n it returns the position of the index of the square number in the array [where i**2=n or i=sqrt(n)]
        and returns false if the binary search does not find n in its squared values.

        INPUT: n as an integer.
        OUTPUT: a tuple (bool, int).

        Examples:
        isperfect(0) = (True, 0)
        isperfect(1) = (True, 1)
        isperfect(3) = (False, 3)
        isperfect(16) = (True, 4)
    """
    # init vector with possible candidates
    vec = arange(((n+1)/2)+1)
    # check if n is in vec**2 in O(log(n)) time with binary search.
    if res:=searchsorted(vec**2, n):
    # the lookup happens in O(1).
         if vec[res]**2 == n:
            return (True, res)
    return(False, n)


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


def getLowUpper_opt(n: int): ## COMMENTS this function could be further optimized.
    """
        This function is the proposed optimized solution to the second helper. It takes an integer n and returns the lower and upper perfect square root to n.
        We will use two "while" loops here, but we could have used "for" loops or whatever.
        The first that will catch the first perfect square root is less than the square root of n.
        The second one will catch the first square root greater than the square root of n.
        But this time using the first optimized helper function instead of the old, slow one.
        INPUT: n as an integer.
        OUTPUT: a tuple (minsqrt:int, maxsqrt:int)

        Examples:
        getLowUpper(3) = (1,2)
        getLowUpper(15) = (3,4)
    """
    i = 1
    ### BEGIN CODE ####
    low = vec_isperfect(n-1)
    upper = vec_isperfect(n+1)

    ## these loops are executed as long as they do not find a perfect root.
    ## once they find the perfect root that is closest to n, they stop.
    while not low[0]:
        i += 1
        low = vec_isperfect(n - i)

    i = 1
    while not upper[0]:
        i += 1
        upper = vec_isperfect(n + i)

    minsqrt, maxsqrt = low[1], upper[1]
    ### END CODE ####

    return minsqrt, maxsqrt


def mysqrt_fast(n: int, error_threshold=0.000000001):
    '''
    takes in a number n and returns the square root of n wihtout using the sqrt function.
    '''
    # create a function that takes in a number n and returns the square root of n wihtout using the sqrt function.
    # create a variable "guess" and set it to n/2
    guess = n/2.0
    # create a variable "error" and set it to 1
    error = abs(guess**2 - n)

    # create a while loop that runs as long as the error is greater than the error_threshold
    while error > error_threshold:
        # create a variable "new_guess" and set it to the average of guess and n/guess
        new_guess = (guess + n/guess)/2
        # create a variable "error" and set it to the absolute value of guess minus new_guess
        error = abs(guess - new_guess)
        # create a variable "guess" and set it to new_guess
        guess = new_guess
    return guess




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
    ## Hint: remember to always start by basic case solution. for the square root problem, we have 0 and 1
    if n == 0 or n == 1:
        return n
    ### END CODE ###



    ### BEGIN CODE ###

    ## solve for special cases.


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

def mysqrt_opt(n: int, error_threshold=0.000000001) -> float:
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
    ## Hint: remember to always start by basic case solution. for the square root problem, we have 0 and 1
    if n == 0 or n == 1:
        return n
    ### END CODE ###

    ### BEGIN CODE ###

    checkup = vec_isperfect(n) # Hint: use the one of the helpers you already coded.
    if checkup[0] : # How to access an element of the tuple?
        return checkup[1] # type: ignore #Choose the right index...
    ### END CODE ###

    iteration = 0 # The variable is used to count the number of times we repeat the instructions in the while loop

    ### BEGING CODE ###
    minsqrt, maxsqrt = getLowUpper_opt(n) #Hint: use the second helper function.

    rst =  (minsqrt + maxsqrt) / 2.0

    while abs(rst**2 - n) > error_threshold:
            if rst**2 < n : # Hint: have a look at the first function.
                    minsqrt = rst
            else :
                    maxsqrt = rst
            rst = (minsqrt + maxsqrt) / 2.0
            iteration +=1
    ### END CODE ####
    return rst # type: ignore


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


    assert round(myvalue, 2) == round(npvalue, 2), "Input test failled. Please, check your script again. your sqrt = {} and numpy sqrt = {}".format(myvalue, npvalue)

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


    ## test the proposed optimized solution.
    myvalue2 = mysqrt_opt(input_n)
    npvalue = sqrt(input_n)
    assert round(myvalue2, 2) == round(npvalue, 2), "Input test failled. Please, check your script again. your sqrt = {} and numpy sqrt = {}".format(myvalue2, npvalue)

    print("The input is n = {}".format(input_n))
    print("Your square root of {} is {}".format(input_n, myvalue2))
    print("The numpy square root of {} is {}".format(input_n, npvalue))
    print("The error precision is ", abs(myvalue2 - npvalue))

    first_test =  random.randint(1, 100, 20)
    first_test_stat = 0
    for n in first_test :
        myvalue2 = mysqrt_opt(n)
        npvalue = sqrt(n)
        if round(myvalue2, 2) == round(sqrt(n), 2):
            first_test_stat = first_test_stat + 1

    if first_test_stat == len(first_test):
        print("All tests past.")
        print("Congratulation on achieving your first assignment.")
    else :
        success_rate = first_test_stat*100./len(first_test)
        print("Only {}% of the tests past".format(str(success_rate)))
        print("Please, check your code and try it again.")

    ## test the proposed optimized solution.
    myvalue3 = mysqrt_fast(input_n) ## COMMENTS: this runs way slower than your slow version with n = 22470020
    npvalue = sqrt(input_n)
    assert round(myvalue3, 2) == round(npvalue, 2), "Input test failled. Please, check your script again. your sqrt = {} and numpy sqrt = {}".format(myvalue3, npvalue)

    print("The input is n = {}".format(input_n))
    print("Your square root of {} is {}".format(input_n, myvalue3))
    print("The numpy square root of {} is {}".format(input_n, npvalue))
    print("The error precision is ", abs(myvalue3 - npvalue))

    first_test =  random.randint(1, 100, 20)
    first_test_stat = 0
    for n in first_test :
        myvalue3 = mysqrt_fast(n)
        npvalue = sqrt(n)
        if round(myvalue3, 2) == round(sqrt(n), 2):
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
