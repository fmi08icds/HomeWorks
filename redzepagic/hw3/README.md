# Runtime 
I looked at percall (cumtime divided by calls) time of all the functions and total time of the program for different parameters n:
- n = 1000000000000:
    - total: 0.406 s
    - isperfect: 0.001 s
    - getLowUpper: 0.000 s 
    - mysqrt: 0.015 s
- n = 10:
    - total: 0.141 s
    - isperfect: 0.000 s
    - getLowUpper: 0.000 s 
    - mysqrt: 0.001 s 
- n = 1000:
    - total: 0.234 s
    - isperfect: 0.000 s
    - getLowUpper: 0.002 s 
    - mysqrt: 0.001 s 
- n = 100000:
    - total: 9.156 s
    - isperfect: 0.010 s
    - getLowUpper: 0.495 s 
    - mysqrt: 0.425 s 


# Time Complexity
- For the Big O notation I looked at function after function:
    - isperfect(n) -> O(n):
        - There is a for-loop in the range between 0 and n/2, so actually O(n/2) but usually linear time is notated as O(n))
    - getLowUpper(n) -> O(n^2): 
        - There are two while-loops which run worst case in O(n)
        - But in those functions call isperfect(n) so the runtime is worst case in O(2 \* n^2)
        - Since the constant factor can be neglected -> O(n^2)
    - mysqrt(n, error_threshold) -> O(n^2):
        - The most expensive funciton called here is getLowUpper(n) with complexity O(n^2)
        - The while-loop can be neglected since it runs faster than O(n^2)

# Improvements 1
- isperfect(n) -> O(sqrt(n)): I could reduce the runtime to O(sqrt(n)), with leaving the loop as soon as i^2 gets greater than n
- getLowUpper(n) -> O(n\*sqrt(n)): Through improving isperfect(n) the runtime of this function also reduces to O(n\*sqrt(n))
- mysqrt(n, error_threshold) -> O(n\*sqrt(n)): Since O(n\*sqrt(n)) is slower than O(n\*log(n)) the complexity of this function is still depending on getLowUpper(n)
- The best total runtime with n = 1000 was 0.109 s, which is faster than the original function with the same n
- With n = 100000 the best runtime was 0.141 s

# Improvements 2
- I also tried vectorizing isperfect(n) with numpy arrays in hw3_vectorization.py, the best total runtime with n = 1000 was 0.078 s
For n = 100000 it was 0.109 s

# Conclusion
- The runtimes varied strongly, still the code with numpy is running sometimes just a little bit faster (probably my numpy solution is to naive), often it is even slower than the solution without numpy