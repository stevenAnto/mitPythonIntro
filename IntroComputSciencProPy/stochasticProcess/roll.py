import random as r

def rollDie():
    """Return a random in between 1 and 6"""
    return r.choice([1,2,3,4,5,6])

def rollN(n):
    result = ' '
    print('result',result)
    for i in range(n):
        result =result+str(rollDie())
    return result

print('bota' ,rollN(20))
