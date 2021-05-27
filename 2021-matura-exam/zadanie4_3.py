with open('instrukcje.txt', 'r') as file:
    dictionaryOfLetters = { letter : 0 for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']}
    for _ in range(2000):
        line = file.readline().split()
        if line[0] == 'DOPISZ':
            try:
                print(int(line[1]))
            except:
                dictionaryOfLetters[line[1].lower()] += 1
        else:
            pass
    for key in dictionaryOfLetters.keys():
        if dictionaryOfLetters[key] == max(dictionaryOfLetters.values()):
            maxLetter = [key, dictionaryOfLetters[key]]
with open('wyniki4.txt', 'a') as file:
    print(f'{maxLetter[0]}, {maxLetter[1]}')
    file.write("\nZadanie 4.3\n\t" + maxLetter[0] + ', ' + str(maxLetter[1]))