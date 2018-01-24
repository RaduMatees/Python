"""Conversia de la baza zece la baza b"""
from numpy import zeros

v = zeros((20), dtype=int)
n = int(input('n='))
b = int(input('b='))
i = 0

while n != 0:
    v[i] = n % b
    i += 1
    n = n // b
print('Exprimarea lui', n, 'in baza', b, 'este', end=' ')

for k in range(i-1, -1, -1):
    print(v[k], end=' ')