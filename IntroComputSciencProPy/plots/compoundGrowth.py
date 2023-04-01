import pylab
principal = 10000 #initial invesment
interestRate = 0.05
years = 20
values =[]
for i in range(years+1):
    values.append(principal)
    principal += principal*interestRate
pylab.figure(1)
pylab.title("5% Growth, compound")
pylab.xlabel('Year')
pylab.ylabel('Value of Principal')
pylab.plot(values)
pylab.show()
