def getBinaryRep(n, numDigits):
    """Assumes n and numDigits are non-negative  ints
    Returns a str of length numDigits that is binary representation of n"""
    result = ''
    while n>0:
        result = str(n%2)+result
        n = n//2
    
    if len(result) >numDigits:
        raise ValueError('not enough digits')
    for i in range(numDigits-len(result)):
        result ='0'+result
    return result

def genPowerSet(L):
    """Assumes L is a list
    Returns a list of lists that contains all posible 
    combinatios of the elements of L
    e.g. if L = [1,2] it will Returns
    [],[1],[2],[1,2]"""
    powerSet = []
    for i in range(0,2**len(L)):
        binStre = getBinaryRep(i, len(L))
        subset = []
        for j in range(len(L)):
            if binStre[j]=='1':
                subset.append(L[j])
        powerSet.append(subset)
    return powerSet

#print (genPowerSet(range(10)))

