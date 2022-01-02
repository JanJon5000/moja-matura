from os import set_inheritable


def ifItIsAChain(list1, list2):
    # list2 ma sie zaweirac w list1
    if list2[0] > list1[0] and list2[1] < list1[1]:
        return True
    return False

with open('dane3.txt') as file:
    lenghts = {}
    sections = []
    for _ in range(2023):
        line = file.readline().replace('\n', '').split()
        sections.append(line)
        l = int(line[1]) - int(line[0]) + 1
        if l not in lenghts.keys():
            lenghts[l] = [line]
        else:
            lenghts[l].append(line)

maxLen = 0
for element in sections:
    for index in lenghts.keys():
        if element in lenghts[index]:
            start = index

    currentLen = 0
    currentSection = element
    for index in range(start-1, 0, -1):
        try:
            passingSections = {}
            for section in lenghts[index]:
                if ifItIsAChain(currentSection, section):
                    passingSections[section] = 0
                    for element in lenghts.keys():
                        if ifItIsAChain(section, element):
                            passingSections[section] += 1
            biggestFrequency = 0
            for n in passingSections.keys():
                if passingSections[n] > biggestFrequency:
                    biggestFrequency = passingSections[n]
                    currentSection = n
        except KeyError:
            continue
    maxLen = max(maxLen, currentLen)

print(maxLen)