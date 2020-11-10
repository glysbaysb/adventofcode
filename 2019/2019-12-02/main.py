#!/bin/env python3
import math

def fuel_required(x):
    fuel = math.floor(x / 3) - 2
    if fuel < 0:
        return 0
    return fuel + fuel_required(fuel)

res = 0
for line in open('input'):
    i = int(line)
    res += fuel_required(i)

print(res)
