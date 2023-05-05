# The objective of the fourth homework:  
The objective is to analyse the code in the template_hw2.py file and achieve the following points: 
* What does the code do? 
* Vectorize the code ?
* Comparison of the computational times


# Answers: 

####  What does the code do ? 
The code employs the **Monte carlo** simulation method to estimates the mathematical constant PI, therefore we can rename the **"NoName"** function to the name **"approximate_pi_with_monte_carlo"**. 
The function works by imagining a circle inscribed in a square of length (R) with the center of the circle in the center of the square , where the area of the circle is (π * R^2 ) and the area of the square is (R^2).
The ratio of the area of the circle to the area of the square is (π * R^2 / R^2) = π , Therefore, we can estimate the mathematical constant π by simulating a large number of random points within the square and counting the fraction of points that fall inside the circle.


####  Vectorize the code ?
A vectorized version of the **approximate_pi_with_monte_carlo** function can be found in the file **approximate_pi_np.py**



#### Comparison of the computational times
To compare the computational times of the original template and the vectorized version of the code, we analyzed the code using the cProfile command. The results show that the vectorized version of the code is significantly faster than the template. While it took approximately **6** seconds to execute the function "approximate_pi_with_monte_carlo" in the template, it only took **0.015** milliseconds to execute the same function in the vectorized version.


##### template
`> python3 -m cProfile approximate_pi.py | grep "NoName"`

   `ncalls  tottime  percall  cumtime  percall`  
   `10000    6.537    0.001   26.586    0.003 approximate_pi.py:22(approximate_pi_with_monte_carlo)`
   
#### vectorized 
`>python3 -m cProfile approximate_pi_np.py | grep "approximate_pi_with_monte_carlo_np"`
  
   `ncalls  tottime  percall  cumtime  percall`  
   `100    0.015    0.000    0.219    0.002 approximate_pi_np.py:10(approximate_pi_with_monte_carlo_np)
`
   






 





