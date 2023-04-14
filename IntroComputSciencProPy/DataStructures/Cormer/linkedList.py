#single
class Node(object):
    def __init__(self,value):
        self.next=None
        self.prev=None
        self.value= value
    def nextN(self):
        return self.next
    def __str__(self):
        return str(self.value)


class LinkedList(object):
    def __init__(self):
        self.head =None
    def search(self,key):
        #retorna un elemento anterior
        x=self.head
        while x!=None and x.value!=key:
            x=x.next
        return x
    def deleter(self,value):
        nodo = search(value)

    def insert(self,value):
        nodo = Node(value)
        #print('type',type(nodo))
        nodo.next =self.head
        self.head = nodo
        print('saliendo insert, esta es la cabeza',self.head)
    def __str__(self):
        lista= ''
        nodo =self.head
        print('cabeza',nodo)
        print('type',type(nodo))
        while nodo!=None:
            print('entro while')
            print('entro',nodo)
            lista= lista+nodo.__str__()+','
            nodo = nodo.nextN()
        return lista






