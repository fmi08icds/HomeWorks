# The objective of the fourth homework:  
The objective is to analyse the code in the template_hw2.py file and achieve the following points: 
* What does the code do? 
* Analyse the code into more details ?
* Vectorize the code ?
* Comparison of the computational times


# Answers: 

####  What does the code do ? 
The code employs the **Monte carlo** simulation method to estimates the mathematical constant PI, therefore we can rename the **"NoName"** function to the name **"approximate_pi_with_monte_carlo"**. 
The function works by imagining a circle inscribed in a square of length (R) with the center of the circle in the center of the square , where the area of the circle is (π * R^2 ) and the area of the square is (R^2).
The ratio of the area of the circle to the area of the square is (π * R^2 / R^2) = π , Therefore, we can estimate the mathematical constant π by simulating a large number of random points within the square and counting the fraction of points that fall inside the circle.



####  Analyse the code into more details ?

###### 1) Monte carlo function: 

* The monte Carlo function starts by initializing two varibales , namely **"Ninf“ and "R“**, where **"R“**    
  represnts the radius of the circel and **"Ninf“** is the count of all points that fall within the circle.
  
* Additionally , two lists , **"list_x"** and **"list_y"** are created to store the x and y coordiantes of the 
  randomly generated points. 
  
* The function then loops **N** times to produce **N** random points that are **uniformly distributed** between  
  zero and one. To determine which points fall within the circel, the function checks if the following condition is
  true:  **x^2 +   y^2 ≤ R^2, x ≥ 0 and y ≥ 0** and this condition can be simplified to **y ≤ f(x,R), where 
  f(x,R) = sqrt(abs(x^2 - R^2))** represents the upper semicircle of a circle with radius R centered at (0,0)
  
* If a point **satisfies** the condition, then its x-coordiante is added to the **list of accepted x’s**

* Finally , the function calculates the fraction of points that fall within the quarter-circel by dividing **“Ninf“ 
  by “N“** and multiplying by 4, where **“Ninf“** is the count of all points that fall within the circle and 
  **“N“** represents the total number of generated points and then the final values will be returned. 
  
###### 1) main function: 
* The main function starts by defining two variables , 'M' and 'N' , 'M' is the number of times the Monte Carlo 
  simulation will be run and N is the number of random points that will be generated in each simulation. 
* in each iteration , the monte_carlo_function will be called M times and the results are stored in the **"list_rst"** list and then the mean and standard deviation of the estimates are calculated using the functions  mean() and std() and added to the **'list_mu' and 'list_sigma'** lists
* After all M simulations have been run, the function plots a histogram of the means using Matplotlib's hist() function. The histogram is created with 100 bins, evenly spaced between 3.12 and 3.17. Finally, the histogram is displayed using Matplotlib's show() function.
* in essence , the monte_carlo_function will be called 100 * 100 = 10000 times and the average of of each 100 values is calculated along with the standard deviation and then the results are plotted 


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
   






 





