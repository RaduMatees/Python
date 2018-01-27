from __future__ import print_function
from numpy import zeros

n = int(input("n="))
m = n
v = zeros((20), dtype = int) # declarerea si initializarea cu 0 a sirului
i = 0
while n != 4:
    v[i] = n
    i = i +1
    if n % 10 == 0:
        n = n//10
    else:
        if n % 10 == 4:
            n = n//10
        else:
            n = n * 2
v[i] = 4
print("Secventa de generare a lui ",m," din 4 este: "),
for k in range(i, -1, -1):
    print(v[k], end = ' ')