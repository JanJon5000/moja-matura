with open('zadanie6_3.txt', 'w') as saveFile:
    with open('dane6.txt') as file:
        numOfAntiPalindromes = 0
        for _ in range(2023):
            isAntiPalindrome = True
            line = file.readline().replace('\n', '')
            for index in range(len(line)):
                if line[index] == line[len(line)-index-1]:
                    isAntiPalindrome = False
            if isAntiPalindrome == True:
                numOfAntiPalindromes += 1
                print(line)
                saveFile.write(line + '\n')
    saveFile.write(str(numOfAntiPalindromes))
    print(numOfAntiPalindromes)