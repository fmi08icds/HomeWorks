# HW3: Time complexity and vectorization
## Time complexity of each function
### `isperfect(n)`: 
  - The worst performance results form iterating through all the numbers from 1 to n-1. 
  - The operation `(i**2)` in each loop takes constant time. 
  - Hence, the time complexity is `O(n)`. 

### `getLowUpper(n)`:
  - The driving factor for time complexity are the two `while` loops (as they call `isperfect`)
  - As outlined in [testing_hw3.ipynb](./testing_hw3.ipynb) under Adaption 1, the distance from a perfect square `z` to the next larger perfect square is equal to `2*sqrt(z) + 1`.
  - For any integer `n = z + a`, for `0 < a < 2*sqrt(z) + 1`, the first loop will run `a-1`-times (due to the first check) 
  - The second loop will run `2*sqrt(z) + 1 - (a + 1)` -times (again, due to calculating `upper` once and checking it before the loop)
  - In total, we get `2*sqrt(z) + 1 - (a + 1) + (a - 1) = 2*sqrt(z) - 1`
  - As `n > z`, number of total loops will always be bounded by `O(sqrt(n))`
  - Finally, as each loop calls `isperfect`, the total time complexity is `O(sqrt(n)*n)`

### `mysqrt(n)`:
  - There is one call of `isperfect` at the beginning -> `O(n)`
  - As the function also calls `getLowUpper`, the first `isperfect` does not matter -> `O(sqrt(n)*n)`
  - The while loop at the end is not only dependent on `n` but also the `error_threshold`. 
    As an approximation, we can treat it as binary search, which has logarithmic complexity -> `O(log(n))`.
    In any case, its time complexity is below `O(sqrt(n)*n)`
  - Hence, the time complexity of `mysqrt` is also `O(sqrt(n)*n)` due to the call of `getLowUpper`

## Time comparison
A detailed evaluation can be found in [evaluation_hw3.ipynb](./evaluation_hw3.ipynb). 
Below are the results for [schmidt_hw3.py](./schmidt_hw3.py) vs. [schmidt_hw2.py](./versions/schmidt_hw2.py)

```
time python schmidt_hw3.py --n=1234567
real	0m7.991s
user	0m3.398s
sys	0m4.571s
```
This implementation is a lot faster than the previous one:
```
time python ./versions/schmidt_hw2.py --n=1234567
real	7m52.303s
user	7m52.059s
sys	0m0.029s
```


## Files and folders
- [schmidt_hw3.py](./schmidt_hw3.py) is the final submission and the best performing version in the [evaluation](./evaluation_hw3.ipynb)
- [versions](./versions) contains different implementations of the functions from HW2
  - [v1](./versions/schmidt_hw2.py): As submitted for hw2
  - [v2](./versions/schmidt_hw2_v2.py): Vectorized getLowUpper
  - [v3](./versions/schmidt_hw2_v3.py): Vectorized isperfect
  - [v4](./versions/schmidt_hw2_v4.py): Vectorized isperfect and only one call of np.sqrt in mysqrt()

- [testing_hw3.ipynb](./testing_hw3.ipynb) contains the experiments that led to the different versions
- [evaluation_hw3.ipynb](./evaluation_hw3.ipynb) compares the different versions in terms runtime