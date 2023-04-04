
class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate druunk')
        else:
            self.drunks[drunk]=loc

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in the Field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
            #use method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist,yDist)

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in the field')
        return self.drunks[drunk]


