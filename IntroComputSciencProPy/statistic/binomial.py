import math
def binomial(n,k,p):
    combinatoria = math.comb(n,k)
 #   print('combinatoria', combinatoria)
    factor2 =p**k
    factor3=(1-p)**(n-k)
#    print(factor2)
#    print(factor3)
    return combinatoria*factor2*factor3


def varies(n,numk):
    values = []
    for i in range(numk[0],numk[1]):
        print(binomial(n,i,1/6))
        values.append(binomial(n,i,1/6))
    return values

print(varies(10,(2,100)))

