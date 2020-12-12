sequence = []
for line in open('input'):
    sequence.append(int(line))

for i in range(25, len(sequence)):
    combinations = []
    for j in range(25, 0, -1):
        for k in range(j, 0, -1):
            combinations.append(sequence[i - j] + sequence[i - j + k])
    if sequence[i] not in combinations:
        answer = sequence[i]
        maxIndex = i
        break

for i in range(maxIndex):
    res = minNum = maxNum  = sequence[i]
    for j in range(i+1, maxIndex):
        if sequence[j] < minNum:
            minNum = sequence[j]
        if sequence[j] > maxNum:
            maxNum = sequence[j]

        res += sequence[j]
        if res == answer:
            print("part 2 ", minNum + maxNum, minNum, maxNum)
        elif res > answer:
            break
