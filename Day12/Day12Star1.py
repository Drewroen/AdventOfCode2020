import json
import copy

f = open("Day12.txt", "r")

text = list(f.read().split('\n'))

dir = 1
n = 0
w = 0

for val in text:
    if val[0:1] == 'W':
        w = w + int(val[1:])
    elif val[0:1] == 'E':
        w = w - int(val[1:])
    elif val[0:1] == 'N':
        n = n + int(val[1:])
    elif val[0:1] == 'S':
        n = n - int(val[1:]) 
    elif val[0:1] == 'L':
        dir = (dir - (int(val[1:]) / 90) + 4) % 4
    elif val[0:1] == 'R':
        dir = (dir + (int(val[1:]) / 90) + 4) % 4
    elif val[0:1] == 'F':
        if dir == 0:
            n = n + int(val[1:])
        if dir == 1:
            w = w - int(val[1:])
        if dir == 2:
            n = n - int(val[1:])
        if dir == 3:
            w = w + int(val[1:])

print(abs(n) + abs(w))