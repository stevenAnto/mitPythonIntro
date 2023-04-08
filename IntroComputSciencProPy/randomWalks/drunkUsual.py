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
    def take_step(self):
        stepChoices = [(0,1),(0,2.0),(1,0),(-1.0,0)]
        return random.choice(stepChoices)
class EW_drunk(Drunk):
    def takeStep(self):
        stepChoices = [(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)

def sim_all(drunk_kinds, walk_lengths, num_trials):
    for d_class in drunk_kinds:
        driver.drunk_test(walk_lengths, num_trials, d_class)




