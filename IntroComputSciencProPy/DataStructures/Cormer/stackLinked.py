import linkedList

class stackLinked(object):
    def __init__(self):
        self.linkedList = linkedList.LinkedList()
        self.top = self.linkedList.head
    def pushL(self,value):
        nodo = linkedList.Node(value)
        nodo.next =self.top
        self.top = nodo
    def popL(self):
        if self.top==None:
            raise ValueError('underflow')
        else:
            nodo = linkedList.top
            self.top = LinkedList.top.next
            return nodo

