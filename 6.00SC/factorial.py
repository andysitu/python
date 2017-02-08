def factI(n):
    ## Iterative implementation of factorial
    """Assumes that n is an int > 0
       Returns n!"""
    result = 1
    while n > 1:
        result *= n
        n-= 1
    return result

def factR(n):
    """ Assumes that n is an int > 0
        Returns n!"""
    if n == 1:
        return 1
    else:
        return factR(n-1) * n
