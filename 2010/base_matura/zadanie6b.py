import pprint
babies = {}
with open('noworodki.txt', 'r') as file:
    for _ in range(180):
        line = file.readline().split()
        if line[3] in babies.keys():
            babies[line[3]] += 1
        else:
            babies[line[3]] = 1
pprint.pprint(babies)