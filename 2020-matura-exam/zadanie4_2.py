with open('wyniki4.txt', 'a') as filesave:
    filesave.write('\nZadanie 4.2\n')
with open('pary.txt', 'r') as file:
    for _ in range(100):
        line = file.readline().split()
        lenght = 1
        string = line[1][0]
        currentLenght = 1; currentLetter = None
        for index in line[1]:
            if index == currentLetter:
                currentLenght+=1
            else:
                if currentLenght > lenght:
                    lenght = currentLenght
                    string = currentLetter
                currentLetter = index
                currentLenght = 1
        properString = str()
        for _ in range(lenght):
            properString += string
        print(properString, lenght)
        with open('wyniki4.txt', 'a') as filesave:
            filesave.write('\t' + properString + ' ' + str(lenght) + '\n')