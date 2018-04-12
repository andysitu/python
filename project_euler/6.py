import math

def sum_sq_diff(n):
    sq_sum = (1/3)*math.pow(n,3) + (1/2) * math.pow(n,2) + (1/6) * n
    sum_sq = (1 + n) * n / 2

    return math.pow(sum_sq, 2) - sq_sum

print(sum_sq_diff(100))
