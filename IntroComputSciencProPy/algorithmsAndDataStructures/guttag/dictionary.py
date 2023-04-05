import random
class intDict(object):
    """A dictionary witn integer keys"""
    def __init__(self, numBuckets):
        """Create a empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
        print("tamani",len(self.buckets))

    def addEntry(self,key,dictVale):
        """Asumes key an int"""
        indice =key%self.numBuckets
        print("indice",indice)
        hashBucket = self.buckets[indice]
        #La forma como resuelve la collision es simplemente almacenar las tuplas en una posicion de una lista
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == key:
                hashBucket[i]=(key,dicVale)
                return
        hashBucket.append((key, dictVale))

    #What is the complexity of getValue, it may be O(1)
    #But if all data is in the same bucket, the complexity could be O(n). If we make large enough the bucket, reduces the time of search
    #this is a tradeoff. We can trade space for time
    def getValue(self, key):
        """Assumes key an int"""
        hasBucket = self.buckets[key%self.numBuckets]
        for e in hashBucket:
            if e[0] == key:
                return e[1]
        return None

    def __str__(self):
        print("tamani",len(self.buckets))
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result +str(e[0])+':'+str(e[1])+'\n'

        return result[:-1]+'}'


D = intDict(17)
print(D)
for i in range(20):
    key = random.choice(range(10**5)) 
    print("k",key)
    D.addEntry(key,i)

#print(D.buckets)

print("The value of the intDcit is:")
print(D)
print("\n","The buckets are:")




