max_num = 0

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        if i * j <= max_num:
            break
        num = i * j
        string_num = str(num)
        if string_num == string_num[::-1] and num > max_num:
            max_num = num

print(max_num)
