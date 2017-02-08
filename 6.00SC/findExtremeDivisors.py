def findExtremeDivisors(n1, n2):
    """ Assumes that n1 and n2 are positive ints
        Returns a tuple containing the smallest common
        divisors > 1 and largest common divisors"""
    divisors = ()
    minVal, maxVal = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            if minVal == None or i < minVal:
                minVal = i
            if maxVal == None or i > maxVal:
                maxVal = i
    return (minVal, maxVal)

print findExtremeDivisors(100, 200)
