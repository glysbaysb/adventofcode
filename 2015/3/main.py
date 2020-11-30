def change(c, location):
    if c == '^':
        return (location[0]+1, location[1])
    elif c == '<':
        return (location[0], location[1]-1)
    elif c == '>':
        return (location[0], location[1]+1)
    elif c == 'v':
        return (location[0]-1, location[1])

santaLocation = (0, 0)
robotLocation = (0, 0)
allHouses = {santaLocation}

for line in open('input'):
    for idx, c in enumerate(line, start=0):
        if idx % 2 == 0:
            santaLocation = change(c, santaLocation)
            allHouses.add(santaLocation)
        else:
            robotLocation = change(c, robotLocation)
            allHouses.add(robotLocation)
    print(len(allHouses))
