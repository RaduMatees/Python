"""Mediile aritmetice a elementelor de Deasupra/Pe/Sub diagonalei principale a matricii A(n,n)"""

from numpy import zeros

n = int(input("n= "))
a = zeros ((n,n), dtype= int)

for i in range (0,n):
    for j in range (0,n):
        print ('a[',i,j,']=')
        a[i,j]=input()
print ('Matricea este')
print (a)

sd, ss, sp= 0.,0.,0.
for i in range (0,n):
    for j in range (0, n):
        if i == j:
            sp = sp + a[i, j]
        elif i<j:
            sd = sd + a[i, j]
        else:
            ss = sd + a[i, j]
print ('Media pe diagonala principala este:',format(sp / n,'.5f'))
print ('Media sub diagonala principala este: ',(ss / ((n*n-n) / 2.),'.5f'))
print ('Media deasupra diagonalei principale este: ')