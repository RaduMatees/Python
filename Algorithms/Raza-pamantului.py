"""Lungimea razei Pamantului"""
from math import sin, pi
from numpy import zeros
beta = zeros(10)
h = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
alfa = [2.0, 2.9, 3.5, 4.1, 4.5, 5.0, 5.4, 5.7, 6.1, 6.4]
for i in range(0, 10):
    beta[i] = 90 - alfa[i]
    print("Raza pamantului pentru inaltimea ", h[i], "este",
          format((h[i] * sin(beta[i] * pi / 180)) / (1 - sin(beta[i] * pi / 180)), '.2f'), "km")
