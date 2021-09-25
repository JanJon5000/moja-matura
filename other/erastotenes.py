n = int(input('podaj ostatnia liczbe w zbiorze liczb do sprawdzenia'))
listOfNumbers = [_ for _ in range(2, n)]
for index in listOfNumbers:
    for index2 in listOfNumbers:
        if index2 % index == 0 and index!=index2:
            listOfNumbers.pop(listOfNumbers.index(index2))
print(listOfNumbers)