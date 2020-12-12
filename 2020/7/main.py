answers = set()
def findGolden(bags, startPoint):
    if startPoint == 'shiny gold':
        return 1
    count = 0
    for color in bags[startPoint]:
        res = findGolden(bags, color)
        if res > 0:
            answers.add(startPoint)
            count += res
    return count

bags = {}
for line in open('input'):
    parts = line.split()
    thisBag = parts[0] + ' ' + parts[1]
    contentCount = int((len(parts) - 4) / 4)
    content = []

    for x in range(contentCount):
        content.append(parts[5 + x*4] + ' ' + parts[5 + x*4 + 1])

    bags[thisBag] = content

for color in bags:
    findGolden(bags, color)
print(len(answers))
