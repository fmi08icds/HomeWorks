# HW3

## Before vectorization
### Complexity analysis

- Each step of the functions is assessed as comments within the file `src/sqrt_complexity_analysis.py`
- Final estimated worst time complexities of functions wrt. to their inputs
    - `has_perfect_sqrt`: O(n)
    - `get_low_and_upper_perfect_sqrt`: O(n^2)
    - `approximate_sqrt`: O(n^2)

### Profiling
- Create profile: `python -m cProfile -o out/sqrt_n_12344.prof src/sqrt_complexity_analysis.py -n 12344c`
- Visualize profile with snakeviz: `snakeviz out/sqrt_n_12344.prof `

## After vectorization
- Vectorized function: `has_perfect_sqrt`
- Results in a x3 speedup of the empirical runtime

### Complexity analysis
- Still the same time complexities
- Unrolling loops to vectorized code is a hardware speedup in terms of better
parallelization capabilities

### Profiling after vectorization
- Create profile: `python -m cProfile -o out/sqrt_vectorized_n_12344.prof src/sqrt_vectorized.py -n 12344c`
- Visualize profile with snakeviz: `snakeviz out/sqrt_vectorized_n_12344.prof `
