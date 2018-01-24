"""Program pentru afisarea elementelor matricii A(m,n) dupa ordinea data de matricea B(m,n)."""

from numpy import zeros
n=int(input("n="))

a=zeros((n+1,n+1), dtype=int)
for i in range (1,n+1):
    for j in range(1, n+1):
        print("a[",i,"][",j,"]=", end=" ")
        a[i][j]=int(input())

b=zeros((n+1,n+1), dtype=int)
for i in range (1,n+1):
    for j in range(1, n+1):
        print("b[",i,"][",j,"]=", end=" ")
        b[i][j]=int(input())

c=zeros((n*n+1), dtype=int)
k=1
for i in range (1,n+1):
    for j in range(1, n+1):
        c[k]=a[i][j]
        k+=1

for i in range (1,n+1):
    for j in range(1, n+1):
        print (c[ b[i][j] ], end=" ")
    print ("\n")