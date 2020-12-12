northSouthAxis = 0
eastWestAxis = 0
facing = 90
for line in open('input'):
    action = line[0]
    val = int(line[1:])

    if action == 'N':
        northSouthAxis += val
    elif action == 'S':
        northSouthAxis -= val
    elif action == 'E':
        eastWestAxis += val
    elif action == 'W':
        eastWestAxis -= val
    elif action == 'L':
        facing -= val
    elif action == 'R':
        facing += val
    elif action == 'F':
        while facing > 360:
            facing -= 360
        while facing < 0:
            facing += 360
            
        if facing == 0 or facing == 360:
            northSouthAxis += val
        elif facing == 180:
            northSouthAxis -= val
        elif facing == 90:
            eastWestAxis += val
        elif facing == 270:
            eastWestAxis -= val


print(northSouthAxis, eastWestAxis, abs(northSouthAxis) + abs(eastWestAxis))
