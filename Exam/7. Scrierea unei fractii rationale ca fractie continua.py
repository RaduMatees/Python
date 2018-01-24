"""Scrierea unei fractii rationale ca fractie continua"""
p = int(input("p="))
q = int(input("q="))
d = p
i = q
r = 1
print(p, "/", q," = [",end =' ')
while r != 0:
    r = d % i
    c = d // i
    print (c, end=' ')
    d = i
    i = r
print ("]")