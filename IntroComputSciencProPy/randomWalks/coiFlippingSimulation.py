import pylab
import random
import variance

def makePlot(xVals,yVals,title,xLabel,yLabel, style, logx=False,logy=False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals, yVals, style)
    if logx:
        pylab.semilogx()
    if logy:
        pylab.semilogy()

def runTrial(numFlips):
    numHeads = 0
    for n in range(numFlips):
        if random.choice(('H','T'))=='H':
            numHeads +=1
    numTails = numFlips - numHeads
    return (numHeads,numTails)

def flipPlot1(minExp,maxExp,numTrials):
    """minExp and maxExp and numTrials >0 minExp<maxExp"""
    #Plots summaries of resultes of numTrials trials of 2**minExp to 2**maxExp coin Flips
    ratiosMeans, diffsMeans, ratiosSds,diffsSDs =[],[],[],[]
    xAxis = []
    for exp in range(minExp,maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios, diffs = [], []
        for t  in range(numTrials):
            numHeads,numTails = runTrial(numFlips)
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads-numTails))
        ratiosMeans.append(sum(ratios)/numTrials)
        diffsMeans.append(sum(diffs)/numTrials)
        ratiosSds.append(variance.stdDev(ratios))
        diffsSDs.append(variance.stdDev(diffs))
    numTrialString = '('+str(numTrials)+'Trial )'
    title = 'Mean Heads / Tails Ratios '+numTrialString
    makePlot(xAxis,ratiosMeans,title, 'Number of slips','Mean Heads / Tails', 'ko',logx=True)
    title = 'SD Heads/Tails Ratios'+ numTrialString
    makePlot(xAxis,ratiosSds,title,'Number of Flips', 'Standard Deviation ', 'ko', True,True)


flipPlot1(4,20,20)
pylab.show()
pylab.savefigure('means anr std of ratios')




    







