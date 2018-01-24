"""Ordonare crescatoare de numere intregi cu metoda numararii"""
from numpy import zeros

n = int(input("n= "))
a = zeros((n), dtype = int)

for i in range(0, n):
    print ("a[", i, "]= ",end = " ")
    a[i] = int(input())
print ("Sirul dat este: ",a)

for i in range(0, n-1):
    for j in range(i+1, n):
        if a[i] > a[j]:
            aux = a[i]
            a[i] = a[j]
            a[j] = aux

print("Sirul ordonat este: ",a)