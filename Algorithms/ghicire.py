"""Ghicirea unui numar generat aleator intre 1 si 1000"""
from random import randint
numar = randint(1,1000)
ghici = int(input("Introduceti un numar intreg "))
contor = 1
while ghici != numar:
    if ghici > numar: print("Numarul tau este mai mare ")
    else: print("Numarul tau este mai mic ")
    ghici = int(input("Introduceti alt numar "))
    contor += 1
print ("Ati ghicit numarul din ",contor, "incercari")