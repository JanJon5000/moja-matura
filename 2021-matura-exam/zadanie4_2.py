with open('instrukcje.txt', 'r') as file:
    longestStreak = ['NOTHING', 0]; currentStreak = ['NOTHING', 0]
    for _ in range(2000):
        line = file.readline().split()
        if line[0] == currentStreak[0]:
            currentStreak[1] += 1
        else:
            if longestStreak[1] < currentStreak[1]:
                longestStreak = currentStreak
            currentStreak = [ line[0], 0 ]
with open('wyniki4.txt', 'a') as file:
    print('najdłuższy ciąg -',longestStreak[0],'o długości',longestStreak[1])
    file.write(f'\nZadanie 4.2\n\t{longestStreak[0]}, {longestStreak[1]}')