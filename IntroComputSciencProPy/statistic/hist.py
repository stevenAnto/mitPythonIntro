import pylab
import random
random.seed(0)
vals = []
for i in range(1000):
    num1 = random.choice(range(0,101))
    num2 = random.choice(range(0,101))
    vals.append(num1+num2)
pylab.hist(vals,bins = 20,ec='k')
pylab.xlabel('Number of Ocurrences')
pylab.savefig('histograma')
pylab.show()
