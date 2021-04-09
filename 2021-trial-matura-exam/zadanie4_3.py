with open('C:\\VSCODE\zadania szkolne\\my-matriculation-tasks-\\2021-trial-matura-exam\\galerie.txt', 'r') as file:
    listOfVariantsWhichAlreadyAppeared = []
    CityCentreWithMaxVariants = {'city': None, 'variants':0}
    CityCentreWithMinVariants = {'city': None, 'variants':100}
    for _ in range(50):
        line = file.readline()
        line = line.split(' ')
        listOfVariantsWhichAlreadyAppeared = []
        for index in range(3, len(line), 2):
            area = int(line[index-1])*int(line[index])
            if area not in listOfVariantsWhichAlreadyAppeared and area != 0:
                listOfVariantsWhichAlreadyAppeared.append(area)

        if len(listOfVariantsWhichAlreadyAppeared) > CityCentreWithMaxVariants['variants']:
            CityCentreWithMaxVariants['variants'] = len(listOfVariantsWhichAlreadyAppeared)
            CityCentreWithMaxVariants['city'] = line[1]
        if len(listOfVariantsWhichAlreadyAppeared) < CityCentreWithMinVariants['variants']:
            CityCentreWithMinVariants['variants'] = len(listOfVariantsWhichAlreadyAppeared)
            CityCentreWithMinVariants['city'] = line[1]

with open('wynik4_3.txt', 'w') as file:
    print('\t miasto o najwiekszej liczbie rodzajow lokali -',CityCentreWithMaxVariants['city'] +', liczba lokali -', CityCentreWithMaxVariants['variants'])
    print('\t miasto o najmniejszej liczbie rodzajow lokali -',CityCentreWithMinVariants['city'] + ', liczba lokali -', CityCentreWithMinVariants['variants'])

    file.write('Zadanie C\n')
    file.write('\tmiasto o najwiekszej liczbie rodzajow lokali - ' + CityCentreWithMaxVariants['city'] + ', liczba lokali - ' + str(CityCentreWithMaxVariants['variants']) + '\n')
    file.write('\tmiasto o najmniejszej liczbie rodzajow lokali - ' + CityCentreWithMinVariants['city'] + ', liczba lokali - ' + str(CityCentreWithMinVariants['variants']) + '\n')
