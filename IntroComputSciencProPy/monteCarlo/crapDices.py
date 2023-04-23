import gameClass
import sys
sys.path.append("..")
from randomWalks.variance import stdDev

def crapsSim(handsPerGame, numGames):
    """Assumes handsPerGame and numGames are ints >0
    Play numGames games of handsPerGame hands"""
    games = []
    #play numGames games
    for t in range(numGames):
        c= gameClass.CrapsGame()
        for i in range(handsPerGame):
            c.playHand()
        games.append(c)
    
    #statistics for each game
    pROIPerGame, dpROIPerGame = [],[]
    for g in games:
        win, losses = g.passResult()
        pROIPerGame.append((win-losses)/float(handsPerGame))
        win, losses, pushes =g.dpResults()
        dpROIPerGame.append((win-losses)/float(handsPerGame))

    #Produce and print summary stastic
    meanROI = str(round((100*sum(pROIPerGame)/numGames),4))+'%'
    sigma=str(round(100*stdDev(pROIPerGame),4))+'%'
    print('Pass:', 'MeanRoi=',meanROI,'Std.Dev=',sigma)
    meanROI = str(round((100*sum(dpROIPerGame)/numGames),4))+'%'
    sigma=str(round(100*stdDev(dpROIPerGame),4))+'%'
    print('Dont'+'Pass:', 'MeanRoi=',meanROI,'Std.Dev=',sigma)


crapsSim(20,10)

