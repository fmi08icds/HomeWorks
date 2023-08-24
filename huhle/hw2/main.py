from numpy import random, sqrt, round
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS

""" Why did you remove the comments?"""
def isperfect(n: int ):
    if n == 0 or n == 1:
        return (True, n)

    ### BEGIN CODE #####
    for i in range(n): # But you already check 0 and 1
        if i*i == n:
            return True, i
    return False, n
    ### END CODE #####


def getLowUpper(n: int):
    i = 1
    ### BEGIN CODE ####
    low = isperfect(n-1)
    upper = isperfect(n+1)

    while not low[0]:
        i += 1
        low = isperfect(n-i) ## good!

    i = 1
    while not upper[0]:
        i += 1
        upper = isperfect(n+i)

    minsqrt, maxsqrt = low[1], upper[1]
    ### END CODE ####

    return minsqrt, maxsqrt



def mysqrt(n: int, error_threshold=0.000000001) -> float:
    ### BEGIN CODE ###
    if n == 0 or n == 1:
        return n
    ### END CODE ###

    ### BEGIN CODE ###
    checkup = isperfect(n)
    if checkup[0]:
        return checkup[1]
    ### END CODE ###

    iteration = 0

    ### BEGING CODE ###
    minsqrt, maxsqrt = getLowUpper(n)

    rst =  (minsqrt + maxsqrt) / 2 # It works but better to use 2. to make sure the div is in ID even for Python versions <3.0

    while abs(rst*rst - n) >= error_threshold:

            if rst*rst < n:
                    minsqrt = rst # Good!
            else :
                    maxsqrt = rst
            rst = (minsqrt + maxsqrt) / 2
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
