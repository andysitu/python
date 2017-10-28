def get_highest_3(num_range):
    nums = []
    for num in range(num_range, 1, -1):
        status = True
        for i in nums:
            if i % num == 0:
                status = False
        if status:
            nums.append(num)
        if len(nums) == 3:
            return nums

def get_divisibles(num):
    interval = 1
    for i in get_highest_3(num):
        interval *= i

    tested = {}
    primes = []
    for n in range(2, num+1):
        if n in tested:
            continue
        cur_prod = 1
        prime_num = 1
        while cur_prod <= num:
            cur_prod *= n
            tested[cur_prod] = 0
            if cur_prod <= num and cur_prod not in primes:
                prime_num = cur_prod
        primes.append(prime_num)
    print(primes)
    cur_num = interval
    while(True):
        cur_status = True
        for i in primes:
            if cur_num % i != 0:
                cur_status = False
                break
        if cur_status:
            return cur_num
        cur_num += interval
        
print(get_divisibles(20))
