#!/bin/env python3
def interpret(instructions, inputVal):
    ip = 0
    output = 0

    while instructions[ip] != 99:
        opcode = instructions[ip] % 100
        opcodeS = str(instructions[ip])
        parAImmediateMode = len(opcodeS) > 2 and opcodeS[-3] == "1"
        parBImmediateMode = len(opcodeS) > 3 and opcodeS[-4] == "1"
        parCImmediateMode = len(opcodeS) > 4 and opcodeS[-5] == "1"


        # Add
        if opcode == 1:
            a =  instructions[instructions[ip + 1]] if not parAImmediateMode else instructions[ip + 1]
            b =  instructions[instructions[ip + 2]] if not parBImmediateMode else instructions[ip + 2]
            if parCImmediateMode:
                instructions[ip + 3] = a + b
            else:
                instructions[instructions[ip + 3]] = a + b

            ip = ip + 4
        # Mul
        elif opcode == 2:
            a =  instructions[instructions[ip + 1]] if not parAImmediateMode else instructions[ip + 1]
            b =  instructions[instructions[ip + 2]] if not parBImmediateMode else instructions[ip + 2]
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
            a =  instructions[instructions[ip + 1]] if not parAImmediateMode else instructions[ip + 1]
            if a != 0:
                b =  instructions[instructions[ip + 2]] if not parBImmediateMode else instructions[ip + 2]
                ip = b
            else:
                ip = ip + 3
        # jnt / jf
        elif opcode == 6:
            a =  instructions[instructions[ip + 1]] if not parAImmediateMode else instructions[ip + 1]
            if a == 0:
                b =  instructions[instructions[ip + 2]] if not parBImmediateMode else instructions[ip + 2]
                ip = b
            else:
                ip = ip + 3
        # lt
        elif opcode == 7:
            a =  instructions[instructions[ip + 1]] if not parAImmediateMode else instructions[ip + 1]
            b =  instructions[instructions[ip + 2]] if not parBImmediateMode else instructions[ip + 2]
            res = 1 if a < b else 0
            if parCImmediateMode:
                instructions[ip + 3] = res
            else:
                instructions[instructions[ip + 3]] = res
            ip = ip + 4
        # EQ
        elif opcode == 8:
            a =  instructions[instructions[ip + 1]] if not parAImmediateMode else instructions[ip + 1]
            b =  instructions[instructions[ip + 2]] if not parBImmediateMode else instructions[ip + 2]
            res = 1 if a == b else 0
            if parCImmediateMode:
                instructions[ip + 3] = res
            else:
                instructions[instructions[ip + 3]] = res
            ip = ip + 4

    return output

for line in open('input'):
    program = [int(x) for x in line.split(',')]
    outputA = interpret(program.copy(), [4, 0])
    outputB = interpret(program.copy(), [3, outputA])
    outputC = interpret(program.copy(), [2, outputB])
    outputD = interpret(program.copy(), [1, outputC])
    print(interpret(program.copy(), [0, outputD]))

