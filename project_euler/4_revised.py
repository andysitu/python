def is_palindrome(num):
    return str(num) == str(num)[::-1]

a = 999
max_palin = 0

while a >= 100:
    if a % 11 == 0:
        b = 999
        b_diff = 1
    else:
        b = 990
        b_diff = 11
    while b >= a:
        if a*b <= max_palin:
            break

        if is_palindrome(a*b):
            max_palin = a * b
        b -= b_diff
    a -= 1


print(max_palin)
