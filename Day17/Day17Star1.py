f = open("Day17.txt", "r")

rules = f.read().split('\n')

def coords_to_string(x, y, z):
    return str(x)+","+str(y)+","+str(z)

active_cells = set()

size = len(rules)

for i in range(len(rules)):
    for j in range(len(rules[i])):
        if rules[i][j] == '#':
            active_cells.add(coords_to_string(i, j, 0))

for turn in range(0, 6):
    new_cells = set()
    for i in range(-(turn + size + 1), turn + size + 1):
        for j in range(-(turn + size + 1), turn + size + 1):
            for k in range(-(turn + size + 1), turn + size + 1):
                count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        for z in range(-1, 2):
                            if x == 0 and y == 0 and z == 0:
                                continue
                            else:
                                coord_string = coords_to_string(i+x, j+y, k+z)
                                if coord_string in active_cells:
                                    count += 1
                if count == 3 or (count == 2 and coords_to_string(i, j, k) in active_cells):
                    new_cells.add(coords_to_string(i, j, k))
    active_cells = new_cells.copy()

print(len(new_cells))