def count(string: str, char: str):
    counter = 0
    for character in string:
        if character == char:
            counter += 1
    return counter

with open('liczby.txt') as file:
    numOfStrings = 0
    for _ in range(1000):
        line = file.readline().replace('\n', '')
        if count(line, '0') > count(line, '1'):
            numOfStrings += 1
    print(numOfStrings)