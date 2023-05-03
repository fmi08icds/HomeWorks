
## System details

```
CPU: 6-core AMD Ryzen 5 5625U with Radeon Graphics (-MT MCP-)
speed/min/max: 3060/1600/4387 MHz
```

## Timings with magic ipython `% timeit`
- template

    `15.9 s ± 93.7 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)`

- with vectorization

    `297 ms ± 6.92 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)`

- with vectorization and `@jit` compile annotations:

    `121 ms ± 440 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)`