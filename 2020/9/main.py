sequence = []
for line in open('input'):
    sequence.append(int(line))

for j in range(25, 0, -1):
    for k in range(j, 0, -1):
        print(25 - j, sequence[25  -j], 25 - j + k, sequence[25 - j + k])

for i in range(25, len(sequence)):
    combinations = []
    for j in range(25, 0, -1):
        for k in range(j, 0, -1):
            combinations.append(sequence[i - j] + sequence[i - j + k])
    if sequence[i] not in combinations:
        print(combinations)
        print(i, sequence[i])
        break
