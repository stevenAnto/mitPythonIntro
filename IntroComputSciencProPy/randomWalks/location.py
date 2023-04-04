class Location(object):
    def __init__(self,x,y):
        """x and y are numbers"""
        self.x, self.y = x,y

    def move(self, deltax,deltay):
        """deltax and deltay are """
        return Location(self.x+deltax, self.y+deltay)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox, oy = other.y, other.y
        xDist , yDist = self.x-ox, self.y-oy
        return (xDist**2+yDist**2)**0.5

    def __str__(str):
        return '<' +str(self.x)+','+str(self.y)+'>'




    


