import pylab
def clear(n,p,steps):
    """assumes n and steps  positives int, p a float"""
    #n:the initial number of moleculs
    #p:the probability of a molecule being cleared
    #steps: the length of simulations
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-p)**t))

    pylab.plot(numRemaining)
    pylab.xlabel('time')
    pylab.ylabel('Molecules Remaininoog')
    pylab.title('Clearance of Drug')
    pylab.savefig('exponential decay')

clear(1000,0.01,1000)
pylab.show()
