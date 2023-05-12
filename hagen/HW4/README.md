<h1>Homework 4</h1>
<h4>--Paula Hagen--</h4>  
   
   
<h2>Function Description</h2>
I named this function circleArea because it calculates the area for a circle with radius R (fixed R=1.0 but could be changed) without using the common formula A=π·r^2.
Instead, it generates random points in a coordinate system and calculates the proportion of them, that fall under the function f(),
so within the quarter circle with radius R. This *4 results in the area of the whole circle. Here, R is 1.0, so the area is π.
In main(), by calling circleArea() many times the mean of all the result will be an approximation of the true circle area.  
Also see comments in the code.


<h2>Optimization</h2>

I vectorized the two for-loops in the NoName=circleArea function. For the first one, I just used the built-in random.rand(N) generator and not the uniform function. This is not ideal, as it doesn't work for another radius than 1. I left it in, though, because otherwise the code is so much slower.   
The second loop I replaced with a vectorized np.array with conditional.
   
  
<h2>Improvements</h2>
   
I used  
`time python slow_version.py`  
`time python fast_version.py`  
to check the overall time difference. The overall time improvement was 8.702s/0.496s, so the fast version is about 17.5 times faster. (For this calculation, I commented out the plt.show())