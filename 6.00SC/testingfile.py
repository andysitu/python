def writeTestFile():
    nameHandler = open('test', 'w')
    for i in range(2):
        name = raw_input('Enter something:')
        nameHandler.write(name + '\n')
    nameHandler.close()


def writeFile():
    nameHandler = open('test', 'w')
    nameHandler.write("test\n")
    nameHandler.write('123')

def openTestFile():
    nameHandle = open('test', 'r')
    for line in nameHandle:
        print line
    nameHandle.read()
    nameHandle.close()


writeFile()
openTestFile()
