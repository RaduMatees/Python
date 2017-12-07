""""Distanta parcursa de un salvamar in cel mai scurt timp"""
from math import sqrt
from numpy import zeros
timpi = zeros (29)

vu = 3
va = 1
ds = 30
dw = 42
L = 48
for y in range(20,49):
    t = sqrt(ds**2+y**2)/vu+sqrt(dw*)