""" Puncte SA """
from numpy import zeros

m = int(input('m='))
n = int(input('n='))
a = zeros((m, n), dtype=int)

def Sa(a, i, j):
    maxim = True
    minim = True
    for k in range(0, n):
        if a[i,k] < a[i,j]:
            minim = False
    for k in range(0, m):
        if a [k,j] > a[i,j]:
            maxim = False
    if (minim and maxim):
        return True
    else:
        return False

print("Dati matricea a")

for i in range(0, m):
    for j in range(0, n):
        print('a[', i, j,']=', end=' ')
        a[i, j] = input()

print("Matricea data este")

print(a)

print("Punctele SA se afla pe pozitiile", end=' ')

for i in range(0, m):
    for j in range(0, n):
        if Sa(a, i, j):
            print("(", i, ",", j, ")", end=' ')