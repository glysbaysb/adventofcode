#!/usr/bin/env python3
input = '1321131112'

def rle(x):
    res = ''
    count = 1
    char = x[0]
    for current in x[1:]:
        if current == char:
            count = count + 1
            continue
        res += str(count) + char
        char = current
        count = 1

    # the last sequence
    res += str(count) + char


    return res

encoded = input
for i in range(50):
    encoded = rle(encoded)
    print(i, encoded, len(encoded))
