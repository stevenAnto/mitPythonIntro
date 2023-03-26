def copy(l1,l2):
    newl=l1[:]
    """Assumes l1 l2 are listt, mutate l2 to be a copy of l1"""
    while len(l2)>0:
        l2.pop()
    for e in newl:
        l2.append(e)

#test

li1 = [1,2,3,4,5,6,7]
li2 = [8,9,10,11,12,13]

#si aplico a la misma lista no cumple
copy(li1,li1)
print(li1)
