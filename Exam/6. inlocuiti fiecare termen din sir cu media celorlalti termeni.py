"""inlocuiti fiecare termen din sir cu media celorlalti termeni"""

s = 0
a = []
n = int(input("n="))

for i in range(n):
    nr = int(input("a["+str(i)+"] = "))
    s += nr
    a.append(nr)

for i in range(len(a)):
    a[i] = (s-a[i]) / (n-1)
    print(a[i], end=" ")