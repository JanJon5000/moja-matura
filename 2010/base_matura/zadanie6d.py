with open('zadanie6.txt', 'a') as fileSave:
    fileSave.write('d)\n')
with open('mamy.txt') as fileMothers:
    mothers = {}
    for _ in range(174):
        mom = fileMothers.readline().split()
        mothers[mom[0]] = mom[1]
with open('noworodki.txt') as fileNewBorns:
    for _ in range(180):
        baby = fileNewBorns.readline().split()
        if baby[2] == mothers[baby[-1]]:
            print(baby[2], baby[3])
            with open('zadanie6.txt', 'a') as fileSave:
                fileSave.write(baby[2] + ' ' + baby[3] + '\n')