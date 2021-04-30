with open('zadanie02.txt', 'r') as file:
    howManyMeetTheCondition = 0
    beyondDecimal = {letter : ['a', 'b', 'c', 'd', 'e', 'f'].index(letter)+10 for letter in ['a', 'b', 'c', 'd', 'e', 'f']}
    for _ in range(1000):
        line = file.readline().split()
        for index in range(0, 2):
            line[index] = line[index].split('(')
            line[index][1] = line[index][1].replace(')', '')
            for character in line[index][0]:
                try:
                    if int(character, int(line[index][1])) > int(line[index][1]):
                        howManyMeetTheCondition += 1
                        break
                except ValueError:
                    if beyondDecimal[character] > int(line[index][1]):
                        howManyMeetTheCondition += 1
                        break           
print(howManyMeetTheCondition)