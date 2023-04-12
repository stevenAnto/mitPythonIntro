class Stack(object):
    def __init__(self):
        self.top = -1
        self.stack = []
    def stackEmpty(self):
        if self.top ==0:
            return True
        else :
            return False
    def push(self,value):
        self.top = self.top+1
        self.stack.append(value)
#        self.stack[self.top]=value
    def pop(self):
        if self.stackEmpty():
            raise ValueError('Underflow')
        else:
            valueAux = self.stack[self.top]
            self.top =self.top-1
            self.stack.pop()
            return valueAux
    def __str__(self):
        return str(self.stack)

