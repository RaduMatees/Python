from math import sqrt

def calc(m,n,p,q):
    return (m+n*sqrt(p))**q

print(format(calc(5,3,16,2), '.2f'))