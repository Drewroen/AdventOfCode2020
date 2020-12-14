import json
import copy
import math

f = open("Day13.txt", "r")

text = list(f.read().split('\n'))

wait = int(text[0])

times = text[1].split(',')

diff = -1
bus = -1

for time in times:
    try:
        temp_diff = math.ceil(wait / int(time)) * int(time) - wait
        if diff == -1 or temp_diff < diff:
            diff = temp_diff
            bus = int(time)
    except:
        diff = diff

print(bus * diff)