import drunkUsual
import Field
import location

def walk(f, d, numSteps ):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps  an int >=0, numTrials an int >0
    dClass a subclass of Drunk
    Simulates numTrials walks of numSteps steps each
    Returns a list of the final distances for each trial """
    Homer =dClass()
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f,Homer,numTrials),1))

    return distances

print(simWalks(20,10, drunkUsual))
