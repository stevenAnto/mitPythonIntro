def removeDups(l1,l2):
    for e1 in l1:
        if e1 in l2:
            l1.remove(e1)

lista1 = [1,2,3,4]
lista2 = [1,2,5,6]
removeDups(lista1,lista2)
print('lista1=',lista1)
