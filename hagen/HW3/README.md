<h1>Homework 3 - Improving square root code</h1>
<h4>--Paula Hagen--</h4>  
   
   
<h2>STEPS</h2>
In the src folder you can find last week's homework (sqrt_slow.py) and my suggestion for a faster programme (sqrt_fast.py).  
This is how I proceeded:

1. Run code in terminal with profile (https://docs.python.org/3.8/library/profile.html):  
`python -m profile -s tottime sqrt_slow.py --n 100000`  
(Orders functions by total time used by all calls of that function)
2. Identify the function taking up most total time (isPerfect())
3. Have a look at the code for complexities of functions
4. Rewrite isPerfect() and profile programme again with same input number


<h2>Code complexity of original version</h2>

(Also see comments in the code)  
- isPerfect() is of O(n) because of the for-loop of size n
- getLowUpper() is of O(n^2), because we have
   - O(n) for calling isPerfect()
   - then O(n) for calling isPerfect() again
   - then O(n*log(n)) for the while-loop, because it calls isPerfect() log(n) times
   - then again O(n*log(n)) for the other while-loop

- mysqrt() is of O(n*log(n)) because we have
   - O(n) for calling isPerfect()
   - then again O(n) for calling isPerfect()
   - then O(n*log(n)) for calling getLowUpper()
   - then O(log(n)) for doing the binary search

=> Rewriting isPerfect() should lead to the biggest improvement as it it is largest part of the complexity and is being called many times. Idea: replacing for-loop with numpy array.
   
  
<h2>Improvements</h2>
   
Profiling again with n=100.000, we get a total time of 0.067 for isPerfect() (Before it was 9.175!!)
I also used  
`time python sqrt_fast.py --n 100000`  
for both versions to check the overall time difference. The overall time improvement was 8.876/0.197, so the fast version is about 45 times faster. For a smaller n, the difference would be smaller, though.
