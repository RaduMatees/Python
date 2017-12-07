"""Rostogolire zar"""

def rost_dreapta(k):
    global sus, jos, stanga, dreapta, fata, spate
    for i in range(0, k):
        sus, jos, stanga, dreapta = stanga, dreapta, jos, sus

def rost_stanga(k):
    global sus, jos, stanga, dreapta, fata, spate
    for i in range(0, k):
        sus, jos, stanga, dreapta = dreapta, stanga, sus, jos

def rost_fata(k):
    global sus, jos, stanga, dreapta, fata, spate
    for i in range(0, k):
        sus, jos, fata, spate = spate, fata, sus, jos

def rost_spate(k):
    global sus, jos, stanga, dreapta, fata, spate
    for i in range(0, k):
        sus, jos, fata, spate = fata, spate, jos, sus

print('Dati pozitia initiala a zarului:')
sus = int(input('Sus = '))
fata = int(input('Fata = '))
dreapta = int(input('Dreapta = '))
jos = 7 - sus
spate = 7 - fata
stanga = 7 - dreapta

while True:
    dir = str(input('Directia de rostogolire? (st, dr, fa, sp)'))
    k = int(input('Numar de rostogoliri?'))
    if dir == 'st':
        rost_stanga(k)
    if dir == 'dr':
        rost_dreapta(k)
    if dir == 'fa':
        rost_fata(k)
    if dir == 'sp':
        rost_spate(k)

    print('Pozitia zarului este: ')
    print('sus = ', sus)
    print('jos = ', jos)
    print('stanga = ', stanga)
    print('dreapta = ', dreapta)
    print('fata = ', fata)
    print('spate = ', spate)
    cont = str(input('Continuati? D/N'))
    if (cont == 'N') or (cont == 'n'):
     break
