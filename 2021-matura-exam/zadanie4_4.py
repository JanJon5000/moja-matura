import string
with open('instrukcje.txt', 'r') as file:
    ourSTR = []
    lettersToSqap = list(string.ascii_uppercase)
    lettersToSqap.append('A')
    dictionary = {}
    for letter in range(1, len(lettersToSqap)):
        dictionary[lettersToSqap[letter - 1]] = lettersToSqap[letter]
    lettersToSqap = dictionary; del dictionary
    for _ in range(2000):
        line = file.readline().split()
        if line[0] == 'USUN':
            del ourSTR[-1]
        elif line[0] == 'DOPISZ':
            ourSTR.append(line[1])
        elif line[0] == 'ZMIEN':
            ourSTR[-1] = line[1]
        elif line[0] == 'PRZESUN':
            if line[1] in ourSTR:
                for letter in ourSTR:
                    if letter == line[1]:
                        ourSTR[ourSTR.index(letter)] = lettersToSqap[line[1]]
                        break
print(''.join(ourSTR))
