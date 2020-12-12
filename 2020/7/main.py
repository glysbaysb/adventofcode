def sumBags(bags, startPoint):
    count = 0
    for color, number in bags[startPoint]:
        count += number + number * sumBags(bags, color)
    return count

bags = {}
for line in open('input'):
    parts = line.split()
    thisBag = parts[0] + ' ' + parts[1]
    contentCount = int((len(parts) - 4) / 4)
    content = []

    for x in range(contentCount):
        content.append((parts[5 + x*4] + ' ' + parts[5 + x*4 + 1],  int(parts[4 + x*4])))

    bags[thisBag] = content

print(sumBags(bags, 'shiny gold'))
