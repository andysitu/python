import math

def get_prime_list(num):
    prime_list = [2]
    prime_factors = []
    sq_num = math.ceil(math.sqrt(num))

    for i in range(2, sq_num):
        prime_status = True
        for prime in prime_list:
            if i % prime == 0:
                prime_status = False
                break
        if prime_status == True:
            prime_list.append(i)
            if num % i == 0:
                prime_factors.append(i)
    return prime_factors

print(get_prime_list(600851475143))
