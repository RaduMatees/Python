def Euclid(d, i):
    while (i != 0):
        r = d % i
        d = i
        i = r
    return d

print(Euclid(18, 15))