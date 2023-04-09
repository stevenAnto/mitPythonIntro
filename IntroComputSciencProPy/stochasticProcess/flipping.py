import pylab
import random as r

def flip(numFlips):
    """numFlips>0"""
    heads = 0
    for i in range(numFlips):
        if r.choice(('H','T'))=='H':
            heads += 1
    return heads/numFlips

def fliSim(numFlipsPerTrial, numTrials):
    """Assumes numFlipsPerTrial and numTrials positive int"""
    frachHeads = []
    for i in range(numTrials):
        frachHeads.append(flip(numFlipsPerTrial))
    mean = sum(frachHeads)/len(frachHeads)
    print(frachHeads)
    return mean

def regressToMean(numFlips, numTrials):
    #Get fraction of heads for each trail of numTrials
    frachHeads = []
    for t in range(numTrials):
        frachHeads.append(flip(numFlips))
    #Find trails, with extrem results and for each the next trial exttrial
    extremes, nextTrials = [],[]
    for i in range(len(frachHeads)-1):
        if frachHeads[i]<0.33 or frachHeads[i]>0.66:
            extremes.append(frachHeads[i])
            nextTrials.append(frachHeads[i+1])
    #plot results
    pylab.plot(range(len(extremes)), extremes,'ko',label='Extremes')
    pylab.plot(range(len(nextTrials)), nextTrials,'k^',label='Next Trial')
    pylab.axhline(0.5)
    pylab.ylim(0,1)
    pylab.xlim(-1,len(extremes)+1)
    pylab.xlabel('Extreme Example and Next Trial')
    pylab.ylabel('Fraction Heads')
    pylab.title('Reression to the Mean')
    pylab.legend(loc = 'best')
    pylab.show()

def flipPlot(minExp, maxEp):
    """Assumes minExp and maxEp positive integers; minExp<maxEp
    Plots results of 2**minExp to 2**maxEp coin flips"""
    ratios, diffs , xAxis = [], [],[]
    for exp in range(minExp,maxEp+1):
        xAxis.append(2**exp)
    print('xAxis', xAxis)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if r.choice(('H','T'))=='H':
                numHeads += 1
        numTails = numFlips - numHeads
        try:
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads-numTails))
        except ZeroDivisionError:
            continue
    print('ratios',ratios)
    print('diffs ',diffs)
    pylab.title('Difference between heads and Tails')
    pylab.xlabel('Number of flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis,diffs,'k')
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.plot(xAxis,ratios,'k')

r.seed(0)
flipPlot(4,20)
pylab.show()




