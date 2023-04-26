import time
import hw2
import hw3
from typing import Callable, List
import polars as pl

N = 10_712_686_868_678_989_898
M = 10

def print_speed(fn: Callable[[int], float], m: int, n: int, label: str):
    """ Executes a function m times with parameter n and prints the time needed """
    
    print(f"### Running {label} {m} times with parameter {n} ###")
    results: List[float] = []
    durations: List[float] = []
    for _ in range(m):
        start_time = time.perf_counter()
        r = fn(n)
        end_time = time.perf_counter()
        ms = 1000*(end_time - start_time)

        results.append(r)
        durations.append(ms)

    runs = pl.DataFrame({"result": results, "elapsed time (ms)": durations})
    average_time = runs.select("elapsed time (ms)").mean().item(0,0)

    print(f"Average time needed: {average_time:.3} ms")
    print("Runs: ", runs)

if __name__ == "__main__":
    print_speed(hw2.sqrt, M, N, "HW2")
    print_speed(hw3.sqrt, M, N, "HW3")

    
