var = input()
var = list(map(int, var.split()))
machines = []
for _ in range(var[0]-1):
    machines.append(int(input()))

result = 0
power = 2
for base in machines:
    print(base, power)
    result += base*(var[1]**power)
    power += 1

print(result%var[2])