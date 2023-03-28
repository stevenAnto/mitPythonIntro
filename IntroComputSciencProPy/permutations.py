import itertools

def convertirNum(lista):
    numS=''
    for i in lista:
        numS = numS+str(i)
    return int(numS)
p = itertools.permutations([1,2,3,4,5],5)

pl = list(p)
print(len(pl))
print(pl)
sumatotal = 0
for i in range(len(pl)):
    num = convertirNum(pl[i])
    sumatotal= sumatotal+num
print(sumatotal)



a = [ 1,2,3,4]
print(convertirNum(a))
print(type(convertirNum(a)))

#suma = itertools.accumulate(pl[1])

#print(list(suma)[2])
