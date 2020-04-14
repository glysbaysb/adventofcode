#!/bin/env python3
import math

for x in range(353096, 843212):
    s = str(x)

    # never decreases
    _min = s[0]
    passed = True
    for i in s[1:]:
        if i < _min:
            passed = False
            break
        _min = i

    if passed is False:
        continue

    # two adjecent digits match
    passed = False
    for i in range(2, len(s)):
        # but not three
        if (s[i] == s[i - 1]) and (s[i] == s[i - 2]):
            passed = True

    if passed is True:
        print(s)
