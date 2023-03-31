#Este algoritmo usa mas memoria que el algoritmo presentado en el libro de Larson
def merge(left,right,compare):
    print("entro",left,right)
    """left and right are sorted"""

    result = []
    i,j = 0,0
    while i < len(left) and j<len(right):
        if compare(left[i],right[j]):
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1

    while(i<len(left)):
        result.append(left[i])
        i +=1
    while(j<len(right)):
        result.append(right[j])
        j +=1
    return result
#jajajaj

def mergeSort(L, compare = lambda x,y:x<y):
    """Assumes L is a list, compare defines an ordering on element of L
    returns a new sorted list with the same elements as L"""
    if len(L)<2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle],compare)
        right = mergeSort(L[middle:],compare)
        return merge(left,right,compare)


listp = [5,2,4,6,1,3,8,7]
print(listp)
print(mergeSort(listp))



