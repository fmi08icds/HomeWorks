- With the following commmand I was able to find out the most time consuming parts in the program:
  <br>

  ```
  python -m cProfile hw3.py --n 300000 | sort -k4,4nr | head -n 50
  ```

- Table:
  <br>

  ```
  ncalls tottime percall cumtime percall filename:lineno(function)
  1335 9.398 0.007 9.410 0.007 .../HomeWorks/bartels/hw3/hw3.py:8(isperfect)
  19 0.001 0.000 9.401 0.495 .../HomeWorks/bartels/hw3/hw3.py:42(getLowUpper)
  ```

      - Runtime for n=300,000 -> 18.5 sec.
      - Runtime for n=1,000,001 ->

- Improvements:

  - First improvement:

    - The for-loop in **isperfect()** can be improved. We dont have to iterate from 1 to n to search for a perfect square root for an n that is not 0 or 1. A square root of n can at most be the half of n (i.e. sqrt(4)=2).
    - Change ... to ...:

    ```
    for i in range(n):
    ```

    ```
    for i in range(int(n/2)):
    ```

  - Runtime for n=300,000 -> 9.4 sec.
  - Runtime for n=1,000,001 -> 58.0 sec.

  - Second Improvement:

    - The runtime in the **isperfect()** method is still high. To avoid this replace the for-loop with a while loop.

      - Change ... to ...:

        ```
        for i in range(int(n/2)):
            if i**2 == n:
                return (True, i)
        return (False, n)
        ```

        ```
        i = 0
        while (i**2 < n):
            i += 1
        if i**2 == n:
            return (True, i)
        else:
            return (False, n)
        ```

    - Runtime for n=300,000 -> 1.2 sec.
    - Runtime for n=1,000,001 -> 1.4 sec.

- ! Time complexity: The time complexity here like in the previous versions is O(n^2). This is because of the combination of while-loop in **getLowUpper()** and the for-loop in **isperfect()**. This improvement only affects an n < 10^8. For a greater n this wont work any more efficiently.

- Third Improvement:

  - The problem is the square calculation of i with every iteration. Previous limitation can be bypassed by estimating with a while loop with a condition of an absolut error of the previous value and the estimator. This has to be implemented in the **mysqrt()** function:

    ```
    e = 1
    while abs(e-(0.5*(e+n/e))):
    	e = 0.5*(e+n/e)
    ```

  - Runtime for n=300,000 -> >0.1 sec.
  - Runtime for n=1,000,001 -> >0.1 sec.

- ! Time complexity: The time complexity here is only O(n). This is because there is only a while-loop in the **mysqrt()** function.
