#!/bin/env python3
import itertools

def getValueFromInstruction(opcodeS, memory, relativeBase, ip):
    parAImmediateMode = len(opcodeS) > 2 and opcodeS[-3] == "1"
    parBImmediateMode = len(opcodeS) > 3 and opcodeS[-4] == "1"
    parARelativeMode = len(opcodeS) > 2 and opcodeS[-3] == "2"
    parBRelativeMode = len(opcodeS) > 3 and opcodeS[-4] == "2"

    if parAImmediateMode:
        a = memory[ip + 1]
    elif parARelativeMode:
        a = memory[relativeBase]
    else:
        a = memory[memory[ip + 1]]

    if parBImmediateMode:
        b = memory[ip + 1]
    elif parBRelativeMode:
        b = memory[relativeBase]
    else:
        b = memory[memory[ip + 1]]

    return [a, b]


def interpret(instructions, inputVal):
    ip = 0
    relativeBase = 0
    output = 0

    while instructions[ip] != 99:
        print(instructions[0:17])
        opcode = instructions[ip] % 100
        opcodeS = str(instructions[ip])

        parAImmediateMode = len(opcodeS) > 2 and opcodeS[-3] == "1"
        parCImmediateMode = len(opcodeS) > 4 and opcodeS[-5] == "1"
        parCRelativeMode = len(opcodeS) > 4 and opcodeS[-5] == "2"


        a, b = getValueFromInstruction(opcodeS, instructions, relativeBase, ip)

        # Add
        if opcode == 1:
            if parCImmediateMode:
                instructions[ip + 3] = a + b
            else:
                instructions[instructions[ip + 3]] = a + b

            ip = ip + 4
        # Mul
        elif opcode == 2:
            if parCImmediateMode:
                instructions[ip + 3] = a * b
            else:
                instructions[instructions[ip + 3]] = a * b

            ip = ip + 4
        # IN
        elif opcode == 3:
            x = inputVal.pop(0)
            if parAImmediateMode:
                instructions[ip + 1] = x
            else:
                instructions[instructions[ip + 1]] = x

            ip += 2
        # OUT
        elif opcode == 4:
            if parAImmediateMode:
                output = instructions[ip + 1]
            else:
                output = instructions[instructions[ip + 1]]

            ip += 2
        # jt
        elif opcode == 5:
            if a != 0:
                ip = b
            else:
                ip = ip + 3
        # jnt / jf
        elif opcode == 6:
            if a == 0:
                ip = b
            else:
                ip = ip + 3
        # lt
        elif opcode == 7:
            res = 1 if a < b else 0
            if parCImmediateMode:
                instructions[ip + 3] = res
            else:
                instructions[instructions[ip + 3]] = res
            ip = ip + 4
        # EQ
        elif opcode == 8:
            res = 1 if a == b else 0
            if parCImmediateMode:
                instructions[ip + 3] = res
            else:
                instructions[instructions[ip + 3]] = res
            ip = ip + 4
        # adjust base pointer
        elif opcode == 9:
            relativeBase = relativeBase + a
            ip = ip + 2


    return output

program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
while len(program) < 1024*1024:
    program.append(0)
print(interpret(program.copy(), [0]))

"""
for line in open('input'):
    #program = [int(x) for x in line.split(',')]
    program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    print(interpret(program.copy(), [0]))
"""
