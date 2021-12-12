crabs = []
for line in open('input'):
    crabs = [int(x) for x in line.split(',')]

pos, cnt = -1, 999999
for i in range(max(crabs)):
    tmp = 0
    for crab in crabs:
        tmp = tmp + abs(i - crab)
    if tmp < cnt:
        pos = i
        cnt = tmp
print(pos, cnt)
