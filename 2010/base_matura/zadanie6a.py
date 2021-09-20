with open('noworodki.txt', 'r') as file:
    maxBoy, maxGirl = [0, None], [0, None]
    for _ in range(180):
        line = file.readline().split()
        if line[1] == 's' and int(line[-2]) > int(maxBoy[0]):
            maxBoy[0] = line[-2]
            maxBoy[1] = line[2]
        if line[1] == 'c' and int(line[-2]) > int(maxGirl[0]):
            maxGirl[0] = line[-2]
            maxGirl[1] = line[2]

    print('najwyzszy chlopiec', maxBoy[1], maxBoy[0])
    print('najwyzsza dziewczynka', maxGirl[1], maxGirl[0])
    with open('zadanie6.txt', 'a') as fileSave:
        fileSave.write('a)\n')
        fileSave.write('najwyzszy chlopiec ' + str(maxBoy[1]) + ' ' + str(maxBoy[0]) + '\n')
        fileSave.write('najwyzszy chlopiec ' + str(maxGirl[1]) + ' ' + str(maxGirl[0]) + '\n')