floor = 0
idx = 1
for line in open('input'):
    for c in line:
        if c == '(':
            floor = floor + 1
        elif c == ')':
            floor = floor - 1

        if floor == -1:
            print(idx)
            break
        idx = idx + 1
