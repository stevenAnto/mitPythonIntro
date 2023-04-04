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
    origin = location.Location(0,0)
    distances = []
    for t in range(numTrials):
        f = Field.Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f,Homer,numSteps),1))

    return distances
#Trail with different walkLengths
def drunkTest(walkLengths, numTrials, dClass):
    for numSteps in walkLengths:
        distances =  simWalks(numSteps,numTrials,dClass)
        print(dClass.__name__,'random walk of ', numSteps, 'steps')
        print('Mean  = ', round(sum(distances)/len(distances),4))
        print('Max = ', max(distances),'Min', min(distances))

drunkTest((0,1,10,100,1000,10000),100,drunkUsual.UsualDrunk)
