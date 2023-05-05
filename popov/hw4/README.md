# Part 1 - Analysis of script 

## `uniform():`
Returns a random value, weighted by the standard (continuous) uniform distribution, from the interval $(a,b)$.

## `f(x,r):` 
$f(x,R) = \sqrt{|x^2 - R^2|}$ defines the equation of the semicircle of radius $R$ for $x \leq R$, centered at the origin $(0,0)$.  

It is clear from the definition of the function $f(x,R)$ that we will be dealing with some kind of calculation related to the unit circle (Since `NoName()` sets $R = 1.0$)

## `NoName(N) -> estimatePi(N)`

After running the script and analysing the function values which lie in very close proximity to the value $\pi$, we rename the function to `estimatePi()`. This script is a monte carlo method for the estimation of the true value of $\pi$. We follow with the logic behind this statement.

## `Code breakdown`

0. A parameter $N$ is passed for the amount of iterations for the function. 

1. Instead of dealing with an entire circle for the approximation/estimation of $\pi$, we can use the positive $x$-$y$-quadrant and for the estimation of the arc length of the quarter circle and multiply by 4 in the final step. Below, we initialize the accepted number of points `Ninf = 0` and the radius $R = 1.0$ for the unit circle. Additionally, we initialize two lists for $x$ input and $y$ value pairings.
~~~
Ninf = 0
R = 1.0

list_x = []
list_y = []
~~~


2. We fill these lists with random values within the range $(0,1)$ using the `uniform()` function provided above and a simple for loop. Additionally we create a list for $x$ values that we will fill for x values which pass our decision procedure. 
~~~
for i in range(N) :
            list_x.append(uniform(0,R))
            list_y.append(uniform(0,R))

list_accepted_x = []
~~~


3. Below is the most important part of the function. We begin by looping through the $(x,y)$ pairing lists and use the function $f(x,R)$ as a decision function. In this decision, a randomly generated $y_i$ is compared with an evaluation $f(x_i,1)$ of the semicircle function (which lies on the boundary = circumference) for a randomly generated $x_i$, for every $i \in (0,N)$. This means, the condition is fulfilled if the point $(x_i, y_i)$ is below the point $\left(x_i, f(x_i,1) \right)$, and thus lies within the quarter circle. If this is the case, we accept $x_i$.
~~~
for i in range(N) :
    if (list_y[i]< f(list_x[i],R)) :
        list_accepted_x.append(list_x[i])
~~~

4. Finally we consider the fact that for $N \to \infty$, the points fill the entire square of side length $R = 1$. The points represent the area, all points within the circle correspond to the area $A_{circle}= \frac{1}{4}\pi R^2$ and the entire area of the square is given by $A_{square} = R^2$. The ratio yields $\frac{A_{square}}{A_{circle}} = \frac{1}{4}\pi$. Thus we calculate the ratio by the amount of accepted point $x_i$ divided by the amount of total points $N$ and multiply by $4$ to retrieve an estimation for $\pi$. 
~~~
Ninf = len(list_accepted_x)
fin = Ninf/float(N)


return 4*fin
~~~

5. Finally, the main function creates a list, gathers M = 1000 observations of `estimatePi()`, calculates mean, standard deviation and plots a histogram with the data. 

# Part 2 - Vectorization

See code and comments in hw4.py 

Used numpy boolean array to count the amount of points that lie within the circle. All calculations can be done through array operations instead of using a for loop. 
