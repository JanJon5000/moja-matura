babies = {}; counterBabies = {}
with open('C:\\VSCODE\\my-matriculation-tasks-\\2010\\base_matura\\noworodki.txt', 'r') as file:
    for _ in range(180):
        line = file.readline().split()
        if line[3] in babies.keys():
            babies[line[3]] += 1
        else:
            babies[line[3]] = 1
for key in babies.keys():
    counterBabies[babies[key]] = key

print(counterBabies[max(counterBabies.keys())],max(counterBabies.keys()))
with open('zadanie6.txt', 'a') as file:
    file.write('b)\n' + str(counterBabies[max(counterBabies.keys())]) + ' ' + str(max(counterBabies.keys())))