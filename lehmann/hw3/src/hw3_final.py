from numpy import random, sqrt, round
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


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

    if n==0 or n==1 :
        return n

    ### begin new code ###
    # If i**2 succeeds n, the number before was the nearest
    # Maybe it could get even faster, if you use some step-size,
    # instead of increasing by 1 everytime

    ### COMMENTS ###
    # This part of the code could have been let in a helper function as in the template> this will be more readable.
    
    nearest = 0 # could also just use i for the nearest value and count i-1 for lowest val
    i = 0
    while i**2 <= n:
        if i**2 == n: # check if it is already perfect square
             return i
        nearest = i
        i += 1

    minsqrt = nearest
    maxsqrt = minsqrt+1 # very good.
    ### end new code ###

    rst = (minsqrt+maxsqrt)/2

    while maxsqrt-minsqrt >= error_threshold :

        if rst**2 < n :
                minsqrt = rst
        else :
                maxsqrt = rst
        rst = (minsqrt+maxsqrt)/2

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
