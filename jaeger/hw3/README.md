# Approach

### 1. Add a function that measures the time
   - for each function call
   - for the sum of each function call
   - for total time complexity

#### Findings:
- isperfect() is called multiple times
- each function calls each other -> sum of each function call doesn't give desired findings as the time is 
similar to the time of the main function 

### 2. Examine different value ranges of n such as 10, 100, 1000 ...

#### Findings:
- time span for n = (approx.)
  - 10: 0.015s
  - 100: 0.015s
  - 1000: 0.025s
  - 10000: 0.015s
  - 100000: 1.75s
  - 1000000: 0.15s
  - 10000000: >15 min (not defined)
  - 100000000: 0.15s 

### 3. Analyze loops and control flows
   1. main() calls mysqrt()
      1. mysqrt() calls getLowUpper()
         1. getLowUpper() calls isperfect()
         2. getLowUpper() calls isperfect()
         3. getLowUpper(): while-loop calls isperfect()
         4. getLowUpper(): while-loop calls isperfect()
            1. isperfect() has for loop based on inputrange

#### Findings: 
- isperfect() is the crucial function as it is called multiple times and even called within a while-loop with range is
partly derived from the input n
- isperfect() also has a for loop with a range determind by the input n
- Conclusion: getLowUpper() and isperfect() have the most impact on the time complexity as they are looping through n (O(n)) while the mysqrt-function itself (except for the calls of the other functions ) has a constant complexity

### 4. Modifications to optimize time complexity
- isperfect() uses a for loop to iterate from 0 to n which has a time complexity of O(n) -> use binary search to find the perfect square root, which has a time complexity of O(log n).
- getLowUpper() also uses linear search to find the upper and lower square roots (O(n)) -> use binary search instead (O(log n))
- mysqrt(): 
  - avoid computing the isperfect() function for all odd integers when n is even; or for all even integers when n is odd 
    -> square root of an odd integer is always odd, and the square root of an even integer is always even
    -> reduce the number of iterations required in the isperfect() function.
  - modify computation of rst inside while loop to use integer division (//) instead of floating point division (/) -> faster

### 5. Measure time again

#### Findings:
- time for n = (approx.)
  - 10: 0.005s
  - 100: 0.005s
  - 1000: 0.005s
  - 10000: 0.005s
  - 100000: 0.005s
  - 1000000: 0.005s
  - 10000000: >15 min (not defined)
  - 100000000: 0.005s 