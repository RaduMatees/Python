"""PRODUS A 2 POLINOAME"""
from numpy import zeros

c = zeros(20, dtype=int)
a = zeros(20, dtype=int)
b = zeros(20, dtype=int)
m = int(input("m="))
n = int(input("n="))

for i in range(0, m):
    print("a[", i, "]=",end=" ")
    a[i] = input()
for i in range(0, n):
    print("b[", i, "]=",end=" ")
    b[i] = input()
for i in range(0, m + n):
    c[i] = 0
for i in range(0, m):
    for j in range(0, n):
        c[i + j] = c[i + j] + a[i] * b[j]
for k in range(0, m + n-1):
    print(c[k])