num = int(raw_input("Enter an integer: "))

root, pwr = 0, 0
ans = -1
status = False
test = 0

print 'num is', num
while root < num-1 and status == False:
    root += 1
    pwr = 0
    while pwr >= 0 and pwr < 5:
        pwr += 1
        test = root**pwr
##        print root, pwr, test
        if test == num:
            status = True
            ans = 1
            break
        if test > num:
            status == True
            break

if ans == -1:
    print("I can't find two integers to fit these criterias")
else:
    print root, "**", pwr, " = ", num
