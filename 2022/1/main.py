elves = [0]

for line in open('input'):
    if len(line) == 1: # \n
        elves.append(0)
        continue
    elves[-1] = elves[-1] + int(line)

elves.sort(reverse=True)
print(elves[0] + elves[1] + elves[2])

