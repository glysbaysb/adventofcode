def interpret(instructions):
    ip = 0

    while instructions[ip] != 99:
        if instructions[ip] == 1:
            posA = instructions[ip + 1]
            posB = instructions[ip + 2]
            posC = instructions[ip + 3]
            instructions[posC] = instructions[posA] + instructions[posB]
            ip = ip + 4
        elif instructions[ip] == 2:
            posA = instructions[ip + 1]
            posB = instructions[ip + 2]
            posC = instructions[ip + 3]
            instructions[posC] = instructions[posA] * instructions[posB]
            ip = ip + 4

