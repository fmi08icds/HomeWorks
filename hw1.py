from numpy import sqrt

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
    
    for i in range(1, n+1):
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
        low = isperfect(n - i*i)
    
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

    rst = (minsqrt + maxsqrt) / 2

    while abs(n - rst ** 2) >= error_threshold :

        if rst ** 2 > n :
            maxsqrt = rst
        else :
            minsqrt = rst
        rst = (maxsqrt + minsqrt) / 2
        iteration +=1
    ### END CODE ####

    return round(rst,9)
