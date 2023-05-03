## HW 3 

### helpers that take time:
- use profile to loak at the time the template needs
- isperfect()
    - has the most calls
    - with big n the most tottime

- getLowUpper() and mysqrt() have around 20 calls each

#### examples

- isperfect()
    - n = 1001
        - 321 calls
        - 0.00 tottime and cumtime
    - n = 30000
        - 597 calls
        - 0.656 tottime and cumtime
        - 0.001 time per call

- getLowerUpper()
    - n = 1001
        - 19 calls
        - 0.00 tottime and cumtime
    - n = 30000
        - 18 calls
        - 0.00 tottime
        - 0.656 cumtime
        - 0.036 time per call

- mysqrt()
    - n = 1001
        - 21 calls
        - 0.016 tottime and cumtime
        - 0.001 time per call
    - n = 30000
        - 21 calls
        - 0.00 tottime
        - 0.656 cumtime
        - 0.031 time per call


### approximation of time complexity for template:
- isperfect() 
    - for-loop from 2 to n-1 -> time complexity of O(n)
- getLowUpper() 
    - two while-loops
    - loop 1 goes from n down and calls isperfect() each time until a perfect square is found
    - loop 2 goes from n up and calls isperfect() each time until a perfect square is found
    - worst case: each loop calls isperfect() multiple times (upper bound by n)-> 2n * isperfect()
    - O(n^2)
- mysqrt()
    - first two lines with constant time -> O(1)
    - calls isperfect() once -> O(n)
    - calls getLowUpper() once -> O(n^2)
    - while loop, which devides rst in half (binary search) -> O(log(n))
    - overall complexity O(n^2), because overall time complexity is dominated by the time complexity of getLowUpper()
- time complexity of the template is O(n^2) because the overall time complexity is dominated by the time complexity of getLowUpper()

### Time Comparison for n = 30000
- template took around 1.60 seconds
- 0.40 seconds with improvement of isperfect()
- 0.34 seconds with improvement of isperfect() and getLowUpper()
- 0.28 seconds with improvement of isperfect(), getLowUpper() and mysqrt()
- around 1.3 seconds saved -> savings around 80 %

### Time Complexity of the new Code (square_root_hw3.py)
- isperfect() 
    - array from 2 to n//2, any funktion iterates through array to look if the condition is met -> worst (n//2)-2 times
    - upper bound time complexity still is O(n)
- getLowUpper() 
    - only one while-loop
    - loop 1 goes from n down and calls isperfect() each time until a perfect square is found
    - worst case: the loop calls isperfect() multiple times (upper bound by n)-> n * isperfect()
    - O(n^2)
- mysqrt()
    - same time complexity O(n^2) but abs() isn't computed anymore -> saves time
- the overall complexity doesn't change, but it computes fasters
