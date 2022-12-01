elves = [0]

for line in open('input'):
    if len(line) == 1: # \n
        elves.append(0)
        continue
    elves[-1] = elves[-1] + int(line)

max_elf = 0
for elf in elves:
    if elf > max_elf:
        max_elf = elf
print(max_elf)

