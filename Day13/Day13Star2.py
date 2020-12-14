import json
import copy
import math

f = open("Day13.txt", "r")

def generate_pair(values):
    result = {}
    for i in range(len(values)):
        if values[i] != 'x':
            temp = int(values[i])
            result[i] = temp
    return result

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

text = list(f.read().split('\n'))

wait = int(text[0])

times = generate_pair(text[1].split(','))

val = 1

while True:
    increment = 1
    for bus_row, bus_time in times.items():
        while(True):
            if (val + bus_row) % bus_time == 0:
                break;
            val += increment
        increment = lcm(increment, bus_time) 
    print(val)
    break
