import random

class Drunk(object):
    def __init__(self, name = None):
        """Assumes name is a str"""
        self.name = name
    def  __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1),(0,-1),(1,0),(-1,0)]
        return random.choice(stepChoices)




