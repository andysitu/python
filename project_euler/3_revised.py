import math

def get_largest_factor(num):
    cur_num = num
    factor = 2
    largest_factor = 1
    while cur_num > 1:
        if cur_num % factor == 0:
            cur_num /= factor
            largest_factor = factor
            while cur_num % factor == 0:
                cur_num /= factor
        factor += 1
    return largest_factor

print(get_largest_factor(600851475143))
