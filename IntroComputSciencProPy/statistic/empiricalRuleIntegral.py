import scipy.integrate
import random
import pylab
def gaussian(x,mu,sigma):
    #print('gaussian val x',x)
    factor1 = (1.0/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2

def checkEmpirical(numTrials):
    contador=0
    for t in range(numTrials):
        mu = random.randint(-10,10)
        sigma = random.randint(1,10)
        print('For mu =', mu, 'and sigma = ', sigma)
        for numStd in (1,2,3):
            contador +=1
            area = scipy.integrate.quad(gaussian,mu-numStd*sigma,mu+numStd*sigma,(mu,sigma))[0]
            print(' Fraction within', numStd, 'std=', round(area,4))
    print('contador',contador)

checkEmpirical(3)
