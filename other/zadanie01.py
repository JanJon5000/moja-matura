with open('zadanie01.txt', 'r') as file:
    howManyMeetTheCondition = 0
    for _ in range(1000):
        line = file.readline().split()
        line[0] = line[0].split('(')
        line[1] = line[1].split('(')
        if int(line[0][0].upper(), int(line[0][1].replace(')', ''))) > int(line[1][0].upper(), int(line[1][1].replace(')', ''))):
            howManyMeetTheCondition += 1
print(howManyMeetTheCondition)