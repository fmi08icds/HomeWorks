# Codeanalysis template_hw2
* I renamed the function NoName(N) to estimPI(N), since it gives
an estimate of PI back when being called. If the Radius
was not 1, the function could also be named estimSurface(N).
* The code calculates the estimated surface of a circle.
Since the radius here is 1, the surface of the unity circle
should be PI.
* Higher values for N and M achieve more precise values.
* The mean values of the unity circle are being plotted in
a diagram. (mean-values between 3.12 and 3.17 on the x-axis
and the number of same values on the y-axis).
* The numbers being displayed count from 0 to 99 for each
iteration (which is explained beneath).

### uniform(a, b)
* This function gives back a random number between a and b.
In this case the number will be between 0 and 1 (the circle
being centered at 0,0 and the radius R being 1). 

### f(x, R)
* This function takes the x-Value of a point as well as
the radius of the circle and gives back the y-Value
so that the point (x,y) lies on the circle with radius R.

### estimPI(N)
* The arrays list_x and list_y store the N values of
the randomly generated points.
* list_accepted_x stores all the values of list_x that are
lying within the circle.
* The value fin is the proportion of all points lying within
the circle and all the points that have x,y values between
0 and 1. -> Which is the estimated surface of a forth of 
the circle.
* The function returns an estimation of the surface of the
circle (4*fin).

### main()
* estimPI() is being called M times per iteration. The results
are being stored in list_rst.
* list_mu receives the average value of list_rst for each
iteration.
* list_sigma receives the standard deviation but is not being
used any further.
* i is being printed out after each iteration to imitate
the loading scale (depending on the value of M)

# Vectorized Version + time comparison
* Instead of using for-loops in the function estimPI(N),
I am using Numpy Arrays. This way the function can be
executed faster, since Operations on an Array can be executed
at the same time.
* Using the command 'time python main.py', the execution time
  (real) for the vectorized version is 0m5.622s
* The execution time for the non-vectorized version is
1m41.908s
* The difference in performance is immense.