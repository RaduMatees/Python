"""Ordonare crescatoare sir de numere intregi. Metoda selectiei"""
from numpy import zeros

n = int(input("Numar de elemente: "))
a = zeros(n, dtype=int)

for i in range(n):
    print('a[', i, ']=', end=' ')
    a[i] = int(input())
print('Sirul dat este: ', a)

for i in range(n):
    minim = a[i]
    ind_min = i
    for j in range(i+1, n):
        if a[j] < minim:
            minim = a[j]
            ind_min = j
    a[ind_min] = a[i]
    a[i] = minim
print('Sirul ordonat este: ', a)