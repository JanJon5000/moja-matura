def compare_two_pairs(pair1, pair2):
    if int(pair1[0]) < int(pair2[0]):
        return pair1
    if len(pair1[1]) > len(pair2[1]):
        maxLen = len(pair1[1])
    else:
        maxLen = len(pair2[1])
    for index in range(maxLen):
        if pair1[1][index] == pair2[1][index]:
            pass
        elif pair1[1][index] < pair2[1][index]:
            return pair1
        elif pair1[1][index] > pair2[1][index]:
            return pair2
with open('pary.txt') as file:
    listOfLines = []
    with open('wyniki4.txt', 'a') as filesave:
        filesave.write('\nZadanie 4.3\n')
    for _ in range(100):
        line = file.readline().split()
        if int(line[0]) == len(line[1]):
            listOfLines.append(line)
    minLine = listOfLines[0]
    print(listOfLines)
    for element in listOfLines:
        minLine = compare_two_pairs(minLine, element)
    print(minLine)