counter = 0
lines = []
for line in open('input'):
    if len(line) > 2:
        lines.append(line.strip())
i = 0
while i < len(lines):
    l1 = lines[i]
    l2 = lines[i+1]
    l3 = lines[i+2]


    res = (set(l1) & set(l2) & set(l3)).pop()
    if res >= 'a' and res <= 'z':
        counter = counter + ord(res) - ord('a') + 1
    else:
        counter = counter + ord(res) - ord('A') + 27

    i = i + 3
print(counter)
        

