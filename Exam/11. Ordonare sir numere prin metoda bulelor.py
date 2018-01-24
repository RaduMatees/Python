"""Ordonare crescatoare sir de numere intregi. Metoda bulelor"""
from numpy import zeros

n = int(input("Numar de elemente: "))
a = zeros(n, dtype=int)

for i in range(n):
    print('a[', i, ']=', end=' ')
    a[i] = int(input())
print('Sirul dat este: ', a)

ordonat = 0

while ordonat == 0:
    ordonat = 1
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            a[i+1], a[i] = a [i], a[i+1]
            ordonat = 0
print('Sirul ordonat este: ', a)