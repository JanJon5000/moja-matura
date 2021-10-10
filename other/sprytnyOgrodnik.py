nm = input()
nm = nm.split()
n = int(nm[0])
m = int(nm[1])
listOfBoxes = input().split()
for element in range(len(listOfBoxes)):
    listOfBoxes[element] = int(listOfBoxes[element])
listOfQuestions = []
if len(listOfBoxes) < n:
    for _ in range(n-len(listOfBoxes)):
        listOfBoxes.append(0)

for _ in range(m):
    listOfQuestions.append(input().split())

for question in listOfQuestions:
    index1 = int(question[0])-1
    index2 = int(question[1])
    print(sum(listOfBoxes[index1:index2]))