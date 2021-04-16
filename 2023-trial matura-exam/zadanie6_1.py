with open('C:\\VSCODE\\zadania szkolne\\my-matriculation-tasks-\\2023-trial matura-exam\\dane6.txt') as file:
    pMinimal = {key : 0 for key in range(0, 11)}
    for _ in range(2023):
        p = 2
        line = file.readline()
        line = line.replace('\n', '')
        for character in line:
            if p <= int(character):
                p += 1
        pMinimal[p] += 1
for index in range(2, 11):
    print(f'podstawa p - {index} - liczba liczb p-minimalnych - {pMinimal[index]}')