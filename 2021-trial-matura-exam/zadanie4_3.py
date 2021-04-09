with open('C:\\VSCODE\zadania szkolne\\my-matriculation-tasks-\\2021-trial-matura-exam\\galerie.txt', 'r') as file:
    listOfVariantsWhichAlreadyAppeared = []
    CityCentreWithMaxVariants = {'city': None, 'variants':0}
    CityCentreWithMinVariants = {'city': None, 'variants':100000}
    for _ in range(50):
        line = file.readline()
        line = line.split(' ')
        listOfVariantsWhichAlreadyAppeared = []
        for index in range(3, len(line), 2):
            area = int(line[index-1])*int(line[index])
            if area not in listOfVariantsWhichAlreadyAppeared:
                listOfVariantsWhichAlreadyAppeared.append(area)

        if len(listOfVariantsWhichAlreadyAppeared) > CityCentreWithMaxVariants['variants']:
            CityCentreWithMaxVariants['variants'] = len(listOfVariantsWhichAlreadyAppeared)
            CityCentreWithMaxVariants['city'] = line[1]
        if len(listOfVariantsWhichAlreadyAppeared) < CityCentreWithMinVariants['variants']:
            CityCentreWithMinVariants['variants'] = len(listOfVariantsWhichAlreadyAppeared)
            CityCentreWithMinVariants['city'] = line[1]

print(CityCentreWithMaxVariants)
print(CityCentreWithMinVariants)
