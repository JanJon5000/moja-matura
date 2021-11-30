with open('dane3.txt') as file:
    lenght = []
    for _ in range(2023):
        line = file.readline().replace('\n', '').split()
        lenght.append(int(line[1]) - int(line[0]) + 1)
lenght.sort()
print(lenght[0], lenght[1])
with open('zadanie3_1.txt', 'w') as fileSave:
    fileSave.write(str(lenght[0]) + ' ' + str(lenght[1]))