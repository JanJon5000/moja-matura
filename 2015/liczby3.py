maxNum = 0
minNum = 100000000000000
with open('liczby.txt') as file:
    for i in range(1000):
        line = int(file.readline().replace('\n', ''), 2)
        if line > maxNum:
            maxNum = line
            maxIndex = i + 1
        if line < minNum:
            minNum = line
            minIndex = i + 1

print(maxIndex, minIndex)