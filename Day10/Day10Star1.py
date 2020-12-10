f = open("Day10.txt", "r")

vals = list(map(lambda num: int(num), f.read().split('\n')))

print(vals)

vals.sort()

total = 0
total2 = 1
for i in range(1, len(vals)):
    if vals[i] - vals[i-1] == 1:
        total = total + 1
    elif vals[i] - vals[i-1] == 3:
        total2 = total2 + 1

if vals[0] == 1:
    total = total + 1


print(total * total2)
