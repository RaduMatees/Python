"""Calculul inverselor nr.naturale cu recursivitate"""

def suma_rec(K):
    s = 0
    if K == 1:
        return 1
    else:
        s = 1 / K + suma_rec(K-1)
        return s
n = int(input('n= '))
print('Suma inverselor este', suma_rec(n))