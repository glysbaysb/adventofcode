northSouthAxisWaypoint = 1
eastWestAxisWaypoint = 10

shipNS = 0
shipEW = 0

for line in open('input'):
    action = line[0]
    val = int(line[1:])

    if action == 'N':
        northSouthAxisWaypoint += val
    elif action == 'S':
        northSouthAxisWaypoint -= val
    elif action == 'E':
        eastWestAxisWaypoint += val
    elif action == 'W':
        eastWestAxisWaypoint -= val
    elif action == 'L':
    elif action == 'R':
        if val == 90:
            tmp = northSouthAxisWaypoint
            northSouthAxisWaypoint = eastWestAxisWaypoint
            eastWestAxisWaypoint = tmp
        elif val = 270:
            tmp = northSouthAxisWaypoint
            northSouthAxisWaypoint = eastWestAxisWaypoint
            eastWestAxisWaypoint = tmp

    elif action == 'F':
        shipNS += val * northSouthAxisWaypoint
        shipEW += val * eastWestAxisWaypoint


print(abs(shipNS - northSouthAxisWaypoint) + abs(shipEW - eastWestAxisWaypoint))
