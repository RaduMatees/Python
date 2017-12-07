'''
3. Se da o lista de numere naturale. Afisati toate numerele din sir care sunt prime.
'''

numbersArr = [2, 5, 7, 18, 17, 43, 20]

primes = []
for nr in numbersArr:
    div = 2
    while div <= nr:
        if nr == 2:
            primes.append(nr)
            break
        if nr % div != 0:
            div += 1
            if nr == div:
                primes.append(nr)
        else:
            break

print(primes)






