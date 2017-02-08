f = open("test",'w')
f.write("HI\n")
f.write('test')
f.write('yoyoyoyoyoyo')
f.close()

f = open("test", 'r')
print f.read()
##for line in f:
##    print line
f.close()
