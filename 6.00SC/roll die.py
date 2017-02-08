import random

def rollDie():
    """Returns random int between 1 and 6"""
    return random.choice(range(1, 7))

def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print result

rollN(100)
