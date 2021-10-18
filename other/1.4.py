def get_sum(sequence):
    maxSUM = -10000000000
    currentSUM = 0
    indexes = [None, None]

    for index in range(len(sequence)):
        currentSUM += sequence[index]

        if currentSUM > 0:
            if currentSUM > maxSUM:
                maxSUM = currentSUM
                indexes[1] = index
        else:
            currentSUM = 0
            indexes[0] = index + 1
            indexes[1] = index + 1
    return indexes

with open('dane1_4.txt') as file:
    sequence1 = []
    for _ in range(100000):
        sequence1.append(int(file.readline()))
    print(get_sum(sequence1))