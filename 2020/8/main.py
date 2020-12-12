instructions = []

for line in open('input'):
    ins, val = line.split()
    instructions.append((ins, val))

visitedInstructions = set()
accumulator = 0
ip = 0
while ip not in visitedInstructions:
    visitedInstructions |= set([ip])

    ins, val = instructions[ip]
    if ins == 'nop':
        ip += 1
    elif ins == 'acc':
        accumulator += int(val)
        ip += 1
    else:
        ip += int(val)
print(accumulator)
