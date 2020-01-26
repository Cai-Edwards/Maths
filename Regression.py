import numpy as np
import matplotlib.pyplot as plt

n = 10

mean = [10, 10]
cov = [[1, 0.8], [0.8, 1]]
new = np.random.multivariate_normal(mean, cov, n)

xlist, ylist = map(list, zip(*new))

xbar = sum(xlist)/n
ybar = sum(ylist)/n

sxy = sum((x-xbar)*(y-ybar) for x, y in zip(xlist, ylist))
sxx = sum((x-xbar)**2 for x in xlist)
syy = sum((y-ybar)**2 for y in ylist)

b = sxy/sxx
a = ybar-(b*xbar)

linx = np.linspace(min(xlist), max(xlist), 150)
liny = [x * b + a for x in linx]

plt.scatter(xlist, ylist)
plt.plot(linx, liny)

PMCC = sxy/(sxx*syy)**0.5
determination = PMCC**2

print(PMCC)
print(determination)

sortedx = sorted(xlist)
rankedx = [sortedx.index(k) for k in xlist]

sortedy = sorted(ylist)
rankedy = [sortedy.index(k) for k in ylist]

SR = 1 - (6*sum((x-y)**2 for x,y in zip(rankedx, rankedy))) / (n*(n**2-1))

print(SR)

plt.show()
