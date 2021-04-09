with open('galerie.txt', 'r') as file:
    countries = dict()
    for _ in range(50):
        line = file.readline()
        line = line.split(' ')
        if line[0] not in countries:
            countries[line[0]] = 1
        else:
            countries[line[0]] += 1

with open('wynik4_1.txt', 'w') as file:

    file.write('Zadanie A\n')
    file.write('\tKraj '+' - '+' ilosc centrow handlowych\n')
    for key in countries:
        file.write('\t' + str(key) + ' - ' + str(countries[key]) + '\n')

    print('Kraj', '-','ilość centrów handlowych\n')
    for key in countries:
        print('\t',key,'-',countries[key])