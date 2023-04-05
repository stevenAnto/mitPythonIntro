import heap

# O(lgn)
def heapExtractMax(vector):
    print('entro heapExtractMax',vector)
    if len(vector)<0:
        raise ValueError('heap underflow1')
    maxi = vector[0]
    vector[0]=vector[len(vector)-1]
    vector.pop()
    print('eliminando el ultimo',vector)
    heap.maxHeapify(vector,0)
    return maxi

# O(lgn)
def heapIncreaseKey(vector,i,key):
    """i is the index where you put the value k
    Assumes key>vector[i]"""
    print('entro heapIncreaseKey',vector)
    print('vector[i]',vector[i], key)
    print(key<vector[i] )
    if  not key<vector[i]:
        raise ValueError('new key is smaller than current key')
    vector[i]=key
    while i>0 and vector[heap.parent(i)]<vector[i]:
        aux = vector[i]
        vector[i]=vector[heap.parent(i)]
        vector[heap.parent(i)]=aux
        i= heap.parent(i)


# O(lgn)
def maxHeapInsert(vector,key):
    vector.append(float("inf"))
    heapIncreaseKey(vector,len(vector)-1,key)
    

#few testincreaseKey
#exercises 6.5.1
"""a = [15,13,9,5,12,8,7,4,0,6,2,1]
heapExtractMax(a)
print(a)"""
#exercises 6.5.2

b = [15,13,9,5,12,8,7,4,0,6,2,1]
maxHeapInsert(b,10)
print(b)




