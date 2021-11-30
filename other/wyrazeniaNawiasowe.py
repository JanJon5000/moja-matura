with open('dane2_3.txt') as file2_3:
    for _ in range(50):
        depth = 0
        maxDepth = 0
        line = file2_3.readline().replace('\n', '')
        for index in line:
            if index == '[':
                depth+=1
            else:
                depth-=1
            maxDepth = max(depth, maxDepth)
        print(line, maxDepth)
        with open('zadanie2_3.txt', 'a') as fileSave:
            fileSave.write(line + ' ' + str(maxDepth) + '\n')

with open('dane2_4.txt') as file2_4:
    for _ in range(50):
        sumBrackets = 0
        line = file2_4.readline().replace('\n', '')
        if line[0] == '[' and line[-1] == ']':
            for index in line:
                if index == '[':
                    sumBrackets+=1
                else:
                    sumBrackets-=1
        else:
            continue
        if sumBrackets == 0:
            print('tak')
            with open('zadanie2_4.txt', 'a') as fileSave:
                fileSave.write(line + 'tak\n')
        else:
            print('nie')
            with open('zadanie2_4.txt', 'a') as fileSave:
                fileSave.write(line + 'nie\n')
