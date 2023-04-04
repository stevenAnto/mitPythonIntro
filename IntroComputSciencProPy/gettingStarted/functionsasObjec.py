def applyToEach(L,f):
    for i in range(len(L)):
        L[i]=f(L[i])

L = [1,-2,3.33]
print ("L= ",L)
applyToEach(L,abs)
print ("L= ",L)
applyToEach(L,int)
print ("L= ",L)
applyToEach(L,factR)
print ("L= ",L)
print ("L= ",L)
