class Circle(object):

    def __init__(self,radio):

        self.PI = 3.14159
        self.radio = radio

    def getArea(self):
        return self.PI*self.radio**2

    def getVolum(self):
        return (4.0/3.0)*self.PI*(radio*3)
    def __str__(self):
        return "Es un circulo with "+ str(self.radio)

