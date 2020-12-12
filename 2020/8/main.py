instructions = []

for line in open('input'):
    ins, val = line.split()
    instructions.append((ins, val))

def run(instructions):
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

        if ip >= len(instructions):
            return (accumulator, True)

    return (accumulator, False)

for x in range(len(instructions)):
    ins, val = instructions[x]
    if ins == 'nop':
        copy = instructions.copy()
        copy[x] = ('jmp', val)
        
        res, success = run(copy)
        if success:
            print(res)
            break
    elif ins == 'jmp':
        copy = instructions.copy()
        copy[x] = ('nop', val)
        
        res, success = run(copy)
        if success:
            print(res)
            break
    else:
        continue
