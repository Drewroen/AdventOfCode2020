import functools

f = open("Day3.txt", "r")
lines = list(f.read().split('\n'))

positions = [0, 0, 0, 0, 0]
trees = [0, 0, 0, 0, 0]
check_line = True
for line in lines:
    for val in range(len(positions)):
        if line[positions[val]:positions[val]+1] == '#' and (val != 4 or check_line == True):
            trees[val] = trees[val] + 1
    
    positions[0] = (positions[0] + 1) % len(line)
    positions[1] = (positions[1] + 3) % len(line)
    positions[2] = (positions[2] + 5) % len(line)
    positions[3] = (positions[3] + 7) % len(line)
    if check_line == False:
        positions[4] = (positions[4] + 1) % len(line)
    check_line = not check_line

print(functools.reduce(lambda a, b: a * b, trees))