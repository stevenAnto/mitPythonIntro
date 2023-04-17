import random
import probabilityHash as p
def simInsertions(numIndices, numInsertions):
    """Assumes numIndices and numInsertions are positive ints
    Return 1 if there is a collision """
    print('entro Inser')
    choices = range(numIndices)#list of possible indices
    used = []
    for i in range(numInsertions):
        print(used)
        hashVal = random.choice(choices)
        if hashVal in used:
            return 1
        else:
            used.append(hashVal)
    return 0

def finProb(numIndices, numInsertions,numTrials):
    collision=0
    for t in range(numTrials):
        collision+=simInsertions(numIndices,numInsertions)
    return collision/numTrials

#modelo
print('Actual probability of a collision ',p.collisionProb(1000,50))
#empirico
print('Estimate probability of a collision ',finProb(1000,50,10000))
#modelo
print('Actual probability of a collision ',p.collisionProb(1000,200))
#empirico
print('Estimate probability of a collision ',finProb(1000,200,10000))
"""that's mean the hashTable has to be enormous to be useful?
This probability tell us little about the expected lookup time. The expected lookup tiem 
depends upon the avergage length of the list implementing  the buckets.
Assuming a uniform distribution, this is the number of insertions/number of buckets'"""
