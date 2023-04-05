#Remember the heap is storaged in an array,
#Where parent(i)=celing (i/2)
#leftChild(i)=2*i
#rightChild(i)=2*i+1
#mal uso de methodos y functions


def leftChild(i):
    return 2*i


def rightChild(i):
    return 2*i+1
def parent(i):
    return i//2

def maxHeapify(vector,i):
    print("entroindice",i)
    l=leftChild(i)
    r=rightChild(i)
    print("l,r",l," ",r)
    if l<len(vector) and vector[l]>vector[i]:
        largest =l
    else:
        largest =i
    if r<len(vector) and vector[r]>vector[largest]:
        largest =r
    if largest != i:
        #excechange
        aux = vector[i]
        vector[i]=vector[largest]
        vector[largest]=aux
        #function recursive
        maxHeapify(vector,largest)


def buildMaxHeap(vector):
    size =len(vector)
    for num in reversed(range(len(vector))):
        maxHeapify(vector,num)
        print("ordenado:",a)

#prueba

a = [4,1,3,2,16,9,10,14,8,7]
print(a)
buildMaxHeap(a)
print(a)

