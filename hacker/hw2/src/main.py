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
def sqrt(n, init_step_size = 0.5, precision = 0.1, max_iter = 10):
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

# bubble sort (for second part of hw2)
def sort_list_asc(l):
    if not isinstance(l, list):
        raise ValueError("input to reverse_list is not a list")
        

    if not all(type(item) is int for item in l):
        raise ValueError("input to reverse_list contains non int")

    if len(l) == 1:
        return l

    for i in range(0,len(l)):
        for ii in range(0,len(l) - 1):
            if l[ii] < l[ii+1]:
                t = l[ii+1]
                l[ii+1] = l[ii]
                l[ii] = t
    return l