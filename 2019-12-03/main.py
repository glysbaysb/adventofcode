#!/bin/env python3
def interpret_intcode(intcode):
    ip = 0
    while intcode[ip] != 99:
        if intcode[ip] == 1:
           posA = intcode[ip + 1]
           posB = intcode[ip + 2]
           posC = intcode[ip + 3]

           intcode[posC] = intcode[posA] + intcode[posB]
           ip = ip + 4
        elif intcode[ip] == 2:
           posA = intcode[ip + 1]
           posB = intcode[ip + 2]
           posC = intcode[ip + 3]

           intcode[posC] = intcode[posA] * intcode[posB]
           ip = ip + 4
        else:
            print('err', ip, intcode[ip])
            raise "err"
    return intcode

#a = [1, 0, 0, 0, 99]
#print(interpret_intcode(a))
#b = [2, 3, 0, 3, 99]
#print(interpret_intcode(b))
#c = [2, 4, 4, 5, 99, 0]
#print(interpret_intcode(c))
'''
for intcodeAsString in open('input'):
    intcode = [int(x) for x in intcodeAsString.split(',')]
    intcode[1] = 12
    intcode[2] = 2
    print(interpret_intcode(intcode)[0])
'''
for intcodeAsString in open('input'):
    origIntcode = [int(x) for x in intcodeAsString.split(',')]
    for i in range(100):
        for j in range(100):
            intcode = list(origIntcode)
            intcode[1] = i
            intcode[2] = j

            res = interpret_intcode(intcode)
            if res[0] == 19690720:
                print(100 * i + j)
                break
