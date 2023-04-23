import time
import hw2
import hw3

N = 10_000_000

if __name__ == "__main__":
    time.sleep(1)
    tic = time.time()
    r = hw2.sqrt(N)
    toc = time.time()
    hw2_ms = 1000*(toc-tic)

    print("### HW2 ###")
    print(f"square root of {N}: {r}")
    print(f"time needed: {hw2_ms:1.2} ms")

    tic = time.time()
    r = hw3.sqrt(N)
    toc = time.time()
    hw3_ms = 1000*(toc-tic)

    print("### HW3 ###")
    print(f"square root of {N}: {r}")
    print(f"time needed: {hw3_ms:1.2} ms")
