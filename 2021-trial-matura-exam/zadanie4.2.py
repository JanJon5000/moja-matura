with open('galerie.txt') as file:
    listOfCitiesAndTheirArea = list()
    maxCity = None
    minCity = None
    shoppingCenters = dict()
    shoppingCenters[None] = {'area' : 0}
    for _ in range(50):
        line = file.readline()
        line = line.split(' ')
        city = line[1]
        del line[0]; del line[0]

        area = 0
        shops = 0
        for num in range(1, 140, 2):
            area += int(line[num]) * int(line[num-1])
            if line[num] != '0' and line[num-1] != '0':
                shops+=1
        
        shoppingCenters[city] = {
            'area' : area,
            'shops' : shops
        }
        if shoppingCenters[city]['area'] > shoppingCenters[maxCity]['area']:
            maxCity = city
        if shoppingCenters[city]['area'] < shoppingCenters[minCity]['area'] or shoppingCenters[minCity]['area'] == 0:
            minCity = city   
    del shoppingCenters[None]
########################################
with open('wynik4_2a.txt', 'w') as file:
    print('a)')
    for key in set(shoppingCenters.keys()):
        print(key, shoppingCenters[key]['area'], shoppingCenters[key]['shops'])
    print('b)')
    print('Miasto z centrum handlowym o najwiekszej powierzchni\n', maxCity, '-', shoppingCenters[maxCity]['area'],'\nMiasto z centrum handlowym o najmniejszej powierzchni\n', minCity, '-', shoppingCenters[minCity]['area'])

    file.write('Zadanie B\n')
    file.write('a)\n')
    for key in set(shoppingCenters.keys()):
        file.write('\t' + str(key) + ' ' + str(shoppingCenters[key]['area']) + ' ' + str(shoppingCenters[key]['shops']) + '\n')

with open('wynik4_2b.txt', 'w') as file:
    file.write('Zadanie B\n')
    file.write('b)\n')
    file.write('\tMiasto z centrum handlowym o najwiekszej powierzchni\n\t' + str(maxCity) + '-' + str(shoppingCenters[maxCity]['area']) + '\n\tMiasto z centrum handlowym o najmniejszej powierzchni\n\t' + str(minCity) + '-' + str(shoppingCenters[minCity]['area']))
