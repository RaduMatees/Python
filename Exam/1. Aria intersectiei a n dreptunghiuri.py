"""Aria intersectiei a n dreptunghiuri """
from numpy import zeros

n = int(input("n="))
XSS = zeros((n), dtype=float)
YSS = zeros((n), dtype=float)
XDJ = zeros((n), dtype=float)
YDJ = zeros((n), dtype=float)

for i in range(0, n):
    print('XSS[', i, ']=')
    XSS[i] = float(input())
    print('YSS[', i, ']=')
    YSS[i] = float(input())
    print('XDJ[', i, ']=')
    XDJ[i] = float(input())
    print('YDJ[', i, ']=')
    YDJ[i] = float(input())

Xstanga = XSS[0]
Xdreapta = XDJ[0]
Yjos = YDJ[0]
Ysus = YSS[0]

for i in range(0, n):
    if Xstanga < XSS[i]:
        Xstanga = XSS[i]
    if Xdreapta > XDJ[i]:
        Xdreapta = XDJ
    if Yjos < YDJ[i]:
        Yjos = YDJ[i]
    if Ysus > YSS[i]:
        Ysus = YSS[i]
if((Xdreapta<Xstanga)or(Ysus<Yjos)):
    print("intersectie vida")
else:
    Aria = (Xdreapta-Xstanga)*(Ysus-Yjos)
    print("Aria=", format(Aria, '.2f'))