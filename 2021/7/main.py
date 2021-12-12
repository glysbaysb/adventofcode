import math

crabs = []
for line in open('input'):
    crabs = [int(x) for x in line.split(',')]

pos, cnt = -1, 999999999
for i in range(max(crabs)):
    tmp = 0
    for crab in crabs:
        tmp = tmp + sum(range(abs(i - crab) + 1))
    if tmp < cnt:
        pos = i
        cnt = tmp
    print(i, tmp)
print(pos, cnt)
