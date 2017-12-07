'''
5. Se da un sir de caractere. Verificati daca sirul de caractere este palindrom.
'''

myString = input('Introduceti un cuvant: ')
myStringArr = []
palindrom = []

for letter in myString:
    myStringArr.append(letter)

for letterTwo in reversed(myStringArr):
    palindrom.append(letterTwo)

if myStringArr == palindrom:
    print(True)
else:
    print(False)
