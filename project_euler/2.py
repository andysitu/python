def get_fibs(max_num):
    fib_dic = [1,2]
    i = 1

    while(True):
        num = fib_dic[i] + fib_dic[i-1]
        if num > max_num:
            break
        else:
            fib_dic.append(num)        
        i += 1

    return fib_dic

fib_list = get_fibs(4000000)

sum = 0

for i in fib_list:
    if i % 2 == 0:
        sum += i

print(sum)
