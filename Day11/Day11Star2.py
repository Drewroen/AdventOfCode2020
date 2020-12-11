import json
import copy

f = open("Day11.txt", "r")

def within_bounds(val1, val2, rows):
    return val1 >= 0 and val1 < len(rows) and val2 >= 0 and val2 < len(rows[0])

rows = list(map(lambda row: list(row), list(f.read().split('\n'))))

new_rows = copy.deepcopy(rows)
started = False

while started is not True or json.dumps(new_rows) != json.dumps(rows) and count_temp < 4:
    started = True
    rows = copy.deepcopy(new_rows)
    for i in range(0, len(rows)):
        for j in range(0, len(rows[i])):
            if rows[i][j] == 'L':
                empty = True
                try:
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if k != 0 or l != 0:
                                tempx = i + k
                                tempy = j + l
                                empty_sight = 0
                                while within_bounds(tempx, tempy, rows) and empty_sight == 0:
                                    if rows[tempx][tempy] == 'L':
                                        empty_sight = 1
                                    elif rows[tempx][tempy] == '#':
                                        empty_sight = -1
                                    tempx = tempx + k
                                    tempy = tempy + l
                                if empty_sight == -1:
                                    empty = False
                except:
                    empty = empty
                
                if empty is True:
                    new_rows[i][j] = '#'
                else:
                    new_rows[i][j] = 'L'
            elif rows[i][j] == '#':
                empty = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        tempx = i + k
                        tempy = j + l
                        empty_sight = 0
                        while within_bounds(tempx, tempy, rows) and empty_sight == 0:
                            if rows[tempx][tempy] == 'L':
                                empty_sight = 1
                            elif rows[tempx][tempy] == '#':
                                empty_sight = -1
                            tempx = tempx + k
                            tempy = tempy + l
                        if empty_sight == -1:
                            empty = empty + 1
                            if i == 0 and j == 8:
                                print(k, l)
                if empty >= 6:
                    new_rows[i][j] = 'L'
count = 0
for i in json.dumps(new_rows): 
    if i == '#': 
        count = count + 1

print(count)