"""Ordonare puncte din plan descrescator dupa distanta la origine"""

from math import sqrt
from numpy import zeros

n = int(input("n ="))
X = zeros((n), dtype = float)
Y = zeros((n), dtype = float)
d = zeros((n), dtype = float)

for i in range (0, n):
    print ('X[', i ,'] =', end = ' ')
    X[i] = float(input())
    print ('Y[', i ,'] =', end = ' ')
    Y[i] = float(input())
print ('Vectorul X este: ', X)
print ('Vectorul Y este: ', Y)

for i in range (0, n):
    d[i] = sqrt (X[i] ** 2 + Y[i] ** 2)

ordonat = False

while not ordonat:
    ordonat = True
    for i in range (0, n - 1):
        if d[i] < d[i + 1]:
            d[i], X[i], Y[i] = d[i + 1], X[i +1], Y[i +1]
            ordonat = False
print ("Punctele ordonate sunt ", end = ' ')

for i in range (0, n):
    print ("(", format(X[i], '.2f'), ", ", format(Y[i], '.2f'), ")", end = ' ')