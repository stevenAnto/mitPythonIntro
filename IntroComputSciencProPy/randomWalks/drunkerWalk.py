import Field
import drunkUsual

def walk(f,d,numSteps):
    """Assumes
    f a Field
    d a Drunk in f
    numSteps an int>=0.
    Moves d numSteps times; 
    Returns the distance betweeen the final location and the location at the start of the walk"""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))


def sinWalks(numSteps, numTrials,dClass):
    """Assumes numSteps an int >=0,numTrials an int >=0
    dClass a subclass of Drun
    Simulates numTrials walks of numSteps steps each
    Returns a list of the final distances for each trial"""
    Homer = dClass()
    origin = Location(0,0)
    distance= []
    for t in range(numTrials):
        f= Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f,Homer, numTrials),1))
        return distance

    def drunkTest(walkLengths, numTrials, dClass):
        """Assumes
        walkLengths a sequence or ints>=0
        numTrials an int >0, dClass a subclass of Drunk"""
        for numSteps in walkLengths:
            distances = simWalks(numSteps, numTrials,dClass)
            print(dClass.__name__,'random walk of ',numSteps,'steps')
            print('Mean =', round(sum(distances)/len(distances),4))
            print("Max = ", max(distances), 'Min = ',min(distances))

