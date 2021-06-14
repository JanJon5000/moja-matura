def is_even(num):
    if num <= 1:
        return False
    for n in range(2, num):
        if num % n == 0 and num != 2:
            return False
    return True

def find_the_sum(number):
    listOfPossibilities = []
    for num in range(2, number):
        if is_even(number - num) and is_even(num):
            listOfPossibilities.append((num, number - num))
    return listOfPossibilities[0]

with open('pary.txt') as file:
    with open('wyniki4.txt', 'w') as filesave:
        filesave.write('Zadanie 4.1\n')
    for _ in range(100):
        line = file.readline().split()
        if int(line[0]) % 2 == 0:
            print(line[0], find_the_sum(int(line[0]))[0], find_the_sum(int(line[0]))[1])
            with open('wyniki4.txt', 'a') as filesave:
                filesave.write('\t' + str(line[0]) + ' ' + str(find_the_sum(int(line[0]))[0]) + ' ' + str(find_the_sum(int(line[0]))[1]) + '\n')
