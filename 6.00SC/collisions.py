import random

def collisionProb(n, k):
    prob = 1.0
    for i in range(1, k):
        prob = prob * ((n-i)/float(n))
    return 1 - prob

def simInsertions(numIndices, numInsertions):
    """ Assumes numIndices and numInsertions are positive ints.
        Returns 1 if there is a collision; 0 otherwise"""
    choices = range(numIndices)
    used = []
    for i in range(numInsertions):
        hashVal = random.choice(choices)
        if hashVal in used: #there is a collision
            return 1
        else:
            used.append(hashVal)
    return 0

def findProb(numIndices, numInsertions, numTrials):
    collisions = 0.0
    for t in range(numTrials):
        collisions += simInsertions(numIndices, numInsertions)
    return collisions/numTrials

print 'Actual Probability of a collision =', collisionProb(1000, 50)
print 'Est. probability of a collision =', findProb(1000, 50, 10000)
print 'Actual probability of a collision =', collisionProb(1000, 200)
print 'Est. probability of a collision =', findProb(1000, 200, 10000)
