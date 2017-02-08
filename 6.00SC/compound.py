import pylab

pylab.figure(1)
principal = 10000 #initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years+1):
    values.append(principal)
    principal += principal * interestRate
pylab.plot(values, linewidth = 30)
pylab.title('5% Growth, Compounded Anually')
pylab.xlabel('Years of Compounding', fontsize = 'x-small')
pylab.ylabel('Value of Principal($)')
pylab.show()
