import pylab
import random
def succesfullStarts(succesProb, numTrials):
    """
    Return a list of the number of attemps """
    triesBeforeSuccess= []
    for t in range(numTrials):
        consecFailures = 0
        while random.random() > succesProb:
            consecFailures +=1
        triesBeforeSuccess.append(consecFailures)
    print(sum(triesBeforeSuccess))
    return triesBeforeSuccess


distribution = succesfullStarts(0.5,5000)
pylab.hist(distribution,bins = 14)
pylab.xlabel('Tries befores succes')
pylab.ylabel('Number of Occurrences out of '+str(5000))
pylab.savefig('Geometri distribution')
pylab.show()
