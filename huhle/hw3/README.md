## 1. Time consumed by each of the three functions used to calculate the squareroot of n
Typing "Python -m profile -s cumtime main.py --n 1000000" in cmd. 
Cumtime for n = 1000000 in seconds:
* Function isperfect(n): 0.000
* Function getLowUpper(n): 0.000
* Function mysqrt(n): 0.016
* Total time: 0.703

for n = 1000000000000
* Function isperfect(n): 0.344
* Function getLowUpper(n): 0.000
* Function mysqrt(n): 0.344
* Total time: 1.016

for n = 1000000000000000000
* Function isperfect(n): 225.234
* Function getLowUpper(n): 0.000
* Function mysqrt(n): 225.234
* Total time: 225.953

for n = 1234567
* Function isperfect(n): 0.250
* Function getLowUpper(n): 0.266
* Function mysqrt(n): 0.266
* Total time: 0.672

### Results:
If n gets bigger, it also takes more time for the program
to execute. If n has a perfect square root, the function
"isperfect(n)" obviously has a similar execution time
as the function "mysqrt(n)", while the exection time of the
function "getLowUpper(n)" is 0.000. If n has no perfect square
root, getLowUpper also takes a longer execution time.

## 2. Time complexity
* Function isperfect(n):
The time complexity for the function isperfect(n) is O(n),
since there is just one for-loop that repeats n times. Within
this loop there is the time complexity O(1), since there is
simply just an if-clause and no other loop.

* Function getLowUpper(n):
The time complexity for the function getLowUpper(n) is O(n**2), 
since the while-loop calls another loop by calling a for-loop
in the function "isperfect(n)". In the worst case, both
loops iterate n times each.

* Function mysqrt(n): The time complexity of the while-loop
is O(log(n)), as long as the termination condition (threshold)
can be neglected. Since "mysqrt(n)" calls the function
"getLowUpper(n)" which has a bigger time complexity, it also
has the time complexity O(n**2).

## 3. Changing the functions to reach a better time complexity
* Function isperfect(n): We do not need to iterate i from 0
to n-1 to check, if i*i equals n. When i gets bigger than the
square root of n, the square of i will not equal n by increasing
i anyway. Therefore, we can stop the function after max. 
sqrt(n) iterations, which is implemented in the code. -> The time
complexity of this function is now O(sqrt(n)).

* Function getLowUpper(n): Since this function calls 
"isperfect(n)" within its while-loop, the time complexity
is now O(n*sqrt(n)).

* Function mysqrt(n): In this functions we had to complete
three code snippets. The first to have a time complexity
of O(1) each, since there are no loops being used. (Except
once we call the function "isperfect" -> O(sqrt(n))). Later on
we call the function "getLowUpper(n)" -> O(n*sqrt(n)) which
is the highest temporal complexity and also the temporal
complexity of this function.