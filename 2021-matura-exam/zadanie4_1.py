with open('instrukcje.txt', 'r') as file:
    lenghtOfTheString = 0
    for _ in range(2000):
        line = file.readline()
        line = line.split()
        if line[0] == 'USUN':
            lenghtOfTheString -= 1
        elif line[0] == 'DOPISZ':
            lenghtOfTheString += 1
with open("wyniki4.txt", 'w') as file:
    print(lenghtOfTheString)
    file.write('Zadanie 4.1\n\t' + str(lenghtOfTheString))