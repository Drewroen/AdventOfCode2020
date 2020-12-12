import json
import copy

def move_to_waypoint(ship, waypoint):
    ship[0] = ship[0] + waypoint[0]
    ship[1] = ship[1] + waypoint[1]

def rotate_waypoint_right(waypoint):
    new_waypoint = [waypoint[1], 0 - waypoint[0]]
    waypoint[0] = new_waypoint[0]
    waypoint[1] = new_waypoint[1]

def rotate_waypoint_left(waypoint):
    for i in range(3):
        rotate_waypoint_right(waypoint)


f = open("Day12.txt", "r")

text = list(f.read().split('\n'))

ship = [0, 0]
waypoint = [1, -10]

for val in text:
    if val[0:1] == 'W':
        waypoint[1] = waypoint[1] + int(val[1:])
    elif val[0:1] == 'E':
        waypoint[1] = waypoint[1] - int(val[1:])
    elif val[0:1] == 'N':
        waypoint[0] = waypoint[0] + int(val[1:])
    elif val[0:1] == 'S':
        waypoint[0] = waypoint[0] - int(val[1:]) 
    elif val[0:1] == 'L':
        for i in range(round(int(val[1:]) / 90)):
            rotate_waypoint_left(waypoint)
    elif val[0:1] == 'R':
        for i in range(round(int(val[1:]) / 90)):
            rotate_waypoint_right(waypoint)
    elif val[0:1] == 'F':
        for i in range(int(val[1:])):
            move_to_waypoint(ship, waypoint)

    print("----")
    print(ship)
    print(waypoint)

print(abs(ship[0]) + abs(ship[1]))