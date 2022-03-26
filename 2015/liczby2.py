with open('liczby.txt') as file:
    primeNumbers = 0
    numbers8 = 0
    for _ in range(1000):
        line = file.readline().replace('\n', '')
        line = int(line, 10)
        if line % 8 == 0:
            numbers8 += 1
        if line % 2 == 0:
            primeNumbers += 1

print(primeNumbers, numbers8)