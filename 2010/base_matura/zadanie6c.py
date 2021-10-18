with open('zadanie6.txt', 'a') as file:
    file.write('\nc)\n')
with open('noworodki.txt') as fileNewBorns:
    babies = {}
    for _ in range(180):
        baby = fileNewBorns.readline().split()
        if baby[-1] not in babies.keys():
            babies[baby[-1]] = [int(baby[-3])]
        else:
            babies[baby[-1]].append(int(baby[-3]))

with open('mamy.txt') as fileMoms:
    for _ in range(174):
        mom = fileMoms.readline().split()
        if int(mom[-1]) < 25 and max(babies[mom[0]]) > 4000:
            print(mom[1])
            with open('zadanie6.txt', 'a') as file:
                file.write(mom[1] + '\n')