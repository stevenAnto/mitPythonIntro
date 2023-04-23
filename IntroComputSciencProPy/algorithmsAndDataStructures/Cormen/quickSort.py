def partition(vector,p,r):
    x = vector[r]
    i = p-1
    print('inicio', vector)
    print('r',r)
    print('prueba', range(p,r))
    for j in range(p,r):
        if vector[j]<=x:
            i +=1
            vector[i],vector[j]=vector[j],vector[i]
        print('como se esta ordenado ', vector)
    vector[i+1],vector[r]=vector[r],vector[i+1]
    return i+1

def quickSort(vector,p,r):
    if p<r:
        q = partition(vector,p,r)
        print('q',q)
        quickSort(vector,p,q-1)
        quickSort(vector,q+1,r)

#test de partition
a = [2,8,7,1,3,5,6,4]

print(quickSort(a,0,len(a)-1))
print('ordenado',a)
