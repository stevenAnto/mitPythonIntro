def partition(vector,p,r):
    x = vector[r]
    i = p-1
    print('inicio', vector)
    print('prueba', range(p,r-1))
    for j in range(p,r-1):
        if vector[j]<=x:
            i +=1
            vector[i],vector[j]=vector[j],vector[i]
        print('como se esta ordenado ', vector)
    vector[i+1],vector[r]=vector[r],vector[i+1]
    return i+1
#test de partition
a = [2,8,7,1,3,5,6,4]

print(partition(a,0,len(a)-1))
print(a)
