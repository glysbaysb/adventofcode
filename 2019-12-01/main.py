#!/bin/env python3
import math

res = 0
for line in open('input'):
    i = int(line)
    res += math.floor(i / 3) - 2

print(res)
