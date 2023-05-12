# Overview
- This program is aimed to approximate the area of a circle with a given R
- The value which has been the most freqeunt is the best approximation (can be seen in a plot)

# uniform(a, b)
- Returns a random number (uniform distribution) between a and b

# f(x, R)
- Calculates and returns a y-coordinate to the given x-coordinate, sucht that (x, y) is on the circle with radius R and center (0, 0)

# approximate_circle_area(N)
This function approximates the integral of a quarter circle with radius R = 1.0 and returns it four times to approximate the area of a whole circle
- Generates N (x, y) pairs such that x and y are random nubers between 0 and R = 1.0
- Counts the (x, y) pairs which are inside of a quarter circle with radius R = 1.0
- It calculates the ratio between the (x, y) pairs inside and outside the quarter circle
- It returns 4 times the ratio

# main
- Calctulates M times the mean of M approximations of the area of a circle with radius R
- Shows the means in a plot
- In the case R = 1.0 the value which has been calculated the most often is Pi, which shows that the approximation works



# Runtime
- The normal version "template_hw2.py" has a complete runtime of: 60.895s
- The vectorized version "hw2_vectorization.py" has a complete runtime of: 4.276s
- As can be seen the vectorized version runs a lot faster than the original one