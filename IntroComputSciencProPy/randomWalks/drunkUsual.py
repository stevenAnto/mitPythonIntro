import driver
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

class Cold_drunk(Drunk):
    def takeStep(self):
        """Se va dos para la izquierda"""
        stepChoices = [(0,1),(0,-2.0),(1,0),(-1.0,0)]
        return random.choice(stepChoices)
class EW_drunk(Drunk):
    def takeStep(self):
        """Solo se mueve a los costados"""
        stepChoices = [(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)

def sim_all(drunk_kinds, walk_lengths, num_trials):
    for d_class in drunk_kinds:
        driver.drunkTest(walk_lengths, num_trials, d_class)

sim_all((UsualDrunk,Cold_drunk, EW_drunk),(100,1000),(10))






