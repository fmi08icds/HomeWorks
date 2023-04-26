from numpy import random, sqrt, round
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
import cProfile, pstats, io

# estimate sqrt wit subtraction method
def sqrt_sub_method(n):
    sub_n = n
    i = 1
    for s in range(1, n, 2):
        if sub_n - s <= 0:
            break
        sub_n = sub_n - s
        i+=1
    return i

# estimate the square root with the given precision
def opt_sqrt(n, init_step_size = 0.5, precision = 0.000000001, max_iter = 10000000):
    # check input variables
    if not isinstance(n, int):
        raise ValueError("input to sqrt is not integer")
    if n < 0:
        raise ValueError("can not calc sqrt of negative number")
    
    # get initial estimate of sqrt with subtraction method
    # this estimate will either be exactly the square root or higher
    est = sqrt_sub_method(n)
    # if n is perfect square it is already found
    if n == est*est:
        return est
    
    step = init_step_size

    # estimate the sqrt until either the given precision is reached or 
    # max amount of iterations has passed
    for i in range(0, max_iter):
        diff = est * est - n
        if (diff > precision * -1) and (diff < precision):
            return est
        if diff < 0:
            est = est + step 
        else:
            est = est - step
        step = step / 2

    raise Exception("max iteration hit before getting result of set precision")

def main() :
    doc_ =  """
                Welcome to the first Python assignment!!!\n
                You will write your first Python script that computes the square root of a given integer n.
                The template_hw1 provides you with the basic structure of a Python script. 
                Feel free to use print for debugging but remember to clean them up before your submission.
                NB: Your performance will not only be evaluated on your capacity to output good results.
                Please make sure you understand each line you code.
            """
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS, description=doc_)
    parser.add_argument('--n', type=int, help="An integer input for which we compute the sqrt root.")
    args = parser.parse_args()
    input_n = args.n

    pr = cProfile.Profile()
    pr.enable()
    myvalue = sqrt(input_n)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    # write output to file
    ps.print_stats()
    with open('out.txt', 'w+') as f:
        f.write(s.getvalue())

if __name__ == '__main__':
    main()