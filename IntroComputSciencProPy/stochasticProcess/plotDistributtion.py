import variance
import random
import pylab
def flip(numFlips):
    """numFlips is a positive in"""
    heads = 0
    for i in range(numFlips):
        if random.choice(('H','T'))=='H':
            heads +=1
    return heads/float(numFlips)

def flipSim(numFlipsperTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsperTrial))
    mean = sum(fracHeads)/len(fracHeads)
    sd = variance.stdDev(fracHeads)#importar
    return (fracHeads, mean, sd)

def labelPlot(numFlips,numTrials,mean,sd):
    print("entro labelPlot")
    pylab.title(str(numTrials)+'Trials of '+str(numFlips)+'flips each')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    pylab.annotate('Mean = '+str(round(mean,4))+'\nSD= '+str(round(sd,4)),size='x-large',xycoords='axes fraction',xy=(0.67,0.5))
def makePlots(numFlips1,numFlips2,numTrials):
    val1, mean1, sd1 = flipSim(numFlips1,numTrials)
    pylab.hist(val1,bins=20,ec='k')
    labelPlot(numFlips1,numTrials,mean1,sd1)
    xmin,xmax=pylab.xlim()
    pylab.figure()
    val2, mean2, sd2 = flipSim(numFlips2,numTrials)
    pylab.savefig('grafico 1')
    pylab.hist(val2,bins=20,ec='k')
    pylab.xlim(xmin,xmax)
    labelPlot(numFlips2,numTrials,mean2,sd2)
    pylab.savefig('grafico 2')


makePlots(100,1000,1000)
pylab.show()
