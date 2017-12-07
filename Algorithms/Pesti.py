"""problema cu pesti"""
"""Pescarii estimeaza marimea pestiilor dintr-un lac dupa legea lui Bertalanffy:
L=Lmax(1-e**{-k(t+"tau")})  unde Lmax = lungimea maxima (58cm) , k = o rata constanta(0,45),
 constanta "tau" = 0,65.
    Sa estimam marimea pestilor din populatia respectiva la 0, 1, 2 , ... , 15 ani"""
from math import e
Lmax = 58
K = 0.45
tau = 0.65
a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for t in a:
    print("Lungimea pestelui la ",t,"ani este: ",format(Lmax*(1-e**(-K*(t+tau))), '.2f'),"cm")