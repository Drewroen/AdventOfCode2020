f = open("Day3.txt", "r")

lines = list(f.read().split('\n'))

pos = 0
trees = 0
for line in lines:
    if line[pos:pos+1] == '#':
        trees = trees + 1
    pos = (pos + 3) % len(line)

print(trees)