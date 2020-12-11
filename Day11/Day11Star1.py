import json
import copy

f = open("Day11.txt", "r")

rows = list(map(lambda row: list(row), list(f.read().split('\n'))))

new_rows = copy.deepcopy(rows)
started = False

count_temp = 0

while started is not True or json.dumps(new_rows) != json.dumps(rows) and count_temp < 4:
    # count_temp = count_temp + 1
    for i in new_rows:
        print(i)
    print("----")
    started = True
    rows = copy.deepcopy(new_rows)
    for i in range(0, len(rows)):
        for j in range(0, len(rows[i])):
            if rows[i][j] == 'L':
                empty = True
                try:
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if i + k < len(rows) and i + k >= 0 and j + l >= 0 and j + l < len(rows[0]): 
                                if rows[i+k][j+l] not in ['L', '.'] and not (k == 0 and l == 0):
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
                        if i + k < len(rows) and i + k >= 0 and j + l >= 0 and j + l < len(rows[0]): 
                            try:
                                if rows[i+k][j+l]=='#':
                                    empty = empty + 1
                            except:
                                empty = empty
                if empty >= 5:
                    new_rows[i][j] = 'L'
count = 0
for i in json.dumps(new_rows): 
    if i == '#': 
        count = count + 1

print(count)