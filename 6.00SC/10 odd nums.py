maxNum = None;

def isOdd(num):
    return num % 2 != 0

def larger(num):
    global maxNum
    if isOdd(num):
        if maxNum == None:
            maxNum = num
        if num > maxNum:
            maxNum = num

for x in range(10):
    num = int(raw_input("enter number: "))
    larger(num)

print maxNum
