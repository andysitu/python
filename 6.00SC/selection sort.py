def selSort(L):
    """ Assumes that L is a list of elements that can
            compared using >.
        Sorts L in ascending order"""
    start = 0
    while start != len(L):
        for i in range(start, len(L)):
            if L[i] < L[start]:
                L[start], L[i] = L[i], L[start]
        start += 1
