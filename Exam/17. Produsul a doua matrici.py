"""Produsul a 2 matrici """
from numpy import zeros

m = int(input("m="))
n = int(input("n="))
p = int(input("p="))
a = zeros((m, n), dtype=float)
b = zeros((n, p), dtype=float)
c = zeros((m, p), dtype=float)

print("dati matricea A ")

for i in range(m):
    for j in range(n):
        print("a[", i, j, "]=", end=" ")
        a[i, j]=input()
print("dati matricea B ")

for i in range(n):
    for j in range(p):
        print("b[", i, j, "]=", end=" ")
        b[i, j] = input()

for i in range(m):
    for j in range(p):
        for k in range(n):
            c[i, j]=c[i, j]+a[i, k]*b[k, j]
print("matricea A este ")
print(a)
print("matricea B este")
print(b)
print("matricea produs c este ")
print(c)