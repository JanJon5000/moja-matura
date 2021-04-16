with open('dane6.txt') as file:
    pSum = {key : {'num':None, 'numSum':0} for key in range(2, 11)}
    for _ in range(2023):
        sumOfNumbers = 0
        p = 2
        line = file.readline()
        line = line.replace('\n', '')
        for character in line:
            if p <= int(character):
                p += 1
            sumOfNumbers += int(character)
        if pSum[p]['numSum'] < sumOfNumbers:
            pSum[p]['num'] = line
            pSum[p]['numSum'] = sumOfNumbers
with open('zadanie6_2.txt', 'w') as file:
    num = 'num'
    for index in range(2, 11):
        print(f'podstawa p - {index} - liczba p-minimalna z najwieksza suma cyfr - {pSum[index][num]}')
        file.write(f'podstawa p - {index} - liczba p-minimalna z najwieksza suma cyfr - {pSum[index][num]}\n')