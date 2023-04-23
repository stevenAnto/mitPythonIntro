import random
"""Realizaremos la simulacion del experimento de lanzar un dado 24 veces y si es rentable,
apostar a que salga el numero 6
Este experimento puede entrar en un binomial 1-(35/36)elevado(24), el cual da 0.49"""
def rollDie():
    return random.choice([1,2,3,4,5,6])

def checkPascal(numTrials):
    """Prints an estiamte of the probability of wining"""
    numWins=0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2==6:
                numWins +=1
                break
    print('Probability of winning= ', numWins/numTrials)

#checkPascal(100000)
