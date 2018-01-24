"""Schema lui Horner"""
from numpy import zeros

n = int(input("Gradul polinomului: "))
a = zeros(n+1, dtype=int)
b = zeros(n+1, dtype=int)
c = int(input('c= '))

for i in range(n+1):
    print('a[', i, ']=', end=' ')
    a[i] = int(input())

b[0] = a[0]

for i in range(n+1):
    b[i] = c*b[i-1]+a[i]
print('Coeficientii catului sunt: ', end=' ')

for i in range(n):
    print(a[i])
print('Restul este: ', b[n])