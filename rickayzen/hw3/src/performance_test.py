import argparse
import cProfile
import signal
import time
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
from hw3_improved import mysqrt as sqrt_new
from numpy import sqrt
from hw2 import mysqrt as sqrt_old
profile = cProfile.Profile()


def log(text):
    print(f"{time.ctime()} - {text}")


def timeout(signum, frame):
    lambda: print("Yeah, I'm gonna stop now")
    raise TimeoutError()


def compare(n: int, threshold=None, execute_old=True, execute_new=True, timeout_time=10) -> (bool, bool):
    """
    Executes the square root function of the old and of the improved version. It returns a tuple consisting of the success of the old function and the success of the new function.
    It is successful if no timeout occurs.  default timeout is ten seconds.
    It prints out the number of runtime as well as the number of iterations for each function call.
    The benchmark is  the numpy.sqrt() function.
    :param threshold: the error threshold. So the accuracy of the result.
    :param n: the value test the functions on
    :param execute_old: by default false
    :param execute_new: by default false
    :param timeout_time: Time, after which function should fail
    :return (success_old, success_new): a tuple with the success booleans
    """
    log(f"Timeout: {timeout_time}")
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(timeout_time)

    success_old = execute_old
    success_new = execute_new
    if execute_new == execute_old:
        track_performance = True
    else:
        track_performance = False
    log(f"n: {n}")
    start = time.time()
    try:
        sqrt(n)
        log(f"Execution time - Numpy benchmark: {time.time() - start}s")
    except TimeoutError:
        success_old = False
        log(f"Benchmark failed for n = {n}")
    try:
        start = time.time()
        if execute_old:
            if track_performance:
                profile.enable()
            if threshold is None:
                complexity = sqrt_old(n)[1]
            else:
                complexity = sqrt_old(n, error_threshold=threshold)[1]
            if track_performance:
                profile.disable()
                profile.dump_stats("perf.stats")
            log(f"Execution time - old: {time.time() - start}s. Operations: {complexity}")
    except TimeoutError:
        success_old = False
        log(f"Old failed for n = {n}")
    start = time.time()
    signal.alarm(timeout_time)
    try:
        if execute_new:
            if track_performance:
                profile.enable()

            if threshold is None:
                complexity = sqrt_new(n)[1]
            else:
                complexity = sqrt_new(n, error_threshold=threshold)[1]
            if track_performance:
                profile.disable()
                profile.dump_stats("perf.stats")
            log(f"Execution time - new: {time.time()- start}s. Operations: {complexity}")
    except TimeoutError:
        success_new = False
        log(f"New failed for n = {n}")
    return success_old, success_new


def execute_test(timeout_time=None, threshold = None):
    """
    Tests the performance of the square root functions of the old and the improved version.
    The results will be printed in the output and the number of function calls will be tracked by the profiler which writes the results in the file "perf.stats".
    The results consist of the runtime and the number of operations.
    :param timeout_time: Optional parameter that sets the time after which a timeout should occur
    :return:
    """
    test_cases = [101, 501, 1001, 5001, 10001, 50001, 100001, 500001, 1000001, 5000001, 10000001, 50000001, 100000001, 500000001]
    success_old = success_new = True
    old_failed_at = new_failed_at = None
    print("Execute test. Timeout time: ", timeout_time)
    for n in test_cases:
        if timeout_time is None:
            success_old, success_new = compare(n,threshold=threshold, execute_old=success_old, execute_new=success_new)
        else:
            success_old, success_new = compare(n, threshold=threshold, execute_old=success_old, execute_new=success_new, timeout_time=timeout_time)
        if new_failed_at is None and not success_new:
            new_failed_at = n
        if old_failed_at is None and not success_old:
            old_failed_at = n
        if not success_new and not success_old:
            break
    print(f"Old failed at n = {old_failed_at} and new failed at n = {new_failed_at}")


def show_stats():
    """
        Shows the stats of the profiler. To note: The profiler tracks only the functions for values that get tested by both classes.
    """
    import pstats
    stats = pstats.Stats("perf.stats")
    print("\n\n")
    print("OVERVIEW OVER THE OLD VERSION\n\n")
    stats.print_callees("hw2.py")
    print("OVERVIEW OVER THE NEW VERSION\n\n")
    stats.print_callees("hw3_improved.py")


def main():
    """
        This script can execute the performance test and read out the data. By default, both get executed.
        '--p' lets you skip the performance test.
        '--s' lets you skip the presentation of the stats.
        '--t int' sets timeout time for each function.
        '--err float' sets the error threshold.
    """
    doc_ = """
        This script can execute the performance test and read out the data. By default, both get executed.
        '--p' lets you skip the performance test.
        '--s' lets you skip the presentation of the stats.
        '--t int' sets timeout time for each function.
        '--err float' sets the error threshold.
    """
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS, description=doc_)
    parser.add_argument('--p', type=bool, action=argparse.BooleanOptionalAction, default=False, help="If added, the performance test will be skipped.")
    parser.add_argument('--s', type=bool, action=argparse.BooleanOptionalAction, default=False, help="If added, the stats of the profiler will not be shown")
    parser.add_argument('--t', type=int, help="An integer input to set the timeout after which a function will fail.")
    parser.add_argument('--err', type=float, help="A float input to set the error threshold - so the level of accuracy.")
    args = parser.parse_args()
    t = None
    err = None
    if hasattr(args, "t"):
        t = args.t
    if hasattr(args, "err"):
        err = args.err
    if not args.p:
        execute_test(t, err)
    if not args.s:
        show_stats()


if __name__ == '__main__':
    main()
