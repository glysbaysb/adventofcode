vents = []
for line in open('input'):
    tmp = line.strip().split(' -> ')
    frm = [int(x) for x in tmp[0].split(',')]
    to = [int(x) for x in tmp[1].split(',')]
    vents.append((frm, to))
X, Y = 1000, 1000
world = [[0 for x in range(X)] for y in range(Y)]
for vent in vents:
    if not (vent[0][0] == vent[1][0] or vent[0][1] == vent[1][1]):
        continue
    if (vent[0][0] == vent[1][0] and vent[0][1] == vent[1][1]):
        x = vent[0][0]
        y = vent[0][1]
        world[y][x] = world[y][x] + 1
        continue

    if vent[0][0] == vent[1][0]:
        x = vent[0][0]
        if vent[0][1] < vent[1][1]:
            for y in range(vent[0][1], vent[1][1]+1):
                world[y][x] = world[y][x] + 1
        else:
            for y in range(vent[0][1], vent[1][1]-1, -1):
                world[y][x] = world[y][x] + 1
    else:
        y = vent[0][1]
        if vent[0][0] < vent[1][0]:
            for x in range(vent[0][0], vent[1][0]+1):
                world[y][x] = world[y][x] + 1
        else:
            for x in range(vent[0][0], vent[1][0]-1, -1):
                world[y][x] = world[y][x] + 1

cnt = 0
for y in range(Y):
    for x in range(X):
        if world[y][x] >= 2:
            cnt = cnt + 1
print(cnt)
