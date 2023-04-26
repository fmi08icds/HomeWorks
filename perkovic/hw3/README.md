# README

## Description

This repository demonstrates the use of the `cProfile` module in Python to gather detailed information about the performance of a script. Specifically, we will focus on the `cumtime` attribute, which gives us the cumulative time spent in each function and its sub-functions. 

## How to Run

To run the script, execute the following command in your terminal:

```bash
python3 -m cProfile hw1.py --n
```

The script takes an argument `n` which represents the input size for the algorithm. We will use `n` to test the performance of our code.

## Results

We ran the script with different values of `n` and obtained the following results:

### n = 1000

```
Result: 72241 function calls (70326 primitive calls) in 0.177 seconds

(isperfect) cumtime = 0.003
(getLowUpper) cumtime = 0.002
(mysqrt) cumtime = 0.015
```

### n = 100000

```
Result: 72843 function calls (70928 primitive calls) in 3.192 seconds

(isperfect) cumtime = 3.011
(getLowUpper) cumtime = 3.000
(mysqrt) cumtime = 3.012
```

### n = 10000000

```
Overload
```

As we can see from the results, the execution time increases as the value of `n` increases. Additionally, we can observe that the `isperfect` and `getLowUpper` functions have relatively small `cumtime` values compared to `mysqrt`, which has a time complexity of `O(n^2)`.

## Big O Notation

We cross-checked the code with the Big O notation for each function and obtained the following results:

- `isperfect` function has a time complexity of `O(n)`
- `getLowUpper` function has a time complexity of `O(n^2)` due to the nested loop created by the call to `isperfect` function.
- `mysqrt` function has a time complexity of `O(log(n))` since the number of iterations of the while loop is determined by the error threshold. 

## Improvements

Upon analyzing the `isperfect` function, we determined that it has a time complexity of `O(n)`. One possible improvement is to implement a cancel function if `i*i` exceeds `n`. This would reduce the number of iterations and improve the overall performance of the function.
