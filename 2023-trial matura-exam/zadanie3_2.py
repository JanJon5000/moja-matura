from pprint import pprint
with open('dane3.txt') as file:
    lenghtFrequency = {}
    lenght = []
    for _ in range(2023):
        line = file.readline().replace('\n', '').split()
        lenght.append(int(line[1]) - int(line[0]) + 1)

    for element in lenght:
        if element in lenghtFrequency.keys():
            lenghtFrequency[element] += 1
        else:
            lenghtFrequency[element] = 1
pprint(lenghtFrequency)
lenght = max(list(lenghtFrequency.values()))
with open('zadanie3_2.txt', 'w') as file:
    for element in lenghtFrequency.keys():
        if lenghtFrequency[element] == lenght:
            file.write(str(element) + '\n')
            print(element)