#!/bin/env python3
def interpret(instructions):
    ip = 0

    while instructions[ip] != 99:
        opcode = instructions[ip] % 100
        opcodeS = str(instructions[ip])
        parAMode = len(opcodeS) > 2 and opcodeS[-3] == "1"
        parBMode = len(opcodeS) > 3 and opcodeS[-4] == "1"
        parCMode = len(opcodeS) > 4 and opcodeS[-5] == "1"

        if opcode == 1:
            a =  instructions[instructions[ip + 1]] if parAMode == 0 else instructions[ip + 1]
            b =  instructions[instructions[ip + 2]] if parBMode == 0 else instructions[ip + 2]
            if parCMode == 1:
                instructions[ip + 3] = a + b
            else:
                instructions[instructions[ip + 3]] = a + b

            ip = ip + 4
        elif opcode == 2:
            a =  instructions[instructions[ip + 1]] if parAMode == 0 else instructions[ip + 1]
            b =  instructions[instructions[ip + 2]] if parBMode == 0 else instructions[ip + 2]
            if parCMode == 1:
                instructions[ip + 3] = a * b
            else:
                instructions[instructions[ip + 3]] = a * b

            ip = ip + 4
        elif opcode == 3:
            x = input()
            if parAMode == 1:
                instructions[i] = x
            else:
                instructions[instructions[i]] = x

            ip += 2
        elif opcode == 4:
            if parAMode == 1:
                print(instructions[i])
            else:
                print(instructions[instructions[i]])

            ip += 2


    return instructions

print(interpret([1002, 4, 3, 4, 33]))

