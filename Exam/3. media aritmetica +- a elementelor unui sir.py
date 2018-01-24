"""media aritmetica +- a elementelor unui sir"""

sir = [2, 4, 2, 4, -33, -22, -11]
suma_termeni_pozitiv = 0
suma_termeni_negativ = 0
nr_elemente_pozitive = 0
nr_elemente_negative = 0

for i in sir:
    if i > 0:
        suma_termeni_pozitiv += i
        nr_elemente_pozitive += 1
    else:
        suma_termeni_negativ += i
        nr_elemente_negative += 1
print("media aritmetica a termenilor pozitivi este ", suma_termeni_pozitiv / nr_elemente_pozitive)

print("media aritmetica a termenilor negative este ", suma_termeni_negativ / nr_elemente_negative)