import diceProblem as die
class CrapsGame(object):
    def __init__(self):
        self.passWins,self.passLosses = 0,0
        self.dpWins,self.dpLosses, self.dpPushes=0,0,0

    def playHand(self):
        throw = die.rollDie()+die.rollDie()
        if throw ==7 or throw==11:
            self.passWins +=1
            self.dpLosses +=1
        elif throw==2 or throw==3 or throw==12:
            self.passLosses +=1
            if throw==12:
                self.dpPushes +=1
            else:
                self.dpWins +=1
        else:
            point =throw
            while True:
                throw=die.rollDie()+die.rollDie()
                if throw==point:
                    self.passWins +=1
                    self.dpLosses +=1
                elif throw==7:
                    self.passLosses +=1
                    self.dpWins +=1
                    break
    def passResult(self):
        return (self.passWins,self.passLosses)
    def dpResults(self):
        return (self.dpWins, self.dpLosses,self.dpPushes)

