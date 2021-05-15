with open('liczby.txt', 'r') as file:
    characters = { 'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15 }
    systemNumbersAndTheirSum = { system : {'sum': 0, 'numberOfThem':0} for system in range(2, 17)}
    for _ in range(100):
        line = file.readline()
        maxNum = max(line)
        try:
            maxNum = characters[maxNum]
        except:
            pass
        maxNum = int(maxNum)
        systemNumbersAndTheirSum[maxNum+1]['numberOfThem'] += 1
        systemNumbersAndTheirSum[maxNum+1]['sum'] += int(line, maxNum+1)
with open('ZAD5_1.txt', 'w') as file:
    file.write('zadanie 5:\n')
    for key in systemNumbersAndTheirSum.keys():
        print(key,'- ilosc liczb -', systemNumbersAndTheirSum[key]['numberOfThem'], 'suma -', systemNumbersAndTheirSum[key]['sum'])
        file.write(str(key) + ' - ilosc liczb - ' + str(systemNumbersAndTheirSum[key]['numberOfThem']) + ' suma - ' + str(systemNumbersAndTheirSum[key]['sum']) + '\n')