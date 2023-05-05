# Approach

### 1. Analyze the code
- main(): 
  - initializes some variables and runs the NoName() function M times and storing the results in two lists
    - NoName(): 
      - calls uniform() N times
        - uniform(): 
          - returns a pair of random numbers between 0 and 1
      - checks if each point has a smaller y-coordinate than the result of f()
        - f():
          - returns y-coordinate of a point on a circle of radius R given its x-coordinate by using the formula of a circle, solving for y
      - points that fall inside the circle (smaller y-coordinate) are stored in a list
      - returns an estimate of pi based on the ratio of the number of points inside the circle to the total number of points, multiplied by 4 (since the stimulation only considers a quarter of the circle)
  - list_mu stores the mean estimate of pi and list_sigma the standard deviation of the estimates
  - plots a histogram of the mean estimates using matplotlib

#### 2. Naming the function:
- code performs a Monte Carlo simulation to estimate the value of pi: concept of "throwing darts" at a circle inscribed in a square
- if a random points lands within the circle, it is considered a hit
- by counting the number of hits and misses, it is possible to estimate the area of the circle and the square and from that the value of pi 
- new name: estimate_pi()

### 3. Optimizing the code
- previous run-time: 9.5s
- the code can be optimized by vectorizing it using numpy
- use numpys random.uniform() function instead of the uniform() function
- use numpy arrays to store x and y values in the estimated_pi() function
- the loop that checks if each point is inside the circle is replaced by a numpy operation that checks all points at once
- new run-time: 0.25s