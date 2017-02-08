import values

def funk(a, b = 2, c = 2):
    return a * b * c

print funk(1)
print funk(10, 10, 10)


def show(a, b, c):
    print a
    print b
    print c

show(b = 2, a = 10, c = 100)

global glovalue
glovalue = 1

def willitrun():
    global abc
    abc += 5

def testit():
    print glovalue
    global abc
    abc = 5
    willitrun()
    print abc
    def test():
        print 'testing'

testit()
print 'v:', values.v
values.increase()
print 'v:', values.v
