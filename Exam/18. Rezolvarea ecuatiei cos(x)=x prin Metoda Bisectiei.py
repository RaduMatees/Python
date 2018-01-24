"""Metoda bisectiei (injumatatirii intervalului pentru rezolvarea numerica aproximativa a ecuatiilor"""

from math import cos

def f(x):
    return cos(x)-x

a=float(input('a='))
b=float(input('b='))
eps=float(input('eps='))
c=(a+b)/2.

while abs(b-a) >= eps:
    if f(c)==0:
        print('radacina este ', c)
    elif f(a)*f(c)<0:
        b=c
    else:
        a=c
    c=(a+b)/2.
print ('radacina aproximativa este', format(c,' .5f'))