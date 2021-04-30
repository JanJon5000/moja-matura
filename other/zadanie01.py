with open('C:\\VSCODE\\my-matriculation-tasks-\\other\\zadanie01.txt') as file:
    howManyMeetTheCondition = 0
    for _ in range(1000):
        line = file.readline().split()
        line[0] = line[0].split('(')
        line[1] = line[1].split('(')
        print(line)
        if int(line[0][0], int(line[0][1].replace(')', ''))) > int(line[1][0], int(line[1][1].replace(')', ''))):
            howManyMeetTheCondition += 1

print(howManyMeetTheCondition)
        