'''
1. Se da un text. Aflati litera care are cele mai multe aparitii in text si afisati aceasta litera.
'''

text = input('Introduceti un text: ')
text = text.lower()
text = text.replace(" ", "")
letters = {}

for character in text:
    if not character in letters:
        letters[character] = 1
    else:
        letters[character] = letters[character] + 1

mostCommonLetter = ''
maximum = 0
for key in letters:
    if letters[key] > maximum:
        maximum += letters[key]
        mostCommonLetter = key

print(mostCommonLetter, maximum)





