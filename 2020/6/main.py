res = 0
answers = set()

for line in open('input'):
    line = line[:-1]
    if line == '':
        res = res + len(answers)
        answers = set()
    for x in list(line):
        answers.add(x)
res = res + len(answers)
print(res)

#########################

groupSet = set()
totalCount = 0
peopleInGroup = 0

for line in open('input'):
    line = line[:-1]
    if line == '':
        totalCount = totalCount + len(groupSet)
        groupSet = set()
        peopleInGroup = 0
        continue

    peopleInGroup = peopleInGroup + 1

    person = set()
    for x in list(line):
        person.add(x)

    if peopleInGroup == 1:
        groupSet = person
    else:
        groupSet = groupSet & person

print(totalCount)

