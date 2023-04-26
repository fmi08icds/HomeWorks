# cProfile results

### Steps taken: 

1. The cProfile results of the original script `mysqrt.py` can be output to a profile file using the following (here we used input size  = 99999)
    > `python -m cProfile -o hw3_profile.prof  mysqrt.py --n=99999`
    
2. This file can be read using the pstats module (standard python module) by using the following:
    > `python3 -m pstats hw3.prof`
    
3. This brings up the pstats profile statistics viewer. We sort by time and view the statistics using the following:
    > `sort time` 
    
    > `stats` 
    
4. The following is the output of top 10 most time-costly methods/functions of the mysqrt script. 

        Tue Apr 25 23:50:20 2023    popov_hw3.prof

                 71284 function calls (69529 primitive calls) in 19.020 seconds

           Ordered by: internal time

           ncalls  tottime  percall  cumtime  percall filename:lineno(function)
              897   18.798    0.021   18.798    0.021 popov_hw3.py:6(isperfect)
            29/27    0.051    0.002    0.055    0.002 {built-in method _imp.create_dynamic}
              111    0.018    0.000    0.018    0.000 {built-in method marshal.loads}
              111    0.015    0.000    0.015    0.000 {method 'read' of '_io.BufferedReader' objects}
              618    0.007    0.000    0.007    0.000 {built-in method posix.stat}
          245/242    0.005    0.000    0.009    0.000 {built-in method builtins.__build_class__}
            29/19    0.005    0.000    0.025    0.001 {built-in method _imp.exec_dynamic}
              111    0.005    0.000    0.005    0.000 {built-in method io.open_code}
              290    0.004    0.000    0.019    0.000 <frozen importlib._bootstrap_external>:1536(find_spec)
               22    0.003    0.000    0.003    0.000 {method 'round' of 'numpy.ndarray' objects}
               
5. A better way to visualize this is to use the tuna profile viewer. (Install with `pip install tuna` and run `tuna hw3_profile.prof`) which yields the following diagram:

![tuna_profile_results.png](attachment:f3db20ca-4558-4978-9895-3aec291c0c5d.png)


We can see that the most costly procedure is the **getLowUpper()** function, which calls **isperfect()** in a loop. Therefore, it will help performance if we can optimize the **getLowUpper()** function to not use the **isperfect()** function in a loop. We solve this by implementing an array of perfect squares and iterating through this array, we can find the 2 neighbouring perfect squares to n. 




# Time complexity analysis of square root function.

Comments next to the code denote the time complexity of the relevant operation. 

        def isperfect(n: int ): 
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
    if n == 0 or n == 1: #O(1) + O(1) = O(1) - only one comparison each necessary in the worst case. 
        return (True, n)

    for i in range(n) : #O(n) - worst case if n is not a perfect square, then i will iterate through the entire range(n)   
        if i ** 2  == n :
            return (True, i)
    return (False, n)
    
    
Total worst case time complexity for the function **isperfect()** is: $$O(1) + O(1) + O(n) = O(n)$$

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
    low = isperfect(n-i)  #O(n) - As determined above
    upper = isperfect(n+i) #O(n)

    while not low[0] : #Complexity of while loop: O(n) 
        i += 1
        low = isperfect(n-i) #Complexity of isperfect() helper: O(n) 

    i = 1
    while not upper[0] : #Complexity of while loop: O(n)
        i += 1
        upper = isperfect(n+i) #Complexity of isperfect() helper O(n)

    minsqrt, maxsqrt = low[1], upper[1] 
    
    return minsqrt, maxsqrt
    

To determine the time complexity of the while loop, consider the following quadratic sequence of perfect squares:

$$ 0,1,4,9,16,25, \dots $$ 
whose sequence of **first common differences** is given by 
$$ 1, 3, 5, 7, 9, \dots $$ 
for which the sequence of **second common differences** is given by 
$$ 2, 2, 2, 2, \dots $$ 

Clearly the sequence of **first common differences** is an arithmetic sequence, which tells us for any $n \in \mathbb{N}$ how far away two perfect squares are from one another, given by the sequence formula: $T_n = 1 + (n-1)\cdot 2$. Thus, the distance between 2 subsequent perfect squares yields the worst case complextiy for the lower and upper bound search of: $O(n)$.

Calling the **isperfect()** function within the while loop yields a total time complexity of the **getLowUpper()** function: $$O(n^2)+O(n^2) = O(n^2)$$

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

    if n == 0 or n == 1 : #Complexity O(1)
        return n



    checkup = isperfect(n) #Complexity O(n) 
    if checkup[0] : 
        return checkup[1] 

    iteration = 0 

    minsqrt, maxsqrt = getLowUpper(n) #Complexity 2 * O(n^2) = O(n^2)  

    rst =  (maxsqrt + minsqrt) / 2 

    while maxsqrt - minsqrt >= error_threshold : #Complexity based on error_threshold -> constant w.r.t n 

            if rst ** 2 < n : #Complexity O(1) - only one comparison 
                    minsqrt = rst
            else :
                    maxsqrt = rst
            rst = (maxsqrt + minsqrt) / 2
            iteration +=1

    return rst
    

### The total complexity of the **mysqrt()** function in the *worst case* is thus: $O(n^2)$


# Vectorization results 

Running cProfile for the same n=99999 as before
> `python -m cProfile -s time hw3_vectorization.py --n=99999`

Results in a much faster result: 

      70372 function calls (68617 primitive calls) in 0.227 seconds

       Ordered by: internal time

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
           21    0.030    0.001    0.030    0.001 hw3_vectorization.py:6(isperfect)
        29/27    0.026    0.001    0.030    0.001 {built-in method _imp.create_dynamic}
          111    0.021    0.000    0.021    0.000 {method 'read' of '_io.BufferedReader' objects}
          111    0.019    0.000    0.019    0.000 {built-in method marshal.loads}
      245/242    0.005    0.000    0.009    0.000 {built-in method builtins.__build_class__}
          618    0.004    0.000    0.004    0.000 {built-in method posix.stat}
          290    0.004    0.000    0.019    0.000 <frozen importlib._bootstrap_external>:1536(find_spec)
        29/19    0.004    0.000    0.012    0.001 {built-in method _imp.exec_dynamic}
          148    0.003    0.000    0.027    0.000 <frozen importlib._bootstrap>:921(_find_spec)
           13    0.003    0.000    0.003    0.000 {built-in method posix.listdir}
