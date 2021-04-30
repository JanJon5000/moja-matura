with open('zadanie02.txt', 'r') as file:
    howManyMeetTheCondition = 0
    beyondDecimal = {letter : ['a', 'b', 'c', 'd', 'e', 'f'].index(letter)+10 for letter in ['a', 'b', 'c', 'd', 'e', 'f']}
    for _ in range(1000):
        line = file.readline().split()
        for index in range(0, 2):
            line[index] = line[index].split('(')
            line[index][1] = line[index][1].replace(')', '')
            maxCharacter = max(line[index][0])
            try:
                maxCharacter = beyondDecimal[maxCharacter]
            except:
                pass
            if int(maxCharacter) >= int(line[index][1]):
                howManyMeetTheCondition += 1
                break
print(howManyMeetTheCondition)