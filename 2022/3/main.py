counter = 0
for line in open('input'):
    p1 = line[:len(line)//2]
    p2 = line[len(line)//2:]

    res = (set(p1) & set(p2)).pop()
    if res >= 'a' and res <= 'z':
        counter = counter + ord(res) - ord('a') + 1
    else:
        counter = counter + ord(res) - ord('A') + 27
print(counter)
        

