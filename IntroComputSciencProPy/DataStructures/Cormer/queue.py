class Queue(object):
    def __init__(self):
        self.array =[]
        self.head=0
        self.tail=0
    def enqueue(self,value):
        self.array.append(value)
        #self.array[self.tail]=value
        self.tail +=1
        #if self.tail=len(self.array):
         #   self.tail=1
        #else self.tail +=1
    def dequeue(self):
        x=self.array[self.head]
        print('es la cabeza',x)
        self.head +=1
        self.array.pop(0)

    def __str__(self):
        return str(self.array)

