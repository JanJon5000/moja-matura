def isPalindrome(text):
    index = 0
    while index < int(len(text)/2):
        if text[index] != text[-index-1]:
            return False
        index+=1
    return True

with open('C:\\VSCODE\\my-matriculation-tasks-\\2010\\base_matura\\dane.txt', 'r') as file:
    for _ in range(1000):
        line = file.readline().replace('\n', '')
        if isPalindrome(line):
            print(line)
            with open('zadanie4.txt', 'a') as fileSave:
                fileSave.write(line + '\n')
