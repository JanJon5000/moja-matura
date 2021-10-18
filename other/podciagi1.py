with open('dane1_3.txt') as file:
    string = list(map(int, file.read().split()))

max1 = max2 = string[0]

for index in string[1:]:
    max1 = max(index, max2 + index)
    max2 = max(max2, max1)

print(max2)