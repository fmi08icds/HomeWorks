# Homework 4

## 1. What does the code do?

The code creates two lists, list_mu and list_sigma, of length 100. 
While list_mu contains the means, list_sigma contains the standard deviations 
of 100 lists (list_rst) of length 1000, which contain random numbers around π (pi).
list_mu is then plotted as a histogram. 
The values of list_mu have a normal distribution. 

## 2. vectorized version of the function `NoName()`

A vectorized form for the `NoName()` function is given below:

    def random_normal_around_pi(n):
        """
        :type n: int
        :return random numbers of a tight normalized distribution around pi
        """
    
        r = 1.0
    
        list_x = np.random.uniform(low=0., high=r, size=n)
        list_y = np.random.uniform(low=0., high=r, size=n)
    
        bool_list_accepted_x = list_y < f(list_x, r)
        list_accepted_x = list_x[bool_list_accepted_x]
    
        fin: float = len(list_accepted_x) / float(n)
    
        return 4*fin


## Comparison of the computational times of the vectorized to the non-vectorized version 

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)

      100    0.215    0.002    0.758    0.008 template_hw2.py:35(NoName)

      100    0.003    0.000    0.012    0.000 template_hw2.py:17(random_normal_around_pi)

