def findExtremeDivisor(n1,n2):
    minVal,maxVal=None,None
    for i in range(2,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            if minVal==None:
                minVal=i
            maxVal=i
    return (minVal,maxVal)

minDivisor,maxDiviso=findExtremeDivisor(100,200)
